import requests

class Weather:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
    
    def getWeather(self):
        city = input("请输入要查询天气的城市:")
        if city == '0':
            print('感谢使用，下次再会！')
        url = 'http://api.map.baidu.com/telematics/v3/' \
          'weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?' % city      
        result = requests.get(url).json()
        error = result.get('error')
        error = int(error)
        if error == 0:
            value = result['results'] #得到一个列表
            inf = value[0] #得到一个字典
            currentCity = inf['currentCity']
            weather_data = inf['weather_data']
            weather = weather_data[0]
            pm = inf['pm25']
            pm = int(pm)
            if (pm > 0) and (pm < 35):
                air_pm = '优'
            elif (pm >= 35) and (pm < 75):
                air_pm = '良'
            elif (pm >= 75) and (pm < 115):
                air_pm = '轻度污染'
            elif (pm >= 115) and (pm < 150):
                air_pm = '中度污染'
            elif (pm >= 150) and (pm < 250):
                air_pm = '重度污染'
            else:
                air_pm = '严重污染'
            print('*查询城市：%s ' % currentCity)
            print('*Pm值：%s  ' % inf['pm25'])
            print('*污染指数：%s' % air_pm)
            print('*当前温度：%s' % weather['date'])
            print('*风向：%s' % weather['wind'])
            print('*天气：%s' % weather['weather'])
            print('*温度：%s' % weather['temperature'])
        else:
            print('查询失败')

    
if __name__ == '__main__':
    weather = Weather()
    weather.getWeather()