# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-02-23 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_auto_20180223_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='number_of_purchase_orders',
            field=models.IntegerField(default=1, verbose_name="Number of PO's to expect"),
        ),
    ]
