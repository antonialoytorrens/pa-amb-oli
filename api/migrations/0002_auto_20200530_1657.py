# Generated by Django 3.0.4 on 2020-05-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='latitud',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='longitud',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fotorestaurant',
            name='imatge',
            field=models.ImageField(default='pic_restaurant/none/no-img.jpg', upload_to='pic_restaurant/'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='web',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
