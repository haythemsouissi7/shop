# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-21 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_auto_20170720_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
