import urllib.request
import urllib.parse
import re
import csv
import pymongo

class MaoyanSpider:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.offset = 0
        self.conn = pymongo.MongoClient("176.140.14.70",27017)
        self.db = self.conn['MaoDB']
        self.myset = self.db['film']
        
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
    
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rlist = p.findall(html)
        self.writeToCsv(rlist)
        
    def writeToCsv(self,rlist):
        for r in rlist:  
            d = {
                'name':r[0].strip(),
                'star':r[1].strip(),
                'releasetime':r[2].strip()
            }
            self.myset.insert(d)
        print('成功存入MaoDB库')

    def workOn(self):
        while True:
            c = input("成功,是否继续(y/n):")
            if c.strip().lower() == 'y':
                url = self.baseurl + str(self.offset)
                self.getPage(url)
                self.offset += 10
                if self.offset >=100:
                    print("退出")
                    break
            else:
                print("退出")
                break
    
if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.workOn()
