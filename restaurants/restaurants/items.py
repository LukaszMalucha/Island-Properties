# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RestaurantsItem(scrapy.Item):
	title = scrapy.Field()
	rating = scrapy.Field()
	cuisine = scrapy.Field()
	locality = scrapy.Field()
	address=scrapy.Field()
	link = scrapy.Field()
	


