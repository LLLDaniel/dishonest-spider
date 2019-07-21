# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
import requests
from Dishonest.settings import USER_AGENT,REDIS_URL,COOKIES_KEY, COOKIES_PROXY_KEY, COOKIES_USER_AGENT_KEY, REDIS_COOKIES_KEY
from scrapy import signals
from Dishonest.spiders import GsxtSpider
from redis import StrictRedis
import pickle
'''
实现随机User-Agent下载器中间
准备User-Agent列表
定义RandomUserAgent类
实现process_request方法, 设置随机的User-Agent
'''

class RandomUserAgent(object):

    def process_request(self, request, spider):
        if isinstance(spider, GsxtSpider):
            return None
        request.headers['User-Agent'] = random.choice(USER_AGENT)
        return None



class ProxyMiddleware(object):

    def process_request(self, request, spider):
        if isinstance(spider, GsxtSpider):   #　导致第三个中间键是公士系统专用
            return None
        protocal = request.url.split('//')[0]
        proxy_url = 'http://127.0.0.1:16888/protocal={}'.format(protocal)
        response = requests.get(proxy_url)
        #　获取代理IP
        request.meta['proxy'] = response.content.decode()
        return None

"""
实现公示系统中间类:
步骤
    1. 实现process_request方法, 从Redis中随机取出Cookie来使用, 关闭页面重定向.
    2. 实现process_response方法, 如果响应码不是200 或 没有内容重试
"""

class GsxtCookieMiddleware(object):

    def __init__(self):
        """建立Redis数据库连接"""
        self.redis = StrictRedis.from_url(REDIS_URL)

    def process_request(self, request, spider):
        """从Redis中随机取出Cookie来使用, 关闭页面重定向."""
        count = self.redis.llen(REDIS_COOKIES_KEY)
        random_index = random.randint(0, count-1)
        # 根据索引取值
        cookie_data = self.redis.lindex(REDIS_COOKIES_KEY, random_index)
        # 反序列化, 把二进制转换为字典
        cookie_dict = pickle.loads(cookie_data)

        # 把cookie信息设置request
        request.headers['User-Agent'] = cookie_dict[COOKIES_USER_AGENT_KEY]
        # 设置请求代理IP
        request.meta['proxy'] = cookie_dict[COOKIES_PROXY_KEY]
        # 设置cookie信息
        request.cookies = cookie_dict[COOKIES_KEY]
        # 设置不要重定向
        request.meta['dont_redirect'] = True

    def process_response(self, request, response, spider):
        """如果响应码不是200 或 没有内容重试"""
        # print(response.status)
        if response.status != 200 or response.body == b'':
            # 备份请求
            req = request.copy()
            # 设置请求不过滤
            req.dont_filter = True
            # 把请求交给引擎
            return req

        return response