# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-01 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('push_notification', '0002_bulkmessage_error_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkmessage',
            name='error_message',
            field=models.TextField(blank=True, help_text='Error Message', null=True),
        ),
    ]