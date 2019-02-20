from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.jd.com/')
key = driver.find_element_by_id("key")
key.send_keys('爬虫书籍')
driver.find_element_by_xpath('//button[@class="button"]').click()
time.sleep(5)
#driver.save_screenshot('ok.png')
while True:
    #执行脚本,进度条拉到最底部
    driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
            )
    time.sleep(1)
    rlist = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
    for r in rlist:
        contentList = r.text.split('\n')
        print(contentList)
        price = contentList[0]
        name = contentList[1]
        commit = contentList[2]
        market = contentList[3]
        
        d = {
                '价格':price,
                '名称':name,
                '评论':commit,
                '店铺':market
                }
        with open('京东.txt','a') as f:
            f.write(str(d)+'\r\n')
    if driver.page_source.find('pn-next disabled') == -1:
        driver.find_element_by_class_name('pn-next').click()
        time.sleep(1)
    else:
        print('爬完了')
        break

driver.quit()