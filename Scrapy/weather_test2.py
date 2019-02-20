
def today():
    if currentCity == city:
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
        print('*    查询城市：%s ' % currentCity)
        print('*    Pm值：%s  ' % inf['pm25'])
        print('*    污染指数：%s' % air_pm)
        print('*    当前温度：%s' % weather['date'])
        print('*    风向：%s' % weather['wind'])
        print('*    天气：%s' % weather['weather'])
        print('*    温度：%s' % weather['temperature'])
 
 
def future():
    wednesday = weather_data[1]
    thursday = weather_data[2]
    finday = weather_data[3]
    print('*********%s未来三天天气预报************' % city)
    print('*    日期：%s' % wednesday['date'])
    print('*    天气：%s' % wednesday['weather'])
    print('*    风向：%s' % wednesday['wind'])
    print('*    温度：%s' % wednesday['temperature'])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('*    日期：%s' % thursday['date'])
    print('*    天气：%s' % thursday['weather'])
    print('*    风向：%s' % thursday['wind'])
    print('*    温度：%s' % thursday['temperature'])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('*    日期：%s' % finday['date'])
    print('*    天气：%s' % finday['weather'])
    print('*    风向：%s' % finday['wind'])
    print('*    温度：%s' % finday['temperature'])
 
 
while True:
    print('*    欢迎使用智游天气查询工具      *')
    print('*     1.查询该城市的实时天气       *')
    print('*     2.查询该城市的未来三天天气     *')
    print('*    0.退出程序                *')
    city = input('请输入您要查询的城市：')
    if city == '0':
        print('感谢使用！')
        break
    import requests
    url = 'http://api.map.baidu.com/telematics/v3/' \
          'weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?' % city
    # 1.通过请求拿回数据
    response = requests.get(url)
    # 2.将数据转换为字典
    result = response.json()
    # 天气预报中的 error的值如果是0，表示输入的城市能查到天气预报，否则没有天气预报数据，返回的error的值不为0
    error = result.get('error')
    error = int(error)
    if error == 0:
        while True:
            choose = input('*                请输入您的操作（退出请输入q）：  ')
            if choose == 'q':
                break
            try:
                choose = int(choose)
            except:
                print('输入有误！请重新输入!')
                continue
            else:
                if choose < 1 or choose > 2:
                    print('您输入的选项不存在！请重新输入!')
                    continue
                else:
                    value = result['results']
                    inf = value[0]
                    currentCity = inf['currentCity']
                    weather_data = inf['weather_data']
                    if choose == 1:
                        today()
                    elif choose == 2:
                        future()
    else:
        print('您输入的城市没有天气预报，请重新输入！')
        continue