# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from restaurants.items import RestaurantsItem
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import csv
from random import randrange
from datetime import datetime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")





class TripSpider(scrapy.Spider):
	name = 'trip'
	allowed_domains = ['www.tripadvisor.ie']
	start_urls = ['http://www.tripadvisor.ie/']

	def parse(self, response):
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		self.driver.get("https://www.tripadvisor.ie/Restaurants-g662606-Costa_Adeje_Adeje_Tenerife_Canary_Islands.html")
		sleep(2)
		body = self.driver.find_element_by_css_selector('body')
		body.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		body.send_keys(Keys.PAGE_UP)
		sleep(1)
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.HOME)

		sel = Selector(text=self.driver.page_source)
		card=sel.xpath('.//div[@class="_1kXteagE"]')

		for i in range(10):
			next_button =  self.driver.find_element_by_xpath('//a[contains(@class, "nav next rndBtn ui_button primary taLnk")]')
			next_button.click()
			sleep(1)
			"""
			hrefy do listy z buttonu a pozniej loop
			"""



		# titles=card.xpath('.//a[@class="_15_ydu6b"]/@href').extract()
		# link_list = []
		# for title in titles:
		# 	t = "https://www.tripadvisor.ie" + title
		# 	link_list.append(t)

		# self.driver.quit()	

		# for link in link_list:
		# 	self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		# 	self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		# 	self.driver.get(link)
		# 	sleep(2)
		# 	page = Selector(text=self.driver.page_source)
			
		# 	l = ItemLoader(item=RestaurantsItem(), selector=page)

		# 	title=page.xpath('.//h1[@class="_3a1XQ88S"]/text()').extract_first()
		# 	rating_string=page.xpath('.//a[@class="_3S6pHEQs"]/span/@title').extract_first()
		# 	if rating_string:
		# 		rating=rating_string.split(" ")[0]  
		# 	else:
		# 		rating="3"
		# 	cuisine_list=page.xpath('.//span[@class="_13OzAOXO _34GKdBMV"]/a/text()').extract()
		# 	if cuisine_list:
		# 		cuisine=(", ").join(cuisine_list[1:])

		# 	location=page.xpath('.//a[@class="_15QfMZ2L"]/text()').extract_first()
		# 	if location:
		# 		locality=location.split(", ")[-2]
		# 		address_list=location.split(", ")[:-2]
		# 		address=(", ").join(address_list)


		# 	l.add_value('title', title)
		# 	l.add_value('rating', rating)
		# 	l.add_value('cuisine', cuisine)
		# 	l.add_value('locality', locality)
		# 	l.add_value('address', address)
		# 	l.add_value('link', link)
		# 	yield l.load_item()	

		# 	self.driver.quit()	

















