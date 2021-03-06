# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-23 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0111_auto_20191023_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('name', models.CharField(max_length=255, verbose_name='Depot Name')),
                ('color', models.CharField(blank=True, max_length=255, null=True, verbose_name='Depot Color')),
            ],
            options={
                'verbose_name': 'Depot',
                'verbose_name_plural': 'Depot Name',
                'db_table': 'depot',
            },
        ),
    ]
