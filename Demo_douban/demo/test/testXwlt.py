# -*- coding : utf-8 -*-
# @Time : 7/14/2020 15:12
# @Author : Briz
# @File : testXwlt.py
# @Software: PyCharm

import xlwt

workbook=xlwt.Workbook(encoding="utf-8")
worksheet=workbook.add_sheet("sheet1")
for i in range(1,10):
    for j in range(1,i+1):
        worksheet.write(i-1, j-1, i*j)
workbook.save('text.xls')