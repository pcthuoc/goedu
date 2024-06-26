# Generated by Django 2.2.24 on 2022-06-17 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("judge", "0149_update_org"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="score",
            field=models.IntegerField(default=0, verbose_name="votes"),
        ),
        migrations.CreateModel(
            name="BlogVote",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.IntegerField()),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="judge.BlogPost",
                    ),
                ),
                (
                    "voter",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="voted_blogs",
                        to="judge.Profile",
                    ),
                ),
            ],
            options={
                "verbose_name": "blog vote",
                "verbose_name_plural": "blog votes",
                "unique_together": {("voter", "blog")},
            },
        ),
    ]
