# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging
# from scrapy.exporters import JsonItemExporter

class SocialcomputingarticlesPipeline (object):
    
    def __init__(self):        
        #self.file = open('behvScieInfo2.json', 'wb')
        
        #self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        #self.exporter.start_exporting()
        #print('file opened')
        settings = get_project_settings()
        
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]
        
    def process_item(self, item, spider):
        # self.exporter.export_item(item)
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.info("URL added to MongoDB database!")
        return item
