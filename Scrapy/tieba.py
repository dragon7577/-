# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 14:57:13 2018

@author: Python
"""

import urllib.request
import urllib.parse
import random
import time

hlist = [
        {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"},
        {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        ]
headers = random.choice(hlist)
baseurl = "http://tieba.baidu.com/f?"
#接收用户输入
name = input("请输入贴吧名称:")
begin = int(input("请输入起始页:"))
end = int(input("请输入终止页:"))
#拼接贴吧主页URL地址
kw = urllib.parse.urlencode({"kw":name})
for page in range(begin,end+1):
    #拼接第pn页完整URL地址
    pn = (page - 1) * 50
    url = baseurl + kw + "&pn" + str(pn)
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    html = res.read().decode("utf-8")
    filename = "第" +str(page) +"页.html"
    with open(filename,"w",encoding="utf-8") as f:
    f.write(html)
        print("第%d页爬取成功" % page)
        time.sleep(1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    