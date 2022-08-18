# Generated by Django 3.2.7 on 2022-08-18 19:56

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0101_alter_stylecontrol_footer_opacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylecontrol',
            name='heading_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='Heading color:'),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='heading_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Heading opacity (%)'),
        ),
    ]
