import requests

baseurl = 'https://sz.lianjia.com/ershoufang/s?'
headers = {'User-Agent':"Mozilla/5.0"}

key = input("搜索内容:")
pn = input("输入页数:")
pn = (int(pn) - 1)*10
#wd = key&pn=10
params = {
        'wd':key,
        'pn':pn,
        }
#无需拼接URL,也不用URL编码
res = requests.get(baseurl,params=params,headers=headers)
res.encoding='utf-8'
html = res.text
print(html)