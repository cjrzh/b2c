# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-27 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0009_auto_20160827_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
