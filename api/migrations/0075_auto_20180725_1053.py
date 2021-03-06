# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-07-25 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0074_auto_20180724_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='cut_and_sealed_date',
            new_name='cut_date'
        ),
        migrations.AddField(
            model_name='job',
            name='sealed_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Sealed Date'),
        ),
    ]
