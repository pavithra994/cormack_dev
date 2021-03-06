# -*- coding: utf-8 -*-

#
#  Copyright (C) 2019 Ocom Software- All Rights Reserved
#  Unauthorized copying of this file, via any medium is strictly prohibited
#  Proprietary and confidential
#  Written by Ocom Software <licence@ocom.com.au, 2019
#
#

# Generated by Django 1.10.7 on 2017-12-06 01:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('name', models.TextField()),
                ('xero_customer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Xero Customer')),
                ('send_invoices', models.BooleanField(default=True, verbose_name='Send Invoices')),
                ('required_part_a', models.BooleanField(default=True, verbose_name='Part A Required?')),
                ('they_supply_pump', models.BooleanField(default=False, verbose_name='They Supply Pump')),
                ('they_supply_etc', models.BooleanField(default=False, verbose_name='They Supply Etc.')),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='CodeDrainType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_drain_type',
                'verbose_name_plural': 'Drain Types',
                'verbose_name': 'Drain Type',
            },
        ),
        migrations.CreateModel(
            name='CodeFileType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_file_type',
                'verbose_name_plural': 'File Types',
                'verbose_name': 'File Type',
            },
        ),
        migrations.CreateModel(
            name='CodeJobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_job_type',
                'verbose_name_plural': 'Job Types',
                'verbose_name': 'Job Type',
            },
        ),
        migrations.CreateModel(
            name='CodePavingColour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_paving_colour',
                'verbose_name_plural': 'Paving Colours',
                'verbose_name': 'Paving Colour',
            },
        ),
        migrations.CreateModel(
            name='CodePavingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_paving_type',
                'verbose_name_plural': 'Paving Types',
                'verbose_name': 'Paving Type',
            },
        ),
        migrations.CreateModel(
            name='CodeRepairType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_repair_type',
                'verbose_name_plural': 'Repair Types',
                'verbose_name': 'Repair Type',
            },
        ),
        migrations.CreateModel(
            name='CodeSupplierType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_supplier_type',
                'verbose_name_plural': 'Supplier Types',
                'verbose_name': 'Supplier Type',
            },
        ),
        migrations.CreateModel(
            name='CodeTaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
            ],
            options={
                'db_table': 'code_task_type',
                'verbose_name_plural': 'Task Types',
                'verbose_name': 'Task Type',
            },
        ),
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('_is_deleted', models.BooleanField(default=False)),
                ('_display_order', models.IntegerField(default=0)),
                ('file', models.FileField(blank=True, max_length=512, null=True, upload_to='uploads')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('who_uploaded', models.CharField(blank=True, max_length=255, null=True, verbose_name='Who Uploaded')),
                ('when_uploaded', models.DateTimeField(auto_now_add=True, null=True)),
                ('url_guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('file_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CodeFileType')),
            ],
            options={
                'db_table': 'file_upload',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('date_received', models.DateField(verbose_name='Date Received')),
                ('comments', models.TextField(blank=True, null=True)),
                ('address', models.TextField()),
                ('suburb', models.CharField(blank=True, max_length=255, null=True, verbose_name='Suburb')),
                ('purchase_order_number', models.TextField()),
                ('job_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Job Number')),
                ('purchase_order_value', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Purchase Order Value')),
                ('sqm', models.IntegerField(verbose_name='SQM')),
                ('pour_date', models.DateTimeField(blank=True, null=True, verbose_name='Pour Date')),
                ('base_inspection_date', models.DateTimeField(blank=True, null=True, verbose_name='Base Inspection Date')),
                ('steel_inspection_date', models.DateTimeField(blank=True, null=True, verbose_name='Steel Inspection Date')),
                ('rock_m3', models.DateField(blank=True, null=True, verbose_name='Rock (m3)')),
                ('rock_booked_date', models.DateTimeField(blank=True, null=True, verbose_name='Rock Booked Date')),
                ('materials', models.DateField(blank=True, null=True, verbose_name='Materials')),
                ('materials_time', models.CharField(blank=True, max_length=255, null=True, verbose_name='Materials Time')),
                ('has_part_a', models.BooleanField(default=False, verbose_name='Has Part A')),
                ('part_a_date', models.DateTimeField(blank=True, null=True, verbose_name='Part A Date')),
                ('part_a_booking_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Part A Booking Number')),
                ('waste_date', models.DateTimeField(blank=True, null=True, verbose_name='Waste Date')),
                ('piers_date', models.DateTimeField(blank=True, null=True, verbose_name='Piers Date')),
                ('piers_inspection_date', models.DateTimeField(blank=True, null=True, verbose_name='Piers Inspection Date')),
                ('piers_concrete_date', models.DateTimeField(blank=True, null=True, verbose_name='Piers Concrete Date')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('call_up_date', models.DateField(blank=True, null=True, verbose_name='Call Up Date')),
                ('take_off_sent', models.DateField(blank=True, null=True, verbose_name='Take Off Sent')),
                ('proposed_start_date', models.DateField(blank=True, null=True, verbose_name='Proposed Start Date')),
                ('excavation_allowance', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Excavation Allowance')),
                ('date_cancelled', models.DateField(blank=True, null=True, verbose_name='Date Cancelled')),
                ('drains', models.IntegerField(default=0, verbose_name='Drains (m)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Client', verbose_name='Client')),
                ('drain_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CodeDrainType', verbose_name='Drain Type')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CodeJobType', verbose_name='Job Type')),
                ('paving_colour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CodePavingColour', verbose_name='Paving Colour')),
                ('paving_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CodePavingType', verbose_name='Paving Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('item', models.CharField(max_length=100, verbose_name='Item')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Unit Price')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Total Price')),
                ('invoiced', models.BooleanField(default=False, verbose_name='Invoiced')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JobTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('description', models.TextField()),
                ('date_scheduled', models.DateField(blank=True, null=True, verbose_name='Date Scheduled')),
                ('complete_date', models.DateTimeField(blank=True, null=True, verbose_name='Complete Date')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('_is_deleted', models.BooleanField(default=False)),
                ('_display_order', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, null=True)),
                ('who', models.CharField(blank=True, max_length=255, null=True, verbose_name='Who')),
                ('when', models.DateTimeField(auto_now_add=True, null=True)),
                ('hide', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'note',
            },
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('date_received', models.DateField(verbose_name='Date Received')),
                ('po_number', models.CharField(max_length=255, verbose_name='PO Number')),
                ('accepted_date', models.DateField(blank=True, null=True, verbose_name='Accepted Date')),
                ('rejected_date', models.DateField(blank=True, null=True, verbose_name='Rejected Date')),
                ('back_charge', models.BooleanField(default=False)),
                ('permit_no', models.CharField(blank=True, max_length=255, null=True, verbose_name='Permit Number')),
                ('due_date', models.DateField(verbose_name='Due Date')),
                ('start_by', models.DateField(verbose_name='Start By')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Job')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepairCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('item', models.CharField(max_length=100, verbose_name='Item')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Unit Price')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Total Price')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('administrator', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'db_table': 'role',
                'verbose_name_plural': 'Users and Roles',
                'verbose_name': 'User and Role',
            },
        ),
        migrations.CreateModel(
            name='Subbie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('name', models.TextField()),
                ('xero_supplier', models.CharField(blank=True, max_length=100, null=True, verbose_name='Xero Supplier')),
                ('rate_per_m', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Rate Per Meter')),
                ('jobs_per_day', models.IntegerField(default=1, verbose_name='Jobs Per Day')),
                ('can_see_plans_before_accept', models.BooleanField(default=False, verbose_name='Can See Plans Before Accept')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('enabled', models.BooleanField(default=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.CodeSupplierType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('active_start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Active Start Date')),
                ('active_end_date', models.DateTimeField(blank=True, null=True, verbose_name='Active End Date')),
                ('name', models.TextField()),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('enabled', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone Number')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='repair',
            name='repair_subbie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subbie', verbose_name='Repair Subbie'),
        ),
        migrations.AddField(
            model_name='repair',
            name='repair_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CodeRepairType', verbose_name='Repair Type'),
        ),
        migrations.AddField(
            model_name='jobtask',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Subbie', verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='jobtask',
            name='task_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CodeTaskType', verbose_name='Task Type'),
        ),
        migrations.AddField(
            model_name='job',
            name='sub_contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Subbie', verbose_name='SubContractor'),
        ),
        migrations.AddField(
            model_name='job',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Supervisor', verbose_name='Supervisor'),
        ),
        migrations.AddField(
            model_name='client',
            name='suppliers',
            field=models.ManyToManyField(to='api.Subbie'),
        ),
    ]
