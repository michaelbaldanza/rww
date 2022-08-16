# Generated by Django 3.2.7 on 2022-08-15 16:58

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0097_auto_20220815_1148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylecontrol',
            name='font_color',
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='Text color:'),
        ),
    ]
