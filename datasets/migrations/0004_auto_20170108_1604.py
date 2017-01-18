# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0003_auto_20170108_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.TextField(null=True)),
                ('snippet', models.TextField(null=True)),
                ('time', models.DateTimeField(null=True)),
                ('model_id', models.IntegerField()),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='document',
            unique_together=set([('dataset', 'model_id')]),
        ),
    ]