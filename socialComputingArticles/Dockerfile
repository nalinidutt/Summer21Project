FROM python:3.9

RUN pip install scrapy sumy pandas pymongo
RUN pip install pymongo[srv]
RUN python -c "import nltk; nltk.download('punkt')"

COPY . .

CMD [ "scrapy", "crawl", "mitNews_crawl" ]
