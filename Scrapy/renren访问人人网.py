import urllib.request
import urllib.parse

url = "http://www.renren.com/969267756/profile"
headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cache-Control': 'max-age=0',
'Connection': 'keep-alive',
'Cookie': 'anonymid=jq7di3n4-mczqb6; depovince=GW; _r01_=1; JSESSIONID=abc-jJI62Cmvk8xVUEYFw; ick_login=5b8bfd14-e40d-4975-b434-b7a77b3a875a; t=5c0b65358df701093a672a513a3b71826; societyguester=5c0b65358df701093a672a513a3b71826; id=969267756; xnsid=d845c6d; ver=7.0; loginfrom=null; jebe_key=8d18216d-5cd1-46bd-b8bb-04568de9bf07%7Cd31a2a2724a9fe1f6eb23102a1c5462a%7C1545961450056%7C1%7C1545961449101; wp_fold=0; jebecookies=874c7c3f-ef38-471a-8643-d8291859e95c|||||',
'Host': 'www.renren.com',
'Referer': 'http://sc.renren.com/scores/mycalendar',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read()

print(str(html))