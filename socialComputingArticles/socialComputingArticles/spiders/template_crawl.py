# LOCAL OUTPUT: 
# MongoDB Collection: 

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

summarizer = LexRankSummarizer()

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    topics = scrapy.Field()
    miniSummary = scrapy.Field()
    finalSummary = scrapy.Field()
    fullText = scrapy.Field()
    url = scrapy.Field()

class <spider name>Spider(CrawlSpider):
    # variables
    n = 100 # number of pages
    count = 0 # counter
    
    name = ''
    allowed_domains = ['']
    start_urls = ['']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        fullText = ''
        finalSummary = ''
        allTopics = ''
        
        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('').get() is not None:
                title = response.xpath('').get()
                author = response.xpath('').get()
                date = response.xpath('').get()
                topics = response.xpath('').getall()
                miniSummary = response.xpath('').get()
                paragraphs = response.xpath('').getall()
                
                for topic in topics:
                    allTopics += (topic + ', ')
                
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
                item["topics"] = allTopics
                item["miniSummary"] = miniSummary
                item["finalSummary"] = finalSummary
                item["fullText"] = fullText
                item["url"] = response.url
                return item
