import re
from lxml import etree
import json
import requests
import random


def write_url(url):
    with open('url_log.txt', "at") as code:
        print(url, file=code)
    code.close()


def get_title_us(html, i):
    title = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'video-title2\']/text()')[0]
    return title


def get_number_us(html, i):
    number = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'uid2\']/text()')[0]
    return number


def get_site_us(html, i):
    site = 'https://javdb4.com' + html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/@href')[0]
    return site


def get_cover_us(html, i):
    cover = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'item-image fix-scale-cover\']/img/@src')[0]
    return cover


def get_title_jp(html, i):
    title = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'video-title\']/text()')[0]
    return title


def get_number_jp(html, i):
    number = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'uid\']/text()')[0]
    return number


def get_site_jp(html, i):
    site = 'https://javdb4.com' + html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/@href')[0]
    return site


def get_cover_jp(html, i):
    cover = html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
            i) + ']/a[@class=\'box\']/div[@class=\'item-image fix-scale-cover\']/img/@src')[0]
    if 'http:' not in cover and 'https:' not in cover:
        cover = 'http:' + cover
    return cover


def get_html(url):
    response = []
    headers = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36 '
    }
    try:
        # 发送请求，获得响应
        response = requests.get(url=url, headers=headers, timeout=10)
    except Exception:
        print('[-]Request Error!Retry...')
        get_html(url)
    # 获得网页源代码
    html = response.text
    html = etree.HTML(html)
    return html


def getTitle(html):
    result = str(html.xpath('/html/body/section/div/h2/strong/text()')).strip(" ['']")
    return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', '').replace(' : ', ''))


def getActor(html):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    result1 = str(html.xpath('//strong[contains(text(),"演員")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"演員")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace(",\\xa0", "").replace("'", "").replace(' ', '').replace(',,',
                                                                                                             '').lstrip(
        ',').replace(',', ', ')


def getStudio(html):
    result1 = str(html.xpath('//strong[contains(text(),"片商")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"片商")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getRuntime(html):
    result1 = str(html.xpath('//strong[contains(text(),"時長")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"時長")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').rstrip('mi')


def getLabel(html):
    result1 = str(html.xpath('//strong[contains(text(),"系列")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"系列")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getNum(html):
    result1 = str(html.xpath('//strong[contains(text(),"番號")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"番號")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result2 + result1).strip('+')


def getYear(getRelease):
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getRelease(html):
    result1 = str(html.xpath('//strong[contains(text(),"時間")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"時間")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+')


def getTag(html):
    result1 = str(html.xpath('//strong[contains(text(),"类别")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"类别")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace(",\\xa0", "").replace("'", "").replace(' ', '').replace(',,',
                                                                                                             '').lstrip(
        ',')


def getCover_small(html):
    result = 'http:' + html.xpath(
        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][1]/a['
        '@class=\'box\']/div[@class=\'item-image fix-scale-cover\']/img/@src')[0]
    return result


def getCover(html):
    result = str(html.xpath('/html/body/section/div/div[@class=\'columns item-content\']/div[@class=\'column column-video-cover\']/a/img/@src')).strip(" ['']")
    return result


def getDirector(html):
    result1 = str(html.xpath('//strong[contains(text(),"導演")]/../following-sibling::span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"導演")]/../following-sibling::span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def each_main(url):
    try:
        html = get_html(url)
        dic = {
            'actor': getActor(html),
            'number': getNum(html),
            'title': getTitle(html).replace("\\n", '').replace('        ', '').replace(getActor(html), '').replace(
                '无码', '').replace('有码', '').replace(getNum(html), '').lstrip(' '),
            'studio': getStudio(html),
            'runtime': getRuntime(html),
            'director': getDirector(html),
            'release': getRelease(html),
            'cover': getCover(html),
            'tag': getTag(html),
            'label': getLabel(html),
            'year': getYear(getRelease(html)),  # str(re.search('\d{4}',getRelease(a)).group()),
            'website': url,
        }
        js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
        return js
    except:
        html = get_html(url)
        dic = {
            'actor': getActor(html),
            'number': getNum(html),
            'title': getTitle(html).replace("\\n", '').replace('        ', '').replace(getActor(html), '').replace(
                '无码', '').replace('有码', '').replace(getNum(html), '').lstrip(' '),
            'studio': getStudio(html),
            'runtime': getRuntime(html),
            'director': getDirector(html),
            'release': getRelease(html),
            'cover': getCover(html),
            'tag': getTag(html),
            'label': getLabel(html),
            'year': getYear(getRelease(html)),  # str(re.search('\d{4}',getRelease(a)).group()),
            'website': url,
        }
        js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
        return js

# each_main('https://javdb3.com/v/xgZKQ')
