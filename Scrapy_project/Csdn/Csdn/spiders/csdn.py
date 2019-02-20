# -*- coding: utf-8 -*-
import scrapy
from Csdn.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/XiaoYi_Eric/article/details/85559389']

    def parse(self, response):
        item = CsdnItem()
        #标题
        item['title'] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        #时间
        item['time'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        #数量
        item['number'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        yield item
