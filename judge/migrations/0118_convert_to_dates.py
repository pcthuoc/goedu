# Generated by Django 2.2.17 on 2021-04-27 14:46

from django.db import migrations, models
from django.db.models import F
from django.utils import timezone


def convert_to_datetime(apps, schema_editor):
    Contest = apps.get_model("judge", "Contest")
    Submission = apps.get_model("judge", "Submission")

    Submission.objects.filter(was_rejudged=True).update(rejudged_date=F("judged_date"))
    Submission.objects.filter(is_locked=True).update(locked_after=timezone.now())
    Contest.objects.filter(is_locked=True).update(locked_after=F("end_time"))


def convert_to_boolean(apps, schema_editor):
    Contest = apps.get_model("judge", "Contest")
    Submission = apps.get_model("judge", "Submission")

    now = timezone.now()

    Submission.objects.filter(rejudged_date__isnull=False).update(was_rejudged=True)
    Submission.objects.filter(locked_after__lt=now).update(is_locked=True)
    Contest.objects.filter(locked_after__lt=now).update(is_locked=True)


class Migration(migrations.Migration):
    dependencies = [
        ("judge", "0117_remove_private_messages"),
    ]

    operations = [
        migrations.AddField(
            model_name="contest",
            name="locked_after",
            field=models.DateTimeField(
                blank=True,
                help_text="Prevent submissions from this contest from being rejudged after this date.",
                null=True,
                verbose_name="contest lock",
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="locked_after",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="submission lock"
            ),
        ),
        migrations.AddField(
            model_name="submission",
            name="rejudged_date",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last rejudge date by admin"
            ),
        ),
        migrations.RunPython(convert_to_datetime, convert_to_boolean, atomic=True),
        migrations.RemoveField(
            model_name="contest",
            name="is_locked",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="is_locked",
        ),
        migrations.RemoveField(
            model_name="submission",
            name="was_rejudged",
        ),
    ]
