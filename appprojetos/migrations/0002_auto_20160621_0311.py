# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 03:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appprojetos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acompanhamento',
            name='atividades',
        ),
        migrations.RemoveField(
            model_name='atividades',
            name='projetos',
        ),
        migrations.RemoveField(
            model_name='projetos',
            name='participantes',
        ),
        migrations.DeleteModel(
            name='Acompanhamento',
        ),
        migrations.DeleteModel(
            name='Atividades',
        ),
        migrations.DeleteModel(
            name='Participantes',
        ),
        migrations.DeleteModel(
            name='Projetos',
        ),
    ]
