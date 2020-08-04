# -*- coding : utf-8 -*-
# @Time : 7/3/2020 15:58
# @Author : Briz
# @File : spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import sqlite3
import urllib.request,urllib.error
import xlwt
import re

from pip._vendor.requests import head



def main():
    baseurl="https://movie.douban.com/top250?start="
    #爬取网页
    datalist=getData(baseurl)
    savepath=".\\doubanTOP250.xls"
    #保存数据
    saveData(datalist,savepath)
    #askURL(baseurl)

findLink=re.compile(r'<a href="(.*?)">')      #创建正则表达式对象
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S)
findTitle=re.compile(r'<span class="title">(.*)</span>')
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge=re.compile(r'<span>(\d*)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*)</span>')
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)


def getData(baseurl):
    datalist=[]
    for i in range(0,10):    #调用获取页面的函数
        url=baseurl+str(i*25)
        html=askURL(url)    #保存获取到的源码

        soup=BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data=[]
            item=str(item)
            link=re.findall(findLink,item)[0]
            data.append(link)
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            title=re.findall(findTitle,item)
            if (len(title)>=2):    #如果有两个以上的名字则只保留前两个，若只有一个名字则保留该名字并留空防止错位
                ctitle=title[0]
                data.append(ctitle)
                ftitle=title[1].replace("/","")    #去掉无关的/符号
                data.append(ftitle)
            else:
                data.append(title[0])
                data.append(" ")        #若外文名不存在则留空防止错位
            rating=re.findall(findRating,item)
            data.append(rating)
            judge=re.findall(findJudge,item)
            data.append(judge)
            inq=re.findall(findInq,item)
            if len(inq)!=0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd=re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)    #去掉<br/>
            data.append(bd.strip())    #去除多余的空格

            datalist.append(data)
    #print(datalist)
    return datalist

def askURL(url):
    haed={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58"}
    request=urllib.request.Request(url,headers=haed)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e.reason):
            print(e.reason)
    return html

def saveData(datalist,savepath):
    print("Saving...")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("douban's movies top250",cell_overwrite_ok=True)
    col=("Movie's details link","Image's link","Movie's CHname","Movie's FOname","Ranking","Number of comments","Overview","Information")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savepath)




if __name__=="__main__":
    main()
    print("Crawl success!")