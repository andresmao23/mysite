# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-21 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('habitantes', models.IntegerField()),
                ('clima', models.CharField(choices=[('CA', 'Caliente'), ('FR', 'Frio'), ('TE', 'Templado')], default='CA', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='fotos')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Departamento'),
        ),
    ]
