# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-23 14:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0014_auto_20180123_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
