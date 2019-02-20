# -*- coding: utf-8 -*-
import scrapy
from Daomubiji.items import DaomubijiItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-1']

    def parse(self, response):
        item = DaomubijiItem()
        baseList = response.xpath('//article/a')
        # print(baseList)
        for base in baseList:
            L = base.xpath('./text()').extract()[0].split()
            item['title'] = L[0]
            item['titleNum'] = L[1]
            item['titleName'] = L[2]
            item['titleLink'] = base.xpath('./@href').extract()[0]
            yield item
