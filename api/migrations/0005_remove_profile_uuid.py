# Generated by Django 3.0.4 on 2020-05-17 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200517_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='uuid',
        ),
    ]
