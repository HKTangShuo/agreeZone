# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-17 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_auto_20200117_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositrecord',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, '未支付'), (2, '支付成功')], default=1, verbose_name='状态'),
        ),
    ]