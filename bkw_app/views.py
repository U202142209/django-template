# encoding: utf-8
'''
 @author :我不是大佬 
 @contact:2869210303@qq.com
 @wx     ;safeseaa
 @qq     ;2869210303
 @github ;https://github.com/U202142209
 @blog   ;https://blog.csdn.net/V123456789987654 
 @file   :views.py
 @time   :2024/8/31 16:05
  '''

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")