# Generated by Django 3.2.7 on 2022-04-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20220323_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinisterialRecordTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
    ]
