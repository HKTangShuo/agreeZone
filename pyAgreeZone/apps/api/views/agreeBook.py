from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.api import models
from apps.api.serializers.agreeBook import AgreeBookModelSerializer, AgreeBookModelDetailSerializer
from utils.filters import ReachBottomFilter, PullDownRefreshFilter
from utils.pagination import RollLimitOffsetPagination


class AgreeBookView(ListAPIView):
    """ 赞书接口"""
    queryset = models.AgreeBook.objects.exclude(status=models.AgreeBook.STATUS_DELETE).order_by('-order')
    serializer_class = AgreeBookModelSerializer
    filter_backends = [ReachBottomFilter, PullDownRefreshFilter]
    pagination_class = RollLimitOffsetPagination


class AgreeBookDetailView(RetrieveAPIView):
    queryset = models.AgreeBook.objects
    serializer_class = AgreeBookModelDetailSerializer
