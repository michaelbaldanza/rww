# Generated by Django 3.2.7 on 2022-07-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0061_auto_20220713_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylecontrol',
            name='font_size',
            field=models.IntegerField(blank=True, choices=[(2, 2), (4, 4), (6, 6), (8, 8), (10, 10), (12, 12), (14, 14), (16, 16), (18, 18), (20, 20), (22, 22), (24, 24), (26, 26), (28, 28), (30, 30), (32, 32), (34, 34), (36, 36), (38, 38), (40, 40)], null=True),
        ),
    ]