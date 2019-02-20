import urllib.request
import urllib.parse
import re
import pymysql
import warnings

class LianjiaSpider:
    def __init__(self):
        self.baseurl = 'https://sz.lianjia.com/ershoufang/pg'
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.db = pymysql.connect('localhost','root','123456','spiderdb',charset='utf8')
        self.cursor = self.db.cursor()
        self.pg = 1
    
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.prasePage(html)
        
    def prasePage(self,html):
        p = re.compile('<div class="address"><div class="houseInfo"><span class="houseIcon"></span><a.*?>(.*?)</a>(.*?)</div>.*?class="totalPrice"><span>(.*?)</span>.*?<span>(.*?)</span>',re.S)
        rlist = p.findall(html)
        print(rlist)
        self.writePageToMysql(rlist)
    
    def writePageToMysql(self,rlist):
        warnings.filterwarnings('ignore')
        ins = 'insert into lianjia(title,layout,size,price) values(%s,%s,%s,%s)'
        for r in rlist:
            L = [
                    r[0].strip(),
                    r[1].strip(),
                    r[2].strip(),
                    r[3].strip()
                    ]
            self.cursor.execute(ins,L)
            self.db.commit()
    
    def workOn(self):
        while True:
            c = input("成功 ,继续?(y/n):")
            if c.strip().lower() == 'y':
                url = self.baseurl + str(self.pg)
                self.pg += 1
                self.getPage(url)
            else:
                print('结束')
                self.cursor.close()
                self.db.close()
                break
    
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.workOn()