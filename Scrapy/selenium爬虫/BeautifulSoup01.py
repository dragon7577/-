from bs4 import BeautifulSoup

html = '''
<div class="test">雄霸</div>
<div class="">步惊云</div>
<div class="test1">段浪
    <span>聂风</span>
</div>
'''
#创建解析对象
soup = BeautifulSoup(html,'lxml')
#调用find_all()方法
rlist = soup.find_all('div',{'class':'test1'})
#print(rlist)
for r in rlist:
    print(r.get_text())
    print(r.span.string)