# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='text',
            field=models.CharField(default='empty text', max_length=100),
            preserve_default=False,
        ),
    ]
