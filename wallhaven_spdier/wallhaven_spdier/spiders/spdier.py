# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：       spdier
   Description:
   Author:           God
   date：            2018/8/8
-------------------------------------------------
   Change Activity:  2018/8/8
-------------------------------------------------
"""
__author__ = 'God'

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spider import CrawlSpider, Rule

from ..items import WallhavenSpdierItem
from ..config import PAGE_NUMBER, BAN_TAGS


class Spider(CrawlSpider):
    name = 'wallhaven'
    allowed_domains = ['alpha.wallhaven.cc']
    bash_url = 'https://alpha.wallhaven.cc/random?page='

    def start_requests(self):
        for i in range(1, PAGE_NUMBER + 1):
            yield Request(self.bash_url + str(i))

    rules = (
        Rule(LinkExtractor(allow=('https://alpha.wallhaven.cc/wallpaper/\d{1,6}$',)), callback='parse_item'),
    )

    def parse_item(self, response):
        item = WallhavenSpdierItem()
        tags = response.xpath('//*[@id="tags"]/child::li/a/text()').extract()
        ban_tags = BAN_TAGS
        for tag in ban_tags:
            if tag in tags:
                return
        item['url'] = str('https:' + response.xpath('//*[@id="wallpaper"]/@src').extract_first(default=0))
        item['name'] = item['url'].split('/')[-1].split('.')[0]
        item['type'] = item['url'].split('/')[-1].split('.')[1]
        yield item

