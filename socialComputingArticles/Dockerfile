FROM python:3.9

# ADD go-spider.py .

RUN pip install scrapy sumy pandas
RUN python -c "import nltk; nltk.download('punkt')"

COPY . .

# CMD [ "python", "./go-spider.py" ]
CMD [ "scrapy", "crawl", "behavioralScientist_crawl", "-o", "behvScieInfo2.json" ]
