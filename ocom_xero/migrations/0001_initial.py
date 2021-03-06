# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-02-14 03:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='XeroInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('other_id', models.IntegerField(null=True, verbose_name='Other ID')),
                ('other_name', models.CharField(max_length=50, null=True, verbose_name='Other Name')),
                ('invoice_number', models.CharField(max_length=50, verbose_name='Invoice No.')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Total Amount')),
                ('invoice', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='Invoice Response')),
            ],
            options={
                'verbose_name': 'Invoice',
                'db_table': 'xero_invoice',
                'verbose_name_plural': 'Invoices',
            },
        ),
    ]
