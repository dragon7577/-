# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:47:43 2018

@author: Python
"""

import urllib.request
import urllib.parse
import json
import requests
#接收用户输入
key = input("请输入要翻译的内容:")
#把Form Data定义成1个大字典
data = {
'i': key,
'from':'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15458146240436',
'sign': '9feaad0a7d5d888a3e72be3b53cebdfb',
'ts': '1545814624043',
'bv': '363eb5a1de8cfbadd0cd78bd6bd43bee',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false',
        }
#把data转为bytes数据类型
#data = urllib.parse.urlencode(data).encode('utf-8')
#发请求,或响应,获取内容
#此处的URL地址为F12抓到的POST的地址
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
headers = {"User-Agent":"Mozilla/5.0"}
res = requests.post(url,data=data,headers=headers)
res.encoding='utf-8'
html = res.text
#print(html)
#把json格式的字符串转为python中字典
rDict = json.loads(html)
print(rDict['translateResult'][0][0]['tgt'])
