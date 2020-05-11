import re
from lxml import etree
import json
from Function.getHtml import get_html


def getTitle(htmlcode):  # 获取标题
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h3/text()')).strip(" ['']")
    result2 = str(re.sub('\D{2}2-\d+', '', result)).replace(' ', '', 1)
    return result2


def getActor(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[5]/a/text()')).strip(" ['']")
        return result
    except:
        return ''


def getActorPhoto(actor):
    actor = actor.split('/')
    d = {}
    for i in actor:
        p = {i: ''}
        d.update(p)
    return d


def getStudio(htmlcode):  # 获取厂商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[3]/a[1]/text()')).strip(" ['']")
    return result


def getNum(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[5]/div[1]/div[2]/p[1]/span[2]/text()')).strip(" ['']")
    # print(result)
    return result


def getRelease(htmlcode2):  #
    html = etree.fromstring(htmlcode2, etree.HTMLParser())
    result = str(html.xpath('//*[@id="container"]/div[1]/div/article/section[1]/div/div[2]/dl/dd[4]/text()')).strip(
        " ['']")
    return result


def getCover(htmlcode):  # 获取封面 #
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result2 = str(html.xpath('//*[@id="slider"]/ul[1]/li[1]/img/@src')).strip(" ['']")
    return 'https://fc2club.com' + result2


def getScore(htmlcode):  # 获取评分 #
    if re.search(r'影片评分</strong>：(\d+)分</h5>', htmlcode):
        score = str(re.findall(r'影片评分</strong>：(\d+)分</h5>', htmlcode)).strip(" ['']")
        score = float(int(score) / 100.0 * 5)
        return str(score)


def getTag(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('/html/body/div[2]/div/div[1]/h5[4]/a/text()'))
    return result.strip(" ['']").replace("'", '').replace(' ', '')


def getYear(release):
    try:
        result = re.search('\d{4}', release).group()
        return result
    except:
        return ''


def main(number):
    try:
        htmlcode = get_html('https://fc2club.com//html/FC2-' + number + '.html')
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        actor = getActor(htmlcode)
        if len(actor) == 0:
            actor = 'FC2系列'
        dic = {
            'title': getTitle(htmlcode).strip(' '),
            'studio': getStudio(htmlcode),
            'score': getScore(htmlcode),
            'runtime': getYear(getRelease(htmlcode)),
            'actor': actor.replace('/', ','),
            'release': getRelease(number),
            'number': 'FC2-' + number,
            'tag': getTag(htmlcode),
            'actor_photo': getActorPhoto(actor),
            'cover': getCover(htmlcode),
            'extrafanart': '',
            'imagecut': 0,
            'director': '',
            'series': '',
            'publisher': '',
            'year': '',
            'outline': '',
            'website': 'https://fc2club.com//html/FC2-' + number + '.html',
            'source': 'fc2fans_club.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in fc2fans_club.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )
    return js


# print(main('1251689'))
# print(main('674239'))
