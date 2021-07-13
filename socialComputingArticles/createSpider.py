
print("Welcome to Scrapy Spider Creator")

spiderName = input("Enter spider name: ")
template = input("Enter spider template: ")
domain = input("Enter main domain: ")
start_url = input("Enter start url: ")

titleX = input("Enter title XPath: ")
authorX = input("Enter author XPath: ")
dateX = input("Enter date XPath: ")
paragraphsX = input("Enter paragraphs XPath: ")

# DOCKERFILE: scrapy genspider -t template spiderName domain
