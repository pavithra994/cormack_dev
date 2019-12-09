# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-07-24 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0071_auto_20180723_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Code')),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Description')),
                ('active_start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Active End Date')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
                'verbose_name': 'Supplier',
                'db_table': 'code_supplier',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CodeSupplierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Code')),
                ('description', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Description')),
                ('active_start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Active End Date')),
                ('created_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Modified Date')),
            ],
            options={
                'verbose_name_plural': 'Supplier Types',
                'verbose_name': 'Supplier Type',
                'db_table': 'code_supplier_type',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='JobSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_date', models.DateField(blank=True, default=None, null=True, verbose_name='Book Date')),
                ('booking_number', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Booking Number')),
                ('book_time', models.ForeignKey(blank=True, db_index=False, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_supply_book_time', to='api.CodeTimeOfDay', verbose_name='Book Time')),
                ('supplier', models.ForeignKey(blank=True, db_index=False, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_supply_supplier', to='api.CodeSupplier', verbose_name='Supplier')),
                ('supplier_type', models.ForeignKey(blank=True, db_index=False, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_supply_supplier_type', to='api.CodeSupplierType', verbose_name='Supplier Type')),
            ],
            options={
                'verbose_name_plural': 'Job Supplies',
                'verbose_name': 'Job Supply',
                'db_table': 'job_supply',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='codesupplier',
            name='supplier_type',
            field=models.ForeignKey(blank=True, db_index=False, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='code_supplier_supplier_type', to='api.CodeSupplierType', verbose_name='Supplier Type'),
        ),
    ]
