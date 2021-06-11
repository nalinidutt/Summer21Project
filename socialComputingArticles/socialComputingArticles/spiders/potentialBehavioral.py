# testing out xpaths, summary, etc, for 1 article, then will apply to crawl spiders
# OUTPUT: potentialBehaviorInfo.json

import scrapy
import sumy

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

summarizer = LexRankSummarizer()

class SocialcomputingarticlesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    intro = scrapy.Field()
    # paragraphs = scrapy.Field()
    finalSummary = scrapy.Field()

class PotentialbehaviorSummSpider(scrapy.Spider):
    name = 'potentialBehavior_summ'
    allowed_domains = ['behavioralscientist.org']
    
    def start_requests(self):
        # specific article links
        urls = ['https://behavioralscientist.org/potential-human-computer-interaction-behavioral-science/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_url)

    def parse_url(self, response):
        finalSummary = ''
        
        title = response.xpath('//*[@id="post-16220"]/header/h1/text()').get()
        date = response.xpath('//*[@id="post-16220"]/header/div[2]/div[1]/div[2]/text()').get()
        author = response.xpath('//*[@id="post-16220"]/header/div[2]/div[1]/div[1]/a/text()').get()
        
        # texts for summarizing
            # intro: //*[@id="post-16220"]/div[2]/blockquote[1]/p/strong/text()
            # 2nd p: //*[@id="post-16220"]/div[2]/p[2]/text()
            # 3rd p: //*[@id="post-16220"]/div[2]/p[3]/text()
            # all paragraphs excluding intro: //*[@id="post-16220"]/div[2]/p/text()
        
        intro = response.xpath('//*[@id="post-16220"]/div[2]/blockquote[1]/p/strong/text()').get()
        paragraphs = response.xpath('//*[@id="post-16220"]/div[2]/p/text()').getall()
        
        fullText = intro
        
        for paragraph in paragraphs:
            fullText+= paragraph
        
        textParser = PlaintextParser.from_string(fullText, Tokenizer('english'))
        summary = summarizer(textParser.document, 2)    # can change number of sentences
        
        for sentence in summary:
            finalSummary += str(sentence)
        
        item = SocialcomputingarticlesItem()
        item["title"] = title
        item["author"] = author
        item["date"] = date
        item["intro"] = intro
        # item["paragraphs"] = paragraphs
        item["finalSummary"] = finalSummary
        yield item
        
