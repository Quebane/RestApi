from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from items import ImageItem
from scrapy import log


class ImageScrapySpider(CrawlSpider):
    name = 'imgur'
    allowed_domains = ['imgur.com']
    start_urls = [r'http://imgur.com']
    rules = (Rule(LinkExtractor(allow=(r'/gallery/[a-zA-Z0-9]*$', ),), callback='parse_item'), )

    def parse_item(self, response):
        image = ImageItem()
        if response.url != 'https://imgur.com/signin':
            image['description'] = response.xpath('//h1[contains(@id, "image-title")]/text()').extract()[0]
            image['url'] = response.css('div#image > div > img').xpath('@src').extract()
        return image