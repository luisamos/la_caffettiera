# Generated by Django 3.1.7 on 2021-04-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitulo', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('imagen', models.ImageField(upload_to='servicios', verbose_name='Imagen')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
