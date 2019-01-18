# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import os
from scrapy2demo.items import Scrapy2DemoItem


class Scrapy2DemoSpider(scrapy.Spider):
    name = "scrapy2demo"

    def start_requests(self):
        urls = [
            'http://www.runoob.com/w3cnote/python-yield-used-analysis.html'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        dir = response.url.split("/")[-2]
        filename = response.url.split("/")[-1]
        body = response.body
        scrapy2demoitem = Scrapy2DemoItem()
        scrapy2demoitem['dir'] = dir
        scrapy2demoitem['filename'] = filename
        scrapy2demoitem['body'] = body
        return scrapy2demoitem
