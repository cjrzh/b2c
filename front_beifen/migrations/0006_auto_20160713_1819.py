# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_auto_20160710_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcartitems',
            name='ware',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.Ware'),
        ),
    ]
