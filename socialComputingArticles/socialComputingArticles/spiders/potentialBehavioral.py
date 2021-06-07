import scrapy

class SocialcomputingarticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()

class PotentialbehavioralSpider(scrapy.Spider):
    name = 'potentialBehavioral'
    allowed_domains = ['behavioralscientist.org']
    
    def start_requests(self):
        # specific article links
        urls = ['https://behavioralscientist.org/potential-human-computer-interaction-behavioral-science/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        title = response.xpath('//*[@id="post-16220"]/header/h1/text()').get()
        intro = response.xpath('//*[@id="post-16220"]/div[2]/blockquote[1]/p/strong/text()').get()
        
        item = SocialcomputingarticlesItem()
        item["title"] = title
        item["intro"] = intro
        yield item
