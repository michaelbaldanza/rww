# Generated by Django 3.2.7 on 2022-07-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0077_rename_name_sacredjourney_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='title',
            field=models.CharField(default='Main Page', max_length=200),
        ),
    ]