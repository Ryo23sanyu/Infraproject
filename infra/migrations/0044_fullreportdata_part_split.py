# Generated by Django 4.2.7 on 2024-07-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0043_damagecomment_fullreportdata_special_links"),
    ]

    operations = [
        migrations.AddField(
            model_name="fullreportdata",
            name="part_split",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]