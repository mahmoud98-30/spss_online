# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20170827_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseTemp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_end', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='license_type',
            field=models.CharField(choices=[('1 year', '1'), ('2 years', '2')], default='1', max_length=50),
        ),
        migrations.AddField(
            model_name='purchasetemp',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='purchasetemp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases_temp', to=settings.AUTH_USER_MODEL),
        ),
    ]