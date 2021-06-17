# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BossPipeline:
    def process_item(self, item, spider):
        return item

class MongodbPipeline(object):
    """保存数据到mongoDB数据库"""
    def open_spider(self, spider):
        self.client = MongoClient("127.0.0.1", 27017)
        self.col = self.client["Boss_copy2"]["python_job"]

    def process_item(self, item, spider):
        item = dict(item)
        self.col.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()

