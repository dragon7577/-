import urllib.request
import urllib.parse
import re
import warnings
import pymysql

class MaoyanSpider:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset='
        self.headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.offset = 0
        self.db = pymysql.connect('localhost','root','123456','spiderdb',charset='utf8')
        self.cursor = self.db.cursor()
        
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode("utf-8")
        self.parsePage(html)
    
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rlist = p.findall(html)
        self.writeToMysql(rlist)
        
    def writeToMysql(self,rlist):
        warnings.filterwarnings('ignore')
        ins = 'insert into film(name,star,releasetime) values(%s,%s,%s)'  
        for r in rlist:
            #execute必须使用列表传参
            self.cursor.execute(ins,[r[0].strip(),r[1].strip(),r[2].strip()[5:15]])
            self.db.commit()

    def workOn(self):
        while True:
            c = input("成功,是否继续(y/n):")
            if c.strip().lower() == 'y':
                url = self.baseurl + str(self.offset)
                self.getPage(url)
                self.offset += 10
                if self.offset >=100:
                    print("退出")
                    self.cursor.close()
                    self.db.close()
                    break
            else:
                print("退出")
                self.cursor.close()
                self.db.close()
                break
        
    
if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.workOn()
