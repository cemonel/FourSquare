# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-22 14:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20180122_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='search',
            old_name='food',
            new_name='venue',
        ),
    ]
