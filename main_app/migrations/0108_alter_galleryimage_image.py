# Generated by Django 3.2.7 on 2022-11-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0107_alter_galleryimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.FileField(upload_to='media/gallery-images/'),
        ),
    ]
