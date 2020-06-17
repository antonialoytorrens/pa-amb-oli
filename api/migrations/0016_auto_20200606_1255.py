# Generated by Django 3.0.4 on 2020-06-06 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200606_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentariRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missatge', models.CharField(max_length=500)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentaris_restaurant', to='api.Restaurant')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='comentaris_restaurant_usuari', to='api.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='ComentarisRestaurant',
        ),
    ]
