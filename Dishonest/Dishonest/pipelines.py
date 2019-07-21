# -*- coding: utf-8 -*-
from Dishonest.settings import MYSQL_HOST,MYSQL_PORT,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DishonestPipeline(object):
    def open_spider(self,spider):
        self.connect = pymysql.connect(host=MYSQL_HOST,password=MYSQL_PASSWORD,user=MYSQL_USER,port=MYSQL_PORT,db=MYSQL_DATABASE)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 如果是自然人，根据身份整号判断
        # 如果是法人，根据年龄判断，年龄是０,根据区域以及名称进行判断是否存在
        if item['age'] == 0:
            select_count_sql = "select count(1) from dishonest where name='{}' and area='{}'".format(item['name'],item['area'])
        else:
            card = item['card_number']
            if len(card) == 18:
                card = card[:-7] + '****' + card[-4:]
                item['card_number'] = card
            select_count_sql = "select count(1) from dishonest where card_number='{}'".format(item['card_number'])
        self.cursor.execute(select_count_sql)
        # 返回查找结果
        count = self.cursor.fetchone()[0]
        if count == 0:
            # 核心语句，获取键和值的两个元组,通用语句
            keys, values = zip(*dict(item).items())
            insert_sql = 'insert into dishonest({}) values({})'.format(','.join(keys),','.join(['%s']*len(values)))
            # 这条语句十分高级，拼接ｖａｌｕｅ
            self.cursor.execute(insert_sql,values)
            self.connect.commit()
            spider.logger.info('插入数据！')
        else:
            spider.logger.info('数据重复！')
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()
