# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class Exp41Pipeline:
    def process_item(self, item, spider):
         print(item['bTitle'])
         print(item['bAuthor'])
         print(item['bDate'])
         print(item['bDate'])
         print(item['bPrice'])
         print(item['bDetail'])
        #con = pymysql.connect(host='localhost',user='root',password='',db='dangdang',charset='utf8mb4')
        #cursor=con.cursor()
        #sql="insert into book(title,author,publish,dat,price,detail) valuse ('%s%s%s%s%s%s')"%(item['bTitle'],item['bAuthor'],item['bPublish'],item['bDate'],item['bPrice'],item['bDetail'])
        #cursor.execute(sql)
        #con.commit()
        #cursor.close()
        #con.close()
         return item
