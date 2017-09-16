# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0011_timelineevent_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_locations/'),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='slug',
            field=models.SlugField(blank=True, help_text='Leave empty/unchanged for default slug.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_thumbnails/'),
        ),
        migrations.AlterField(
            model_name='timelineevent',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='timeline_event_thumbnails/'),
        ),
    ]