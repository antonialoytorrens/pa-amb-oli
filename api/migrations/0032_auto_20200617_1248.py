# Generated by Django 3.0.7 on 2020-06-17 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_auto_20200617_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggerimentrestaurant',
            old_name='missatge',
            new_name='explicacio',
        ),
    ]