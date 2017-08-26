# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-20 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import produit.models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_auto_20170717_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image1',
            field=models.ImageField(blank=True, default=None, upload_to=produit.models.group_based_upload_to),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image2',
            field=models.ImageField(blank=True, default=None, upload_to=produit.models.group_based_upload_to),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image3',
            field=models.ImageField(blank=True, default=None, upload_to=produit.models.group_based_upload_to),
        ),
    ]
