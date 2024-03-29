# Generated by Django 3.2.7 on 2022-07-02 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0054_alter_galleryimage_font_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtAndMusicPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('art_heading', models.CharField(default='Photography', max_length=20)),
                ('music_heading', models.CharField(default='Music', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='stylecontrol',
            name='font_weight',
            field=models.CharField(blank=True, choices=[('NO', 'normal'), ('BO', 'bold'), ('LI', 'lighter'), ('BE', 'bolder')], max_length=200, null=True),
        ),
    ]
