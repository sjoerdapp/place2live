"""
"""
from scrapy import Spider
from scrapy.loader import ItemLoader

from ..items import TrafficIndexItem


class TrafficSpider(Spider):
    """A configuration of a spider."""
    name = "traffic"
    custom_settings = {
        "FEED_EXPORT_FIELDS": ("world_rank", "city", "country", "congestion_level"),
    }
    allowed_domains = ["tomtom.com"]
    start_urls = ["https://www.tomtom.com/en_gb/traffic-index/ranking/"]

    def parse(self, response):
        """Scrape a list of world rankings, cities, countries, and congestion levels"""
        """Then populate an item with the data and return it"""
        # Base XPath for extract need values
        xpath_selector = "//div[@id='RankingPage-table']//td[{}]"
        world_ranks = response.xpath(xpath_selector.format(1)).getall()
        cities = response.xpath(xpath_selector.format(3)).getall()
        countries = response.xpath(xpath_selector.format(4)).getall()
        congestion_levels = response.xpath(xpath_selector.format(5)).getall()
        for rank, city, country, level in zip(
            world_ranks, cities, countries, congestion_levels,
        ):
            i = ItemLoader(item=TrafficIndexItem())
            i.add_value("world_rank", rank)
            i.add_value("city", city)
            i.add_value("country", country)
            i.add_value("congestion_level", level)
            yield i.load_item()
