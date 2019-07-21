# -*- coding: utf-8 -*-
import scrapy
import json
from datetime import datetime
from Dishonest.items import DishonestItem


class CourtSpider(scrapy.Spider):
    name = 'court'
    allowed_domains = ['court.gov.cn']
    # 由于是post请求
    # start_urls = ['http://jszx.court.gov.cn/api/front/getPublishInfoPageList']
    # start_urls = ['http://jszx.court.gov.cn/api/front/getPublishInfoPageList']

    # 构建初始请求
    def start_requests(self):
        self.post_url = 'http://jszx.court.gov.cn/api/front/getPublishInfoPageList'
        data = {

                'pageNo': '1',  # 当前页号
                'pageSize': '10',  # 页面容量

        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'http://jszx.court.gov.cn/front/zxxx.jspx'
            }
        yield scrapy.FormRequest(self.post_url,formdata=data,callback=self.parse)

    def parse(self, response):
        # print(response.text)
        results = json.loads(response.text)
        page_count = results['pageCount']
        for i in range(page_count):
            data = {
                'pageNo': str(i),  # 当前页号
                'pageSize': '10',  # 页面容量
            }
            yield scrapy.FormRequest(self.post_url, formdata=data, callback=self.parse_data)
        pass
    '''
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
    create_date = scrapy.Field()
    '''
    def parse_data(self,response):
        item = DishonestItem()
        res = json.loads(response.text)
        datas = res['data']
        for data in datas:
            item['name'] = data['name']
            item['age'] = data['age']
            item['area'] = data['areaName']
            item['card_number'] = data['cardNum']
            # card = data['cardNum']

            item['business_entity'] = data['buesinessEntity']
            item['content'] = data['duty']
            item['publish_date']= data['publishDate']
            item['publish_unit'] = data['courtName']
            item['create_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(item)
            yield item


