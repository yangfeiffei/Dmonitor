# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20161030_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='port',
            field=models.IntegerField(default=2375, verbose_name='docker\u8fd0\u884c\u7aef\u53e3'),
        ),
    ]