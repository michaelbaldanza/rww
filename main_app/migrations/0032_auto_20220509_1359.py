# Generated by Django 3.2.7 on 2022-05-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0031_auto_20220506_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='art_and_music_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='blog_image',
            field=models.FileField(blank=True, null=True, upload_to='media/ministerial-record-images/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='guided_meditations_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='ministry_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='sacred_journeys_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='spiritual_direction_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
    ]