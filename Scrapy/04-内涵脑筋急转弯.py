# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:18:07 2018

@author: Python
"""

import urllib.request
import urllib.parse
import re

class NeihanSpider:
    def __init__(self):
        self.baseurl = "https://www.neihan8.com/njjzw/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        self.Page = 2
        
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)
    
    def parsePage(self,html):
        p = re.compile('<div class="text-.*?title="(.*?)">.*?class="desc">(.*?)</div>',re.S)
        rlist = p.findall(html)
        print(rlist)
        self.writePage(rlist)
    
    def writePage(self,rlist):
        for rtuple in rlist:
            with open("neihan.txt","a") as f:
                f.write(rtuple[0].strip()+"\n")
                f.write(rtuple[1].strip()+"\n\n")
                
        
    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input('成功,是否继续(y/n):')
            if c.strip().lower() == "y":
                url = self.baseurl + "index_" + str(self.Page) + ".html"
                self.getPage(url)
                self.Page += 1
            else:
                print("爬取结束")
                break
    
if __name__ == '__main__':
    spider = NeihanSpider()
    spider.workOn()

























