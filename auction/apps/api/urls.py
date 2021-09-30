#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from apps.api.views import auth
from apps.api.views import topic
from apps.api.views import agreePoint
from apps.api.views import agreeMessage
from apps.api.views import coupon
from apps.api.views import order

urlpatterns = [
    url(r'^msg/', auth.MessageView.as_view()),
    url(r'^login/', auth.LoginView.as_view()),
    url(r'^oss/credential/$', auth.OssCredentialView.as_view()),

    # 首页通知
    url(r'^agreeMessage/$', agreeMessage.AgreeMessageView.as_view()),
    url(r'^agreeMessage/(?P<pk>\d+)/$', agreeMessage.AgreeMessageDetailView.as_view()),


    # 话题
    url(r'^agreeTopic/$', topic.TopicView.as_view()),

    url(r'^agreePoint/$', agreePoint.AgreePointView.as_view()),
    url(r'^agreePoint/(?P<pk>\d+)/$', agreePoint.AgreePointDetailView.as_view()),

    url(r'^agreePoint/favor/$', agreePoint.AgreePointFavorView.as_view()),
    url(r'^comment/$', agreePoint.CommentView.as_view()),
    url(r'^comment/favor/$', agreePoint.CommentFavorView.as_view()),
    url(r'^follow/$', agreePoint.FollowView.as_view()),
    url(r'^auction/deposit/(?P<pk>\d+)/$', agreeMessage.AuctionDepositView.as_view()),
    url(r'^pay/deposit/$', agreeMessage.PayDepositView.as_view()),
    url(r'^pay/deposit/notify/$', agreeMessage.PayDepositNotifyView.as_view()),
    url(r'^bid/$', agreeMessage.BidView.as_view()),
    # 优惠券
    url(r'^coupon/$', coupon.CouponView.as_view()),
    url(r'^user/coupon/$', coupon.UserCouponView.as_view()),
    url(r'^choose/coupon/$', coupon.ChooseCouponView.as_view()),
    # 订单
    url(r'^order/$', order.OrderView.as_view()),
    url(r'^pay/(?P<pk>\d+)/$', order.PayView.as_view()),
    url(r'^pay/now/$', order.PayNowView.as_view()),
    url(r'^address/$', order.AddressView.as_view()),

]
