import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    summary = scrapy.Field()
    headings = scrapy.Field()

class mitNewsCrawlSpider(CrawlSpider):
    name = 'mitNews_crawl'
    allowed_domains = ['news.mit.edu']
    start_urls = ['https://news.mit.edu/topic/human-computer-interaction']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        if response.xpath('//*[@id="block-mit-content"]/div/article/div/div[1]/span/text()').get() is not None:
            title = response.xpath('//*[@id="block-mit-page-title"]/div/h1/span/text()').get()
            summary = response.xpath('//*[@id="block-mit-content"]/div/article/div/div[1]/span/text()').get()
            
            item = SocialcomputingarticlesItem()
            item["title"] = title
            item["summary"] = summary
            item["headings"] = headings
            return item
