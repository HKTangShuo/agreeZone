from rest_framework.generics import ListAPIView, RetrieveAPIView
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


class AgreeMessageDetailView(RetrieveAPIView):
    """通知+通知详情接口"""
    queryset = models.AgreeMessage.objects
    serializer_class = AgreeMessageModelSerializer


class AgreePointDetailView(RetrieveAPIView):
    """
    TODO 待完成 围观数+1
    获取动态详细接口
    """
    queryset = models.AgreePoint.objects
    # serializer_class =
