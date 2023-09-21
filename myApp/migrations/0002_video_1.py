# Generated by Django 4.2.5 on 2023-09-21 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Video_1",
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
                ("name", models.CharField(max_length=100)),
                ("vid", models.FileField(blank=True, upload_to="uploads/")),
            ],
        ),
    ]