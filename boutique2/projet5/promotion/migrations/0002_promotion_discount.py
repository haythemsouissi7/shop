# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-16 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='discount',
            field=models.IntegerField(null=True),
        ),
    ]
