import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

while True:
    city = input("请输入要查询天气的城市:")
    if city == '0':
        print('感谢使用，下次再会！')
        break
    url = 'http://api.map.baidu.com/telematics/v3/' \
          'weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?' % city         
    res = requests.get(url)
    r = res.json()
    print(r['results'])
    break