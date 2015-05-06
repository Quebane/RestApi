import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from items import ImageItem
from scrapy.http import Request


class ImageScrapy(CrawlSpider):
    name = 'imgur'
    allowed_domains = ['imgur.com']
    start_urls = [r'http://imgur.com']
    rules = (Rule(LinkExtractor(allow=(r'/gallery/[a-zA-Z0-9]*', ),), callback='parse_item'), )

    def parse_item(self, response):
        image = ImageItem()
        image['description'] = response.xpath('//h1[contains(@id, "image-title")]/text()').extract()[0]
        image['url'] = response.url
        return image