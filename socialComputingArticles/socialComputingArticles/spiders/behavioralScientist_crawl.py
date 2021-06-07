import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    intro = scrapy.Field()

class BehavioralscientistCrawlSpider(CrawlSpider):
    name = 'behavioralScientist_crawl'
    allowed_domains = ['behavioralscientist.org']
    start_urls = ['https://behavioralscientist.org/topics/technology/']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        if response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/div/p[1]/text()').get() is not None:
            title = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/header/h1/text()').get()
            intro = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/div/p[1]/text()').get()
            
            item = SocialcomputingarticlesItem()
            item["title"] = title
            item["intro"] = intro
            return item

