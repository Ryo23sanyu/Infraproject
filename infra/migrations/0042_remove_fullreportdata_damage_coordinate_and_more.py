# Generated by Django 4.2.7 on 2024-07-24 11:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0041_fullreportdata_damage_coordinate_x_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fullreportdata",
            name="damage_coordinate",
        ),
        migrations.RemoveField(
            model_name="fullreportdata",
            name="picture_coordinate",
        ),
    ]