# OUTPUT: behvScieInfo.csv

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

import sumy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

summarizer = LexRankSummarizer()

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    intro = scrapy.Field()
    finalSummary = scrapy.Field()

class BehavioralscientistCrawlSpider(CrawlSpider):
    # variables
    n = 100 # number of pages
    count = 0 # counter
    
    name = 'behavioralScientist_crawl'
    allowed_domains = ['behavioralscientist.org']
    start_urls = ['https://behavioralscientist.org/topics/technology/']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True),)

    def parse_item(self, response):
        finalSummary = ''
        
        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/div/p[1]/text()').get() is not None:
                title = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/header/h1/text()').get()
                author = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/header/div[2]/div[1]/div[1]/text()').get()
                date = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/header/div[2]/div[1]/div[2]/text()').get()
                intro = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/div/p[1]/text()').get()
                paragraphs = response.xpath('/html/body/div/div[2]/div/div/main/div[1]/div[1]/article/div/p/text()').getall()

                fullText = intro
                
                for paragraph in paragraphs:
                    fullText+= paragraph
                
                textParser = PlaintextParser.from_string(fullText, Tokenizer('english'))
                summary = summarizer(textParser.document, 2)    # can change number of sentences

                for sentence in summary:
                    finalSummary += str(sentence)
                    
                self.count +=1

                item = SocialcomputingarticlesItem()
                item["title"] = title
                item["author"] = author
                item["date"] = date
                item["intro"] = intro
                item["finalSummary"] = finalSummary
                return item

