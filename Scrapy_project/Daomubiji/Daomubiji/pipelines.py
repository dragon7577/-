# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from Daomubiji.settings import *
import pymysql
import pymongo

class DaomubijiPipeline(object):
    def process_item(self, item, spider):
        print("============")
        print(item['title'])
        print(item['titleNum'])
        print(item['titleName'])
        print(item['titleLink'])
        print("=============")
        return item

class MongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(host=MONGODB_HOST,port=MONGODB_PORT)
        self.db = self.conn[MONGODB_DB]
        self.myset = self.db[MONGODB_SET]

    def process_item(self,item,spider):
        d = dict(item)
        self.myset.insert_one(d)
        return item
