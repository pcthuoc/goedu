# Generated by Django 2.2.24 on 2022-04-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0131_solution_pdf_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='content',
            field=models.TextField(blank=True, verbose_name='editorial content'),
        ),
    ]
