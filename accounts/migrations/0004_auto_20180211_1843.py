# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180211_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user2',
            name='user',
            field=models.CharField(max_length=120),
        ),
    ]
