# -*- coding : utf-8 -*-
# @Time : 7/7/2020 13:50
# @Author : Briz
# @File : testBs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re

file=open("baidu.html","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")

#print(bs.title)
#print(bs.title.string)
#print(bs.a.attrs)
#print(bs)
#print(bs.head.contents[1])


# t_list=bs.find_all("a")
#
# for i in t_list:
#     print(i)

# t_list=bs.find_all(re.compile("a"))
# print(t_list)

# t_list=bs.find_all(text="hao123")
# for i in t_list:
#     print(i)


# t_list=bs.find_all(text=re.compile("\d"))
# for i in t_list:
#     print(i)

# print(bs.select(".mnav"))
# print(bs.select("#u1"))
# print(bs.select(".mnav"))

# t_list = bs.find_all(["meta","title"])
# for item in t_list:
#     print(item)
print(bs.select('a[class="bri"]'))
print(bs.select('a[href="http://tieba.baidu.com"]'))

