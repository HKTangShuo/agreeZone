#!/usr/bin/env python
# -*- coding:utf-8 -*-
import uuid
from django.db.models.fields.files import FieldFile
from apps.api import models
from utils.tencent.cos import upload_file

from .bootstrap import BootStrapModelForm


class AgreeMessageModelForm(BootStrapModelForm):
    exclude_bootstrap_class = ['cover']

    class Meta:
        model = models.AgreeMessage
        exclude = ['status']

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





