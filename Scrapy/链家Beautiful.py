from bs4 import BeautifulSoup
import pymongo
import requests


class LianjiaSpider:
    def __init__(self):
        self.baseurl = 'https://bj.lianjia.com/ershoufang/'
        self.headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
        self.conn = pymongo.MongoClient(
                '127.0.0.1',
                27017)
        self.db = self.conn['Lianjia']
        self.myset = self.db['houseInfo']
        
    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)
        
    def parsePage(self,html):
        soup = BeautifulSoup(html,'lxml')
        rlist = soup.find_all('li',attrs={"class":"clear LOGCLICKDATA"})
        for r in rlist:
            Info = r.find('div',attrs={"class":"houseInfo"}).get_text().split('/')
            name = Info[0]
            huxing =Info[1]
            area = Info[2]
            positionInfo = r.find('div',attrs={"class":"positionInfo"}).get_text().split('/')
            louceng = positionInfo[0]
            year  = positionInfo[1]
            address = positionInfo[2]
            totalPrice = r.find('div',attrs={"class":"totalPrice"}).get_text()
            unitPrice = r.find('div',attrs={"class":"unitPrice"}).get_text()
            d = {
                    '名称':name,
                    '户型':huxing,
                    '面积':area,
                    '楼层':louceng,
                    '年份':year,
                    '地点':address,
                    '总价':totalPrice,
                    '单价':unitPrice
                    }
            self.myset.insert_one(d)
    
    def workOn(self):
        n = int(input("请输入页数:"))
        for pg in range(1,n+1):
            url = self.baseurl + str(pg) + '/'
            self.getPage(url)
            print("第%d页爬取成功" % pg)
    
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.workOn()