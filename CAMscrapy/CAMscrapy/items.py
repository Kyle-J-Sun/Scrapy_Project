# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class CamscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Course_name = Field()
    href = Field()
    Accep_Rate = Field()
    Admission_Rate = Field()
    Enroll_Year = Field()
    Apply_Num = Field()
    Offer_Num = Field()
    Admission_Num = Field()
