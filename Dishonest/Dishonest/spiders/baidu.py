# -*- coding: utf-8 -*-
import scrapy
import json
from jsonpath import jsonpath
from Dishonest.items import DishonestItem
from _datetime import datetime


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn=10&rn=10&ie=utf-8&oe=utf-8']


    def parse(self, response):
        datas = json.loads(response.text)
        # print(datas)
        disp_num = jsonpath(datas, '$..dispNum')[0]
        # print(disp_num)
        # name =
        url_patten = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn={}&rn=10&ie=utf-8&oe=utf-8'
        for i in range(0, disp_num, 10):
            url = url_patten.format(i)
            yield scrapy.Request(url, callback=self.parse_data)


    def parse_data(self, response):
        '''解析数据'''
        item = DishonestItem()
        data_str = json.loads(response.text)
        # print(len(data_str))
        # item['name'] = jsonpath(data_str, '$..iname')
        results = jsonpath(data_str, '$..result')[0]
        # print(len(results))
        for result in results:
            item['name'] = result['iname']
            item['age'] = result['age']
            item['area'] = result['areaName']
            item['business_entity'] = result['businessEntity']
            item['content'] = result['duty']
            item['card_number'] = result['cardNum']
            item['publish_date'] = result['publishDate']
            item['publish_unit'] = result['courtName']
            item['create_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            item['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print(item)
            yield item
        '''{"StdStg":6899,"StdStl":8,"_update_time":"1563185224","cambrian_appid":"0","changefreq":"always","age":"55","areaName":"安徽","areaNameNew":"安徽","businessEntity":"","cardNum":"3423011964****3224","caseCode":"(2019)皖1122执1194号","courtName":"来安县人民法院","disruptTypeName":"有履行能力而拒不履行生效法律文书确定义务","duty":"一、被告储成玲于本判决生效后十日内偿还原告张梅红借款人民币330000元及利息（自2019年3月13日起按年利率6%计算至付清之日止）；","focusNumber":"0","gistId":"(2019)皖1122民初1103号","gistUnit":"安徽省来安县人民法院","iname":"储成玲","partyTypeName":"0","performance":"全部未履行","performedPart":"暂无","publishDate":"2019年07月13日","publishDateStamp":"1562947200","regDate":"20190709","sexy":"女性","sitelink":"http:\/\/zxgk.court.gov.cn\/","type":"失信被执行人名单","unperformPart":"暂无","lastmod":"2019-07-15T03:08:21","loc":"http:\/\/shixin.court.gov.cn\/detail?id=707091354","priority":"1.0","SiteId":2015330,"_version":269,"_select_time":1563179419}
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
            update_date = scrapy.Field()'''


