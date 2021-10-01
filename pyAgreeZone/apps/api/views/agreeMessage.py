from rest_framework.generics import ListAPIView
from utils.pagination import RollLimitOffsetPagination
from utils.filters import ReachBottomFilter, PullDownRefreshFilter

from apps.api import models
from apps.api.serializers.agreeMessage import AgreeMessageModelSerializer


class AgreeMessageView(ListAPIView):
    """ 赞同通知接口"""
    queryset = models.AgreeMessage.objects.exclude(status=models.AgreeMessage.STATUS_NOT_START).order_by('-id')
    serializer_class = AgreeMessageModelSerializer
    filter_backends = [ReachBottomFilter, PullDownRefreshFilter]
    pagination_class = RollLimitOffsetPagination


