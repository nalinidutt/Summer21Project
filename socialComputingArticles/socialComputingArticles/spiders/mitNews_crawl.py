# OUTPUT: mitNewsInfo.csv
# MongoDB collection: mitNews

# import pandas as pd
import pymongo

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.exceptions import CloseSpider

import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

summarizer = LexRankSummarizer()

"""
colnames = ['author', 'date', 'finalSummary', 'miniSummary', 'title', 'url']
data = pd.read_csv('mitNewsInfo.csv', names=colnames)
urls = data.url.tolist()
"""

class SocialcomputingarticlesItem(scrapy.Item):
    title = scrapy.Field()
    miniSummary = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    finalSummary = scrapy.Field()
    fullText = scrapy.Field()
    url = scrapy.Field()

class mitNewsCrawlSpider(CrawlSpider):
    # variables
    n = 100 # number of pages
    count = 0 # counter
    
    name = 'mitNews_crawl'
    allowed_domains = ['news.mit.edu']
    start_urls = ['https://news.mit.edu/topic/human-computer-interaction']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        fullText = ''
        finalSummary = ''
        
        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('//*[@id="block-mit-content"]/div/article/div/div[1]/span/text()').get() is not None:
                title = response.xpath('//*[@id="block-mit-page-title"]/div/h1/span/text()').get()
                author = response.xpath('//*[@id="block-mit-content"]/div/article/div/div[3]/span[1]/text()').get()
                date = response.xpath('//*[@id="block-mit-content"]/div/article/div/div[4]/time/text()').get()
                miniSummary = response.xpath('//*[@id="block-mit-content"]/div/article/div/div[1]/span/text()').get()

                paragraphs = response.xpath('//*[@id="block-mit-content"]/div/article/div/div[7]/div[1]/div/div/p/text()').getall()

                for paragraph in paragraphs:
                    fullText+= paragraph

                textParser = PlaintextParser.from_string(fullText, Tokenizer('english'))
                summary = summarizer(textParser.document, 2)    # can change number of sentences

                for sentence in summary:
                    finalSummary += str(sentence)
                
                if finalSummary is not None:
                   self.count +=1

                    item = SocialcomputingarticlesItem()
                    item["title"] = title
                    item["author"] = author
                    item["date"] = date
                    item["miniSummary"] = miniSummary
                    item["finalSummary"] = finalSummary
                    item["fullText"] = fullText
                    item["url"] = response.url
                    return item
