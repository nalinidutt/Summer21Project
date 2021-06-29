FROM python:3.9

RUN pip install scrapy sumy pandas pymongo
RUN pymongo[srv]
RUN python -c "import nltk; nltk.download('punkt')"

COPY . .

CMD [ "scrapy", "crawl", "mitNews_crawl" ]
