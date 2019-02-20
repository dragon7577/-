import requests
import pymysql
import re
import warnings

class NoteSpider:
    def __init__(self):
        self.url = "http://code.tarena.com.cn/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.auth = ('tarenacode',"code_2013")
        self.db = pymysql.connect('localhost','root','123456','spiderdb',charset='utf8')
        self.cursor = self.db.cursor()
    
    def getPrasePage(self):
        res = requests.get(self.url,auth=self.auth,
                           headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        p = re.compile('<a href="(.*?)/.*?</a>',re.S)
        rlist = p.findall(html)
        print(rlist)
        self.writePage(rlist)
        
    
    def writePage(self,rlist):
        warnings.filterwarnings('ignore')
        ctab = "create table if not exists tarenaNote(name varchar(30))"
        ins = 'replace into tarenaNote values(%s)'
        self.cursor.execute(ctab)
        for r in rlist:
            if r != '..':
                self.cursor.execute(ins,[r])
                self.db.commit()
        self.cursor.close()
        self.db.close()
            
    
if __name__ == '__main__':
    spider = NoteSpider()
    spider.getPrasePage()
    print('成功')