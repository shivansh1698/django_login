# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0003_remove_user_text'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='users',
        ),
    ]
