# Generated by Django 3.2.7 on 2023-03-15 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0110_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.date(2023, 3, 15)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.date(2023, 3, 15)),
        ),
    ]
