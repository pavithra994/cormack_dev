# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-14 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0102_auto_20191009_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='piers_concrete_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='piers_concrete_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
    ]