import requests


url = 'http://www.gsxt.gov.cn/affiche-query-area-info-paperall.html?noticeType=11&areaid=100000&noticeTitle=&regOrg=110000'

data = {
    # 'draw': '1',
    'start': '0',
    'length': '10'
}

# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    # 'Referer': 'http://www.gsxt.gov.cn/corp-query-entprise-info-xxgg-100000.html',
    'Cookie': '__jsluid_h=d791f7fe24032fd21dcfdfa8deca9d41; __jsl_clearance=1563508070.342|0|%2BJMXM5Wg82hPsEz1B%2Far%2BzmSpNo%3D; SECTOKEN=6962413454592052553;  tlb_cookie=S172.16.12.68'
}

proxies = {
    'http':'http://110.52.235.85:9999'
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
print(response.content.decode())