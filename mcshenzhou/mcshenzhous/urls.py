#coding=utf-8
from django.conf.urls import include, url
from . import views

urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    #介绍服务器
    url(r'^intro1$', views.intro1, name='intro1'),
    #介绍内部人员
    url(r'^intro2$', views.intro2, name='intro2'),
    #介绍声明
    url(r'^intro3$', views.intro3, name='intro3'),
    #内部人员:服主
    url(r'^op1$', views.op1, name='op1'),
    #内部人员：爱天骑
    url(r'^op2$', views.op2, name='op2'),
    #内部人员：韩壮士
    url(r'^op3$', views.op3, name='op3'),
    #内部人员：eatsalt
    url(r'^op4$', views.op4, name='op4'),
    #内部人员:DONY010
    url(r'^op5$', views.op5, name='op5'),
    #内部人员:初恋_狼王的荣耀
    url(r'^op6$', views.op6, name='op6'),
    #内部人员：shadow
    url(r'^op7$', views.op7, name='op7'),
    #内部人员:电脑
    url(r'^op8$', views.op8, name='op8'),
    #内部人员：小可爱来了哇
    url(r'^op9$', views.op9, name='op9'),
    #内部人员：梦中梦见梦幻
    url(r'^op10$', views.op10, name='op10'),
    #内部人员:DGKLPD
    url(r'^op11$', views.op11, name='op11'),
]
