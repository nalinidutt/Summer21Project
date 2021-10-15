import scrapy

class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    city = scrapy.Field()
    temp = scrapy.Field()
    cond = scrapy.Field()
    uv = scrapy.Field()

class GoogledefSpider(scrapy.Spider):
    name = 'googleDef'
    allowed_domains = ['google.com']
    # start_urls = ['http://google.com/']
    
    def start_requests(self):
        # Weather.com URL for Charlotte's weather
        urls = ["https://weather.com/weather/today/l/d1ffcaa6f03d9444be57cc3c00bb996859df6be82a64f748f4ec3834a25fcaba"]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)


    def parse_url(self, response):
        # Extracting city, temperature, air quality and condition from the response using XPath
        city = response.xpath('').get()
        temp = response.xpath('').get()
        cond = response.xpath('').get()
        uv = response.xpath('').get()
        
        city = city.replace(' Weather', '')
        temp += 'F'
        
        item = WeatherItem()
        item["city"] = city
        item["temp"] = temp
        item["cond"] = cond
        item["uv"] = uv
        yield item

