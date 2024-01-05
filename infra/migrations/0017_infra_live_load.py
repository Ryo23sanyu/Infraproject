# Generated by Django 4.2.7 on 2024-01-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0016_infra_latitude_infra_longitude"),
    ]

    operations = [
        migrations.AddField(
            model_name="infra",
            name="live_load",
            field=models.CharField(
                blank=True,
                choices=[
                    ("one", "一等橋"),
                    ("two", "二等橋"),
                    ("three", "三等橋"),
                    ("unknown", "不明"),
                ],
                max_length=50,
            ),
        ),
    ]