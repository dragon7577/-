# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:11:36 2018

@author: Python
"""

import urllib.request
import urllib.parse
import csv

with open("test.csv",'a',newline='',encoding="gb18030") as f:
    writer = csv.writer(f)
    writer.writerow(['徐哥',33])
    writer.writerow(['超哥',23])