import requests

url = "http://baidu.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
res = requests.get(url,headers=headers)
res.encoding='utf-8'
print(res.encoding)
print(type(res.text))
print(type(res.content))
print(res.status_code)
print(res.url)