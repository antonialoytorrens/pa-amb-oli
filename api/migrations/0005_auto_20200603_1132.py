# Generated by Django 3.0.4 on 2020-06-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_noticia_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Esdeveniment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titol', models.TextField()),
                ('longitud', models.DecimalField(decimal_places=5, max_digits=30)),
                ('latitud', models.DecimalField(decimal_places=5, max_digits=30)),
                ('since', models.DateTimeField()),
                ('until', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TipusSuggeriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='descripcio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='web',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Suggeriment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_restaurant', models.CharField(blank=True, max_length=100, null=True)),
                ('direccio', models.CharField(blank=True, max_length=100, null=True)),
                ('horari', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcio', models.TextField(blank=True, null=True)),
                ('telefon', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('reservaTaula', models.BooleanField(blank=True, null=True)),
                ('responsableRestaurant', models.BooleanField(blank=True, null=True)),
                ('imatge_restaurant', models.ImageField(blank=True, default='pic_restaurant/none/no-img.jpg', null=True, upload_to='pic_restaurant/')),
                ('tipus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.TipusSuggeriment')),
            ],
        ),
    ]