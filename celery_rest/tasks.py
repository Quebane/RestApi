from celery_rest import app
from image_scrap.models import History
from django.utils import timezone
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from scrapy_project.imgur_get.spiders import ImageScrapy
from scrapy.utils.project import get_project_settings


@app.task(track_started=True)
def count():
    if History.objects.filter(date=timezone.now().date()).exists():
        history = History.objects.get(date=timezone.now().date())
        nums = history.nums
        history.nums = history.images.count()
        if history.nums != nums:
            history.save()
            print 'New nums is ' + str(history.nums)


@app.task
def get_image():
    spider = ImageScrapy()
    settings = get_project_settings()
    crawler = Crawler(settings)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    log.start()
    reactor.run()