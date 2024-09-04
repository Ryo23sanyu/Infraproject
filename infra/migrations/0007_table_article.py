# Generated by Django 4.2.7 on 2024-08-26 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0006_partsnumber_unique_parts_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="table",
            name="article",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="infra.article",
            ),
        ),
    ]