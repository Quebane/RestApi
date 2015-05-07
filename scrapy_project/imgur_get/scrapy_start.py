from scrapy import log, signals
from spiders import ImageScrapySpider
from scrapy.settings import Settings
import settings as s
from scrapy.crawler import Crawler
from twisted.internet import reactor
from billiard import Process


class ScriptCrawl(Process):

        def __init__(self, spider):
            Process.__init__(self)
            setting = Settings()
            setting.setmodule(s)
            self.crawler = Crawler(setting)
            self.crawler.configure()
            self.crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
            self.spider = spider

        def run(self):
            self.crawler.crawl(self.spider)
            self.crawler.start()
            reactor.run()


def run_spider():
    spider = ImageScrapySpider()
    crawler = ScriptCrawl(spider)
    crawler.start()
    crawler.join()