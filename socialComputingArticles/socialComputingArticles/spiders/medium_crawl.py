
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
    finalSummary = scrapy.Field()
    fullText = scrapy.Field()
    url = scrapy.Field()

class MediumCrawlSpider(CrawlSpider):
    n = 100
    count = 0
    name = 'medium_crawl'
    allowed_domains = ['medium.com', 'uxdesign.cc']
    start_urls = ['https://medium.com/topic/ux']
    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        fullText = ''
        finalSummary = ''

        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('/html/body/div[1]/div/div[3]/article/div/section[2]/div/div/p/text()').get() is not None:
                title = response.xpath('/html/body/div/div/div[3]/article/div/section[1]/div/div/div/h1/strong/text()').get()
                author = response.xpath('/html/body/div/div/div[3]/article/div/section[1]/div/div/div/div/div/div[1]/div[2]/div/div/span/div/div/a/p/text()').get()
                paragraphs = response.xpath('/html/body/div[1]/div/div[3]/article/div/section[2]/div/div/p/text()').getall()

                for paragraph in paragraphs:
                    fullText+= paragraph

                textParser = PlaintextParser.from_string(fullText, Tokenizer('english'))
                summary = summarizer(textParser.document, 2)

                for sentence in summary:
                    finalSummary += str(sentence)

                if finalSummary is not None:
                    self.count +=1

                    item = SocialcomputingarticlesItem()
                    item["title"] = title
                    item["author"] = author
                    item["finalSummary"] = finalSummary
                    item["fullText"] = fullText
                    item["url"] = response.url
                    return item