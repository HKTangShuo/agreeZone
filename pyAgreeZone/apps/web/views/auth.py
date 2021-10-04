from django.shortcuts import render, redirect

from apps.api.models import WebUserInfo
from pyAgreeZone import settings


def login(request):
    if request.method == "GET":
        return render(request, 'web/login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    current_user = WebUserInfo.objects.filter(name=user, password=pwd, status=WebUserInfo.STATUS_VALID).first()

    if not current_user:
        return render(request, 'web/login.html', {'msg': "用户名或密码错误!"})
    request.session[settings.SESSION_KEY] = {'id': current_user.id, 'nickname': current_user.nickname}
    # init_permission(current_user, request)
    return redirect('/index/')


def logout(request):
    request.session.flush()
    return redirect('/login/')


def index(request):
    return redirect('/agreeMessage/list/')
