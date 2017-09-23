# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-17 00:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(default='New', on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickets.Status'),
        ),
    ]
