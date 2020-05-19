#-*- coding = utf-8 -*-
#@Time      : 2020/5/17 16:49
#@Author    : Shanhe.Tan
#@File      : spider.py
#@Software  : PyCharm

import sys
import re                               #正则表达式进行文字匹配
from bs4 import BeautifulSoup           #进行网页解析，获取数据
import urllib.request,urllib.error      #指定URL获取网页数据
import xlwt                             #进行excel操作
import sqlite3                          #进行SQLite数据库操作

def main():
    print("hello")
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    #保存数据
    # savaData(savepath)

    askURL("https://movie.douban.com/top250?start=0")

#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10):           #调用获取页面信息的函数，10次
        url = baseurl + str(i * 25)
        html = askURL(url)          #保存获取到的网页源码

        # 逐一解析数据


    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head = {    #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72"
    }   #用户代理，表示告诉服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接受什么水平的文件内容

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html



#保存数据
def savaData(savepath):
    pass



if __name__ == "__main__":  #当程序执行时
    #调用函数
    main()