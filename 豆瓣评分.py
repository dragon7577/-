from lxml import etree
from selenium import webdriver
import time
import requests
from PIL import Image
from pytesseract import *

url = 'https://www.douban.com/'
headers = {"User-Agent":"Mozilla/5.0"}
driver = webdriver.Chrome()
driver.get(url)
time.sleep(1)
#把验证码图片的连接提取出来，并发请求，保存到本地
parseHtml = etree.HTML(driver.page_source)
result = parseHtml.xpath('//img[@id="captcha_image"]/@src')[0]
print(result)
res = requests.get(url=result,headers=headers)
res.encoding='utf-8'
html = res.content
with open("验证码.jpg",'wb') as f:
    f.write(html)
#把图片转为字符串
img = Image.open('验证码.jpg')
result = image_to_string(img)
print(result)
#用户名、密码
uname = driver.find_element_by_name('form_email')
uname.send_keys('13928006932')
pwd = driver.find_element_by_name('form_password')
pwd.send_keys('dong719261661')
yzm = driver.find_element_by_id('captcha_field')
yzm.send_keys(result)
login = driver.find_element_by_class_name('bn-submit')
login.click()
time.sleep(2)
