# Generated by Django 3.2.7 on 2022-07-30 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0090_alter_guidedmeditationpage_main_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='style_sheet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.stylesheet'),
        ),
    ]