# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-19 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lastname',
        ),
    ]