import requests

url = "http://httpbin.org/get"
headers = {"User-Agent":"Mozilla/5.0"}
proxies = {'http':"http://309435365:szayclhp@112.74.108.33:16818"}

res = requests.get(url,proxies=proxies,headers=headers,timeout=5)
res.encoding='utf-8'
html = res.text
print(html)