# -*- coding: utf-8 -*-

import scrapy
from newsSpider.items import NewsspiderItem 

class DmozSpider(scrapy.Spider):
    name = "huxiu"
    start_urls = [
        "http://www.huxiu.com"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        filename = "huxiu"
        with open(filename, 'wf') as f:
            for newsCell in response.css("div.mod-b"):               
                item = NewsspiderItem()
                item["title"] = (newsCell.css("h3 a").extract())[0].encode("utf-8")
                f.write(item["title"])
                yield item