# Generated by Django 4.2.7 on 2023-12-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0004_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="infra",
            name="top_structure",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]