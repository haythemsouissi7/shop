# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-18 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0005_auto_20170816_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
