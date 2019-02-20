# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 10:14:56 2018

@author: Python
"""
import re
html = '''
<div class="animal">
<p class="name">
<a title="Tiger"></a>
</p>
<p class="content">
     Two tigers two tigers run fast
</p>
</div>
<div class="animal">
<p class="name">
<a title="Rabbit"></a>
</p>
<p class="content">
    Small white rabbit white and white
</p>
</div>
'''
#p1 = re.compile('([A-Z][a-z]+.*)')
p2 = re.compile('<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>',re.S)
rlist = p2.findall(html)
print(rlist)
for r in rlist:
    print("动物名称:%s" % r[0].strip())
    print("动物描述:%s"% r[1].strip())
    print('*'*30)