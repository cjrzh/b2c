# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0006_auto_20160712_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='realname',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]