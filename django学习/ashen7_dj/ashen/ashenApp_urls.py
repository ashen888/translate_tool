#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  django.conf.urls import  include,url
# from  django.contrib import admin

from . import views as tv
urlpatterns = [

         url(r'normalmap/', tv.do_normalmap),

        # 带参数的url
        # 圆括号表示的是一个参数 里面的内容作为参数传递给被调用的函数
        # 参数名称以问号加大写P开头  尖括号里面的就是参数的名字
        # 尖括号后表示正则 [0-9]表示内容仅能是由0-9的数字构成
        # 后面的大括号表示出现的次数 表示只能出现4个0-9的数字
        url(r'withparam/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])',tv.withparam),
        url(r'^ypdashen',tv.do_app),
]
