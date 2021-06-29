# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymongo
# from itemadapter import ItemAdapter
# from scrapy.utils.project import get_project_settings
# from scrapy.exporters import JsonItemExporter

class SocialcomputingarticlesPipeline (object):  
    
    collection_name = 'mitNews'
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB', 'scrapyItems')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri, ssl = True)
        self.db = self.client[self.mongo_db]
        self.db[self.collection_name].delete_many({})

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        count = self.db[self.collection_name].count({"url": item["url"]})
        if (count == 0):
            self.db[self.collection_name].insert_one(dict(item))
        return item
