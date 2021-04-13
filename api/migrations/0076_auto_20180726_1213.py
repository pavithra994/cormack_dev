# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-07-26 02:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0075_auto_20180725_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='notify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='cut_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Cut Date'),
        ),
    ]
