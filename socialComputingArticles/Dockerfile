FROM python:3.9

# ADD go-spider.py .

RUN pip install scrapy sumy pandas pymongo
RUN pymongo[srv]
RUN python -c "import nltk; nltk.download('punkt')"

COPY . .

# CMD [ "python", "./go-spider.py" ]
CMD [ "scrapy", "crawl", "mitNews_crawl" ]
