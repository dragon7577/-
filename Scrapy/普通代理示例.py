# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 11:30:19 2018

@author: Python
"""

import requests

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0"}
proxies = {'http':"http://37.192.32.213:36344"}

res = requests.get(url,proxies=proxies,headers=headers,timeout=5)
res.encoding='utf-8'
html = res.text
print(html)