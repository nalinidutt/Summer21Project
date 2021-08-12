FROM python:3.9

# WORKDIR /code

RUN pip install sumy scrapy pymongo numpy pymongo[srv]
RUN python -c "import nltk; nltk.download('punkt')"

COPY . .

ENTRYPOINT [ "scrapy" ]

CMD [ "crawl", "<spider name>" ]
