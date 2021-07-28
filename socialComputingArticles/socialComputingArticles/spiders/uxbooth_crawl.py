
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
    finalSummary = scrapy.Field()
    fullText = scrapy.Field()
    url = scrapy.Field()

class UxboothCrawlSpider(CrawlSpider):
    n = 100
    count = 0
    name = 'uxbooth_crawl'
    allowed_domains = ['uxbooth.com']
    start_urls = ['https://www.uxbooth.com/articles/']
    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),

    def parse_item(self, response):
        fullText = ''
        finalSummary = ''

        if self.count >= self.n:
            raise CloseSpider('all done')
        else:
            if response.xpath('/html/body/article/div[2]/div[2]/div/div[1]/div/p/text()').get() is not None:
                title = response.xpath('/html/body/article/header/div[2]/div/div[1]/h1/text()').get()
                author = response.xpath('/html/body/article/header/div[2]/div/div[2]/div[1]/div[2]/a/div[1]/text()').get()
                date = response.xpath('/html/body/article/header/div[2]/div/div[2]/div[2]/div[2]/text()').get()
                paragraphs = response.xpath('/html/body/article/div[2]/div[2]/div/div[1]/div/p/text()').getall()

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
                    item["date"] = date
                    item["finalSummary"] = finalSummary
                    item["fullText"] = fullText
                    item["url"] = response.url
                    return item