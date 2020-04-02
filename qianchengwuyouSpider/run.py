# -*- coding: utf-8 -*-
import os, sys
# 配置环境变量
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append('F:\python\python_file\qianchengwuyouSpider\qianchengwuyou')
sys.path.insert(0, BASE_PATH)
from core.db import Mysql
from core.df import Df
from core.da import Dshow
from scrapy import cmdline


# 执行
if __name__ == '__main__':
    # cmdline.execute("scrapy crawl quanguo".split())

    # db = Mysql()
    # df = Df(db.select_key())
    # df.write()

    ds = Dshow()
    ds.start_draw()