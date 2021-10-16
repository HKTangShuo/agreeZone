#!/usr/bin/env python
# -*- coding:utf-8 -*-

DEBUG = True
ALLOWED_HOSTS = ['*']

# wx小程序
WX_APPID = 'wxc00033f1d87fd79b'
WX_SECRET = 'cea39c64d0e976b81cf47884762164f8'
WX_GRANT_TYPE = 'authorization_code'

# 腾讯云对象存储
OOS_SECRET_ID = 'AKIDLl4C9vEFgx2vd98giXAdu1wfJm29QRlw'
OOS_SECRET_KEY = 'Bk9NXnuBJGhy5ztdBcBYnpysWMUpunYB'
OOS_BUCKET = 'agree-1300971352'
OOS_REGION = 'ap-nanjing'

SMS_EXPIRED_TIME = 60
# 测试用 线上改为True
SMS_ENABLE = False
# 腾讯云短信
SMS_RANDOM_CODE = 6666
SMS_TEMPLATE_ID = '571053'
SMS_SDK_APPID = 1400345192
SMS_SECRET_ID = 'AKIDLl4C9vEFgx2vd98giXAdu1wfJm29QRlw'
SMS_SECRET_KEY = 'Bk9NXnuBJGhy5ztdBcBYnpysWMUpunYB'
SMS_SIGN_NAME = '我就装B怎么了'
SMS_REGION = 'ap-guangzhou'

# celery 定时任务
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_TASK_SERIALIZER = 'json'
