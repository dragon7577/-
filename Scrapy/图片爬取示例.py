import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545973743385&di=7f0579b54915442bde2951ddb048ba6d&imgtype=0&src=http%3A%2F%2Fpic4.iqiyipic.com%2Fimage%2F20181016%2F23%2F03%2Fv_119993043_m_601_720_405.jpg'
headers = {"User-Agent":"Mozilla/5.0"}

#发请求,指编码,获内容
res = requests.get(url,headers=headers)
res.encoding='utf-8'
html = res.content

with open('赵丽颖.jpg','wb') as f:
    f.write(html)
print('ok')