# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-08 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0012_auto_20180108_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='email',
            field=models.EmailField(default='no email', max_length=254),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='username',
            field=models.CharField(default='no Username', max_length=30),
            preserve_default=False,
        ),
    ]
