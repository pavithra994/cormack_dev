# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-02-22 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0033_auto_20180222_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('number', models.CharField(max_length=50, verbose_name='Purchase Order Number')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Purchase Order Value')),
                ('details', models.CharField(blank=True, max_length=255, null=True, verbose_name='Purchase Order Number')),
            ],
            options={
                'verbose_name_plural': 'Job Purchase Orders',
                'verbose_name': 'Job Purchase Order',
                'db_table': 'job_purchase_order',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='purchase_orders',
            field=models.ManyToManyField(to='api.JobPurchaseOrder'),
        ),
    ]