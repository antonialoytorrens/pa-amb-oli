# Generated by Django 3.0.4 on 2020-06-04 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20200604_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotorestaurant',
            name='imatge',
            field=models.ImageField(default='static/images/pic_restaurant/none/no-img.jpg', upload_to='static/images/pic_restaurant/'),
        ),
    ]