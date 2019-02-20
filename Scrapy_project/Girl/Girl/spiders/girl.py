# -*- coding: utf-8 -*-
import scrapy


class GirlSpider(scrapy.Spider):
    name = 'girl'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def parse(self, response):
        pass
