# Generated by Django 3.1.7 on 2021-04-04 20:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_pagina_orden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagina',
            options={'ordering': ['-orden'], 'verbose_name': 'Página', 'verbose_name_plural': 'Páginas'},
        ),
        migrations.AlterField(
            model_name='pagina',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]