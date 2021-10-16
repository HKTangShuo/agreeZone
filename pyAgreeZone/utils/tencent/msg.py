#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

from pyAgreeZone import settings
from utils.response import BaseResponse


def send_china_msg(phone, code):
    """
    发送短信
    :param code:短信验证码，如：86
    :param phone: 手机号，示例："15131255555"
    :return:
    """
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    response = BaseResponse()
    try:
        phone = "{}{}".format("+86", phone)
        cred = credential.Credential(settings.SMS_SECRET_ID, settings.SMS_SECRET_KEY)
        client = sms_client.SmsClient(cred, settings.SMS_REGION)

        req = models.SendSmsRequest()
        req.SmsSdkAppid = settings.SMS_SDK_APPID
        # 短信签名内容: 使用 UTF-8 编码，必须填写已审核通过的签名，签名信息可登录 [短信控制台] 查看
        req.Sign = settings.SMS_SIGN_NAME
        # 示例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号，最多不要超过200个手机号
        req.PhoneNumberSet = [phone, ]
        # 模板 ID: 必须填写已审核通过的模板 ID。模板ID可登录 [短信控制台] 查看
        req.TemplateID = settings.SMS_TEMPLATE_ID
        # 模板参数: 若无模板参数，则设置为空
        req.TemplateParamSet = [code, ]

        resp = client.SendSms(req)
        print(resp)

        response.message = resp.SendStatusSet[0].Message
        if resp.SendStatusSet[0].Code == "Ok":
            response.status = True

    except TencentCloudSDKException as err:
        response.message = err.message

    return response


if __name__ == '__main__':
    result = send_china_msg("999", "15595769530")
    print(result.status, result.message)
