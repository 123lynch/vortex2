# Generated by Django 4.1 on 2023-05-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userbase",
            name="address_line_1",
        ),
        migrations.RemoveField(
            model_name="userbase",
            name="address_line_2",
        ),
        migrations.RemoveField(
            model_name="userbase",
            name="postcode",
        ),
        migrations.RemoveField(
            model_name="userbase",
            name="town_city",
        ),
        migrations.AlterField(
            model_name="userbase",
            name="about",
            field=models.TextField(blank=True, null=True),
        ),
    ]
