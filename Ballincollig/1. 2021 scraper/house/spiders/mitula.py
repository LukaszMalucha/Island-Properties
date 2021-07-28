# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
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
from datetime import date

from house.items import BallincolligItem

## AVOID HANDSHAKE ERRORS
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--incognito")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")

software_names = [SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value,] 
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

today = date.today()
todays_date = today.strftime("%Y-%m-%d")

urls = [
"https://homes.mitula.ie/searchRE/level2-Ballincollig/sort-0/min_price-200000/max_price-400000/q-houses-ballincollig?req_sgmt=REVTS1RPUDtTRU87U0VSUDs=",
"https://homes.mitula.ie/searchRE/level1-Cork/level2-Ballincollig/sort-0/min_price-200000/max_price-400000/q-houses-ballincollig/pag-2?req_sgmt=REVTS1RPUDtTRU87U0VSUDs=",
"https://homes.mitula.ie/searchRE/level1-Cork/level2-Ballincollig/sort-0/min_price-200000/max_price-400000/q-houses-ballincollig/pag-3?req_sgmt=REVTS1RPUDtTRU87U0VSUDs=",
"https://homes.mitula.ie/searchRE/level1-Cork/level2-Ballincollig/sort-0/min_price-200000/max_price-400000/q-houses-ballincollig/pag-4?req_sgmt=REVTS1RPUDtTRU87U0VSUDs="
]



class MitulaSpider(scrapy.Spider):
    name = 'mitula'
    allowed_domains = ['homes.mitula.ie']
    start_urls = ['https://homes.mitula.ie/']

    def parse(self, response):
        agent = user_agent_rotator.get_random_user_agent()
        options.add_argument(f"user-agent={agent}")
        self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
        self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))


        links = []
        for page in urls:
            agent = user_agent_rotator.get_random_user_agent()
            options.add_argument(f"user-agent={agent}")
            self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
            self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
            self.driver.get(page)
            sleep(2)
            self.driver.get(page)
            body = self.driver.find_element_by_css_selector('body')
            sleep(1)
            body.send_keys(Keys.END)
            sleep(1)
            body.send_keys(Keys.HOME)
            sel = Selector(text=self.driver.page_source)


            adverts = sel.xpath('//div[contains(@class, "lis_ting_Ad item-card")]')

            for ad in adverts:
            
                full_link = "mitula.ie"

                price =  ad.xpath('.//div[contains(@class, "item-card__price ")]/text()').extract_first()
                address =  ad.xpath('.//span[contains(@class, "item-card__title hover-cursor-pinter  ")]/text()').extract_first()  
                try:  
                    beds = ad.xpath('//div[contains(@class, "item-card__property")]/span/text()')[0].extract()    
                except:
                    beds = "0"   
                try:
                    baths = ad.xpath('//div[contains(@class, "item-card__property")]/span/text()')[1].extract()    
                except:
                    baths = "0"  
                try:                    
                    size = ad.xpath('//div[contains(@class, "item-card__property")]/span/text()')[2].extract()     
                except:
                    size = "0"


                property_type = "None"
                popularity = "None"

                l = ItemLoader(item=BallincolligItem(), selector=sel)
                l.add_value('price', price)                     
                l.add_value('address', address)       
                l.add_value('beds', beds)
                l.add_value('baths', baths)
                l.add_value('size', size)
                l.add_value('property_type', property_type)
                l.add_value('popularity', popularity)
                l.add_value('date', todays_date)
                yield l.load_item()   

            
        self.driver.quit()    











                



           