# Generated by Django 3.0.7 on 2020-06-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20200613_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='profile',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True),
        ),
    ]
