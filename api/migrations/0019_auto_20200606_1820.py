# Generated by Django 3.0.4 on 2020-06-06 16:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200606_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='valoracio',
        ),
        migrations.CreateModel(
            name='ValoracioRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracio', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='valoracio_restaurant_usuari', to='api.Profile')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='valoracio_restaurant', to='api.Restaurant')),
            ],
        ),
    ]
