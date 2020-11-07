# -*- coding: utf-8 -*-
import scrapy


class UkSpider(scrapy.Spider):
	name = 'uk'
	allowed_domains = ['www.wikipwdia.org']
	start_urls = ['https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/United_Kingdom_medical_cases']

	def parse(self, response):
		table = response.xpath('//tbody')[0] 
		trs = table.xpath('.//tr')[4:]
		for tr in trs:
			date=tr.xpath('.//th').extract_first()[41:]
		
			daily_cases_1 = tr.xpath('.//td[1]//text()').extract_first()
			daily_cases_2 = tr.xpath('.//td[2]//text()').extract_first()
			daily_cases_3 = tr.xpath('.//td[3]//text()').extract_first()
			daily_cases_4 = tr.xpath('.//td[4]//text()').extract_first()

			if daily_cases_1:
				daily_cases_1=daily_cases_1.replace("\n","")
				daily_cases_1=daily_cases_1.replace("â€‰","")

			if daily_cases_2:
				daily_cases_2=daily_cases_2.replace("\n","")
				daily_cases_2=daily_cases_2.replace("â€‰","")

			if daily_cases_3:
				daily_cases_3=daily_cases_3.replace("\n","")        
				daily_cases_3=daily_cases_3.replace("â€‰","")        

			if daily_cases_4:
				daily_cases_4=daily_cases_4.replace("\n","") 
				daily_cases_4=daily_cases_4.replace("â€‰","")     





			yield {"date":date, "daily_cases1":daily_cases_1, "daily_cases2":daily_cases_2,"daily_cases3":daily_cases_3,"daily_cases4":daily_cases_4,"country":"UK"}