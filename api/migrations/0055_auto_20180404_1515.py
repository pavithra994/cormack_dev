# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-04-04 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0054_auto_20180404_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repair',
            name='po_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='PO Number'),
        ),
    ]
