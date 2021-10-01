# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-10-01 01:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211001_0950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=11, verbose_name='部门名')),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='depart',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Department', verbose_name='部门'),
        ),
    ]