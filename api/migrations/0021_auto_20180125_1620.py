# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-01-25 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20180112_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='codetasktype',
            name='background_colour',
            field=models.CharField(default='#ffffff', max_length=128),
        ),
        migrations.AddField(
            model_name='codetasktype',
            name='foreground_colour',
            field=models.CharField(default='#8080ff', max_length=128),
        ),
    ]
