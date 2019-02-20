import requests
import json
import pymysql

class DoubanSpider:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.db = pymysql.connect('localhost',
                                  'root',
                                  '123456',
                                  'spiderdb',
                                  charset='utf8'
                                  )
        self.cursor = self.db.cursor()
    
    def getPage(self,params):
        res = requests.get(self.url,params=params,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
#        print(html)是一个列表[{1部电影},{},..]
        self.parsePage(html)
    
    def parsePage(self,html):
        ins = 'insert into doubanfilm values(%s,%s)'
        rlist = json.loads(html)
        for rdict in rlist:
            title = rdict['title']
            score = rdict['score']
            L = [title.strip(),float(score.strip())]
            self.cursor.execute(ins,L)
            self.db.commit()
        self.cursor.close()
        self.db.close()
    
    def workOn(self):
        print("***************")
        print("|剧情|喜剧|动作|")
        print("***************")
        #存放所有类型的列表
        kinds = ["剧情","喜剧","动作"]
        fDict = {
                "剧情":"11",
                "喜剧":"24",
                "动作":"5"
                }
        kind = input("请输入类型:")
        if kind in kinds:
            number = input("请输入数量:")
            params = {
                'type':fDict[kind],
                'interval_id':'100:90',
                'action':'',
                'start':'0',
                'limit':number
                }
            self.getPage(params)
        else:
            print("电影类型不存在")
    
if __name__ == '__main__':
    spider = DoubanSpider()
    spider.workOn()
    
#https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=1