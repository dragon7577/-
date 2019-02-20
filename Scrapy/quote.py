# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:25:44 2018

@author: Python
"""

#请求模块
import urllib.request
#url地址编码模块
import urllib.parse
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
baseurl = "http://www.baidu.com/s?wd="
#接收用户从终端输入
key = input("请输入要搜索的内容:")
#进行urlencode编码
key = urllib.parse.quote(key)
#拼接url
url = baseurl + key
#print(url)
# *********************************
#创建请求对象
req = urllib.request.Request(url,headers=headers)
#获取响应对象
res = urllib.request.urlopen(req)
#获取内容
html = res.read().decode("utf-8")
print(html)