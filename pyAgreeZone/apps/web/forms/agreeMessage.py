#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid

from django import forms
from django.db.models.fields.files import FieldFile
from django.forms import widgets

from apps.api import models
from utils.tencent.cos import upload_file

from .bootstrap import BootStrapModelForm


class AgreeMessageModelForm(BootStrapModelForm):
    exclude_bootstrap_class = ['cover']
    content = forms.CharField(label='内容', widget=widgets.Textarea(attrs={'class': 'form-control'}),
                              error_messages={'required': "该字段是必填项！"})

    class Meta:
        model = models.AgreeMessage
        exclude = ['status', 'look_count']
        # 页面显示顺序
        fields = ['title', 'cover', 'start_time', 'end_time', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        # 上传文件
        cover_file_object = cleaned_data.get('cover')
        if not cover_file_object or isinstance(cover_file_object, FieldFile):
            return cleaned_data

        ext = cover_file_object.name.rsplit('.', maxsplit=1)[-1]
        file_name = "{0}.{1}".format(str(uuid.uuid4()), ext)
        cleaned_data['cover'] = upload_file(cover_file_object, file_name)
        return cleaned_data
