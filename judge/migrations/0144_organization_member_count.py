# Generated by Django 2.2.24 on 2022-04-17 05:37

from django.db import migrations, models


def count_organization_member(apps, schema_editor):
    Organization = apps.get_model("judge", "Organization")
    for org in Organization.objects.all():
        org.member_count = org.members.count()
        org.save()


def undo_count_organiation_member(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("judge", "0143_allow_underscore"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="member_count",
            field=models.IntegerField(default=0),
        ),
        migrations.RunPython(
            count_organization_member, undo_count_organiation_member, atomic=True
        ),
    ]
