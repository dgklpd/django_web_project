#coding=utf-8
from django.conf.urls import include, url

from . import views

urlpatterns = [
    #1
    url(r'^a1$', views.a1, name='a1')
    ]
