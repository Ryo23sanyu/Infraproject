# Generated by Django 4.2.7 on 2024-08-05 12:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("infra", "0067_damagecomment_auto_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="company",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="first_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to.",
                related_name="customuser_set_from_infra",
                to="auth.group",
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_name",
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="customuser_set_from_infra",
                to="auth.permission",
            ),
        ),
    ]