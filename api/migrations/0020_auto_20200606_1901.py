# Generated by Django 3.0.4 on 2020-06-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200606_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentarirestaurant',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
    ]