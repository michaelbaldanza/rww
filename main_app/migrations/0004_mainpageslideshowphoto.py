# Generated by Django 3.2.7 on 2022-02-13 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_photo_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageSlideshowPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.photo')),
            ],
        ),
    ]
