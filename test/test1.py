'''----------------------------------------------------Title------------------------------------------------------------

---------------------------------------------------------------------------------------------------------------------'''
import requests
from lxml import etree
import http.client
from selenium.webdriver import ActionChains
import re
import json

def getNewsURLList(baseURL) :
    headers = {
        'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    x = requests.get(baseURL, headers=headers)
    html = x.content.decode('utf8')
    selector = etree.HTML(html)
    accept_rate = selector.xpath(
        '//div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12"]/div[@class="singlepost"]/div[@class="row"]/div[@class="col-lg-6"]/div[@class="row"]/div[@class="col-lg-12 col-md-12 col-sm-12 col-xs-12 offerRate"]/div[@class="review-sidebar offerRate"]/div[@class="review-box"]/div[@class="review-total displayRate"]/text()')
    accept_rate = accept_rate[0] if accept_rate else None
    # accept_rate1 = accept_rate if accept_rate != '— ' else accept_rate1 =  None
    if accept_rate != '\n— ':
        accept_rate1 = accept_rate
    else :
        accept_rate1 =  None
    content2 = '''
        FUNNEL_DATA[4324] = "2018-19"{:[{"label":"Applications","backgroundColor":"#1E77B4","value":65}],"2017-18":[{"label":"Applications","backgroundColor":"#1E77B4","value":61},{"label":"Offers","backgroundColor":"#FB7D0F","value":43}],"2016-17":[{"label":"Applications","backgroundColor":"#1E77B4","value":57},{"label":"Offers","backgroundColor":"#FB7D0F","value":44}],"2015-16":[{"label":"Applications","backgroundColor":"#1E77B4","value":62},{"label":"Offers","backgroundColor":"#FB7D0F","value":50}],"2014-15":[{"label":"Applications","backgroundColor":"#1E77B4","value":72},{"label":"Offers","backgroundColor":"#FB7D0F","value":61},;
    FUNNEL_SELECTED[4324] = "2018-19";
    '''
    contents = selector.xpath('//div[@class="container"]/script/text()')[0]
    pattern = '"2018-19".*?}]'
    con = re.findall(pattern, content2)[0]
    pattern2 = re.compile('"2018-19".*?"Applications".*?value":(\d+)}', re.S)
    con2 = re.findall(pattern2, con)
    pattern3 = re.compile('"2018-19".*?"Offers".*?value":(\d+)}', re.S)
    con2.extend(re.findall(pattern3, con))
    pattern4 = re.compile('"2018-19".*?"Admissions".*?value":(\d+)}', re.S)
    con2.extend(re.findall(pattern4, con))
    print(con)
    print(con2)
    # pattern0 = re.compile('FUNNEL_DATA.*?("2018-19")', re.S)
    # con = re.findall(pattern0, content2)
    # if con:
    #     pattern1 = re.compile('FUNNEL_DATA.*?Applications.*?value":(\d+)', re.S)
    #     con1 = re.findall(pattern1, content2)
    #     print(con1)


    # print(con)
    # if con.span(22 == :
    #     app = new_contents[0].span(72,74)
    #     print(app)
    # offers = new_contents[1]
    # admission = new_contents[2]
    # yield applications, offers, admission  # 创建一个生成器
    # print(contents)
    yield contents
    # yield applications.replace(":",""), accept_rate.replace('\n', ''), accept_rate1
    # print(new_contents)
    # print(new_contents[0])

if __name__ == '__main__' :
    urltemplate = "https://www.admissionreport.com/university-college-london/msc-urban-studies"
    # 构造一个网页链接模版
    # print(testurl)
    urllist = getNewsURLList(urltemplate)
    for new_contents in urllist:
        print(new_contents)
    for accept_rate, accept_rate1, applicationsin in urllist:
        print(applications, accept_rate1, accept_rate)

    # newsContents = getNewsContent(urllist)
    # f = open("news.txt", "wb")  # python3需要使用wb而不是w
    # wb = lambda x : f.write((x + '\r\n').encode('utf-8'))
    # for title, url, ptime, news, in newsContents :
    #     wb('~' * 100)
    #     wb(title)
    #     wb(url)
    #     wb(ptime)
    #     wb(news)
    # f.close()
