# -*- coding: utf-8 -*-
import scrapy


class FranceSpider(scrapy.Spider):
    name = 'france'
    allowed_domains = ['www.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/France_medical_cases']


    def parse(self, response):
    	table = response.xpath('//tbody')[1] 
    	trs = table.xpath('.//tr')[3:]
    	for tr in trs:
    		date=tr.xpath('./td/text()').extract_first()
    	
    		daily_cases = tr.xpath('./th/text()').extract_first()

    		if daily_cases:
    			daily_cases=daily_cases.replace("\n","")

    		yield {"date":date, "daily_cases":daily_cases, "country":"France"}