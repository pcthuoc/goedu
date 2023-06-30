# Generated by Django 3.2.16 on 2023-06-11 11:30

from django.db import migrations, models


def github_to_auto(apps, schema_editor):
    Profile = apps.get_model("judge", "Profile")
    Profile.objects.filter(ace_theme="tomorrow").update(ace_theme="auto")


def auto_to_github(apps, schema_editor):
    Profile = apps.get_model("judge", "Profile")
    Profile.objects.filter(ace_theme="auto").update(ace_theme="tomorrow")


class Migration(migrations.Migration):
    dependencies = [
        ("judge", "0165_profile_site_theme"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="ace_theme",
            field=models.CharField(
                choices=[
                    ("auto", "Follow site theme"),
                    ("ambiance", "Ambiance"),
                    ("chaos", "Chaos"),
                    ("chrome", "Chrome"),
                    ("clouds", "Clouds"),
                    ("clouds_midnight", "Clouds Midnight"),
                    ("cobalt", "Cobalt"),
                    ("crimson_editor", "Crimson Editor"),
                    ("dawn", "Dawn"),
                    ("dreamweaver", "Dreamweaver"),
                    ("eclipse", "Eclipse"),
                    ("github", "Github"),
                    ("idle_fingers", "Idle Fingers"),
                    ("katzenmilch", "Katzenmilch"),
                    ("kr_theme", "KR Theme"),
                    ("kuroir", "Kuroir"),
                    ("merbivore", "Merbivore"),
                    ("merbivore_soft", "Merbivore Soft"),
                    ("mono_industrial", "Mono Industrial"),
                    ("monokai", "Monokai"),
                    ("pastel_on_dark", "Pastel on Dark"),
                    ("solarized_dark", "Solarized Dark"),
                    ("solarized_light", "Solarized Light"),
                    ("terminal", "Terminal"),
                    ("textmate", "Textmate"),
                    ("tomorrow", "Tomorrow"),
                    ("tomorrow_night", "Tomorrow Night"),
                    ("tomorrow_night_blue", "Tomorrow Night Blue"),
                    ("tomorrow_night_bright", "Tomorrow Night Bright"),
                    ("tomorrow_night_eighties", "Tomorrow Night Eighties"),
                    ("twilight", "Twilight"),
                    ("vibrant_ink", "Vibrant Ink"),
                    ("xcode", "XCode"),
                ],
                default="auto",
                max_length=30,
                verbose_name="Ace theme",
            ),
        ),
        migrations.RunPython(github_to_auto, auto_to_github, atomic=True),
    ]
