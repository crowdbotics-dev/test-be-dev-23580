# Generated by Django 2.2.26 on 2022-02-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("home", "0001_load_initial_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contact", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Home1",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.BigIntegerField()),
            ],
        ),
    ]
