# Generated by Django 3.2.7 on 2022-08-16 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0098_auto_20220815_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='audio_file_caption',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mainpage',
            name='blog_image',
            field=models.FileField(blank=True, null=True, upload_to='media/main-menu-images/'),
        ),
    ]
