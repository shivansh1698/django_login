# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0004_auto_20171223_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='text',
            field=models.CharField(default='no text', max_length=100),
            preserve_default=False,
        ),
    ]
