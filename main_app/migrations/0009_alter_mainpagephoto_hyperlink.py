# Generated by Django 3.2.7 on 2022-02-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_mainpagephoto_hyperlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagephoto',
            name='hyperlink',
            field=models.CharField(blank=True, choices=[('SD', 'Spiritual Direction'), ('BL', 'Blog'), ('GM', 'Guided Meditations'), ('MY', 'Ministry'), ('SJ', 'Sacred Journeys'), ('AM', 'Art and Music')], max_length=2, null=True),
        ),
    ]
