# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 00:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sampleset',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samplesets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='samplesetversion',
            name='sampleset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='api.Sampleset'),
        ),
    ]
