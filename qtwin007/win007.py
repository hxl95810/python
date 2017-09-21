# -*- coding: utf-8 -*-
import scrapy


class Win007Spider(scrapy.Spider):
    name = 'win007'
    allowed_domains = ['www.win007.com']
    start_urls = ['http://www.win007.com/']

    def parse(self, response):
        pass
