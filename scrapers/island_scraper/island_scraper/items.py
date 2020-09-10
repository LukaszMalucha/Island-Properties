# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IslandScraperItem(scrapy.Item):
	island = scrapy.Field()
	locality = scrapy.Field()
	area = scrapy.Field()
	price = scrapy.Field()
	beds = scrapy.Field()
	size = scrapy.Field()
	floor = scrapy.Field()
	date = scrapy.Field()