# Generated by Django 4.2.7 on 2024-07-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0031_material_partsnumber_main_frame_partsnumber_material"),
    ]

    operations = [
        migrations.CreateModel(
            name="Main_Frame",
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
                (
                    "主要部材",
                    models.CharField(
                        choices=[("有り", "有り"), ("無し", "無し")], max_length=50
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="partsnumber",
            name="main_frame",
        ),
        migrations.AddField(
            model_name="partsnumber",
            name="main_frame",
            field=models.ManyToManyField(to="infra.main_frame"),
        ),
    ]