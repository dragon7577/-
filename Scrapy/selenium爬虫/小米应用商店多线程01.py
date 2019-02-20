import requests
from multiprocessing import Queue
from threading import Thread
from lxml import etree
import time

class XiaomiSpider:
    def __init__(self):
        self.baseurl = 'http://app.mi.com/category/12#page='
        self.mainurl = 'http://app.mi.com'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.urlQueue = Queue()
        self.parseQueue = Queue()
    
    def getUrl(self):
        for page in range(20):
            url = self.baseurl +str(page)
            #把拼接的url地址放到url队列中
            self.urlQueue.put(url)
    
    #采集线程函数,get出URL发请求,把html给解析函数
    def getHtml(self):
        while True:
            #先判断队列是否为空
            if not self.urlQueue.empty():
                url = self.urlQueue.get()
                #三步走
                res = requests.get(url,headers=self.headers)
                res.encoding = 'utf-8'
                html = res.text
                #把 html 放到解析队列中
                self.parseQueue.put(html)
            else:
                break
    #解析线程函数,get出html源码,提取出并处理数据
    def getData(self):
        while True:
            if not self.parseQueue.empty():
                html = self.parseQueue.get()
                #创建解析对象,调用xpath
                parseHtml = etree.HTML(html)
                baselist = parseHtml.xpath('//ul[@id="all-applist"]//li')
                for base in baselist:
                    name = base.xpath('./h5/a/text()')[0]
                    link = self.mainurl + base.xpath('./h5/a/@href')[0]
                    d = {
                            '分类':'学习教育',
                            '名称':name,
                            '连接':link
                            }         
                    with open('小米.json','a',encoding='utf-8') as f:
                        f.write(str(d) + '\n')
            else:
                break
    #主函数
    def workOn(self):
        self.getUrl()
        t1list = []
        t2list = []
        for i in range(5):
            t = Thread(target=self.getHtml)
            t1list.append(t)
            t.start()
        for i in t1list:
            i.join()
        for i in range(5):
            t = Thread(target=self.getData)
            t2list.append(t)
            t.start()
        for i in t2list:
            i.join()
    
if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print("执行时间:%.2f" % (end - start))
    
    