#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
import json
import os
import uuid
import datetime
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from apps.api import models
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from apps.web.forms.agreeMessage import AgreeMessageModelForm

from apps.web import tasks
from pyAgreeZone import settings


def agreeMessage_list(request):
    queryset = models.AgreeMessage.objects.all().order_by('-id')
    return render(request, 'web/agreeMessage_list.html', {'queryset': queryset})


def agreeMessage_add(request):
    if request.method == 'GET':
        ctime = datetime.datetime.now()
        form = AgreeMessageModelForm(
            initial={
                'start_time': ctime + datetime.timedelta(minutes=5),
                'end_time': ctime + datetime.timedelta(days=10),
            }
        )
        return render(request, 'web/agreeMessage_add.html', {'form': form, "formTitle": '添加通知'})
    form = AgreeMessageModelForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        instance = form.save()
        # celery定时任务
        # 定时任务 通知未开始--> 开始
        message_start_datetime = datetime.datetime.utcfromtimestamp(form.instance.start_time.timestamp())
        start_task_id = tasks.to_start_agreeMessage_task.apply_async(args=[instance.id],
                                                                     eta=message_start_datetime).id
        # 定时任务 通知开始 -> 结束
        message_end_datetime = datetime.datetime.utcfromtimestamp(form.instance.end_time.timestamp())
        end_task_id = tasks.to_end_agreeMessage_task.apply_async(args=[instance.id], eta=message_end_datetime).id

        models.AgreeMessageTask.objects.create(
            task=start_task_id,
            end_task=end_task_id,
            agreeMessage=instance
        )

        return redirect('agreeMessage_list')
    return render(request, 'web/agreeMessage_add.html',
                  {'form': form, "formTitle": '添加通知', 'content': request.POST.get('content')})


def agreeMessage_delete(request, pk):
    models.AgreeMessage.objects.filter(id=pk).delete()
    return JsonResponse({'status': True})


def agreeMessage_edit(request, pk):
    msg = models.AgreeMessage.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = AgreeMessageModelForm(instance=msg)
        return render(request, 'web/agreeMessage_add.html', {'form': form, "formTitle": '编辑通知'})
    form = AgreeMessageModelForm(data=request.POST, files=request.FILES, instance=msg)
    if form.is_valid():
        # 修改定时任务：如果时间不一致，则修改定时任务执行时间
        # 1.时间如果时间有变更 form.changed_data
        value = form.changed_data
        form.save()
        return redirect('agreeMessage_list')
    return render(request, 'web/agreeMessage_add.html', {'form': form})


def agreeMessage_uploadImg(request):
    # TODO 先实现，有空后面再优化
    img = request.FILES.get('imgFile')

    path = os.path.join(settings.MEDIA_ROOT, 'messageImg', img.name)
    with open(path, 'wb') as f:
        for line in img:
            f.write(line)

    response = {
        'error': 0,
        'url': '/media/messageImg/%s' % img.name
    }
    return HttpResponse(json.dumps(response))
