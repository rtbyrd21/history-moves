# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 23:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0003_auto_20160925_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]