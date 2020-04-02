# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class QianchengwuyouItem(scrapy.Item):
    # define the fields for your item here like:
    ls = ['url', 'name', 'salary', 'region', 'workplace',
          'cp_name', 'cp_type', 'cp_scale', 'welfare',
          'exp', 'edu', 'demand', 'pubdate', 'skill',
          'detail'] #'industry'
    for fd in ls:
        exec(fd + '=scrapy.Field()') #Item 对象是种简单的容器，保存了爬取到得数据。
                                     #  其提供了 类似于词典(dictionary-like)
                                     #  的API以及用于声明可用字段的简单语法。
