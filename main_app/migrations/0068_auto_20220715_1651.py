# Generated by Django 3.2.7 on 2022-07-15 21:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0067_alter_mainpage_body_opacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='image_heading_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='body_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='tagline_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]