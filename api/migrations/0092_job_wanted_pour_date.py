# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-05-21 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0091_job_drain_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='wanted_pour_date',
            field=models.DateField(blank=True, null=True, verbose_name='Wanted Pour Date'),
        ),
    ]