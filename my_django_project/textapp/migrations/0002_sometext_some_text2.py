# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sometext',
            name='some_text2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
