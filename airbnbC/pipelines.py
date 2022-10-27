# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy import settings
import logging
from decouple import config
from itemadapter import ItemAdapter


class AirbnbcPipeline:
    def process_item(self, item, spider):
        return item

class MongoDBPipeline:
    
    def __init__(self):
        quibble_db = pymongo.MongoClient(config("DATABASE_URL"))
        data_db = quibble_db.scraped_airbnb_data
        self.collection = data_db.data_collection
        self.items = []
        

    def process_item(self, item, spider):
        item_dict = ItemAdapter(item).asdict()
        self.items.append(item_dict)
        # self.collection.insert_one(item_dict)
        return item

    def close_spider(self, spider):
        self.collection.insert_many(self.items)
