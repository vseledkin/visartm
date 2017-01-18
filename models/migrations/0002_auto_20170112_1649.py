# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 16:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datasets', '0010_remove_dataset_main_modality'),
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentInTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Document')),
            ],
        ),
        migrations.CreateModel(
            name='TopicInTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TopicInTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TopicRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='DocumentTopicRelation',
            new_name='TopicInDocument',
        ),
        migrations.AddField(
            model_name='artmmodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artmmodel',
            name='layers_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='artmmodel',
            name='main_modality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasets.Modality'),
        ),
        migrations.AddField(
            model_name='artmmodel',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='layer',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='topicrelated',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='topicrelated',
            name='topic1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk1', to='models.Topic'),
        ),
        migrations.AddField(
            model_name='topicrelated',
            name='topic2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fk2', to='models.Topic'),
        ),
        migrations.AddField(
            model_name='topicintopic',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='topicintopic',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='topicintopic',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='topicinterm',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='topicinterm',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Term'),
        ),
        migrations.AddField(
            model_name='topicinterm',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Topic'),
        ),
        migrations.AddField(
            model_name='documentintopic',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.ArtmModel'),
        ),
        migrations.AddField(
            model_name='documentintopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.Topic'),
        ),
    ]