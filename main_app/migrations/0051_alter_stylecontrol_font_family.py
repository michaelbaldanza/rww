# Generated by Django 3.2.7 on 2022-06-01 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0050_auto_20220601_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stylecontrol',
            name='font_family',
            field=models.CharField(blank=True, choices=[('AR', 'Arial'), ('CA', 'Calibri'), ('CM', 'Cambria'), ('FG', 'Franklin Gothic'), ('FU', 'Futura'), ('GA', 'Garamond'), ('HE', 'Helvetica'), ('PA', 'Papyrus'), ('RO', 'Rockwell'), ('SO', 'Source Sans Pro'), ('TN', 'Times New Roman'), ('VE', 'Verdana')], default='SO', max_length=200, null=True),
        ),
    ]
