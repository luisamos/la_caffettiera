# Generated by Django 3.1.7 on 2021-04-04 01:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210404_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='fecha_publicacion',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 4, 1, 7, 17, 40091, tzinfo=utc), verbose_name='Fecha de publicación'),
        ),
    ]
