# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-14 02:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_commentrecord_root'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='follow',
            field=models.ManyToManyField(blank=True, null=True, related_name='_userinfo_follow_+', to='api.UserInfo', verbose_name='关注'),
        ),
    ]