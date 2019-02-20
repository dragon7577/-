from selenium import webdriver

driver = webdriver.PhantomJS()
driver.get('http://www.qiushibaike.com/text/')
#查找单个节点
rOne = driver.find_element_by_class_name('content')
#print(rOne.text)
rMany = driver.find_elements_by_class_name('content')
for r in rMany:
    print('*' * 40)
    print(r.text)