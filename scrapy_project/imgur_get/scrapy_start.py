from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from spiders import ImageScrapySpider
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings
import settings


class ScriptCrawl():

    def __init__(self):
        setting = Settings()
        setting.setmodule(settings)
        self.crawler = Crawler(setting)
        self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        self.crawler.configure()
        self.crawler.crawl(ImageScrapySpider())
        self.crawler.start()
        reactor.run()
        log.start()