# Generated by Django 3.2.7 on 2022-07-29 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0083_auto_20220729_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritualdirection',
            name='style_sheet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.stylesheet'),
        ),
    ]