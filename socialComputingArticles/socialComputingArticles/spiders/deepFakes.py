import scrapy

class SocialcomputingarticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()

class DeepfakesSpider(scrapy.Spider):
    name = 'deepFakes'
    allowed_domains = ['analyticsindiamag.com']
    #start_urls = ['http://analyticsindiamag.com/']
    
    def start_requests(self):
        # Specific article url
        urls = ['https://analyticsindiamag.com/stanford-university-professor-maneesh-agrawala-on-video-editing-tools-deep-fakes-more/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        title = response.xpath('//*[@id="post-10041140"]/div[1]/div/div/header/h1/text()').get()
        intro = response.xpath('//*[@id="post-10041140"]/div[3]/div/div/div/div/div[2]/div[1]/p[1]/text()').get()
        
        item = SocialcomputingarticlesItem()
        item["title"] = title
        item["intro"] = intro
        yield item
