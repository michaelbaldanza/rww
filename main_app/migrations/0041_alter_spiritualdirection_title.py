# Generated by Django 3.2.7 on 2022-05-24 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0040_alter_mainpage_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiritualdirection',
            name='title',
            field=models.TextField(blank=True, default='Spiritual Direction', null=True),
        ),
    ]
