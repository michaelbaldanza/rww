# Generated by Django 3.2.7 on 2022-07-30 02:52

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0084_spiritualdirection_style_sheet'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylecontrol',
            name='header_maintext_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='"Sitting Quietly" opacity (%)'),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='header_smalltext_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='"by Rev. Wayne Walder opacity" (%'),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='image_heading_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='image_heading_font_family',
            field=models.CharField(blank=True, choices=[('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='image_heading_opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Image heading opacity (%)'),
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='opacity',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Opacity (%)'),
        ),
        migrations.AlterField(
            model_name='stylecontrol',
            name='header_maintext_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='"Sitting Quietly" color'),
        ),
        migrations.AlterField(
            model_name='stylecontrol',
            name='header_maintext_font_family',
            field=models.CharField(blank=True, choices=[('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], max_length=200, null=True, verbose_name='"Sitting Quietly" font family'),
        ),
        migrations.AlterField(
            model_name='stylecontrol',
            name='header_smalltext_color',
            field=colorfield.fields.ColorField(blank=True, default=None, image_field=None, max_length=18, null=True, samples=None, verbose_name='"by Rev. Wayne Walder" color'),
        ),
        migrations.AlterField(
            model_name='stylecontrol',
            name='header_smalltext_font_family',
            field=models.CharField(blank=True, choices=[('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], max_length=200, null=True, verbose_name='"by Rev. Wayne Walder" font family'),
        ),
    ]
