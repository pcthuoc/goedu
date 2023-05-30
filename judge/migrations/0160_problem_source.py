# Generated by Django 2.2.24 on 2022-08-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0159_contest_virtual_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='source',
            field=models.CharField(blank=True, db_index=True, help_text='Source of problem. Please credit the source of the problemif it is not yours', max_length=200, verbose_name='Problem source'),
        ),
    ]
