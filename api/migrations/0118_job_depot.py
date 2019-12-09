# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-23 11:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0117_auto_20191023_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='depot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.Depot', verbose_name='Depot'),
        ),
    ]