# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_auto_20160710_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcartitems',
            name='ware',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='front.Ware'),
        ),
    ]