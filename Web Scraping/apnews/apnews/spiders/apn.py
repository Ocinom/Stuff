import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from apnews.items import Article

class APN_Spider(CrawlSpider):
    name = 'apn'
    allowed_domains = ['apnews.com']
    start_urls = ['http://apnews.com/']

    rules = [
        Rule(LinkExtractor(allow=r'article/.*$'), callback='parse', follow=True)
    ]

    def parse(self, response):
        article = Article()
        article['article_name'] = response.xpath("//h1[starts-with(@class, 'Component-h1')]/text()").get()
        article['author'] = response.xpath("//span[starts-with(@class, 'Component-bylines')]/text()").get()
        article['date'] = response.xpath("//span[@data-key='timestamp']/@title").get()
        article['url'] = response.url
        return article
