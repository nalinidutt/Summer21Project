FROM python:3.9

# ADD go-spider.py .

RUN pip install scrapy

COPY . .

# CMD [ "python", "./go-spider.py" ]
CMD [ "scrapy", "crawl", "behavioralScientist_crawl", "-o", "behvScieInfo.json" ]
