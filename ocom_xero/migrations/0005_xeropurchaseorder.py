# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-03-05 00:31
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocom_xero', '0004_xeroconnection'),
    ]

    operations = [
        migrations.CreateModel(
            name='XeroPurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('other_id', models.IntegerField(db_index=True, null=True, verbose_name='Other ID')),
                ('other_name', models.CharField(db_index=True, max_length=50, null=True, verbose_name='Other Name')),
                ('purchase_order_number', models.CharField(db_index=True, max_length=50, verbose_name='Purchase Order No.')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Total Amount')),
                ('purchase_order', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Purchase Order Response')),
            ],
            options={
                'verbose_name_plural': 'Purchase Orders',
                'db_table': 'xero_purchase_order',
                'verbose_name': 'Purchase Order',
            },
        ),
    ]
