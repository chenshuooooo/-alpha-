# -*- coding:utf-8 -*-
from scrapy import cmdline
import sys
sys.path.append(r'D:\python project\exp4_1\spiders\dangdang')#添加爬虫路径，防止报错找不到路径
cmdline.execute('scrapy crawl dangdang'.split())#运行爬虫