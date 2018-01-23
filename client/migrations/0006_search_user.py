# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-23 13:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0005_auto_20180122_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]