# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field, Item
from scrapy.loader.processors import MapCompose
from w3lib.html import remove_tags


def parse_string(value):
    end = value.index("%")
    return value[: end + 1]


def strip_string(value):
    return value.strip()


class TrafficIndexItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    world_rank = Field(input_processor=MapCompose(remove_tags))
    city = Field(input_processor=MapCompose(remove_tags))
    country = Field(input_processor=MapCompose(remove_tags, strip_string))
    congestion_level = Field(input_processor=MapCompose(remove_tags, parse_string))
