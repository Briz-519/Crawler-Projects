# -*- coding : utf-8 -*-
# @Time : 7/29/2020 13:57
# @Author : Briz
# @File : YYeTs.py
# @Software: PyCharm

import urllib.request,urllib.error
import re
from bs4 import BeautifulSoup
import xlwt


findLink=re.compile(r'<a href="(.*?)".*target="_blank">',re.S)
findImg=re.compile(r'<img rel="(.*?)"',re.S)
findCtitle=re.compile(r'<strong>(.*?)</strong>')
findEtitle=re.compile(r'<span class="f14">(.*?)</span>')
findType=re.compile(r'<p>(.*?)<br/>.*<span>.*</span></p>')
findState=re.compile(r'<p>.*<br/>(.*?)<span>.*</span></p>')
findCollect=re.compile(r'<span> \( 收藏 (\d*) \)</span>')
def main():
    baseurl = "http://www.rrys2020.com/html/top/total_fav_list.html"
    datalist = getData(baseurl)
    savepath = ".\\YYeTs_TOP50.xls"
    saveData(datalist, savepath)

def getData(baseurl):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58"
    }
    request=urllib.request.Request(baseurl,headers=headers)
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e.reason):
            print(e.reason)
    datalist = []
    soup=BeautifulSoup(html,'html.parser')
    for item in soup.find_all('div',class_="a0"):
        item=str(item)
        data=[]
        url=[]
        # Link=str(re.findall(findLink,item))
        # data.append("http://www.rrys2020.com"+str(Link))
        Imgurl=re.findall(findImg,item)
        data.append(Imgurl)
        Ctitle=re.findall(findCtitle,item)
        data.append(Ctitle)
        Etitle = re.findall(findEtitle, item)
        data.append(Etitle)
        Type=re.findall(findType,item)
        data.append(Type)
        State=re.findall(findState,item)
        data.append(State)
        Collect=re.findall(findCollect,item)
        data.append(Collect)
        datalist.append(data)

    #print(datalist)
    return datalist

def saveData(datalist, savepath):
    print("Saving...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("douban's movies top250", cell_overwrite_ok=True)
    col=("Img","Cname","Ename","Type","State","Fav")
    for i in range(0,7):
        sheet.write(1,i,col[i])
    for i in range(1,51):
        data=datalist[i]
        for j in range(0,7):
            sheet.write(i+1,j,data[j])
    book.save(savepath)


if __name__=="__main__":
    main()
    print("Finish!")