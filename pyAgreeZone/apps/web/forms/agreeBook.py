import uuid

from django import forms
from django.db.models.fields.files import FieldFile
from django.forms import widgets

from apps.api import models
from apps.web.forms.bootstrap import BootStrapModelForm
from utils.tencent.cos import upload_file


class AgreeBookModelForm(BootStrapModelForm):
    exclude_bootstrap_class = ['cover', 'url']
    content = forms.CharField(label='内容', widget=widgets.Textarea(attrs={'class': 'form-control'}),
                              error_messages={'required': "该字段是必填项！"})

    class Meta:
        model = models.AgreeBook
        exclude = ['read_count']
        # 页面显示顺序
        fields = ['cover', 'title', 'author', 'url', 'desc', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        # 上传文件
        cover_file_object = cleaned_data.get('cover')
        book_file_object = cleaned_data.get('url')

        if not isinstance(cover_file_object, FieldFile):
            ext = cover_file_object.name.rsplit('.', maxsplit=1)[-1]
            file_name = "{0}.{1}".format(str(uuid.uuid4()), ext)
            cleaned_data['cover'] = upload_file(cover_file_object, file_name)

        if not isinstance(book_file_object, FieldFile):
            ext = book_file_object.name.rsplit('.', maxsplit=1)[-1]
            file_name = "{0}.{1}".format(str(uuid.uuid4()), ext)
            cleaned_data['url'] = upload_file(book_file_object, file_name)

        return cleaned_data
