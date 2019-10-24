# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
from scrapy import Field
from scrapy import Item
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

__author__ = "aserhii@protonmail.com"


def filter_question(value):
    """"""
    return value if value != '?' else None


class CountryItem(Item):
    """
    """

    country = Field()
    freedomhouse_score = Field(output_processor=TakeFirst())
    quality_of_life_index = Field(input_processor=MapCompose(filter_question))
    purchasing_power_index = Field(input_processor=MapCompose(filter_question))
    safety_index = Field(input_processor=MapCompose(filter_question))
    health_care_index = Field(input_processor=MapCompose(filter_question))
    cost_of_living_index = Field(input_processor=MapCompose(filter_question))
    property_price_to_income_ratio = Field(input_processor=MapCompose(filter_question))
    traffic_commute_time_index = Field(input_processor=MapCompose(filter_question))
    pollution_index = Field(input_processor=MapCompose(filter_question))
    climate_index = Field(input_processor=MapCompose(filter_question))


def parse_string(value):
    end = value.index("%")
    return value[:end + 1]


def strip_string(value):
    return value.strip()


class TrafficIndexItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    world_rank = Field(input_processor=MapCompose(remove_tags))
    city = Field(input_processor=MapCompose(remove_tags))
    country = Field(input_processor=MapCompose(remove_tags, strip_string))
    congestion_level = Field(input_processor=MapCompose(remove_tags, parse_string))
