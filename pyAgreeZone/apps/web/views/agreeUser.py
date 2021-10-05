from django.shortcuts import render

from apps.api import models


def agreeUser_list(request):
    queryset = models.UserInfo.objects.all().order_by('-id')
    return render(request, 'web/agreeUser_list.html', {'queryset': queryset})


def agreeUser_depart_deny(request, pk):
    models.UserInfo.objects.filter(id=pk).update(depart_status=models.UserInfo.DEPART_STATUS_INVALID)
    return agreeUser_list(request)


def agreeUser_depart_pass(request, pk):
    models.UserInfo.objects.filter(id=pk).update(depart_status=models.UserInfo.DEPART_STATUS_VALID)
    return agreeUser_list(request)
