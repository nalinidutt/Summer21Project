from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from weather.spiders.weather_spider import WeatherSpiderSpider

process = CrawlerProcess(get_project_settings())
process.crawl(WeatherSpiderSpider)
process.start()