# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from island_scraper.items import IslandScraperItem
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

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value] 

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)


## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")



class GranCanariaSpider(scrapy.Spider):
	name = 'gran_canaria'
	allowed_domains = ['www.idealista.com']
	start_urls = ['http://www.idealista.com/']

	def parse(self, response):
		agent = user_agent_rotator.get_random_user_agent()
		options.add_argument(f"user-agent={agent}")
		self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
		# self.driver = webdriver.Firefox(executable_path=str(Path(Path.cwd(), "geckodriver.exe")))
		self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
		self.driver.get("https://www.idealista.com/en/venta-viviendas/las-palmas/gran-canaria/con-precio-hasta_200000,metros-cuadrados-mas-de_40,pisos,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,aireacondicionado,ultimas-plantas,plantas-intermedias,obra-nueva,buen-estado/")
		sleep(1)
		body = self.driver.find_element_by_css_selector('body')
		body.send_keys(Keys.PAGE_DOWN)
		sleep(1)
		body.send_keys(Keys.PAGE_UP)
		sleep(1)
		body.send_keys(Keys.PAGE_DOWN)
		body.send_keys(Keys.HOME)

		sel = Selector(text=self.driver.page_source)	

		pages = sel.xpath('.//span[@class="breadcrumb-info"]/text()').extract()[1]
		pages = pages.replace(",", "").split(" ")[0]
		pages = int(pages) / 30 
		pages_count = int(pages) + 1

		self.driver.quit()


		for page in range (pages_count):
			agent = user_agent_rotator.get_random_user_agent()
			options.add_argument(f"user-agent={agent}")
			self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
			# self.driver = webdriver.Firefox(executable_path=str(Path(Path.cwd(), "geckodriver.exe")))

			self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
			self.driver.get(f"https://www.idealista.com/en/venta-viviendas/las-palmas/gran-canaria/con-precio-hasta_200000,metros-cuadrados-mas-de_40,pisos,de-dos-dormitorios,de-tres-dormitorios,de-cuatro-cinco-habitaciones-o-mas,aireacondicionado,ultimas-plantas,plantas-intermedias,obra-nueva,buen-estado/pagina-{page}.htm")
			sleep(1)
			body = self.driver.find_element_by_css_selector('body')
			sleep(1)
			body.send_keys(Keys.END)
			sleep(1)
			body.send_keys(Keys.HOME)

			try:
				picture = self.driver.find_elements_by_css_selector('picture')[randrange(1, 5)]
				hov = ActionChains(driver).move_to_element(picture)
				hov.perform()
			except:
				pass	

			sel = Selector(text=self.driver.page_source)
			adverts = sel.xpath('//article[contains(@class, "item")]')

			for advert in adverts:
				try:
					l = ItemLoader(item=IslandScraperItem(), selector=advert)
					title = advert.xpath('.//a[contains(@class, "item-link")]/@title').extract_first()
					address = title.split(" in ")[1]
					address_list = address.split(", ")
					locality = address_list[-1]	
					area = ""
					if len(address_list) > 1:				
						area =  address.split(", ")[-2]							
					price_string = advert.xpath('.//span[contains(@class, "item-price")]/text()').extract_first()
					price = price_string.replace(",", "")
					beds_string = advert.xpath('.//span[contains(@class, "item-detail")]/text()').extract_first()
					beds = beds_string.strip()
					size_string = advert.xpath('.//span[contains(@class, "item-detail")]/text()')[1].extract()
					size = size_string.strip()
					try:
						floor_string = advert.xpath('.//span[contains(@class, "item-detail")]/text()')[2].extract()
						floor = floor_string.replace("Floor", "").strip()
					except:
						floor		
					date = datetime.today().strftime('%Y-%m-%d')

				except:
					pass	

				l.add_value('island', "Mallorca")		
				l.add_value('locality', locality)
				l.add_value('area', area)
				l.add_value('price', price)
				l.add_value('beds', beds)
				l.add_value('size', size)
				l.add_value('floor', floor)
				l.add_value('date', date)
				yield l.load_item()	

			sleep(1)		
			self.driver.quit()		
