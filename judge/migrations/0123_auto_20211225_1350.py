# Generated by Django 2.2.24 on 2021-12-25 13:50

import django.core.validators
from django.db import migrations, models
import judge.models.problem_data
import judge.utils.problem_data


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0122_auto_20211225_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='problemdata',
            name='custom_checker',
            field=models.FileField(blank=True, null=True, storage=judge.utils.problem_data.ProblemDataStorage(), upload_to=judge.models.problem_data.problem_directory_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['cpp', 'py'])], verbose_name='custom checker file'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='memory_limit',
            field=models.PositiveIntegerField(help_text='The memory limit for this problem, in kilobytes (e.g. 256mb = 262144 kilobytes).', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1048576)], verbose_name='memory limit'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='points',
            field=models.FloatField(help_text="Points awarded for problem completion. Points are displayed with a 'p' suffix if partial. 1-1.5: beginner problems; 1.5-2: simple algorithm                                             (binary search, sieve, etc.); 2-3: advanced algorithm                                             (dp, dijkstra, dsu, etc.); 2.5-3.5: 1st probs of VOI; 3.5-4.5: 2nd probs of                                             VOI; 4.5-6: 3rd prob of VOI.", validators=[django.core.validators.MinValueValidator(0)], verbose_name='points'),
        ),
    ]
