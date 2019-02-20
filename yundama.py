from lxml import etree
from selenium import webdriver
import time
import requests
from PIL import Image
from pytesseract import *
import http.client, mimetypes, urllib, json, time, requests

######################################################################

class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'
    username = ''
    password = ''
    appid = ''
    appkey = ''

    def __init__(self, username, password, appid, appkey):
        self.username = username
        self.password = password
        self.appid = str(appid)
        self.appkey = appkey

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def report(self, cid):
        data = {'method': 'report', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid), 'flag': '0'}
        response = self.request(data)
        if (response):
            return response['ret']
        else:
            return -9001

    def post_url(self, url, fields, files=[]):
        for key in files:
            files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text


url = 'https://www.douban.com/'
headers = {"User-Agent":"Mozilla/5.0"}
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
#把验证码图片的连接提取出来，并发请求，保存到本地
parseHtml = etree.HTML(driver.page_source)
rLink = parseHtml.xpath('//img[@id="captcha_image"]/@src')[0]
res = requests.get(url=rLink,headers=headers)
res.encoding='utf-8'
html = res.content
with open("getimage.jpg",'wb') as f:
    f.write(html)

username = 'zhenghongyu'

# 密码
password = '381650127yhz'

# 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appid = 1

# 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
appkey = '22cc5376925e9387a23cf797cb9ba745'

# 图片文件
filename = 'getimage.jpg'

# 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype = 3000

# 超时时间，秒
timeout = 10

# 检查
if (username == 'username'):
    print('请设置好相关参数再测试')
else:
    # 初始化
    yundama = YDMHttp(username, password, appid, appkey)

    # 登陆云打码
    uid = yundama.login();
    print('uid: %s' % uid)

    # 查询余额
    balance = yundama.balance();
    print('balance: %s' % balance)

    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(filename, codetype, timeout);
    print('cid: %s, result: %s' % (cid, result))

#用户名、密码
uname = driver.find_element_by_name('form_email')
uname.send_keys('719261661@qq.com')
pwd = driver.find_element_by_name('form_password')
pwd.send_keys('dong719261661')
yzm = driver.find_element_by_id('captcha_field')
yzm.send_keys(result)
login = driver.find_element_by_class_name('bn-submit')
login.click()
time.sleep(3)
 
# driver.close()