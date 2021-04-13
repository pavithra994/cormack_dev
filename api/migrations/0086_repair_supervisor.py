# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-25 05:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0085_repaircost_invoiced'),
    ]

    operations = [
        migrations.AddField(
            model_name='repair',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Supervisor', verbose_name='Supervisor'),
        ),
    ]
