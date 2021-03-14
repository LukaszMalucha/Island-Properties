# -*- coding: utf-8 -*-
import scrapy


class IrelandSpider(scrapy.Spider):
    name = 'ireland'
    allowed_domains = ['www.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Republic_of_Ireland_medical_cases']

    def parse(self, response):
    	table = response.xpath('//tbody')[2] 
    	trs = table.xpath('.//tr')[2:]
    	for tr in trs:
    		date=tr.xpath('.//td/text()').extract()
    			
    		daily_cases = tr.xpath('.//td[28]//text()').extract_first()

    		if daily_cases:
    			daily_cases=daily_cases.replace("\n","")

    		yield {"date":date, "daily_cases":daily_cases, "country":"Ireland"}
