# -*- coding: utf-8 -*-
from pathlib import Path
from random import randrange
from time import sleep

import scrapy
from restaurants.items import RestaurantsItem
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

        link_list = []
        for i in range(10):
            sel = Selector(text=self.driver.page_source)
            card = sel.xpath('.//div[@class="_1kXteagE"]')

            titles = card.xpath('.//a[@class="_15_ydu6b"]/@href').extract()
            for title in titles:
                t = "https://www.tripadvisor.ie" + title
                link_list.append(t)
            next_link = sel.xpath(
                './/a[contains(@class, "nav next rndBtn ui_button primary taLnk")]/@href').extract_first()
            next_link = "https://www.tripadvisor.ie" + next_link
            self.driver.get(next_link)
            sleep(2)

        self.driver.quit()

        for link in link_list[250:]:
            self.driver = webdriver.Chrome(str(Path(Path.cwd(), "chromedriver.exe")), chrome_options=options)
            self.driver.set_window_size(randrange(1100, 1200), randrange(800, 900))
            self.driver.get(link)
            sleep(1)
            page = Selector(text=self.driver.page_source)

            l = ItemLoader(item=RestaurantsItem(), selector=page)

            title = page.xpath('.//h1[@class="_3a1XQ88S"]/text()').extract_first()
            rating_string = page.xpath('.//a[@class="_3S6pHEQs"]/span/@title').extract_first()
            if rating_string:
                rating = rating_string.split(" ")[0]
            else:
                rating = "3"
            cuisine_list = page.xpath('.//span[@class="_13OzAOXO _34GKdBMV"]/a/text()').extract()
            if cuisine_list:
                cuisine = (", ").join(cuisine_list[1:])

            location = page.xpath('.//a[@class="_15QfMZ2L"]/text()').extract_first()
            if location:
                locality = location.split(", ")[-2]
                address_list = location.split(", ")[:-2]
                address = (", ").join(address_list)

            l.add_value('title', title)
            l.add_value('rating', rating)
            l.add_value('cuisine', cuisine)
            l.add_value('locality', locality)
            l.add_value('address', address)
            l.add_value('link', link)
            yield l.load_item()

            self.driver.quit()
