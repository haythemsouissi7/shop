# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0017_auto_20170724_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='Picture',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='username',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]
