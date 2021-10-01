from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.api import models
from apps.api.models import Topic
from apps.web.forms.agreeTopic import AgreeTopicModelForm


def agreeTopic_list(request):
    queryset = models.Topic.objects.exclude(status=Topic.STATUS_DELETE).all().order_by('-id')

    return render(request, 'web/agreeTopic_list.html', {'queryset': queryset})


def agreeTopic_delete(request, pk):
    models.Topic.objects.filter(id=pk).update(status=Topic.STATUS_DELETE)
    return JsonResponse({'status': True})


def agreeTopic_edit(request, pk):
    topic_object = models.Topic.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = AgreeTopicModelForm(instance=topic_object)
        return render(request, 'web/common_form.html', {'form': form, "formTitle": "编辑话题"})
    form = AgreeTopicModelForm(data=request.POST, instance=topic_object)
    if form.is_valid():
        form.save()
        return redirect('agreeTopic_list')
    return render(request, 'web/common_form.html', {'form': form})


def agreeTopic_add(request):
    if request.method == 'GET':
        form = AgreeTopicModelForm()
        return render(request, 'web/common_form.html', {'form': form, "formTitle": "添加话题"})
    form = AgreeTopicModelForm(data=request.POST, files=request.FILES)

    if form.is_valid():
        instance = form.save()
        return redirect('agreeTopic_list')
    return render(request, 'web/common_form.html', {'form': form})
