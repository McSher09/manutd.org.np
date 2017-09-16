# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notification', '0008_auto_20170718_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdevice',
            name='dev_id',
            field=models.CharField(max_length=50, unique=True, verbose_name='Device ID'),
        ),
        migrations.AlterField(
            model_name='userdevice',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Is active?'),
        ),
        migrations.AlterField(
            model_name='userdevice',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='userdevice',
            name='reg_id',
            field=models.CharField(max_length=255, unique=True, verbose_name='Registration ID'),
        ),
    ]