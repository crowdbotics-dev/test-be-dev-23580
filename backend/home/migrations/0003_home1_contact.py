# Generated by Django 2.2.26 on 2022-02-16 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_email_home1'),
    ]

    operations = [
        migrations.AddField(
            model_name='home1',
            name='contact',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
