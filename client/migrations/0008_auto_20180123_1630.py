# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-23 13:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_auto_20180123_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
