# -*- coding: utf-8 -*-
import scrapy


class GermanySpider(scrapy.Spider):
    name = 'germany'
    allowed_domains = ['www.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Germany_medical_cases']


    def parse(self, response):
    	table = response.xpath('//tbody')[0] 
    	trs = table.xpath('.//tr')[3:]
    	for tr in trs:
    		date=tr.xpath('.//th/text()').extract()
    	
    		daily_cases = tr.xpath('.//td[18]//text()').extract_first()

    		if daily_cases:
    			daily_cases=daily_cases.replace("\n","")

    		yield {"date":date, "daily_cases":daily_cases, "country":"Germany"}
