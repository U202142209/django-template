# encoding: utf-8
'''
 @author :我不是大佬 
 @contact:2869210303@qq.com
 @wx     ;safeseaa
 @qq     ;2869210303
 @github ;https://github.com/U202142209
 @blog   ;https://blog.csdn.net/V123456789987654 
 @file   :response.py
 @time   :2024/7/12 14:01
  '''

import datetime
from django.http import JsonResponse


class Response:
    @staticmethod
    def get_now_time():
        return datetime.datetime.now().strftime('%F %T')

    @staticmethod
    def setError(msg, error_code=500, data=None):
        return JsonResponse(
            data={
                "timestamp": Response.get_now_time(),
                "code": error_code,
                "msg": msg,
                "data": data,
            },
            json_dumps_params={'ensure_ascii': False},
            content_type="application/json; charset=utf-8"
        )

    @staticmethod
    def setSuccess(msg, data=None):
        return JsonResponse({
            "code": 200,
            "msg": msg,
            "data": data,
        },
            json_dumps_params={'ensure_ascii': False},
            content_type="application/json; charset=utf-8")
