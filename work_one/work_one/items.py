# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorkOneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     title= scrapy.Field()
     location= scrapy.Field()
     posted= scrapy.Field()
     skillSet= scrapy.Field()
     Category= scrapy.Field()
