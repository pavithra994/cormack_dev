# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-27 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0087_auto_20190327_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='no_job',
            field=models.BooleanField(default=False, verbose_name='Has No Job'),
        ),
    ]
