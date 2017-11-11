# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-23 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('client_number', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.IntegerField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_number', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('cell_phone', models.IntegerField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('item_number', models.IntegerField()),
                ('item_type', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('qty_on_hand', models.IntegerField(max_length=10)),
                ('expired_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Donor',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='investment',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='customer',
        ),
        migrations.RenameField(
            model_name='donor',
            old_name='cust_number',
            new_name='donor_number',
        ),
        migrations.DeleteModel(
            name='Fund',
        ),
        migrations.DeleteModel(
            name='Investment',
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]