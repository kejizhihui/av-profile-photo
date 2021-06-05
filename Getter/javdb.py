import re
from bs4 import BeautifulSoup, SoupStrainer
from lxml import etree
import json
from Function.getHtml import get_html_javdb
from Function.getHtml import post_html


def getTitle(htmlcode):
    try:
        html = etree.fromstring(htmlcode, etree.HTMLParser())
        result = str(html.xpath('/html/body/section/div/h2/strong/text()')).strip(" ['']")
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', '').replace(' : ', ''))
    except:
        return re.sub('.*\] ', '', result.replace('/', ',').replace('\\xa0', ''))


def getActor(htmlcode):  # //*[@id="center_column"]/div[2]/div[1]/div/table/tbody/tr[1]/td/text()
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = html.xpath(
        '//strong[text()="演員:"]/../span/strong[@class="symbol female"][last()]/preceding-sibling::a/text()')
    result2 = html.xpath(
        '//strong[text()="Actor(s):"]/../span/strong[@class="symbol female"][last()]/preceding-sibling::a/text()')
    return result1 + result2


def getActorPhoto(actor):  # //*[@id="star_qdt"]/li/a/img
    d = {}
    for i in actor:
        if ',' not in i or ')' in i:
            p = {i: ''}
            d.update(p)
    return d


def getStudio(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"片商:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Maker:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getPublisher(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"發行:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Publisher:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getRuntime(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"時長")]/../span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Duration:")]/../span/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').rstrip('mi').rstrip(' minute(s)')


def getSeries(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"系列:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Series:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getNumber(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result1 = str(html.xpath('//strong[contains(text(),"番號:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    result2 = str(html.xpath('//strong[contains(text(),"ID:")]/../span/a/text()')).strip(
        " ['']").replace('_', '-')
    return str(result2 + result1).strip('+')


def getYear(release):
    try:
        result = str(re.search('\d{4}', release).group())
        return result
    except:
        return release


def getRelease(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"日期:")]/../span/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Released Date:")]/../span/text()')).strip(" ['']")
    return str(result1 + result2).strip('+')


def getTag(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"類別:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Tags:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace(",\\xa0", "").replace("'", "").replace(' ', '').replace(',,',
                                                                                                             '').lstrip(
        ',')


# def getCover_small(htmlcode, count):
#     html = etree.fromstring(htmlcode, etree.HTMLParser())
#     result = html.xpath("//div[@class='grid-item column']/a[@class='box']/div/img/@data-src")[count]
#     if 'thumbs' not in result:
#         result = html.xpath("//div[@class='grid-item column']/a[@class='box']/div/img/@src")[count]
#     if not 'https' in result:
#         result = 'https:' + result
#     return result


def getCover(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    result = html.xpath("//img[@class='video-cover']/@src")
    if len(result) >= 1:
        result = result[0]
    # 有时xpath找不到元素，所以要用bs4
    if not result:
        soup = BeautifulSoup(htmlcode, 'lxml', parse_only=SoupStrainer('img', {'class': 'video-cover'}))
        if soup.img is not None:
            result = soup.img['src']
    return result


def getExtraFanart(htmlcode):  # 获取封面链接
    html = etree.fromstring(htmlcode, etree.HTMLParser())
    extrafanart_list = html.xpath("//div[@class='message-body']/div[@class='tile-images preview-images']/a/@href")
    if '#preview-video' in extrafanart_list:
        extrafanart_list.remove('#preview-video')
    return extrafanart_list


def getDirector(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result1 = str(html.xpath('//strong[contains(text(),"導演:")]/../span/a/text()')).strip(" ['']")
    result2 = str(html.xpath('//strong[contains(text(),"Director:")]/../span/a/text()')).strip(" ['']")
    return str(result1 + result2).strip('+').replace("', '", '').replace('"', '')


def getScore(htmlcode):
    html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
    result = str(html.xpath("//span[@class='score-label']/text()")).strip(" ['']")
    score = 0
    if re.search(r'\(.+分\)', result):
        score = re.findall(r'\((.+)分\)', result)[0]
    return format(float(score), '0.1f')


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
    except Exception as error_info:
        print('Error in javdb.getOutlineScore : ' + str(error_info))
    return outline, score


def main(number, appoint_url, isuncensored=False):
    try:
        if appoint_url == '':
            # ========================================================================搜索番号
            htmlcode = get_html_javdb('https://javdb.com/search?q=' + number + '&f=all').replace(u'\xa0', u' ')
            if str(htmlcode) == 'ProxyError':
                raise TimeoutError
            html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
            counts = len(html.xpath(
                '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\']'))
            if counts == 0:
                raise Exception('Movie Data not found in javdb.main!')
            # ========================================================================遍历搜索结果，找到需要的番号所在URL
            count = 1
            movie_found = 0
            for count in range(1, counts + 1):
                number_get = html.xpath(
                    '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
                        count) + ']/a[@class=\'box\']/div[@class=\'uid\']/text()')[0]
                if number_get.upper() == number.upper():
                    movie_found = 1
                    break
            if movie_found == 0:
                raise Exception('Movie Data not found in javdb.main!')
            result_url = 'https://javdb.com' + html.xpath('//*[@id="videos"]/div/div/a/@href')[count - 1]
        else:
            result_url = appoint_url
        # ========================================================================请求、判断结果
        html_info = get_html_javdb(result_url + '?locale=zh').replace(u'\xa0', u' ')
        if str(html_info) == 'ProxyError':
            raise TimeoutError
        # ========================================================================获取评分、简介
        imagecut = 1
        outline = ''
        if isuncensored and (re.match('^\d{4,}', number) or re.match('n\d{4}', number)):  # 无码，收集封面、评分
            imagecut = 0
            score = getScore(html_info)
        elif 'HEYZO' in number.upper():  # HEYZO，收集封面、评分、简介
            imagecut = 0
            outline, score = getOutlineScore(number)
        else:  # 其他，收集评分、简介
            outline, score = getOutlineScore(number)
        # ========================================================================收集信息
        actor = getActor(html_info)
        if len(actor) == 0 and 'FC2-' in number.upper():
            actor.append('FC2-NoActor')
        dic = {
            'actor': str(actor).strip(" [',']").replace('\'', ''),
            'title': getTitle(html_info).replace('中文字幕', '').replace('無碼', '').replace("\\n", '').replace('_',
                                                                                                          '-').replace(
                number.upper(), '').replace(number, '').strip().replace(' ', '-').replace('--', '-'),
            'studio': getStudio(html_info),
            'publisher': getPublisher(html_info),
            'outline': outline,
            'score': score,
            'runtime': getRuntime(html_info).replace(' 分鍾', ''),
            'director': getDirector(html_info),
            'release': getRelease(html_info),
            'number': number.upper(),
            'cover': getCover(html_info),
            'cover_small': '',
            'extrafanart': getExtraFanart(html_info),
            'imagecut': imagecut,
            'tag': getTag(html_info),
            'series': getSeries(html_info),
            'year': getYear(getRelease(html_info)),  # str(re.search('\d{4}',getRelease(htmlcode)).group()),
            'actor_photo': getActorPhoto(actor),
            'website': result_url,
            'source': 'javdb.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in javdb.main : ' + str(error_info))
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
            # ========================================================================搜索番号
            htmlcode = get_html_javdb('https://javdb.com/search?q=' + number + '&f=all').replace(u'\xa0', u' ')
            if str(htmlcode) == 'ProxyError':
                raise TimeoutError
            html = etree.fromstring(htmlcode, etree.HTMLParser())  # //table/tr[1]/td[1]/text()
            counts = len(html.xpath(
                '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\']'))
            if counts == 0:
                raise Exception('Movie Data not found in javdb.main_us!')
            # ========================================================================遍历搜索结果，找到需要的番号所在URL
            number_series = number.split('.')[0]
            number_date = '20' + number.replace(number_series, '').strip('.')
            number_date = number_date.replace('.', '-')
            count = 1
            movie_found = 0
            for count in range(1, counts + 1):  # 遍历搜索结果，找到需要的番号
                series_get = html.xpath(
                    '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
                        count) + ']/a[@class=\'box\']/div[@class=\'uid2\']/text()')[0]
                if not series_get:
                    series_get = html.xpath(
                        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column horz-cover\'][' + str(
                            count) + ']/a[@class=\'box\']/div[@class=\'uid2\']/text()')[0]
                date_get = html.xpath(
                    '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column\'][' + str(
                        count) + ']/a[@class=\'box\']/div[@class=\'meta\']/text()')[0]
                if not date_get:
                    date_get = html.xpath(
                        '//div[@id=\'videos\']/div[@class=\'grid columns\']/div[@class=\'grid-item column horz-cover\'][' + str(
                            count) + ']/a[@class=\'box\']/div[@class=\'meta\']/text()')[0]
                if re.search('\d{4}-\d{1,2}-\d{1,2}', date_get):
                    date_get = re.findall('\d{4}-\d{1,2}-\d{1,2}', date_get)[0]
                elif re.search('\d{1,2}/\d{1,2}/\d{4}', date_get):
                    date_get_tmp = date_get
                    date_get = re.findall('\d{1,2}/\d{1,2}', date_get_tmp)[0]
                    year_get = re.findall('\d{4}', date_get_tmp)[0]
                    date_get = year_get + '-' + date_get
                series_get = series_get.replace(' ', '')
                date_get = date_get.replace('/', '-')
                if (series_get.upper() == number_series.upper()
                    or series_get.replace('-', '').upper() == number_series.upper()) and number_date == date_get:
                    movie_found = 1
                    break
            if movie_found == 0:
                raise Exception('Movie Data not found in javdb.main_us!')
            result_url = 'https://javdb.com' + html.xpath('//*[@id="videos"]/div/div/a/@href')[count - 1]
        # ========================================================================请求、判断结果
        html_info = get_html_javdb(result_url + '?locale=zh').replace(u'\xa0', u' ')
        if str(html_info) == 'ProxyError':
            raise TimeoutError
        # ========================================================================收集信息
        actor = getActor(html_info)
        number = getNumber(html_info)
        dic = {
            'actor': str(actor).strip(" [',']").replace('\'', ''),
            'title': getTitle(html_info).replace('中文字幕', '').replace("\\n", '').replace('_', '-').replace(number,
                                                                                                          '').strip(),
            'studio': getStudio(html_info),
            'publisher': getPublisher(html_info),
            'outline': '',
            'score': getScore(html_info),
            'runtime': getRuntime(html_info).replace(' 分鍾', ''),
            'director': getDirector(html_info),
            'release': getRelease(html_info),
            'number': number,
            'cover': getCover(html_info),
            'cover_small': '',
            'extrafanart': getExtraFanart(html_info),
            'imagecut': 0,
            'tag': getTag(html_info),
            'series': getSeries(html_info),
            'year': getYear(getRelease(html_info)),  # str(re.search('\d{4}',getRelease(htmlcode)).group()),
            'actor_photo': getActorPhoto(actor),
            'website': result_url,
            'source': 'javdb.py',
        }
    except TimeoutError:
        dic = {
            'title': '',
            'website': 'timeout',
        }
    except Exception as error_info:
        print('Error in javdb.main_us : ' + str(error_info))
        dic = {
            'title': '',
            'website': '',
        }
    js = json.dumps(dic, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'), )  # .encode('UTF-8')
    return js


'''
print(main('abs-141'))
print(main('HYSD-00083'))
print(main('IESP-660'))
print(main('n1403'))
print(main('GANA-1910'))
print(main('heyzo-1031'))
print(main_us('x-art.19.11.03'))
print(main('032020-001'))
print(main('S2M-055'))
print(main('LUXU-1217'))
'''
# print(main('IPX-604', ''))
# print(main('SSIS-084', ''))
# print(main('abs-141', ''))
# print(main('HYSD-00083', ''))
# print(main('IESP-660', ''))
# print(main('n1403', ''))
# print(main('GANA-1910', ''))
# print(main('heyzo-1031', ''))
# print(main_us('x-art.19.11.03', ''))
# print(main('032020-001', ''))
# print(main('S2M-055', ''))
# print(main('LUXU-1217', ''))
# print(main_us('x-art.19.11.03', ''))
