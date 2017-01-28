# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0044_auto_20170128_2225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='vw_bow_provided',
            new_name='vw_provided',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='vw_plain_provided',
        ),
        migrations.AddField(
            model_name='document',
            name='text_id',
            field=models.TextField(null=True),
        ),
    ]
