#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyAgreeZone.settings")
django.setup()

from apps.api import models

result = models.Topic.objects.bulk_create([
    models.Topic(title='上班摸鱼'),
    models.Topic(title='下班去哪玩儿'),
    models.Topic(title='Java技术分享'),
    models.Topic(title='吐槽大会'),
])
print(result)
