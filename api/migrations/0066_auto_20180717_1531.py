# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2018-07-17 05:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0065_auto_20180717_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='base_inspection_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_inspection_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='part_a_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='part_a_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='piers_inspection_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piers_inspection_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='piers_concrete_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piers_concrete_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='piers_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='piers_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='pour_date_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pour_date_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='rock_booked_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rock_booked_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='steel_inspection_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steel_inspection_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
        migrations.AddField(
            model_name='job',
            name='waste_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='waste_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
    ]
