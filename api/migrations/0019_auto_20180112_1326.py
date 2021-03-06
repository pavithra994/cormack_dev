# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-01-12 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20180109_1737'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='rock_m3',
        ),
        migrations.AddField(
            model_name='job',
            name='rock_m3',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='Rock (m3)'),
        ),
        migrations.RemoveField(
            model_name='job',
            name='sqm',
        ),
        migrations.AddField(
            model_name='job',
            name='sqm',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='SQM'),
        ),
    ]
