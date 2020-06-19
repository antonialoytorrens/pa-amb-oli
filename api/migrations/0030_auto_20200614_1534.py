# Generated by Django 3.0.7 on 2020-06-14 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_restaurant_imatge'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='data_alta',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='data_modificacio',
            field=models.DateTimeField(auto_now=True),
        ),
    ]