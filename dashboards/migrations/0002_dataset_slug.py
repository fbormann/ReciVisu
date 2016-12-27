# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 01:24
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='test', editable=False, populate_from='name', unique=True, verbose_name='Slug'),
        ),
    ]