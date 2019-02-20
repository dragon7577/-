import requests
from lxml import etree
import urllib.parse

class BaiduTmgSpider:
    def __init__(self):
        self.baseurl = "http://tieba.baidu.com"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    
    #获取所有帖子的URL列表
    def getPageUrl(self,url,num3):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        #提取页面中的href
        parseHtml = etree.HTML(html)
        tlist = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        num1 = 0
        for t in tlist:
            num1 += 1
            tLink = self.baseurl + t
            self.getImgUrl(tLink,num1,num3)
    
    #获取1个帖子中所有图片的URL列表
    def getImgUrl(self,tLink,num1,num3):
        #获取一个帖子的响应内容
        res = requests.get(tLink,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        #从帖子的html中提取图片的src
        parseHtml = etree.HTML(html)
        imgList = parseHtml.xpath('//cc//img/@src')
        #依次遍历图片链接调用写入函数
        num2 = 0
        for img in imgList:
            num2 +=1
            self.writeImage(img,num1,num2,num3)
            
    def writeImage(self,img,num1,num2,num3):
        #对图片链接发请求,获取res.content
        res = requests.get(img,headers=self.headers)
        res.encoding='utf-8'
        html = res.content
        #写入本地文件
        try:
            with open('%d-%d-%d.jpg'% (num3,num1,num2),'wb') as f:
                f.write(html)
                print('%d-%d-%d成功'% (num3,num1,num2))
        except:
            print('%d-%d-%d失败'% (num3,num1,num2))
    
    def workOn(self):
        name = input('贴吧名:')
        begin = int(input('起始页:'))
        end = int(input('终止页:'))
        for n in range(begin,end+1):
            num3 = n
            pn = 1
            params = {
                    'kw':name,
                    'pn':pn
                    }
            params = urllib.parse.urlencode(params)
            #拼接url
            url = self.baseurl + "/f?" + params
            pn += 1
            self.getPageUrl(url,num3)
    
if __name__ == '__main__':
    spider = BaiduTmgSpider()
    spider.workOn()