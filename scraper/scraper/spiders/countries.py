"""
"""
import re

import requests
from bs4 import BeautifulSoup
from scrapy import Spider
from scrapy.loader import ItemLoader

from ..items import CountryItem

__author__ = "aserhii@protonmail.com"


class CountriesSpider(Spider):
    """A configuration of a spider."""

    name = "countries"
    custom_settings = {
        'FEED_EXPORT_FIELDS': (
            "country",
            "freedomhouse_score",
            "quality_of_life_index",
            "purchasing_power_index",
            "safety_index",
            "health_care_index",
            "cost_of_living_index",
            "property_price_to_income_ratio",
            "traffic_commute_time_index",
            "pollution_index",
            "climate_index",
        )
    }
    start_urls = ["https://www.numbeo.com/quality-of-life/"]

    def parse(self, response):
        """Scrape a list of countries and go each page."""
        for country_url in response.xpath(
            "//a[contains(@href, 'ountry_result.jsp?country=')]/@href"
        ).getall():
            yield response.follow(country_url, self.parse_item)

    def parse_item(self, response):
        """Scrape data from the country' page."""
        i = ItemLoader(item=CountryItem(), response=response)

        country = response.xpath("//span[@itemprop='name']/text()").getall()[-1]
        i.add_value("country", country)

        quality_list = response.css(".table_indices ::text").getall()
        quality_of_life_index = [i.strip() for i in quality_list][-3]
        i.add_value("quality_of_life_index", quality_of_life_index)

        purchasing_power_index = response.xpath(
            "//a[contains(text(), "
            "'Purchasing Power Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("purchasing_power_index", purchasing_power_index)

        safety_index = response.xpath(
            "//a[contains(text(), "
            "'Safety Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("safety_index", safety_index)

        health_care_index = response.xpath(
            "//a[contains(text(), "
            "'Health Care Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("health_care_index", health_care_index)

        climate_index = response.xpath(
            "//a[contains(text(), "
            "'Climate Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("climate_index", climate_index)

        cost_of_living_index = response.xpath(
            "//a[contains(text(), "
            "'Cost of Living Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("cost_of_living_index", cost_of_living_index)

        property_price_to_income_ratio = response.xpath(
            "//a[contains(text(), "
            "'Property Price to Income Ratio')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("property_price_to_income_ratio", property_price_to_income_ratio)

        traffic_commute_time_index = response.xpath(
            "//a[contains(text(), "
            "'Traffic Commute Time Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("traffic_commute_time_index", traffic_commute_time_index)

        pollution_index = response.xpath(
            "//a[contains(text(), "
            "'Pollution Index')]/parent::td/following-sibling::td/text()"
        ).get()
        i.add_value("pollution_index", pollution_index)

        try:
            # TODO: remove "requests" and "bs4" deps
            base_url = "https://freedomhouse.org/report/freedom-world/2018/{}"
            res = requests.get(base_url.format(country))
            soup_text = BeautifulSoup(res.text, "lxml").text
            regex = r"Aggregate Score:(.{0,9})"
            reg = re.compile(regex)
            sc_dirty = reg.search(soup_text).group(1)
            score = "".join([s for s in sc_dirty.split()[0] if s.isdigit()])
            score = float(score)
        except AttributeError:
            score = None

        i.add_value("freedomhouse_score", score)
        yield i.load_item()
