

from inspect import signature
from django.core.cache import cache, caches
from django.db.models.query import QuerySet
from django.core.handlers.wsgi import WSGIRequest
import hashlib
from judge.logging import log_debug

MAX_NUM_CHAR = 50
NONE_RESULT = "__None__"

# Lấy cache layer l0 nếu có
l0_cache = caches["l0"] if "l0" in caches else None

def finished_submission(sub):
    keys = ["user_complete:%d" % sub.user_id, "user_attempted:%s" % sub.user_id]
    if hasattr(sub, "contest"):
        participation = sub.contest.participation
        keys += ["contest_complete:%d" % participation.id]
        keys += ["contest_attempted:%d" % participation.id]
    cache.delete_many(keys)
def arg_to_str(arg):
    """
    Chuyển đổi đối số thành chuỗi duy nhất dùng để tạo key cache.
    """
    if hasattr(arg, "id"):
        return str(arg.id)
    if isinstance(arg, (list, QuerySet)):
        return hashlib.sha1(str(list(arg)).encode()).hexdigest()[:MAX_NUM_CHAR]
    if len(str(arg)) > MAX_NUM_CHAR:
        return str(arg)[:MAX_NUM_CHAR]
    return str(arg)

def filter_args(args_list):
    """
    Loại bỏ các đối số là instance của WSGIRequest.
    """
    return [x for x in args_list if not isinstance(x, WSGIRequest)]

def cache_wrapper(prefix, timeout=None, expected_type=None):
    """
    Decorator để cache kết quả của hàm dựa trên các đối số và kết quả trả về.
    """
    def get_key(func, *args, **kwargs):
        """
        Tạo key cache từ các đối số của hàm.
        """
        args_list = list(args)
        signature_args = list(signature(func).parameters.keys())
        args_list += [kwargs.get(k) for k in signature_args[len(args):]]
        args_list = filter_args(args_list)
        args_list = [arg_to_str(i) for i in args_list]
        key = prefix + ":" + ":".join(args_list)
        key = key.replace(" ", "_")
        return key

    def _get(key):
        """
        Lấy giá trị từ cache, ưu tiên từ l0_cache trước nếu có.
        """
        if not l0_cache:
            return cache.get(key)
        result = l0_cache.get(key)
        if result is None:
            result = cache.get(key)
        return result

    def _set_l0(key, value):
        """
        Đặt giá trị vào l0_cache nếu có.
        """
        if l0_cache:
            l0_cache.set(key, value, 30)

    def _set(key, value, timeout):
        """
        Đặt giá trị vào cache chính với timeout nhất định.
        """
        _set_l0(key, value)
        cache.set(key, value, timeout)

    def decorator(func):
        """
        Hàm decorator chính.
        """
        def _validate_type(cache_key, result):
            """
            Kiểm tra loại dữ liệu của kết quả nếu có kiểu dữ liệu mong đợi.
            """
            if expected_type and not isinstance(result, expected_type):
                data = {
                    "function": f"{func.__module__}.{func.__qualname__}",
                    "result": str(result)[:30],
                    "expected_type": expected_type,
                    "type": type(result),
                    "key": cache_key,
                }
                log_debug("invalid_key", data)
                return False
            return True

        def wrapper(*args, **kwargs):
            """
            Wrapper để thực hiện việc lấy kết quả từ cache hoặc tính toán lại nếu không có trong cache.
            """
            cache_key = get_key(func, *args, **kwargs)
            result = _get(cache_key)
            if result is not None and _validate_type(cache_key, result):
                _set_l0(cache_key, result)
                if type(result) == str and result == NONE_RESULT:
                    result = None
                return result
            result = func(*args, **kwargs)
            if result is None:
                cache_result = NONE_RESULT
            else:
                cache_result = result
            _set(cache_key, cache_result, timeout)
            return result

        def dirty(*args, **kwargs):
            """
            Xóa bỏ key cache tương ứng.
            """
            cache_key = get_key(func, *args, **kwargs)
            cache.delete(cache_key)
            if l0_cache:
                l0_cache.delete(cache_key)

        def prefetch_multi(args_list):
            """
            Đặt trước các key cache để tối ưu hóa hiệu suất.
            """
            keys = [get_key(func, *args) for args in args_list]
            results = cache.get_many(keys)
            for key, result in results.items():
                if result is not None:
                    _set_l0(key, result)

        def dirty_multi(args_list):
            """
            Xóa nhiều key cache cùng một lúc.
            """
            keys = [get_key(func, *args) for args in args_list]
            cache.delete_many(keys)
            if l0_cache:
                l0_cache.delete_many(keys)

        # Gắn các phương thức bổ sung vào wrapper
        wrapper.dirty = dirty
        wrapper.prefetch_multi = prefetch_multi
        wrapper.dirty_multi = dirty_multi

        return wrapper

    return decorator
