# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from KCLscrapy.items import KclscrapyItem
from urllib import parse
from scrapy.utils.response import get_base_url


class KclspiderSpider(scrapy.Spider):
    name = 'KCLspider'
    allowed_domains = ['https://www.admissionreport.com/imperial-college-london/msc-science-communication']
    start_urls = ['https://www.admissionreport.com/imperial-college-london/msc-science-communication']

    def parse(self, response):
        item = KclscrapyItem()
        selector = Selector(response)
        courses = selector.xpath('//div[@class="strip_booking"]/div[@class="row"]')
        print(courses)
        for each in courses:
            course = each.xpath('div[@class="col-lg-7 col-md-7 col-sm-7 col-xs-12"]/div[@class="review-descriptions"]/h4/a/text()').extract()[0]
            uni = each.xpath('div[@class="col-lg-2 col-md-2 col-sm-2 col-xs-12"]/a/text()').extract()[0]
            acceptrate = each.xpath('div[@class="col-lg-3 col-md-3 col-sm-3 col-xs-12"]/div[@class="date"]/span[@class="day"]/strong/text()').extract()[0]
            # intro1 = each.xpath(
            #     'div[@class="strip_booking"]/div[@class="row"]/div[@class="col-lg-7 col-md-7 col-sm-7 col-xs-12"]/div[@class="review-descriptions"]/p/text()'
            # ).extract()[0]
            # intro2 = each.xpath(
            #     'div[@class="strip_booking"]/div[@class="row"]/div[@class="col-lg-7 col-md-7 col-sm-7 col-xs-12"]/div[@class="review-descriptions"]/p/strong/text()'
            # ).extract()
            # intro21 = intro2[0]
            # intro22 = intro2[1]
            item['acceptrate'] = acceptrate
            item['Uni'] = uni
            item['Course'] = course
            yield item

        # nextlink = selector.xpath('//span[@class="next"]/a/@href').extract()
        # if nextlink :
        #     nextlink = nextlink[0]
        #     yield Request(nextlink, callback=self.parse)


