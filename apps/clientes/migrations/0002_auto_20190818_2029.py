# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-19 01:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientes',
            options={'permissions': set([('cliente_permission', 'Usuario_cliente')])},
        ),
    ]
