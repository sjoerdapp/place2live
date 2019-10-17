# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field
from scrapy import Item
from scrapy.loader.processors import MapCompose


def parse_string(value):
    end = value.index("%")
    return value[: end + 1]


def parse_int(value):
    return int(value)


def parse_float(value):
    return float(value)


def strip_string(value):
    return value.strip()


class InflationItem(Item):
    inflation = Field()
    country = Field(input_processor=MapCompose(strip_string))
    year = Field(input_processor=MapCompose(parse_int))
