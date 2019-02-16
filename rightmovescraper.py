# -*- coding: utf-8 -*-
import scrapy


class RightmovescraperSpider(scrapy.Spider):
    name = 'rightmovescraper'
    allowed_domains = ['https://www.rightmove.co.uk/property-to-rent/']
    start_urls = ['http://https://www.rightmove.co.uk/property-to-rent//']

    def parse(self, response):
        pass
