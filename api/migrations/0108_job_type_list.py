# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-10-17 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0107_auto_20191016_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type_list',
            field=models.TextField(blank=True, null=True),
        ),
    ]