import datetime
import uuid

from django import forms
from django.core.exceptions import ValidationError
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

    def is_valid_img(self, name):

        return name.endswith('png') or name.endswith('jpg') or name.endswith('jpeg')

    def clean_cover(self):
        cover = self.cleaned_data.get('cover')
        if not self.is_valid_img(cover.name):
            raise forms.ValidationError('图片名不合法')
        return cover

    def clean(self):
        if datetime.datetime.utcfromtimestamp(
                self.cleaned_data['start_time'].timestamp()) >= datetime.datetime.utcfromtimestamp(
            self.cleaned_data['end_time'].timestamp()):
            raise ValidationError('开始时间必须小于结束时间！')

        # 上传文件
        cleaned_data = self.cleaned_data
        cover_file_object = cleaned_data.get('cover')

        if not cover_file_object or isinstance(cover_file_object, FieldFile):
            return cleaned_data

        ext = cover_file_object.name.rsplit('.', maxsplit=1)[-1]
        file_name = "{0}.{1}".format(str(uuid.uuid4()), ext)
        cleaned_data['cover'] = upload_file(cover_file_object, file_name)
        return cleaned_data
