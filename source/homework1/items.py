# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YelpItem(scrapy.Item):
    doc_id = scrapy.Field()
    url = scrapy.Field()
    raw_content = scrapy.Field()
    timestamp_crawl = scrapy.Field()
    pass
