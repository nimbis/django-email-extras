# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-18 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_extras', '0004_use_djangos_emailfield'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='key',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Key',
        ),
    ]
