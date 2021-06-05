import json
import re
from bs4 import BeautifulSoup
from lxml import etree
from Function.getHtml import get_html


def getActorPhoto(htmlcode):  # //*[@id="star_qdt"]/li/a/img
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'avatar-box'})
    d = {}
    for i in a:
        l = i.img['src']
        t = i.span.get_text()
        p2 = {t: l}
        d.update(p2)
    return d


def getTitle(a):
    try:
        html = etree.fromstring(a, etree.HTMLParser())
        result = str(html.xpath('/html/body/div[2]/h3/text()')).strip(" ['']")  # [0]
        return result.replace('/', '')
    except:
        return ''


def getActor(a):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    soup = BeautifulSoup(a, 'lxml')
    a = soup.find_all(attrs={'class': 'avatar-box'})
    d = []
    for i in a:
        d.append(i.span.get_text())
    return d


def getStudio(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//p[contains(text(),"制作商: ")]/following-sibling::p[1]/a/text()')).strip(" ['']").replace(
        "', '", ' ')
    return result1


def getRuntime(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"长度:")]/../text()')).strip(" ['分钟']")
    return result1


def getSeries(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//p[contains(text(),"系列:")]/following-sibling::p[1]/a/text()')).strip(" ['']")
    return result1


def getNum(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"识别码:")]/../span[2]/text()')).strip(" ['']")
    return result1


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release


def getRelease(a):
    html = etree.fromstring(a, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//span[contains(text(),"发行时间:")]/../text()')).strip(" ['']")
    return result1


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div[1]/div[1]/a/img/@src')).strip(" ['']")
    return result


def getCover_small(htmlcode, count):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    cover_small = html.xpath("//div[@id='waterfall']/div[" + str(count) + "]/a/div[@class='photo-frame']/img/@src")[0]
    return cover_small


def getTag(a):  # 获取演员
    soup = BeautifulSoup(a, 'lxml')
    a = soup.find_all(attrs={'class': 'genre'})
    d = []
    for i in a:
        d.append(i.get_text())
    return d


def getUrl(number):
    response = get_html('https://avsox.website/cn/search/' + number)
    html = etree.fromstring(response, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    url_list = html.xpath('//*[@id="waterfall"]/div/a/@href')
    if len(url_list) > 0:
        for i in range(1, len(url_list) + 1):
            number_get = str(html.xpath(
                '//*[@id="waterfall"]/div[' + str(i) + ']/a/div[@class="photo-info"]/span/date[1]/text()')).strip(
                " ['']")
            if number.upper() == number_get.upper():
                page_url = 'https:' + url_list[i-1]
                return i, response, page_url
    return 0, response, ''


def main(number, appoint_url=''):
    try:
        count, response, url = getUrl(number)
        if str(response) == 'ProxyError':
            raise TimeoutError
        if appoint_url != '':
            url = appoint_url
        elif url == '':
            raise Exception('Movie Data not found in avsox!')
        web = get_html(url)
        soup = BeautifulSoup(web, 'lxml')
        info = str(soup.find(attrs={'class': 'row movie'}))
        number = getNum(web)
        dic = {
            'actor': getActor(web),
            'title': getTitle(web).strip(number).strip().replace(' ', '-'),
            'studio': getStudio(info),
            'runtime': getRuntime(info),
            'release': getRelease(info),
            'number': getNum(info),
            'tag': getTag(web),
            'series': getSeries(info),
            'year': getYear(getRelease(info)),
            'actor_photo': getActorPhoto(web),
            'cover': getCover(web),
            'cover_small': getCover_small(response, count),
            'extrafanart': '',
            'imagecut': 3,
            'director': '',
            'publisher': '',
            'outline': '',
            'score': '',
            'website': url,
            'source': 'avsox.website',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in avsox.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


# print(main('051119-917'))
# print(main('032620_001'))
# print(main('032620_001', 'https://avsox.website/cn/movie/cb8d28437cff4e90'))