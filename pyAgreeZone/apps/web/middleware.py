import re

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from pyAgreeZone import settings


class LoginMiddleware(MiddlewareMixin):
    """
    登录信息判断
    """

    def process_request(self, request):
        """
        当用户请求刚进入时候出发执行
        :param request:
        :return:
        """

        current_url = request.path_info
        for valid_url in settings.VALID_URL_LIST:
            if re.match(valid_url, current_url):
                # 白名单中的URL无需权限验证即可访问
                return None

        hasLogin = request.session.get(settings.SESSION_KEY)
        if not hasLogin:
            return redirect('/login/')
