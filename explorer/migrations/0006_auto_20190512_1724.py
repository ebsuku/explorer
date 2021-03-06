# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-12 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('explorer', '0005_auto_20190503_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dataset',
            name='version',
            field=models.IntegerField(default=2018),
        ),
        migrations.AddField(
            model_name='geography',
            name='source',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='geography',
            name='version',
            field=models.IntegerField(default=2018),
        ),
    ]
