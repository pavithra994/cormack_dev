# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-07-18 04:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_auto_20180718_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='building_inspector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='building_inspector', to='api.Subbie', verbose_name='Building Inspector'),
        ),
        migrations.AddField(
            model_name='job',
            name='pod_delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Pod Delivery Date'),
        ),
        migrations.AddField(
            model_name='job',
            name='pod_delivery_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pod_delivery_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='steel_delivery_date',
            field=models.DateField(blank=True, null=True, verbose_name='Steel Delivery Date'),
        ),
        migrations.AddField(
            model_name='job',
            name='steel_delivery_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steel_delivery_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='termite_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='termite_supplier', to='api.Subbie', verbose_name='Termite Supplier'),
        ),
    ]
