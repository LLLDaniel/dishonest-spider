# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
'''
抓取数据: 失信人名称, 失信人号码,法人(企业), 失信内容, 公布日期, 公布/执行单位, 创建日期, 更新日期
'''
import scrapy


class DishonestItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    card_number = scrapy.Field()
    # 企业年龄是０
    age = scrapy.Field()
    area = scrapy.Field()
    business_entity = scrapy.Field()
    content = scrapy.Field()
    publish_date = scrapy.Field()
    publish_unit = scrapy.Field()
    create_date = scrapy.Field()




    update_date = scrapy.Field()
    pass
