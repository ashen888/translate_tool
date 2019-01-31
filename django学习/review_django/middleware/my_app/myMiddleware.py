#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.utils.deprecation import MiddlewareMixin

class Mymiddle(MiddlewareMixin):
    def process_request(self,request):
        print('get参数为:',request.GET.get('a'))