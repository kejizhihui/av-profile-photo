#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from lxml import etree
import json
from Function.getHtml import get_html


def getTitle(a):
    html = etree.fromstring(a, etree.HTMLParser())
    result = html.xpath('//*[@id="title"]/text()')[0]
    return result


def getActor(a):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    html = etree.fromstring(a, etree.HTMLParser())
    result = str(html.xpath("//td[contains(text(),'出演者')]/following-sibling::td/span/a/text()")).strip(" ['']").replace(
        "', '", ',')
    return result


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    actor = actor.split(',')
    d = {}
    for i in actor:
        if ',' not in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'メーカー')]/following-sibling::td/a/text()")[0]
    except:
        result1 = html.xpath("//td[contains(text(),'メーカー')]/following-sibling::td/text()")[0]
    return result1


def getPublisher(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'レーベル')]/following-sibling::td/a/text()")[0]
    except:
        result1 = html.xpath("//td[contains(text(),'レーベル')]/following-sibling::td/text()")[0]
    return result1


def getRuntime(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = html.xpath("//td[contains(text(),'収録時間')]/following-sibling::td/text()")[0]
    return re.search('\d+', str(result1)).group()


def getSeries(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'シリーズ：')]/following-sibling::td/a/text()")[0]
    except:
        result1 = html.xpath("//td[contains(text(),'シリーズ：')]/following-sibling::td/text()")[0]
    return result1


def getNum(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'品番：')]/following-sibling::td/a/text()")[0]
    except:
        result1 = html.xpath("//td[contains(text(),'品番：')]/following-sibling::td/text()")[0]
    return result1


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'発売日：')]/following-sibling::td/a/text()")[0].lstrip('\n')
    except:
        result1 = html.xpath("//td[contains(text(),'発売日：')]/following-sibling::td/text()")[0].lstrip('\n')
    return result1


def getTag(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = str(html.xpath("//td[contains(text(),'ジャンル：')]/following-sibling::td/a/text()")).strip(" ['']")
    except:
        result1 = str(html.xpath("//td[contains(text(),'ジャンル：')]/following-sibling::td/text()")).strip(" ['']")
    return result1.replace("', '", ",")


def getCover(htmlcode, number):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = html.xpath('//*[@id="' + number + '"]/@href')[0]
    return result


def getExtraFanart(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    old_list = html.xpath("//div[@id='sample-image-block']/a[@name='sample-image']/img/@src")
    new_list = []
    for extrafanart in old_list:
        new_list.append(extrafanart.replace('-', 'jp-'))
    return new_list


def getDirector(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    try:
        result1 = html.xpath("//td[contains(text(),'監督：')]/following-sibling::td/a/text()")[0]
    except:
        result1 = html.xpath("//td[contains(text(),'監督：')]/following-sibling::td/text()")[0]
    return result1


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//div[@class='mg-b20 lh4']/text()")[0]).replace('\\n', '').replace('\n', '')
    return result


def getScore(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath("//p[@class='d-review__average']/strong/text()")[0]).replace('\\n', '').replace('\n', '').replace('点', '')
    return result


def main(number):
    try:
        htmlcode = get_html('https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=' + number)
        url = 'https://www.dmm.co.jp/digital/videoa/-/detail/=/cid=' + number
        if '404 Not Found' in htmlcode:
            htmlcode = get_html('https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=' + number)
            url = 'https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=' + number
        if '404 Not Found' in htmlcode:
            raise Exception('Movie Data not found in dmm!')
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        actor = getActor(htmlcode)
        dic = {
            'title': getTitle(htmlcode).strip(getActor(htmlcode)),
            'studio': getStudio(htmlcode),
            'publisher': getPublisher(htmlcode),
            'outline': getOutline(htmlcode),
            'score': getScore(htmlcode),
            'runtime': getRuntime(htmlcode),
            'director': getDirector(htmlcode),
            'actor': actor,
            'release': getRelease(htmlcode),
            'number': getNum(htmlcode),
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode).replace('-', ''),
            'year': getYear(getRelease(htmlcode)),
            'actor_photo': getActorPhoto(actor),
            'cover': getCover(htmlcode, number),
            'extrafanart': getExtraFanart(htmlcode),
            'imagecut': 1,
            'website': url,
            'source': 'dmm.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in dmm.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))  # .encode('UTF-8')
    return js

# main('DV-1562')
# print(main('mide00139'))
# print(main('kawd00969'))
