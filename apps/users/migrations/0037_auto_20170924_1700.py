# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 11:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0036_cardstatus_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardstatus',
            name='membership',
        ),
        migrations.AlterField(
            model_name='cardstatus',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='card_status', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]