import requests
from multiprocessing import Queue
from threading import Thread
from lxml import etree
import time
import urllib.parse
import json

class XiaomiSpider:
    def __init__(self):
        self.baseurl = 'http://app.mi.com/categotyAllListApi?'
        self.mainurl = 'http://app.mi.com/details?id'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.urlQueue = Queue()
        self.parseQueue = Queue()
    
    def getUrl(self):
        for page in range(20):
            params = {
                'page':str(page),
                'categoryId':'2',
                'pageSize':'30',
            }
            params = urllib.parse.urlencode(params)
            url = self.baseurl + params
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
            try:
                #html为json格式的字符串
                html = self.parseQueue.get(block=True,timeout=0.5)
                hList = json.loads(html)['data']
                # hList : [[应用1信息],[应用2信息],]
                for h in hList:
                    name = h['displayName']
                    link = self.mainurl + h['packageName']
                    d = {
                            '名称':name,
                            '链接':link
                            }         
                    with open('小米.json','a',encoding='utf-8') as f:
                        f.write(str(d) + '\n')
            except:
                print("出错")
                break
    #主函数
    def workOn(self):
        self.getUrl()
        tlist = []
        for i in range(5):
            t1 = Thread(target=self.getHtml)
            t2 = Thread(target=self.getData)
            tlist.append(t1)
            tlist.append(t2)
            t1.start()
            t2.start()
        for i in tlist:
            i.join()
        
    
if __name__ == '__main__':
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print("执行时间:%.2f" % (end - start))
    
    