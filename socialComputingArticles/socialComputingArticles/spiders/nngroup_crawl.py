# OUTPUT: nngroupInfo.csv

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
    topics = scrapy.Field()
    miniSummary = scrapy.Field()
    finalSummary = scrapy.Field()

class NngroupCrawlSpider(CrawlSpider):
    # variables
    n = 10 # number of pages
    count = 0 # counter
    
    name = 'nngroup_crawl'
    allowed_domains = ['nngroup.com']
    start_urls = ['https://www.nngroup.com/topic/human-computer-interaction/#articles']

    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        fullText = ''
        finalSummary = ''
        allTopics = ''
        
        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('/html/body/main/section/div/div/div/article/div/div[1]/section[1]/p/text()').get() is not None:
                title = response.xpath('/html/body/main/section/div/div/div/article/h1/text()').get()
                author = response.xpath('//*[@id="body-content"]/article/div/div[1]/section[2]/div[1]/div[1]/ul/li/a/text()').get()
                date = response.xpath('//*[@id="body-content"]/article/div/div[1]/section[2]/div[1]/div[1]/div/p/text()').get()
                topics = response.xpath('//*[@id="body-content"]/article/div/div[1]/section[2]/div[1]/div[2]/ul/li/text()').getall()
                miniSummary = response.xpath('/html/body/main/section/div/div/div/article/div/div[1]/section[1]/p/text()').get()
                paragraphs = response.xpath('//*[@id="articleBody"]/p/text()').getall()
                
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
                return item
