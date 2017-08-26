# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-10 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produit', '0022_auto_20170806_1613'),
        ('authentication', '0002_utilisateur'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('discription', models.CharField(max_length=250)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.Utilisateur')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.Produit')),
            ],
        ),
    ]
