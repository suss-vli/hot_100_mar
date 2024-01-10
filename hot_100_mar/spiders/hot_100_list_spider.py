import scrapy


class Hot100ListSpiderSpider(scrapy.Spider):
    name = "hot_100_list_spider"
    allowed_domains = ["hot_100_list_spider.com"]
    start_urls = ["https://hot_100_list_spider.com"]

    def parse(self, response):
        pass
