from django.conf.urls import url
from apps.api.views import auth, agreeBook
from apps.api.views import agreeTopic
from apps.api.views import agreePoint
from apps.api.views import agreeMessage

urlpatterns = [
    url(r'^msg/', auth.MessageView.as_view()),
    url(r'^login/', auth.LoginView.as_view()),
    url(r'^oss/credential/$', auth.OssCredentialView.as_view()),

    # 话题
    url(r'^agreeTopic/$', agreeTopic.TopicView.as_view()),
    # 首页通知
    url(r'^agreeMessage/$', agreeMessage.AgreeMessageView.as_view()),
    url(r'^agreeMessage/(?P<pk>\d+)/$', agreeMessage.AgreeMessageDetailView.as_view()),

    # 赞点
    url(r'^agreePoint/$', agreePoint.AgreePointView.as_view()),
    url(r'^agreePoint/(?P<pk>\d+)/$', agreePoint.AgreePointDetailView.as_view()),
    url(r'^agreePoint/favor/$', agreePoint.AgreePointFavorView.as_view()),

    url(r'^comment/$', agreePoint.CommentView.as_view()),
    url(r'^comment/favor/$', agreePoint.CommentFavorView.as_view()),
    url(r'^follow/$', agreePoint.FollowView.as_view()),

    # 赞书
    url(r'^agreeBook/$', agreeBook.AgreeBookView.as_view()),
    url(r'^agreeBook/(?P<pk>\d+)/$', agreeBook.AgreeBookDetailView.as_view()),

]
