import urllib.request
import urllib.parse
import re
import csv

class MaoyanSpider:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.offset = 0
        
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
            r = list(r)
            with open("猫眼.csv",'a',newline='',encoding='gb18030') as f:
                writer = csv.writer(f)
                writer.writerow(r)
                
    def workOn(self):
        while True:
            c = input("成功,是否继续(y/n):")
            if c.strip().lower() == 'y':
                url = self.baseurl + str(self.offset)
                self.getPage(url)
                self.offset += 10
                if self.offset >110:
                    print("退出")
                    break
            else:
                print("退出")
                break
    
if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.workOn()