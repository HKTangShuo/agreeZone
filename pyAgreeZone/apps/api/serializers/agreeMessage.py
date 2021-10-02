#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework import serializers
from apps.api import models


class AgreeMessageModelSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    cover = serializers.CharField()

    class Meta:
        model = models.AgreeMessage
        fields = ['id', 'title', 'status', 'cover', 'look_count','content']

    def get_status(self, obj):
        status_class_mapping = {
            2: 'preview',
            3: 'pyAgreeZone',
            4: 'stop'
        }
        return {'text': obj.get_status_display(), 'class': status_class_mapping.get(obj.status)}
