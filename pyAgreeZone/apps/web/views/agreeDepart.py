from django.http import JsonResponse
from django.shortcuts import render, redirect

from apps.api import models
from apps.api.models import Department
from apps.web.forms.agreeDepart import AgreeDepartModelForm


def agreeDepart_list(request):
    queryset = models.Department.objects.exclude(status=Department.STATUS_DELETE).all().order_by('-id')

    return render(request, 'web/agreeDepart_list.html', {'queryset': queryset})


def agreeDepart_delete(request, pk):
    models.Department.objects.filter(id=pk).update(status=Department.STATUS_DELETE)
    return JsonResponse({'status': True})


def agreeDepart_edit(request, pk):
    depart_object = models.Department.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = AgreeDepartModelForm(instance=depart_object)
        return render(request, 'web/common_form.html', {'form': form, "formTitle": "编辑部门"})
    form = AgreeDepartModelForm(data=request.POST, instance=depart_object)
    if form.is_valid():
        form.save()
        return redirect('agreeDepart_list')
    return render(request, 'web/common_form.html', {'form': form})


def agreeDepart_add(request):
    if request.method == 'GET':
        form = AgreeDepartModelForm()
        return render(request, 'web/common_form.html', {'form': form, "formTitle": "添加部门"})
    form = AgreeDepartModelForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect('agreeDepart_list')
    return render(request, 'web/common_form.html', {'form': form})
