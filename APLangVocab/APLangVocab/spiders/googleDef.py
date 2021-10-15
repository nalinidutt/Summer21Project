import scrapy

class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # word = scrapy.Field()
    wordType = scrapy.Field()
    definition = scrapy.Field()

class GoogledefSpider(scrapy.Spider):
    name = 'googleDef'
    allowed_domains = ['google.com']
    # start_urls = ['http://google.com/']
    
    def start_requests(self):
        # urls for defs
        urls = ["https://www.merriam-webster.com/dictionary/extra"]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)


    def parse_url(self, response):
        # word = response.xpath('').get()
        wordType = response.xpath('//*[@id="left-content"]/div[1]/div[1]/span/a/text()').get()
        definition = response.xpath('//*[@id="dictionary-entry-1"]/div[2]/div[1]/span[1]/div/span[2]/span[1]/text()').get()
        
        item = WeatherItem()
        # item["word"] = word
        item["wordType"] = wordType
        item["definition"] = definition
        yield item

