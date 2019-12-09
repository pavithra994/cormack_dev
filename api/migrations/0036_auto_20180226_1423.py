# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-02-26 03:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_client_number_of_purchase_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobtask',
            name='active_end_date',
        ),
        migrations.RemoveField(
            model_name='jobtask',
            name='active_start_date',
        ),
    ]