# Generated by Django 3.1.2 on 2022-04-05 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
