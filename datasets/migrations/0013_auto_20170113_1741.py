# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 17:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0012_dataset_time_provide'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='time_provide',
            new_name='time_provided',
        ),
    ]