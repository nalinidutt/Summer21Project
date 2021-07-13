# "a" = append

from createSpider import spiderName, template, domain, start_url, titleX, authorX, dateX, paragraphsX

fileName = spiderName + ".py"

spiderClassName = spiderName.split("_")
spiderClassNameF = ""

for section in spiderClassName:
    sectionf = section.lower()
    sectionf = sectionf.title()
    
    spiderClassNameF += sectionf

with open("createSpider.py", "a") as f:
    # scrapy import statements
    f.write("\nimport scrapy\nfrom scrapy.linkextractors import LinkExtractor\nfrom scrapy.spiders import CrawlSpider, Rule\nfrom scrapy.exceptions import CloseSpider")
    
    f.write("\n") # spacer
    
    # sumy import statements
    f.write("\nfrom sumy.parsers.plaintext import PlaintextParser\nfrom sumy.nlp.tokenizers import Tokenizer\nfrom sumy.summarizers.lex_rank import LexRankSummarizer\nsummarizer = LexRankSummarizer()")
    
    f.write("\n")
    
    # items class
    f.write("\nclass SocialcomputingarticlesItem(scrapy.Item):\n    title = scrapy.Field()\n    author = scrapy.Field()\n    date = scrapy.Field()\n    finalSummary = scrapy.Field()\n    fullText = scrapy.Field()\n    url = scrapy.Field()")
    
    f.write("\n")
    
    if template == "crawl":
        f.write("\nclass " + spiderClassNameF + "Spider(CrawlSpider):")
        f.write("\n    n = 100\n    count = 0\n    name = '" + spiderName + "'\n    allowed_domains = ['" + domain + "']\n    start_urls = ['" + start_url + "']\n    rules = (Rule(LinkExtractor(allow=r'/'), callback='parse_item', follow=True)),")
        
        f.write("\n")
        
        f.write("\n    def parse_item(self, response):")
        
        f.write("\n        fullText = ''")
        f.write("\n        finalSummary = ''")
        
        f.write("\n")
        
        f.write("\n        if self.count >= self.n:")
        f.write("\n            raise CloseSpider('all done')")
        f.write("\n        else:")
        f.write("\n            if response.xpath('" + paragraphsX + "').get() is not None:")
        f.write("\n                title = response.xpath('" + titleX + "').get()")
        f.write("\n                author = response.xpath('" + authorX + "').get()")
        f.write("\n                date = response.xpath('" + dateX + "').get()")
        f.write("\n                paragraphs = response.xpath('" + paragraphsX + "').getall()")
        
        f.write("\n")
        
        f.write("\n                for paragraph in paragraphs:")
        f.write("\n                    fullText+= paragraph")
        
        f.write("\n")
        
        f.write("\n                textParser = PlaintextParser.from_string(fullText, Tokenizer('english'))")
        f.write("\n                summary = summarizer(textParser.document, 2)")
        
        f.write("\n")
        
        f.write("\n                for sentence in summary:")
        f.write("\n                    finalSummary += str(sentence)")
        
        f.write("\n")
        
        f.write("\n                if finalSummary is not None:")
        f.write("\n                    self.count +=1")
        
        f.write("\n")
        
        f.write("\n                    item = SocialcomputingarticlesItem()")
        f.write("\n                    item[" + '"title"' + "] = title")
        f.write("\n                    item[" + '"author"' + "] = author")
        f.write("\n                    item[" + '"date"' + "] = date")
        f.write("\n                    item[" + '"finalSummary"' + "] = finalSummary")
        f.write("\n                    item[" + '"fullText"' + "] = fullText")
        f.write("\n                    item[" + '"url"' + "] = response.url")
        f.write("\n                    return item")
    
    
 
