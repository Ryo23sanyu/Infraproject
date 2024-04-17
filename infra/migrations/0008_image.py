# Generated by Django 4.2.7 on 2024-04-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0007_alter_number_bottom_number_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("photo", models.ImageField(upload_to="photos/")),
            ],
        ),
    ]