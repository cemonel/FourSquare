# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='food',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='search',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
    ]