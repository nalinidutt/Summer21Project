
print("Welcome to Scrapy Spider Creator")

spiderName = input("Enter spider name: ")
template = input("Enter spider template: ")
domain = input("Enter main domain: ")
start_url = input("Enter start url: ")

# DOCKERFILE: scrapy genspider -t template spiderName domain
