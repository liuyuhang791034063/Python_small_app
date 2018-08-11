# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from .settings import IMAGES_STORE


# 重写父类方法
class WallhavenSpdierPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        folder = item['name']
        type = item['type']
        filename = u'full/{0}.{1}'.format(folder, type)
        return filename

    def get_media_requests(self, item, info):
        """
        :param item: spider.py中返回的item
        :param info:
        :return:
        """
        img_url = item['url']
        if img_url == 0:
            return
        yield Request(img_url, meta={'item': item})

    def get_images(self, response, request, info):
        path = IMAGES_STORE + self.file_path(request, response=response, info=info)
        orig_image = response.body
        fp = open(path, 'wb')
        fp.write(orig_image)
        fp.close()
        return None, None, None

# 自定义实现管道
# 效率太低
# class WallhavenSpdierPipeline(object):
#     def process_item(self, item, spider):
#         url = item['url']
#         name = item['name']
#         type = item['type']
#         filepath = IMAGES_STORE + '/full/{0}.{1}'.format(name, type)
#         agent = random.choice(agents)
#         headers = {
#             'User-Agent': agent
#         }
#         fp = open(filepath, 'wb')
#         image = requests.get(url, headers=headers).content
#         fp.write(image)
#         fp.close()
