import json
import os
import datetime
from pyAgreeZone import celery_app
from celery.result import AsyncResult
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from apps.api import models
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
    # 取消定时任务
    task_obj = models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).first()
    task_start_result = AsyncResult(id=task_obj.task, app=celery_app)
    task_end_result = AsyncResult(id=task_obj.end_task, app=celery_app)
    task_start_result.revoke()
    task_end_result.revoke()
    models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).delete()
    models.AgreeMessage.objects.filter(id=pk).delete()
    return JsonResponse({'status': True})


def agreeMessage_edit(request, pk):
    msg = models.AgreeMessage.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = AgreeMessageModelForm(instance=msg)
        return render(request, 'web/agreeMessage_add.html', {'form': form, "formTitle": '编辑通知'})
    form = AgreeMessageModelForm(data=request.POST, files=request.FILES, instance=msg)
    if form.is_valid():
        # 如果时间不一致，则修改定时任务执行时间
        value = form.changed_data
        if ('start_time' in value):
            message_start_datetime = datetime.datetime.utcfromtimestamp(form.cleaned_data['start_time'].timestamp())

            # 更新状态
            ctime = datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp())
            if ctime < message_start_datetime:
                form.cleaned_data['status'] = models.AgreeMessage.STATUS_NOT_START
                models.AgreeMessage.objects.filter(id=pk).update(status=models.AgreeMessage.STATUS_NOT_START)
            else:
                models.AgreeMessage.objects.filter(id=pk).update(status=models.AgreeMessage.STATUS_START)

            # 定时任务处理
            task_obj = models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).first()
            task_start_result = AsyncResult(id=task_obj.task, app=celery_app)
            task_start_result.revoke()

            start_task_id = tasks.to_start_agreeMessage_task.apply_async(args=[pk],
                                                                         eta=message_start_datetime).id

            models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).update(task=start_task_id)

        if ('end_time' in value):
            task_obj = models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).first()
            task_end_result = AsyncResult(id=task_obj.end_task, app=celery_app)
            task_end_result.revoke()

            message_end_datetime = datetime.datetime.utcfromtimestamp(form.cleaned_data['end_time'].timestamp())
            end_task_id = tasks.to_end_agreeMessage_task.apply_async(args=[pk],
                                                                     eta=message_end_datetime).id
            models.AgreeMessageTask.objects.filter(agreeMessage_id=pk).update(end_task=end_task_id)

            # 更新状态
            ctime = datetime.datetime.utcfromtimestamp(datetime.datetime.now().timestamp())
            if ctime > message_end_datetime:
                models.AgreeMessage.objects.filter(id=pk).update(status=models.AgreeMessage.STATUS_END)
            else:
                models.AgreeMessage.objects.filter(id=pk).update(status=models.AgreeMessage.STATUS_START)
        # form.save()
        models.AgreeMessage.objects.filter(id=pk).update(**form.cleaned_data)
        return redirect('agreeMessage_list')
    else:
        return render(request, 'web/agreeMessage_add.html', {'form': form, 'errors': form.errors['__all__'][0]})


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
