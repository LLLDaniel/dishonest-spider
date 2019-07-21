import requests
from pprint import pprint


url = 'http://jszx.court.gov.cn/api/front/getPublishInfoPageList'
data = {
    'pageNo': '2360', # 当前页号
    'pageSize': '10', # 页面容量
}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'http://jszx.court.gov.cn/front/zxxx.jspx'
           }
response = requests.post(url,headers=headers,data=data)
print(response.content.decode())