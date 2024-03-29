# Generated by Django 3.2.7 on 2023-03-14 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0109_sacredjourneypage_upcoming_journeys_blurb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='media/event')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('zoom_link', models.TextField(blank=True, null=True)),
                ('description', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('style_sheet', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.stylesheet')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
