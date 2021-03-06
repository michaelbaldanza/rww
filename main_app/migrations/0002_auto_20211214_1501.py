# Generated by Django 3.2.7 on 2021-12-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meditation',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='meditation',
            name='source',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='source',
            field=models.URLField(blank=True, null=True),
        ),
    ]
