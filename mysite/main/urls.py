#coding=utf-8
from django.conf.urls import include, url

from . import views

urlpatterns = [
    #index
    url(r'^$', views.index, name='index'),
]