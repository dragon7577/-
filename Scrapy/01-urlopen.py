# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 11:12:21 2018

@author: Python
"""

import urllib.request
# 直接发请求,并得到相应对象
url = "http://www.taobao.com/"
response = urllib.request.urlopen(url)
print(response.read().decode("utf-8"))
