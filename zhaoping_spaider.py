#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-4-19 下午7:43
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : zhaoping_spaider.py
# @Software: PyCharm
import requests,json
import pymysql
from bs4 import BeautifulSoup

class ZLZP(object):
    def __init__(self):
        self.city = "西安" #input('请输入工作城市:')
        self.work = "python工程师" #input('请输入工作类型:')
        self.page = 5 #input('请输入查询页数:')
        self.list = []

    def search(self):
        for i in range(self.page+1):
            url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl=' + self.city + '&kw=' + self.work + "&p=" +chr(i)
            soup = BeautifulSoup(requests.get(url).text)
            job_name = soup.select("table.newlist > tr > td.zwmc > div > a ")
            fankui_num = soup.select("table.newlist > tr > td.fk_lv")
            community_name = soup.select("table.newlist > tr > td.gsmc ")
            zwyx_num = soup.select("table.newlist > tr > td.zwyx")
            gzdd = soup.select("table.newlist > tr > td.gzdd")
            for a,b,c,d,e in zip(job_name,fankui_num,community_name,zwyx_num,gzdd):
                data ={
                    'job_name':a.get_text(),
                    'fankui_num':b.get_text(),
                    'community_name':c.get_text(),
                    'zwyx_num':d.get_text(),
                    'gzdd':e.get_text()
                }
                self.list.append(data)

    def sive(self):
        db = pymysql.connect("localhost", "root", "123456", "TESTDB",charset="utf8")
        curser = db.cursor()
        for i in self.list:
            sql = "insert into ZP_info values('%s','%s','%s','%s','%s')"

            # sql = "insert into ZP_info values('%s','%s','%s','%s','%s')"
            try:
                curser.execute('insert into ZP_info values("%s","%s","%s","%s","%s")' %(i['job_name'], i['fankui_num'], i['community_name'], i['zwyx_num'], i['gzdd']))
                db.commit()
                print('添加OK')
            except:
                db.rollback()
        db.close()

a = ZLZP()

