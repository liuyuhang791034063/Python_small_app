#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-4-26 下午3:48
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : test.py
# @Software: PyCharm

from urllib.request import urlopen,Request,build_opener,urlretrieve,install_opener,HTTPError
from bs4 import BeautifulSoup
import os
download_base_url = "https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-"
downloadDirectory = "E:\p"


def gethtml(basehtml, i, types):
    opener = build_opener()
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    install_opener(opener)

    url = basehtml + types + "?page=" + str(i)
    print(url)
    req= Request(url)
    html = urlopen(req)
    bsObj = BeautifulSoup(html,"lxml")
    picture = bsObj.find("section", {"class": "thumb-listing-page"}).ul
    for i in picture:
        url = download_base_url + i.figure["data-wallpaper-id"] + ".jpg"
        print(url)
        try:
            urlretrieve(url, getDownloadPath(downloadHtml, url, downloadDirectory))
        except HTTPError:
            print("页面未找到")


def getDownloadPath(baseurl, absoluteurl, downloaddirectory):
    path = absoluteurl.replace("www.","")
    path = path.replace(baseurl,"")
    path = downloadDirectory+path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    return path


basehtml = "https://alpha.wallhaven.cc"
downloadHtml = "https://wallpapers.wallhaven.cc"

print("请选择类型:")
print("1.最新 2.榜单")
m = input()
if m == str(1):
    types = "/latest"
else:
    types = "/toplist"
n = input("请选择页数:")
for i in range(int(n)):
    gethtml(basehtml, i+1, types)

