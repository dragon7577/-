from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://music.163.com/#/discover/toplist?id=2250011882')
time.sleep(5)
title = driver.find_elements_by_xpath('//tr[@class="even"]//b/@class')
for t in title:
    print(t.text)