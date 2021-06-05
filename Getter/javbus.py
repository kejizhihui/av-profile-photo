import re
from pyquery import PyQuery as pq
from lxml import etree
from bs4 import BeautifulSoup
import json
from Function.getHtml import get_html
from Function.getHtml import post_html


def getActorPhoto(htmlcode):
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'star-name'})
    d = {}
    for i in a:
        l = i.a['href']
        t = i.get_text()
        html = etree.fromstring(get_html(l), etree.HTMLParser())
        p = 'https://javbus.com' + str(html.xpath('//*[@id="waterfall"]/div[1]/div/div[1]/img/@src')).strip(" ['']")
        p2 = {t: p}
        d.update(p2)
    return d


def getTitle(htmlcode):  # 获取标题
    doc = pq(htmlcode)
    title = str(doc('div.container h3').text())
    try:
        title2 = re.sub('n\d+-', '', title)
        return title2
    except:
        return title


def getStudio(htmlcode):  # 获取厂商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"製作商")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getPublisher(htmlcode):  # 获取发行商
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"發行商")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getYear(getRelease):  # 获取年份
    try:
        result = str(re.search('\d{4}', getRelease).group())
        return result
    except:
        return getRelease


def getCover(htmlcode):  # 获取封面链接
    doc = pq(htmlcode)
    image = doc('a.bigImage')
    return 'https://javbus.com' + image.attr('href')


def getExtraFanart(htmlcode):  # 获取封面链接
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    extrafanart_list = html.xpath("//div[@id='sample-waterfall']/a/@href")
    return extrafanart_list


def getRelease(htmlcode):  # 获取出版日期
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"發行日期")]/../text()')).strip(" ['']")
    return result


def getRuntime(htmlcode):  # 获取分钟
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"長度")]/../text()')).strip(" ['']")
    return result


def getActor(htmlcode):  # 获取女优
    b = []
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'star-name'})
    for i in a:
        b.append(i.get_text())
    return b


def getNum(htmlcode):  # 获取番号
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"識別碼")]/following-sibling::span/text()')).strip(" ['']")
    return result


def getDirector(htmlcode):  # 获取导演
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"導演")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getOutlineScore(number):  # 获取简介
    outline = ''
    score = ''
    try:
        response = post_html("https://www.jav321.com/search", query={"sn": number})
        detail_page = etree.fromstring(response, etree.HTMLParser())
        outline = str(detail_page.xpath('/html/body/div[2]/div[1]/div[1]/div[2]/div[3]/div/text()')).strip(" ['']")
        if re.search(r'<b>平均評価</b>: <img data-original="/img/(\d+).gif" />', response):
            score = re.findall(r'<b>平均評価</b>: <img data-original="/img/(\d+).gif" />', response)[0]
            score = str(float(score) / 10.0)
        else:
            score = str(re.findall(r'<b>平均評価</b>: ([^<]+)<br>', response)).strip(" [',']").replace('\'', '')
        if outline == '':
            dmm_htmlcode = get_html(
                "https://www.dmm.co.jp/search/=/searchstr=" + number.replace('-', '') + "/sort=ranking/")
            if 'に一致する商品は見つかりませんでした' not in dmm_htmlcode:
                dmm_page = etree.fromstring(dmm_htmlcode, etree.HTMLParser())
                url_detail = str(dmm_page.xpath('//*[@id="list"]/li[1]/div/p[2]/a/@href')).split(',', 1)[0].strip(
                    " ['']")
                if url_detail != '':
                    dmm_detail = get_html(url_detail)
                    html = etree.fromstring(dmm_detail, etree.HTMLParser())
                    outline = str(html.xpath('//*[@class="mg-t0 mg-b20"]/text()')).strip(" ['']").replace('\\n',
                                                                                                          '').replace(
                        '\n', '')
    except Exception as error_info:
        print('Error in javbus.getOutlineScore : ' + str(error_info))
    return outline, score


def getSeries(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = str(html.xpath('//span[contains(text(),"系列")]/following-sibling::a/text()')).strip(" ['']")
    return result


def getCover_small(number):  # 从avsox获取封面图
    try:
        htmlcode = get_html('https://avsox.website/cn/search/' + number)
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        counts = len(html.xpath("//div[@id='waterfall']/div/a/div"))
        if counts == 0:
            return ''
        for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
            number_get = html.xpath(
                "//div[@id='waterfall']/div[" + str(count) + "]/a/div[@class='photo-info']/span/date[1]/text()")
            if len(number_get) > 0 and number_get[0].upper() == number.upper():
                cover_small = \
                html.xpath("//div[@id='waterfall']/div[" + str(count) + "]/a/div[@class='photo-frame']/img/@src")[0]
                return cover_small
    except Exception as error_info:
        print('Error in javbus.getCover_small : ' + str(error_info))
    return ''


def getTag(htmlcode):  # 获取标签
    tag = []
    soup = BeautifulSoup(htmlcode, 'lxml')
    a = soup.find_all(attrs={'class': 'genre'})
    for i in a:
        if 'onmouseout' in str(i):
            continue
        tag.append(i.get_text())
    return tag


def find_number(number):
    # =======================================================================有码搜索
    if not (re.match('^\d{4,}', number) or re.match('n\d{4}', number) or 'HEYZO' in number.upper()):
        htmlcode = get_html('https://www.javbus.com/search/' + number + '&type=1')
        html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
        counts = len(html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div"))
        if counts != 0:
            for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
                number_get = html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div[" + str(
                    count) + "]/a[@class='movie-box']/div[@class='photo-info']/span/date[1]/text()")[0]
                number_get = number_get.upper()
                number = number.upper()
                if number_get == number or number_get == number.replace('-', '') or number_get == number.replace('_',
                                                                                                                 ''):
                    result_url = html.xpath(
                        "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(
                            count) + "]/a[@class='movie-box']/@href")[0]
                    return result_url
    # =======================================================================无码搜索
    htmlcode = get_html('https://www.javbus.com/uncensored/search/' + number + '&type=1')
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    counts = len(html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div"))
    if counts == 0:
        return 'not found'
    for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
        number_get = html.xpath("//div[@id='waterfall']/div[@id='waterfall']/div[" + str(
            count) + "]/a[@class='movie-box']/div[@class='photo-info']/span/date[1]/text()")[0]
        number_get = number_get.upper()
        number = number.upper()
        if number_get == number or number_get == number.replace('-', '') or number_get == number.replace('_', ''):
            result_url = html.xpath(
                "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
            return result_url
        elif number_get == number.replace('-', '_') or number_get == number.replace('_', '-'):
            result_url = html.xpath(
                "//div[@id='waterfall']/div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
            return result_url
    return 'not found'


def main(number, appoint_url):
    try:
        if appoint_url:
            result_url = appoint_url
        else:
            result_url = find_number(number)
        if result_url == 'not found':
            raise Exception('Movie Data not found in javbus.main!')
        htmlcode = get_html(result_url)
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        outline, score = getOutlineScore(number)
        number = getNum(htmlcode)
        dic = {
            'title': str(getTitle(htmlcode)).replace(number, '').strip().replace(' ', '-'),
            'studio': getStudio(htmlcode),
            'publisher': getPublisher(htmlcode),
            'year': getYear(getRelease(htmlcode)),
            'outline': outline,
            'score': score,
            'runtime': getRuntime(htmlcode).replace('分鐘', '').strip(),
            'director': getDirector(htmlcode),
            'actor': getActor(htmlcode),
            'release': getRelease(htmlcode),
            'number': number,
            'cover': getCover(htmlcode),
            'extrafanart': getExtraFanart(htmlcode),
            'imagecut': 1,
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode),
            'actor_photo': getActorPhoto(htmlcode),
            'website': result_url,
            'source': 'javbus.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in javbus.main : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


def main_uncensored(number, appoint_url):
    try:
        result_url = ''
        if appoint_url == '':
            result_url = find_number(number)
        else:
            result_url = appoint_url
        if result_url == 'not found':
            raise Exception('Movie Data not found in javbus.main_uncensored!')
        htmlcode = get_html(result_url)
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        number = getNum(htmlcode)
        outline = ''
        score = ''
        if 'HEYZO' in number.upper():
            outline, score = getOutlineScore(number)
        dic = {
            'title': getTitle(htmlcode).replace(number, '').strip().replace(' ', '-'),
            'studio': getStudio(htmlcode),
            'publisher': '',
            'year': getYear(getRelease(htmlcode)),
            'outline': outline,
            'score': score,
            'runtime': getRuntime(htmlcode).replace('分鐘', '').strip(),
            'director': getDirector(htmlcode),
            'actor': getActor(htmlcode),
            'release': getRelease(htmlcode),
            'number': getNum(htmlcode),
            'cover': getCover(htmlcode),
            'extrafanart': getExtraFanart(htmlcode),
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode),
            'imagecut': 3,
            'cover_small': getCover_small(number),  # 从avsox获取封面图
            'actor_photo': getActorPhoto(htmlcode),
            'website': result_url,
            'source': 'javbus.py',
        }
        if dic['cover_small'] == '':
            dic['imagecut'] = 0
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in javbus.main_uncensored : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


def main_us(number, appoint_url=''):
    try:
        if appoint_url:
            result_url = appoint_url
        else:
            htmlcode = get_html('https://www.javbus.one/search/' + number)
            if str(htmlcode) == 'ProxyError':
                raise TimeoutError
            html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
            counts = len(html.xpath("//div[@class='row']/div[@id='waterfall']/div"))
            if counts == 0:
                raise Exception('Movie Data not found in javbus.main_us!')
            result_url = ''
            cover_small = ''
            for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
                number_get = html.xpath("//div[@id='waterfall']/div[" + str(
                    count) + "]/a[@class='movie-box']/div[@class='photo-info']/span/date[1]/text()")[0]
                if number_get.upper() == number.upper() or number_get.replace('-', '').upper() == number.upper():
                    result_url = html.xpath(
                        "//div[@id='waterfall']/div[" + str(count) + "]/a[@class='movie-box']/@href")[0]
                    cover_small = html.xpath(
                        "//div[@id='waterfall']/div[" + str(
                            count) + "]/a[@class='movie-box']/div[@class='photo-frame']/img[@class='img']/@src")[0]
                    break
            if result_url == '':
                raise Exception('Movie Data not found in javbus.main_us!')
        htmlcode = get_html(result_url)
        if str(htmlcode) == 'ProxyError':
            raise TimeoutError
        number = getNum(htmlcode)
        dic = {
            'title': getTitle(htmlcode).replace(number, '').strip(),
            'studio': getStudio(htmlcode),
            'year': getYear(getRelease(htmlcode)),
            'runtime': getRuntime(htmlcode).replace('分鐘', '').strip(),
            'director': getDirector(htmlcode),
            'actor': getActor(htmlcode),
            'release': getRelease(htmlcode),
            'number': getNum(htmlcode),
            'tag': getTag(htmlcode),
            'series': getSeries(htmlcode),
            'cover': getCover(htmlcode),
            'extrafanart': getExtraFanart(htmlcode),
            'cover_small': '',
            'imagecut': 0,
            'actor_photo': getActorPhoto(htmlcode),
            'publisher': '',
            'outline': '',
            'score': '',
            'website': result_url,
            'source': 'javbus.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in javbus.main_us : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


'''
print(find_number('KA-001'))
print(main_uncensored('010115-001'))
print(main('ssni-644'))
print(main_uncensored('012715-793'))
print(main_us('sexart.15.06.10'))
print(main_uncensored('heyzo-1031'))
'''

# print(main('ssni-644', "https://www.javbus.com/SSNI-644"))
# print(main('ssni-802', ""))
# print(main_us('DirtyMasseur.20.07.26', "https://www.javbus.one/DirtyMasseur-20-07-26"))
