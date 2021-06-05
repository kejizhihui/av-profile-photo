import re
from lxml import etree
import json
from Function.getHtml import get_html


def getTitle(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('//*[@id="center_column"]/div[1]/h1/text()')).strip(" ['']")
        return result.replace('/', ',')
    except:
        return ''


def getActor(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"出演")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"出演")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('/', ',').replace('\'', '').replace(' ', '').replace('\\n', '')


def getActorPhoto(actor):
    d = {}
    for i in actor:
        if i and ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"メーカー：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getPublisher(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"レーベル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getRuntime(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"収録時間：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).rstrip('min').replace('\'', '').replace(' ', '').replace('\\n', '')


def getSeries(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"シリーズ：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getNum(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"品番：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"品番：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"配信開始日：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getTag(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//th[contains(text(),"ジャンル：")]/../td/text()')).strip(" ['']")
    return str(result1 + result2).replace('\'', '').replace(' ', '').replace('\\n', '')


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="center_column"]/div[1]/div[1]/div/div/h2/img/@src')).strip(" ['']")
    return result


def getExtraFanart(htmlcode):  # 获取封面链接
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    extrafanart_list = html.xpath("//dl[@id='sample-photo']/dd/ul/li/a[@class='sample_image']/@href")
    return extrafanart_list


def getOutline(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//*[@id="introduction"]/dd/p[1]/text()')).strip(" ['']")
    return result


def getScore(htmlcode):
    return str(re.findall(r'5点満点中 (\S+)点', htmlcode)).strip(" ['']")


def main(number, appoint_url):
    try:
        number = number.upper()
        url = 'https://www.mgstage.com/product/product_detail/' + str(number) + '/'
        if appoint_url != '':
            url = appoint_url
        htmlcode = str(get_html(url, cookies={'adc': '1'}))
        htmlcode = htmlcode.replace('ahref', 'a href')  # 针对a标签、属性中间未分开
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        actor = getActor(htmlcode).replace(' ', '')
        release = getRelease(htmlcode)
        dic = {
            'title': getTitle(htmlcode).replace("\\n", '').replace('        ', '').strip(','),
            'studio': getStudio(htmlcode).strip(','),
            'publisher': getPublisher(htmlcode).strip(','),
            'outline': getOutline(htmlcode).replace('\n', '').strip(','),
            'score': getScore(htmlcode).strip(','),
            'runtime': getRuntime(htmlcode).strip(','),
            'actor': actor.strip(','),
            'release': release.strip(',').replace('/', '-'),
            'number': getNum(htmlcode).strip(','),
            'cover': getCover(htmlcode).strip(','),
            'extrafanart': getExtraFanart(htmlcode),
            'imagecut': 0,
            'tag': getTag(htmlcode).strip(','),
            'series': getSeries(htmlcode).strip(','),
            'year': getYear(release).strip(','),
            'actor_photo': getActorPhoto(actor.split(',')),
            'director': '',
            'website': url,
            'source': 'mgstage.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in mgstage.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js
'''
print(main('200GANA-2240'))
print(main('SIRO-4042'))
print(main('300MIUM-382'))
'''
# print(main('300MIUM-382', ''))
# print(main('300MIUM-382', 'https://www.mgstage.com/product/product_detail/300MIUM-382/'))
