# Generated by Django 4.2.7 on 2024-01-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0019_infra_rule_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="infra",
            name="coastline_distance",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="notices",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="proximity_method",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="road_conditions",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="third_party",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="traffic_regulation",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="infra",
            name="under_structure",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]