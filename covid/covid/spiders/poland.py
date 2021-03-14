# -*- coding: utf-8 -*-
import scrapy


class PolandSpider(scrapy.Spider):
    name = 'poland'
    allowed_domains = ['www.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/Poland_medical_cases']

    def parse(self, response):
    	table = response.xpath('//tbody')[0] 
    	trs = table.xpath('.//tr')[1:]
    	for tr in trs:
    		date=tr.xpath('.//td/span/text()').extract_first()
    		if not date:
    			date=tr.xpath('.//td/text()').extract_first()
    		daily_cases = tr.xpath('.//td[5]//text()').extract_first()

    		if daily_cases:
    			daily_cases=daily_cases.replace("\n","")

    		yield {"date":date, "daily_cases":daily_cases, "country":"Poland"}


