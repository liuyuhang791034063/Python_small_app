#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-4-26 下午5:14
# @Author  : GodFather
# @Email   : liuyuhang791034063@qq.com
# @File    : test.py
# @Sotware: PyCharm

from urllib.request import urlopen
from urllib.error import HTTPError
import json
from time import sleep
import smtplib
from email.mime.text import MIMEText
from email.header import Header

HOST = "smtp.163.com"
sender="l791034063@163.com"
receivers = ['liuyuhang791034063@qq.com']

def getdate(baseUrl):
    html = urlopen(baseUrl)
    try:
        a = json.loads(html.read())
        datetime = a["sysTime2"]
        return datetime
    except HTTPError:
        return None

def datetime_deal(datetime):
    one = datetime.split(' ')[0]
    two = datetime.split(' ')[1]
    year,month,day = one.split('-')
    hour,minute,second = two.split(':')
    return year+"年 "+month+"月 "+day+"日 "+hour+"时 "+minute+"分 "+second+"秒"

def sendemail(datetime):
    msg = MIMEText('现在的时间是%s' % datetime,'plain', 'utf-8')
    msg['From'] = Header('老刘','utf-8')
    msg['To'] = receivers[0]
    msg['Subject'] = Header('老刘报时间', 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(HOST, 25)
        smtpObj.login(sender, 'l791034063')
        smtpObj.sendmail(sender, receivers, msg.as_string())
        smtpObj.quit()
    except smtplib.SMTPException:
        print('Error')

baseUrl = "http://quan.suning.com/getSysTime.do"
hour_old = getdate(baseUrl).split(' ')[1].split(':')[2]

while True:
    datetime = getdate(baseUrl)
    print(hour_old)
    hour = datetime.split(' ')[1].split(':')[2]
    print(hour)
    if hour != hour_old:
        datetime = datetime_deal(datetime)
        sendemail(datetime)
        hour_old = hour
        print("发送成功!")
    if hour is None:
        print("发送失败!")
        break
    sleep(10)
