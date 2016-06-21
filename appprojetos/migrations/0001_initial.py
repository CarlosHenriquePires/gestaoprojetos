# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 03:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acompanhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data')),
            ],
        ),
        migrations.CreateModel(
            name='Atividades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('dataInicio', models.DateField(auto_now_add=True, verbose_name='Data Inicio')),
                ('dataTermino', models.DateField(verbose_name='Data Término')),
                ('custos', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Custos')),
            ],
        ),
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('dataInicio', models.DateField(auto_now_add=True, verbose_name='Data Inicio')),
                ('dataTermino', models.DateField(verbose_name='Data Término')),
                ('justificativa', models.CharField(max_length=500, verbose_name='Justificativa')),
                ('metodologia', models.CharField(max_length=800, verbose_name='Metodologia')),
                ('resultados', models.CharField(max_length=500, verbose_name='Resultados Esperados')),
                ('participantes', models.ManyToManyField(to='appprojetos.Participantes')),
            ],
        ),
        migrations.AddField(
            model_name='atividades',
            name='projetos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprojetos.Projetos', verbose_name='Projetos'),
        ),
        migrations.AddField(
            model_name='acompanhamento',
            name='atividades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appprojetos.Atividades', verbose_name='Atividades'),
        ),
    ]
