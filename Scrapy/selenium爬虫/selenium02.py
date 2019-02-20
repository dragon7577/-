from selenium import webdriver
import time

driver = webdriver.PhantomJS()
#打开百度
driver.get("http://www.baidu.com/")
#找到 搜索框 ,发送文字
key = input("请输入要搜索的内容:")
driver.find_element_by_id('kw').send_keys(key)
#找到 百度一下 按钮,点击一下
driver.find_element_by_id('su').click()
#截图
time.sleep(1)
driver.save_screenshot('美女.png')
driver.quit()
