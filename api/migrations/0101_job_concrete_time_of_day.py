# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-02 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0100_job_base_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='concrete_time_of_day',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='concrete_time_of_day', to='api.CodeTimeOfDay', verbose_name='Time Of Day'),
        ),
    ]