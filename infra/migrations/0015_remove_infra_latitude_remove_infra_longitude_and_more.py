# Generated by Django 4.2.7 on 2024-01-05 02:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0014_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="infra",
            name="latitude",
        ),
        migrations.RemoveField(
            model_name="infra",
            name="longitude",
        ),
        migrations.AlterField(
            model_name="infra",
            name="code",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
