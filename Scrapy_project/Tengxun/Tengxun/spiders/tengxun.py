# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem

class TengxunSpider(scrapy.Spider):
    name = "tengxun"
    allowed_domains = ["hr.tencent.com"]
    # 基准URL，方便后续做URL拼接
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(0)]

    def parse(self, response):
        # 把284页的URL地址都给调度器入队列
        for i in range(0,2841,10):
            url = self.url + str(i)
            # scrapy.Request()
            yield scrapy.Request(url,callback=self.parseHtml)

    def parseHtml(self,response):
        # 创建item对象
        item = TengxunItem()
        # 每个职位节点对象列表
        baseList = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        for base in baseList:
            item['zhName'] = base.xpath('./td[1]/a/text()').extract()[0]
            item['zhType'] = base.xpath('./td[2]/text()').extract()
            # 部分页面职位类型为 空,在此做判断
            if item['zhType']:
                item['zhType'] = item['zhType'][0]
            else:
                item['zhType'] = "无"
            item['zhNum'] = base.xpath('./td[3]/text()').extract()[0]
            item['zhAddress'] = base.xpath('./td[4]/text()').extract()[0]
            item['zhTime'] = base.xpath('./td[5]/text()').extract()[0]
            item['zhLink'] = base.xpath('./td[1]/a/@href').extract()[0]

            yield  item









