# -*- coding: utf-8 -*-
import scrapy
import scrapy
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.selector import Selector
from LSEscrapy.items import LsescrapyItem
from urllib import parse
import re
import copy

class LseadmissionscrapySpider(scrapy.Spider):
    name = 'LSEadmissionscrapy'
    # allowed_domains = ['https://www.admissionreport.com/university-college-london/all']
    start_urls = ['https://www.admissionreport.com/london-school-of-economics/all']

    def parse(self, response):
        item = LsescrapyItem()
        selector = Selector(response)
        courses = selector.xpath('//ul[@id="cat_nav"]/li')
        for eachcourse in courses:
            coursename = eachcourse.xpath('a/text()').extract()[0]
            href = eachcourse.xpath('a/@href').extract()[0]

            item['Course_name'] = coursename
            item['href'] = parse.urljoin(u'https://www.admissionreport.com', href)
            item['Accep_Rate'] = ""
            item['Admission_Rate'] = ""
            item['Enroll_Year'] = ""
            item['Apply_Num'] = ""
            item['Offer_Num'] = ""
            item['Admission_Num'] = ""

            mhref = item['href']
            # yield item
            yield Request(url = mhref, meta={'course' : copy.deepcopy(item)}, callback=self.parse_acceptencerate) #使用深复制
            # print(Request.meta)

    def parse_acceptencerate(self, response) :
        item = response.meta['course']
        selector = Selector(response)

        enroll = selector.xpath(
            '//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12"]/div[@class="row"]/div[@class="col-lg-9"]/ul/li/a/text()').extract()
        enroll_year = enroll[0] if enroll else None

        accept_rate = selector.xpath(
            '//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12"]/div[@class="singlepost"]/div[@class="row"]/div[@class="col-lg-6"]/div[@class="row"]/div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 offerRate"]/div[@class="review-sidebar offerRate"]/div[@class="review-box"]/div[@class="review-total displayRate"]/text()').extract()
        accept_rate = accept_rate[0] if accept_rate else None
        accept_rate1 = accept_rate if accept_rate != '\n— ' else None

        admission_rate = selector.xpath(
            '//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12"]/div[@class="singlepost"]/div[@class="row"]/div[@class="col-lg-6"]/div[@class="row"]/div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 acceptanceRate"]/div[@class="review-sidebar acceptanceRate"]/div[@class="review-box"]/div[@class="review-total displayRate"]/text()').extract()
        admission_rate = admission_rate[0] if admission_rate else None
        admission_rate1 = admission_rate if admission_rate != '\n— ' else None


        framwork = selector.xpath('//div[@class="container"]/script/text()').extract()
        pattern = '"2018-19".*?}]'
        try:
            string = re.findall(pattern, str(framwork))[0]
            pattern2 = re.compile('"2018-19".*?"Applications".*?value":(\d+)}', re.S)
            string2 = re.findall(pattern2, string)
            pattern3 = re.compile('"2018-19".*?"Offers".*?value":(\d+)}', re.S)
            string2.extend(re.findall(pattern3, string))
            pattern4 = re.compile('"2018-19".*?"Admissions".*?value":(\d+)}', re.S)
            string2.extend(re.findall(pattern4, string))
        except:
            pattern00 = '"2017-18".*?}]'
            try:
                string = re.findall(pattern00, str(framwork))[0]
                pattern2 = re.compile('"2017-18".*?"Applications".*?value":(\d+)}', re.S)
                string2 = re.findall(pattern2, string)
                pattern3 = re.compile('"2017-18".*?"Offers".*?value":(\d+)}', re.S)
                string2.extend(re.findall(pattern3, string))
                pattern4 = re.compile('"2017-18".*?"Admissions".*?value":(\d+)}', re.S)
                string2.extend(re.findall(pattern4, string))
            except:
                pattern01 = '"2016-17".*?}]'
                try :
                    string = re.findall(pattern01, str(framwork))[0]
                    pattern2 = re.compile('"2016-17".*?"Applications".*?value":(\d+)}', re.S)
                    string2 = re.findall(pattern2, string)
                    pattern3 = re.compile('"2016-17".*?"Offers".*?value":(\d+)}', re.S)
                    string2.extend(re.findall(pattern3, string))
                    pattern4 = re.compile('"2016-17".*?"Admissions".*?value":(\d+)}', re.S)
                    string2.extend(re.findall(pattern4, string))
                except :
                    pattern02 = '"2015-16".*?}]'
                    try :
                        string = re.findall(pattern02, str(framwork))[0]
                        pattern2 = re.compile('"2015-16".*?"Applications".*?value":(\d+)}', re.S)
                        string2 = re.findall(pattern2, string)
                        pattern3 = re.compile('"2015-16".*?"Offers".*?value":(\d+)}', re.S)
                        string2.extend(re.findall(pattern3, string))
                        pattern4 = re.compile('"2015-16".*?"Admissions".*?value":(\d+)}', re.S)
                        string2.extend(re.findall(pattern4, string))
                    except:
                        pattern03 = '"2014-15".*?}]'
                        try :
                            string = re.findall(pattern03, str(framwork))[0]
                            pattern2 = re.compile('"2014-15".*?"Applications".*?value":(\d+)}', re.S)
                            string2 = re.findall(pattern2, string)
                            pattern3 = re.compile('"2014-15".*?"Offers".*?value":(\d+)}', re.S)
                            string2.extend(re.findall(pattern3, string))
                            pattern4 = re.compile('"2014-15".*?"Admissions".*?value":(\d+)}', re.S)
                            string2.extend(re.findall(pattern4, string))
                        except:
                            pattern04 = '"2013-14".*?}]'
                            try :
                                string = re.findall(pattern04, str(framwork))[0]
                                pattern2 = re.compile('"2013-14".*?"Applications".*?value":(\d+)}', re.S)
                                string2 = re.findall(pattern2, string)
                                pattern3 = re.compile('"2013-14".*?"Offers".*?value":(\d+)}', re.S)
                                string2.extend(re.findall(pattern3, string))
                                pattern4 = re.compile('"2013-14".*?"Admissions".*?value":(\d+)}', re.S)
                                string2.extend(re.findall(pattern4, string))
                            except:
                                string2 = []


        try:
            applications = string2[0] if string2 else None
        except IndexError:
            applications = None

        try :
            offers = string2[1] if string2 else None
        except IndexError :
            offers = None

        try:
            admissions = string2[2] if string2 else None
        except IndexError :
            admissions = None

        item['Accep_Rate'] = accept_rate1.strip().replace('/n', '').replace('%',"") if accept_rate1 != None else accept_rate1
        item['Admission_Rate'] = admission_rate1.strip().replace('/n', '').replace("%","") if admission_rate1 != None else admission_rate1
        item['Enroll_Year'] = enroll_year
        item['Apply_Num'] = applications.strip().replace(':', "") if applications != None else applications
        item['Offer_Num'] = offers.strip().replace(':', '') if offers != None else offers
        item['Admission_Num'] = admissions.strip().replace(':', '') if admissions != None else admissions
        yield copy.deepcopy(item)