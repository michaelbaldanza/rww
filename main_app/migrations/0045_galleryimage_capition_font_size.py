# Generated by Django 3.2.7 on 2022-05-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0044_spiritualdirection_blurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='capition_font_size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
