# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2017-12-12 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171207_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('key', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]