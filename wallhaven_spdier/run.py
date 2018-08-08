# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       run
   Description:
   Author:           God
   date：            2018/8/8
-------------------------------------------------
   Change Activity:  2018/8/8
-------------------------------------------------
"""
__author__ = 'God'

from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'wallhaven'])