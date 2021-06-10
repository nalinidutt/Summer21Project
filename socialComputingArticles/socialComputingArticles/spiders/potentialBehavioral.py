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
    intro = scrapy.Field()
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
        intro = response.xpath('//*[@id="post-16220"]/div[2]/blockquote[1]/p/strong/text()').get()
        
        textParser = PlaintextParser.from_string(intro, Tokenizer('english'))
        summary = summarizer(textParser.document, 2)
        
        for sentence in summary:
            finalSummary += str(sentence)
        
        item = SocialcomputingarticlesItem()
        item["title"] = title
        item["intro"] = intro
        item["finalSummary"] = finalSummary
        yield item
