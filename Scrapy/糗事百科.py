import requests
from lxml import etree
import pymongo

class QiushiSpider:
    def __init__(self):
        self.baseurl = 'https://www.qiushibaike.com/text/'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.conn = pymongo.MongoClient("127.0.0.1",27017)
        self.db = self.conn['Qiushidb']
        self.myset = self.db['qiushi']
    
    def getPage(self):
        res = requests.get(url=self.baseurl,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        self.parsePage(html)
    
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        baseList = parseHtml.xpath('//div[contains(@id,"qiushi_tag_")]')
        for base in baseList:
            username = base.xpath('./div/a/h2')
            if username:
                username =username[0].text.strip()
            else:
                username = '匿名用户'
            content = base.xpath('./a/div[@class="content"]/span/text()')
            content = "".join(content).strip()
            laughNum = base.xpath('.//i[@class="number"]')[0].text
            pingNum = base.xpath('.//i[@class="number"]')[1].text
            d ={
                'username':username,
                'content':content.strip(),
                'laughNum':laughNum,
                'pingNum':pingNum
                }
            self.myset.insert_one(d)
    
    def workOn(self):
        print('正在爬取中......')
        self.getPage()
        print('爬取结束,存入Qiushidb库')
    
if __name__ == '__main__':
    spider = QiushiSpider()
    spider.workOn()