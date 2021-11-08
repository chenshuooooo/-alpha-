# -*- coding:utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import sys
import io
from urllib.parse import quote
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')  # 改变标准输出的默认编码
file_medicine = open('5.txt',mode='w',encoding='utf-8')
medicine_list=['头孢','板蓝根','感冒灵']#要爬取的药物名称序列,根据需求添加
cot = len(medicine_list)
i=0
count=1
while i<cot:
    name=quote(medicine_list[i])#将中文解析为URL编码方式
    n=0
    i=i+1
    while n <= 10:#10为要爬取的页数，如果要全爬，可以设置比该药物页数大一点
        n = n + 1
        url = "http://www.china-yao.com/?act=search&typeid=1&keyword=" + name + "&page=" + str(n)
        req = urllib.request.Request(url=url)
        data = urllib.request.urlopen(req)
        data = data.read()
        dammit = UnicodeDammit(data, ["utf-8", 'gbk'])
        data = dammit.unicode_markup
        soup = BeautifulSoup(data, 'lxml')
        tags = soup.select('tr td')
        for tag in tags:
            if count % 6 != 0:
                file_medicine.write(tag.text + ',')
            if count % 6 == 0:
                file_medicine.write(tag.text + '\n')
            count += 1
    print(count)
    #print(type(soup))
