# Generated by Django 3.0.4 on 2020-05-31 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200530_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titol', models.TextField()),
                ('cos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FotoNoticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imatge', models.ImageField(default='pic_noticia/none/no-img.jpg', upload_to='pic_noticia/')),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Noticia')),
            ],
        ),
    ]
