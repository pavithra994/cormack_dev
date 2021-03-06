# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-03-05 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocom_xero', '0006_auto_20180305_1132'),
    ]

    operations = [
        migrations.DeleteModel(
            name='XeroInvoice',
        ),
        migrations.DeleteModel(
            name='XeroPurchaseOrder',
        ),
        migrations.AddField(
            model_name='xeroentity',
            name='other_id',
            field=models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Other ID'),
        ),
        migrations.AddField(
            model_name='xeroentity',
            name='other_name',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Other Name'),
        ),
    ]
