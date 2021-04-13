# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-12-17 19:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0120_auto_20191029_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesupplier',
            name='supplier_type',
            field=models.ForeignKey(blank=True, db_index=False, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='code_supplier_type', to='api.CodeSupplierType', verbose_name='Supplier Type'),
        ),
        migrations.AlterField(
            model_name='job',
            name='building_inspector_supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job_building_inspector_supplier', to='api.CodeSupplier', verbose_name='Building Inspector Supplier'),
        ),
        migrations.AlterField(
            model_name='job',
            name='depot_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.CodeDepotType', verbose_name='Depot Type'),
        ),
        migrations.AlterField(
            model_name='job',
            name='piers_concrete_date',
            field=models.DateField(blank=True, null=True, verbose_name='Piers Concrete Date'),
        ),
    ]
