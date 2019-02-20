from bs4 import BeautifulSoup

html = '<div class="test">雄霸</div>'
#创建解析对象
soup = BeautifulSoup(html,'lxml')
#调用find_all()方法
rlist = soup.find_all('div',{'class':'test'})
print(rlist)