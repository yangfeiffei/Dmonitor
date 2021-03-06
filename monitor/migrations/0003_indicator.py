# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-30 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20160930_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=32, null=True, verbose_name='指标名')),
                ('types', models.CharField(choices=[('cpu', 'CPU'), ('mem', 'Memory'), ('io', 'IO'), ('network', 'Network')], max_length=16, verbose_name='类型')),
                ('parameter', models.CharField(max_length=16, verbose_name='指标参数')),
            ],
        ),
    ]
