# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2017-12-14 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20171213_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='sqm',
            field=models.IntegerField(blank=True, null=True, verbose_name='SQM'),
        ),
    ]
