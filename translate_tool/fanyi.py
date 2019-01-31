#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import urllib.parse
import time
import random
import hashlib
import json

class search(object):
    def __init__(self):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    def getData(self,search_name):
        salt = ((time.time() * 1000) + random.randint(1,10))
        sign_text = "fanyideskweb" + search_name + str(salt) + "6x(ZHw]mwzX#u0V7@yfwK"
        md5 = hashlib.md5()
        md5.update(sign_text.encode())
        sign = md5.hexdigest()

        data = {
            'i': search_name,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': str(salt),  # 得到的就是salt的那个字符串
            'sign': sign,  # 得到摘要
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }
        return data

    def getHeaders(self,data):
        headers = {
            'Accept': 'application/json,text/javascript, */*; q=0.01',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN, zh;q = 0.9',
            'Connection': 'keep-alive',
            'Content-Length': str(len(data)),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF - 8',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-654222404@10.168.1.241;JSESSIONID=aaaDUWMyhP6Ay - Fhw8yyw;OUTFOX_SEARCH_USER_ID_NCOO=1242777781.6841502;___rl__test__cookies=1538017049629',
            'Host': 'fanyi.youdao.com',
            'Origin': 'http://fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com /',
            'User-Agent': 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/68.0.3440.106 Safari/537.36',
            'X-Requested - With': 'XMLHttpRequest'
        }
        return headers

    def getResponse(self,data,headers):
        _data = urllib.parse.urlencode(data).encode('utf-8')
        _headers = headers
        response = requests.post(self.url,data=_data,headers=_headers)
        return response.text

    def getResult(self,response):
        result_text = json.loads(response)
        # src = result_text['translateResult'][0][0]['src']
        result = result_text['translateResult'][0][0]['tgt']
        return result

    def main(self,search_name):
        app = search()
        data = app.getData(search_name)
        headers = app.getHeaders(data)
        response = app.getResponse(data,headers)
        result = app.getResult(response)
        return result

