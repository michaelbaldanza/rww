# Generated by Django 3.2.7 on 2022-05-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0038_auto_20220516_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('audio_file', models.FileField(upload_to='media/meditations/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]