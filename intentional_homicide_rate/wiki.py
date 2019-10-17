# -*- coding: utf-8 -*-
import csv

import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate",
    ]

    def parse(self, response):
        country_names_pre = response.xpath("(//table)[2]//a/text()").getall()
        country_names = country_names_pre[3:]
        rank = []
        for i in response.xpath("(//table)[2]//td[1]/text()").getall():
            data = i.replace("\n", "").replace(" ", "")
            if len(data) > 0 and int(data):
                rank.append(data)
        area = []
        for i in response.xpath("(//table)[2]//td[2]/text()").getall():
            data = i.replace("\n", "")
            if len(data) > 0:
                area.append(data)
        subarea = []
        for i in response.xpath("(//table)[2]//td[3]/text()").getall():
            data = i.replace("\n", "")
            if len(data) > 0:
                subarea.append(data)
        rate = []
        for i in response.xpath("(//table)[2]//td[4]/text()").getall():
            data = i.replace("\n", "")
            if len(data) > 0:
                rate.append(data)

        count = []
        for i in response.xpath("(//table)[2]//td[5]/text()").getall():
            data = i.replace("\n", "")
            if len(data) > 0:
                count.append(data)

        year = []
        for i in response.xpath("(//table)[2]//td[6]/text()").getall():
            data = i.replace("\n", "")
            if len(data) > 0:
                year.append(data)
        array = []
        for key, name in enumerate(country_names):
            buff = []
            buff.append(name)
            buff.append(rank[key])
            buff.append(area[key])
            buff.append(subarea[key])
            buff.append(rate[key])
            buff.append(count[key])
            buff.append(year[key])
            array.append(buff)
            print(buff)
        with open("intentional_homicide_rates.csv", "w") as write:
            writer = csv.writer(write)
            for i in array:
                writer.writerow(i)
