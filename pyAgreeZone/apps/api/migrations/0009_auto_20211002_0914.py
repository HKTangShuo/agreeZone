# Generated by Django 2.1.8 on 2021-10-02 01:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20211002_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreemessage',
            name='video',
        ),
        migrations.AlterField(
            model_name='agreemessage',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=512, verbose_name='内容'),
        ),
    ]