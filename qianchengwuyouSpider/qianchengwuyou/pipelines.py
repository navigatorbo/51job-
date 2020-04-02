# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql

class QianchengwuyouPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect('localhost', 'root', '123456', charset='utf8', db='z_51job')
        self.cursor = self.db.cursor()
    def close_spider(self, spider):
        # self.db.commit()
        self.cursor.close()
        self.db.close()
    def process_item(self, item, spider):
        ls = list(item)
        sentence = 'insert quanguo (' + ','.join(ls) + ') values (' + ','.join(['"%({})s"'.format(field) for field in ls]) + ');'
        self.cursor.execute(sentence % item)
        self.db.commit()
        return item
