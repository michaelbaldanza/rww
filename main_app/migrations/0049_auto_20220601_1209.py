# Generated by Django 3.2.7 on 2022-06-01 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0048_auto_20220531_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stylecontrol',
            name='global_style',
        ),
        migrations.AddField(
            model_name='stylecontrol',
            name='font_choice_test',
            field=models.CharField(blank=True, choices=[('AR', 'arg'), ('CA', 'arg'), ('CM', 'arg'), ('FG', 'arg'), ('FU', 'arg'), ('GA', 'arg'), ('HE', 'arg'), ('PA', 'arg'), ('RO', 'arg'), ('SO', 'arg'), ('TN', 'arg'), ('VE', 'arg')], max_length=2, null=True),
        ),
    ]