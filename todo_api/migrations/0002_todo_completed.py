# Generated by Django 5.1 on 2024-10-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="completed",
            field=models.BooleanField(default=False),
        ),
    ]
