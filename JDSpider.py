# -*- coding:utf-8 -*-
import scrapy
from ..items import csSpiderProjectItem

class JdspiderSpider(scrapy.Spider):
    name = 'JDSpider'
    allowed_domains = ['www.jd.com']
    start_urls = ['https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&enc=utf-8&wq=%E4%B9%A6%E5%8C%85&pvid=96c565ca1fbe485a8ab8799471d23cf7']
    global count
    count = 0  # 计数，爬取学号后三位104项后就停止

    def get_url(self):
        #翻页处理
        for i in range(4):
            url='https://search.jd.com/Search?keyword=%E4%B9%A6%E5%8C%85&qrst=1&wq=%E4%B9%A6%E5%8C%85&stock=1&pvid=4e63e6d0e3c8426f89e2d2e573728468&page='+str(i)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        global count
        item = csSpiderProjectItem()
        lists = response.xpath('//ul[@class="gl-warp clearfix"]/li')
        for li in lists:
            item['price']=li.xpath('.//div[@class="p-price"]/strong/i/text()').extract()
            item['description']=li.xpath('.//div[@class="p-name p-name-type-2"]//em/text()').extract()
            yield item
        if self.count<=104:
            self.count+=1


