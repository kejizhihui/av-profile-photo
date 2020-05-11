import re
from lxml import etree
import json
from Function.getHtml import post_html


def getActorPhoto(actor):
    data = {}
    for i in actor:
        actor_photo = {i: ''}
        data.update(actor_photo)
    return data


def getTitle(response):
    return str(re.findall(r'<h3>(.+) <small>', response)).strip(" ['']")


def getActor(response):
    if re.search(r'<a href="/star/\S+">(\S+)</a> &nbsp;', response):
        return str(re.findall(r'<a href="/star/\S+">(\S+)</a> &nbsp;', response)).strip(" [',']").replace('\'', '')
    elif re.search(r'<a href="/heyzo_star/\S+">(\S+)</a> &nbsp;', response):
        return str(re.findall(r'<a href="/heyzo_star/\S+">(\S+)</a> &nbsp;', response)).strip(" [',']").replace('\'',
                                                                                                                '')
    else:
        return str(re.findall(r'<b>女优</b>: ([^<]+) &nbsp; <br>', response)).strip(" [',']").replace('\'', '')


def getStudio(response):
    return str(re.findall(r'<a href="/company/\S+">(\S+)</a>', response)).strip(" ['']")


def getRuntime(response):
    return str(re.findall(r'<b>播放时长</b>: (\d+) \S+<br>', response)).strip(" ['']")


def getSeries(response):
    return str(re.findall(r'<b>系列</b>: <a href="/series/\S+">(\S+)</a>', response)).strip(" ['']")


def getWebsite(detail_page):
    return 'https:' + detail_page.xpath('//a[contains(text(),"简体中文")]/@href')[0]


def getNum(response):
    return str(re.findall(r'<b>番号</b>: (\S+)<br>', response)).strip(" ['']").upper()


def getScore(response):
    if re.search(r'<b>评分</b>: <img data-original="/img/(\d+).gif" />', response):
        score = re.findall(r'<b>评分</b>: <img data-original="/img/(\d+).gif" />', response)[0]
        return str(float(score) / 10.0)
    else:
        return str(re.findall(r'<b>评分</b>: ([^<]+)<br>', response)).strip(" [',']").replace('\'', '')


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release


def getRelease(response):
    return str(re.findall(r'<b>发行日期</b>: (\d+-\d+-\d+)<br>', response)).strip(" ['']").replace('0000-00-00', '')


def getCover(detail_page):
    cover_url = str(detail_page.xpath("/html/body/div[@class='row'][2]/div[@class='col-md-3']/div[@class='col-xs-12 "
                                      "col-md-12'][1]/p/a/img[@class='img-responsive']/@src")).strip(" ['']")
    if cover_url == '':
        cover_url = str(
            detail_page.xpath("//*[@id='vjs_sample_player']/@poster")).strip(" ['']")
    return cover_url


def getExtraFanart(htmlcode):
    extrafanart_list = htmlcode.xpath("/html/body/div[@class='row'][2]/div[@class='col-md-3']/div[@class='col-xs-12 col-md-12']/p/a/img[@class='img-responsive']/@src")
    return extrafanart_list


def getCoverSmall(detail_page):
    return str(detail_page.xpath("//div[@class='panel-body']/div[@class='row'][1]/div[@class='col-md-3']/img["
                                 "@class='img-responsive']/@src")).strip(" ['']")


def getTag(response):  # 获取演员
    return re.findall(r'<a href="/genre/\S+">(\S+)</a>', response)


def getOutline(detail_page):
    return str(detail_page.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div/text()')).strip(" ['']")


def main(number, isuncensored=False):
    try:
        response = post_html("https://www.jav321.com/search", query={"sn": number})
        if str(response) == 'ProxyError':
            raise TimeoutError
        if '未找到您要找的AV' in response:
            raise Exception('Movie Data not found in jav321!')
        detail_page = etree.fromstring(response, etree.HTMLParser())
        release = getRelease(response)
        actor = getActor(response)
        imagecut = 1
        cover_small = ''
        if 'HEYZO' in number.upper() or isuncensored:
            imagecut = 3
            cover_small = getCoverSmall(detail_page)
            if cover_small == '':
                imagecut = 0
        dic = {
            'actor': actor,
            'title': getTitle(response),
            'studio': getStudio(response),
            'outline': getOutline(detail_page),
            'runtime': getRuntime(response),
            'release': release,
            'number': getNum(response),
            'score': getScore(response),
            'tag': getTag(response),
            'series': getSeries(response),
            'year': getYear(release),
            'actor_photo': getActorPhoto(actor.split(',')),
            'cover': getCover(detail_page),
            'extrafanart': getExtraFanart(detail_page),
            'cover_small': cover_small,
            'imagecut': imagecut,
            'director': '',
            'publisher': '',
            'website': getWebsite(detail_page),
            'source': 'jav321.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in jav321.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


'''
print(main('msfh-010'))
print(main('kavr-065'))
print(main('ssni-645'))
print(main('sivr-038'))
print(main('ara-415'))
print(main('luxu-1257'))
print(main('heyzo-1031'))
print(main('ABP-905'))
'''
