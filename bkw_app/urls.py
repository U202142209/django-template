# encoding: utf-8
from django.urls import path
from .views import index

# http://127.0.0.1:8000/bkw_app/
urlpatterns = [
    path('', index, name='index'),
]
