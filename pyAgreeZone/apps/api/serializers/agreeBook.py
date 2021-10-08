from rest_framework import serializers

from apps.api import models


class AgreeBookModelSerializer(serializers.ModelSerializer):
    cover = serializers.CharField()

    class Meta:
        model = models.AgreeBook
        fields = ['id', 'title', 'desc', 'cover', 'read_count', 'author']


class AgreeBookModelDetailSerializer(serializers.ModelSerializer):
    cover = serializers.CharField()

    class Meta:
        model = models.AgreeBook
        exclude = ['order', 'id']
