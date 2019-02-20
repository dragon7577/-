from selenium import webdriver
import time

#如何设置Chrome为无界面浏览器
opt = webdriver.ChromeOptions()
opt.set_headless()
opt.add_argument('windows-size=1920x3000')
driver = webdriver.Chrome(options=opt)

driver.get('http://www.renren.com/')
#窗口最大化
driver.maximize_window()
#用户名和密码发送
uname = driver.find_element_by_name('email')
uname.send_keys('13928006932')
pwd = driver.find_element_by_name('password')
pwd.send_keys('dong719261661')
#driver.save_screenshot('yam.png')
#yzm = input("请输入验证码:")
#driver.find_element_name('iode').send_keys(yzm)
driver.find_element_by_id('login').click()
time.sleep(3)
driver.save_screenshot('成功.png')