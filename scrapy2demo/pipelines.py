# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class Scrapy2DemoPipeline(object):

    def process_item(self, item, spider):

        if not os.path.exists(item['dir']):
            os.mkdir(item['dir'])
        with open(item['dir'] + os.sep + item['filename'], 'wb') as f:
            f.write(item['body'])
        # self.log('Saved file %s' % item['filename'])
        return item
