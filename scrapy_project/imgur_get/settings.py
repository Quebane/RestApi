# -*- coding: utf-8 -*-

# Scrapy settings for google_get project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'imgur_get'

SPIDER_MODULES = ['scrapy_project.imgur_get.spiders']
NEWSPIDER_MODULE = 'scrapy_project.imgur_get.spiders'

ITEM_PIPELINES = {'scrapy_project.imgur_get.pipelines.ImgurGetPipeline': 100}