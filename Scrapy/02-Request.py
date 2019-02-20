# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:31:02 2018

@author: Python
"""

import urllib.request
 # 创建请求对象(Request())
url = "http://www.baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
req = urllib.request.Request(url,headers=headers)
 #获取响应对象(urlopen())
res = urllib.request.urlopen(req)
 #获取内容(read().decode("utf-8"))
html = res.read().decode("utf-8")
#print(html)
#获取HTTP响应码
print(res.getcode())
#获取实际数据URL
print(res.geturl())