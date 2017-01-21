# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0034_document_terms_count'),
        ('models', '0019_auto_20170119_1132'),
        ('visual', '0009_polygon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polygon',
            old_name='title',
            new_name='label',
        ),
        migrations.AddField(
            model_name='polygon',
            name='document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.Document'),
        ),
        migrations.AddField(
            model_name='polygon',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='models.ArtmModel'),
        ),
    ]
