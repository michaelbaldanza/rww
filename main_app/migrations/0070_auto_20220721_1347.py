# Generated by Django 3.2.7 on 2022-07-21 18:47

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0069_auto_20220721_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='body_font_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='Body Color'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='body_font_family',
            field=models.CharField(blank=True, choices=[('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], max_length=200, null=True, verbose_name='Body Font'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='body_font_size',
            field=models.IntegerField(blank=True, choices=[(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (36, 36), (38, 38), (40, 40)], null=True, verbose_name='Body Size'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='body_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Body Opacity'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='image_heading_font_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='Image Heading Color'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='image_heading_font_family',
            field=models.CharField(blank=True, choices=[('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], max_length=200, null=True, verbose_name='Image Heading Font'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='image_heading_font_size',
            field=models.IntegerField(blank=True, choices=[(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (36, 36), (38, 38), (40, 40)], null=True, verbose_name='Image Heading Size'),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='image_heading_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Image Heading Opacity'),
        ),
    ]
