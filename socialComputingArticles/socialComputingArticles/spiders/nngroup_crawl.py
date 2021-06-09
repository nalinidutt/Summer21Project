import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()

class NngroupCrawlSpider(CrawlSpider):
    name = 'nngroup_crawl'
    allowed_domains = ['nngroup.com']
    start_urls = ['https://www.nngroup.com/topic/human-computer-interaction/#articles']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        if response.xpath('/html/body/main/section/div/div/div/article/div/div[1]/section[1]/p/text()').get() is not None:
            title = response.xpath('/html/body/main/section/div/div/div/article/h1/text()').get()
            summary = response.xpath('/html/body/main/section/div/div/div/article/div/div[1]/section[1]/p/text()').get()
            
            item = SocialcomputingarticlesItem()
            item["title"] = title
            item["summary"] = summary
            return item
