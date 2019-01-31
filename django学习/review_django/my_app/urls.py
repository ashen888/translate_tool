#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    # url是一个类 里面有三个参数
    url(r'^$',views.index),
    #这是正则的组 group(1) group(2) 括号里的就是给调用函数的参数
    # 参数名称以?P开头<user> 尖括号里面表示参数名称
    url(r'(?P<user>[1-9]{1}[0-9]{5,12})/(?P<password>\w+)',views.withargs),
    url(r'grade/$',views.grade),
    url(r'^students/',views.students),
    url(r'^grade/([0-9]+)$',views.select_stu),
    url(r'^add/students',views.add_students),
    url(r'^add/stuinfo',views.add_students),
    url(r'^get_attr',views.get_attr),
    url(r'^get_abc',views.get_abc),
    url(r'^get_list',views.get_list),
    url(r'register/$',views.register),
    url(r'register/login_success',views.receipt),
    url(r'response',views.response),
    url(r'cookie_test/',views.cookie_test),
    url(r'show_cookie/',views.show_cookie),
    url(r'Redirect1',views.Redirect1,name='r1'),
    url(r'Redirect2',views.Redirect2),
    # 这个indexz如果不加^ 会把包括indexz的url都匹配到
    url(r'^indexz$',views.indexz),
    url(r'^login$',views.login),
    url(r'show_indexz',views.show_indexz),
    url(r'^quit',views.quit_func),
    url(r'^template/$',views.temp),
    url(r'^good/(\d+)',views.good,name='good'),
    url(r'^main_page/',views.main_page),
    url(r'^detail/',views.detail),
    url(r'^postfile',views.postfile),
    url(r'^csrf/',views.csrf),
    url(r'^verifycode/',views.verifycode),
    url(r'^dengluqq/',views.dengluqq),
    url(r'^check/',views.check),
    url(r'^upfile',views.upfile),
    url(r'^savefile',views.savefile),
    url(r'^students_page/(\d+)',views.students_page),
    url(r'^ajax',views.ajax),
    url(r'^stuinfo/',views.stuinfo),
    url(r'^edit/',views.edit),
    url(r'^celery',views.celery),
]
