# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-11 16:08
from __future__ import unicode_literals

import collection.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='picture',
            field=models.ImageField(blank=True, default=None, upload_to=collection.models.group_based_upload_to),
        ),
    ]
