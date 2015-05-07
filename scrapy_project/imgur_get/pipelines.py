# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import requests
from rest_api.settings import ADMIN_TOKEN


class ImgurGetPipeline(object):

    def process_item(self, item, spider):
        data = json.dumps(dict(item))
        requests.post(url='http://127.0.0.1:8000/image_scrap/image/', data=data,
                      headers={'Authorization': 'Token ' + ADMIN_TOKEN})
        return item