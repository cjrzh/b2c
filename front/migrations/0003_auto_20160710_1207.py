# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 12:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20160710_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]