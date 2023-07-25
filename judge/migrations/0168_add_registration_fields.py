from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0167_profile_upload_image_perm'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='registration_end',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='registration end time'),
        ),
        migrations.AddField(
            model_name='contest',
            name='registration_start',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='registration start time'),
        ),
    ]
