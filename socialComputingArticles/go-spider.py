from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from socialComputingArticles.spiders.#spider_name import # <spider_class_name>

process = CrawlerProcess(get_project_settings())
process.crawl(# <spider_class_name>)
process.start()
