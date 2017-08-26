# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-11 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0022_auto_20170806_1613'),
        ('collection', '0002_collection_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='produit',
        ),
        migrations.AddField(
            model_name='collection',
            name='produit',
            field=models.ManyToManyField(to='produit.Produit'),
        ),
    ]
