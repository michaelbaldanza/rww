# Generated by Django 3.2.7 on 2022-07-14 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0062_alter_stylecontrol_font_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainpage',
            old_name='main_text',
            new_name='body',
        ),
    ]
