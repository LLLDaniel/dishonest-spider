import requests
from pprint import pprint


url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=6899&query=%E5%A4%B1%E4%BF%A1%E4%BA%BA&pn=10&rn=10&ie=utf-8&oe=utf-8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Referer': 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_pq=ef311f9e0000a959&rsv_t=9ae1xcshhA5xpdJipqaTmsKHLvVAVES8wzqIx6nzJB24F8b%2F%2BPElvL5fL4Q&rqlang=cn&rsv_enter=1&rsv_sug3=12&rsv_sug1=9&rsv_sug7=101&rsv_sug2=1&rsp=0&rsv_dl=th_0&rsv_sug9=es_0_1&inputT=9700&rsv_sug4=10054&rsv_sug=1'
           }
response = requests.get(url,headers=headers)
pprint(response.text)
with open('res.txt','w') as f:
    f.write(response.text)


