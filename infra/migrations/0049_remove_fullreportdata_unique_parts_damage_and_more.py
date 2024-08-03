# Generated by Django 4.2.7 on 2024-07-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0048_fullreportdata_unique_parts_damage"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="fullreportdata",
            name="unique_parts_damage",
        ),
        migrations.AddConstraint(
            model_name="fullreportdata",
            constraint=models.UniqueConstraint(
                fields=(
                    "parts_name",
                    "damage_name",
                    "parts_split",
                    "join",
                    "picture_number",
                    "this_time_picture",
                    "last_time_picture",
                    "textarea_content",
                    "damage_coordinate_x",
                    "damage_coordinate_y",
                    "span_number",
                    "special_links",
                ),
                name="unique_parts_damage",
            ),
        ),
    ]