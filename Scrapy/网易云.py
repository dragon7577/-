import requests
from lxml import etree

class WangyiyunSpider:
    def __init__(self):
        self.baseurl = 'https://music.163.com/#/song?id=165379'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    
    def getPage(self):
        res = requests.get(url=self.baseurl,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        with open('wang.html','a') as f:
            f.write(html)
        self.parsePage(html)
    
    def parsePage(self,html):
        parseHtml = etree.HTML(html)
        baseList = parseHtml.xpath('//div[@class="hd"]//em/text()')
        for base in baseList:
            print(base.text)
    
    def workOn(self):
        print('正在爬取中......')
        self.getPage()
        print('爬取结束')
    
if __name__ == '__main__':
    spider = WangyiyunSpider()
    spider.workOn()