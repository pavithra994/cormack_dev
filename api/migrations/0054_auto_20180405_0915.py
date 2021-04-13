# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-04-04 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20180319_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='piers_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Proposed Piers Date'),
        ),
        migrations.AlterField(
            model_name='job',
            name='pour_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Proposed Pour Date'),
        ),
        migrations.AlterField(
            model_name='jobcost',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='repaircost',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Quantity'),
        ),
    ]
