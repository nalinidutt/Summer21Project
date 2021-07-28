# Summer 2021 Project
Web scraping articles and summarizing info with python. Run `createSpider.py` to generate new spider
## Requirements
* scrapy
* sumy
* pymongo
* pymongo[srv]
* numpy
## Build Docker Image
`docker build -t <tag> .` Tag can only be lowercase
### Checklist before building image
* Rename collection in `pipelines.py`
* Edit spider name in Dockerfile
## Run Docker Image (interactive)
`docker run -it <tag>`
## Sources (start urls)
* https://news.mit.edu/topic/human-computer-interaction
* https://behavioralscientist.org/topics/technology/
* https://www.nngroup.com/topic/human-computer-interaction/#articles
* https://medium.com/topic/ux
* https://www.uxbooth.com/articles/
* https://uxmag.com/articles
