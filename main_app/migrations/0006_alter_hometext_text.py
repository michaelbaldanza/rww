# Generated by Django 3.2.7 on 2021-11-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_hometext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometext',
            name='text',
            field=models.TextField(blank=True, unique=True),
        ),
    ]
