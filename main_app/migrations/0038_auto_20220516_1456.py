# Generated by Django 3.2.7 on 2022-05-16 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_galleryimage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Meditation',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.RemoveField(
            model_name='sacredjourney',
            name='banner_picture',
        ),
    ]
