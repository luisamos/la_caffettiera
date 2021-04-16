# Generated by Django 3.1.7 on 2021-04-04 01:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Nombre')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('fecha_publicacion', models.DateTimeField(default=datetime.datetime(2021, 4, 4, 1, 3, 31, 442157, tzinfo=utc), verbose_name='Fecha de publicación')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categoria', models.ManyToManyField(to='blog.Categoria', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
