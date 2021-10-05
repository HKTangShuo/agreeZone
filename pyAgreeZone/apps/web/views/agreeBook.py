import json
import os
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from apps.api import models
from apps.web.forms.agreeBook import AgreeBookModelForm
from pyAgreeZone import settings


def agreeBook_list(request):
    queryset = models.AgreeBook.objects.filter(~Q(status=models.AgreeBook.STATUS_DELETE)).all().order_by('-id')
    return render(request, 'web/agreeBook_list.html', {'queryset': queryset})


def agreeBook_add(request):
    if request.method == 'GET':
        form = AgreeBookModelForm()
        return render(request, 'web/agreeBook_add.html', {'form': form, "formTitle": '添加赞书'})
    form = AgreeBookModelForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('agreeBook_list')
    return render(request, 'web/agreeBook_list.html',
                  {'form': form, "formTitle": '添加赞书', 'content': request.POST.get('content')})


def agreeBook_delete(request, pk):
    models.AgreeBook.objects.filter(id=pk).update(status=models.AgreeBook.STATUS_DELETE)
    return JsonResponse({'status': True})


def agreeBook_edit(request, pk):
    book_obj = models.AgreeBook.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = AgreeBookModelForm(instance=book_obj)
        return render(request, 'web/agreeBook_add.html', {'form': form, "formTitle": '编辑赞书'})
    form = AgreeBookModelForm(data=request.POST, files=request.FILES, instance=book_obj)
    if form.is_valid():
        form.save()
        return redirect('agreeBook_list')
    return render(request, 'web/agreeBook_add.html', {'form': form})


def agreeBook_uploadImg(request):
    # TODO 先实现，有空后面再优化
    img = request.FILES.get('imgFile')

    path = os.path.join(settings.MEDIA_ROOT, 'bookImg', img.name)
    with open(path, 'wb') as f:
        for line in img:
            f.write(line)

    response = {
        'error': 0,
        'url': '/media/bookImg/%s' % img.name
    }
    return HttpResponse(json.dumps(response))
