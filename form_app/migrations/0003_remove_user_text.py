# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0002_user_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='text',
        ),
    ]
