from django.conf.urls import url

from apps.web.views import agreeMessage, agreeTopic, agreeDepart, auth

urlpatterns = [
    url(r"login/", auth.login, name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^index/$', auth.index, name='index'),

    # 通知管理
    url(r'^agreeMessage/list/$', agreeMessage.agreeMessage_list, name='agreeMessage_list'),
    url(r'^agreeMessage/add/$', agreeMessage.agreeMessage_add, name='agreeMessage_add'),
    url(r'^agreeMessage/add/uploadImg/', agreeMessage.agreeMessage_uploadImg),
    url(r'^agreeMessage/delete/(?P<pk>\d+)/$', agreeMessage.agreeMessage_delete, name='agreeMessage_delete'),
    url(r'^agreeMessage/edit/(?P<pk>\d+)/$', agreeMessage.agreeMessage_edit, name='agreeMessage_edit'),

    # 话题管理
    url(r'^agreeTopic/list/$', agreeTopic.agreeTopic_list, name='agreeTopic_list'),
    url(r'^agreeTopic/add/$', agreeTopic.agreeTopic_add, name='agreeTopic_add'),
    url(r'^agreeTopic/edit/(?P<pk>\d+)/$', agreeTopic.agreeTopic_edit, name='agreeTopic_edit'),
    url(r'^agreeTopic/delete/(?P<pk>\d+)/$', agreeTopic.agreeTopic_delete, name='agreeTopic_delete'),

    # 部门管理
    url(r'^agreeDepart/list/$', agreeDepart.agreeDepart_list, name='agreeDepart_list'),
    url(r'^agreeDepart/add/$', agreeDepart.agreeDepart_add, name='agreeDepart_add'),
    url(r'^agreeDepart/edit/(?P<pk>\d+)/$', agreeDepart.agreeDepart_edit, name='agreeDepart_edit'),
    url(r'^agreeDepart/delete/(?P<pk>\d+)/$', agreeDepart.agreeDepart_delete, name='agreeDepart_delete'),

    # 赞书管理

    # 用户管理

]
