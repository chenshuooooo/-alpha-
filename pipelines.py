# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql
class Exp42Pipeline:
    def process_item(self, item, spider):
         print("{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t{:^10}\t".format
      (item["Id"],item["Currency"],item["TSP"],
      item["CSP"],item["TBP"],item["CBP"],item["Times"]))

         connect = pymssql.connect(host='localhost', user='chenshuo', password='cs031904104',
                                   database='cs031904104', charset='UTF-8')  # 连接到sql server数据库
         cur = connect.cursor()  # 创建操作游标
         #表的创建在数据库中完成
         # 插入数据
         try:
             cur.execute(
                 "insert into rate_cs (id,Currency,TSP,CSP,TBP,CBP,Times) values ('%d','%s','%s','%s','%s','%s','%s')" % (
                     item['Id'], item['Currency'].replace("'", "''"), item['TSP'].replace("'", "''"),
                     item['CSP'].replace("'", "''"), item['TBP'].replace("'", "''"),
                     item['CBP'].replace("'", "''"), item['Times'].replace("'", "''")))
             connect.commit()  # 提交命令
         except Exception as er:
             print(er)

         connect.close()#关闭与数据库的连接
         return item

