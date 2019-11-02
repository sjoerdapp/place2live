import re

from bs4 import BeautifulSoup as bs
from inflation.items import InflationItem
from scrapy import Spider
from scrapy.loader import ItemLoader


class InflationSpider(Spider):
    name = "inflation"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_countries_by_inflation_rate"]

    def parse(self, response):
        table = bs(response.body, "html.parser").findAll("tbody")[2]

        countries = [
            c["title"] for c in table.findAll("a", href=True, title=True)
        ]
        dateCandidates = table.findAll("td", {"data-sort-value": True})
        dates = [re.findall(r'\d+', yr)[0] for yr in dateCandidates]
        inflations = []
        for td in [i.replace("−", "-") for i in table.findAll("td")]:
            if isinstance(td, float):
                inflations.append(td)

        for inflation, country, date in zip(
            inflations, countries, dates,
        ):
            i = ItemLoader(item=InflationItem())
            i.add_value("inflation", inflation)
            i.add_value("date", date)
            i.add_value("country", country)
            yield i.load_item()
