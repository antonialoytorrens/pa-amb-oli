# Generated by Django 3.0.4 on 2020-06-04 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_esdeveniment_descripcio'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='fax',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='web',
            field=models.TextField(blank=True, null=True),
        ),
    ]
