# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0041_remove_term_matrix_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='tag_modality',
        ),
        migrations.RemoveField(
            model_name='dataset',
            name='word_modality',
        ),
        migrations.AddField(
            model_name='modality',
            name='index_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='modality',
            name='is_tag',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='modality',
            name='is_word',
            field=models.BooleanField(default=True),
        ),
    ]
