import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()

class mitNewsCrawlSpider(CrawlSpider):
    name = 'mitNews_crawl'
    allowed_domains = ['news.mit.edu']
    start_urls = ['https://news.mit.edu/topic/human-computer-interaction']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
      # add XPaths
        if response.xpath('').get() is not None:
            title = response.xpath('').get()
            summary = response.xpath('').get()
            
            item = SocialcomputingarticlesItem()
            item["title"] = title
            item["summary"] = summary
            return item
