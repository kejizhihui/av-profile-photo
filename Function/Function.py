#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import json
from configparser import ConfigParser
import requests
from lxml import etree
from Getter import avsox, javlibrary, javbus, javdb, fc2fans_club, mgstage, dmm


# ========================================================================获取视频列表
def movie_lists(escape_folder):
    if escape_folder != '':
        escape_folder = re.split('[,，]', escape_folder)
    total = []
    file_type = ['.mp4', '.avi', '.rmvb', '.wmv', '.mov', '.mkv', '.flv', '.ts', '.MP4', '.AVI', '.RMVB', '.WMV',
                 '.MOV', '.MKV', '.FLV', '.TS', ]
    file_root = os.getcwd()
    for root, dirs, files in os.walk(file_root):
        if escape_folder != '':
            flag_escape = 0
            for folder in escape_folder:
                if folder in root:
                    flag_escape = 1
                    break
            if flag_escape == 1:
                continue
        for f in files:
            if os.path.splitext(f)[1] in file_type:
                path = root + '/' + f
                path = path.replace(file_root, '.')
                path = path.replace("\\\\", "/").replace("\\", "/")
                total.append(path)
    return total


# ========================================================================获取番号
def getNumber(filepath):
    filepath = filepath.replace('-C.', '.').replace('-c.', '.')
    filename = os.path.splitext(filepath.split('/')[-1])[0]
    # filename = filename.replace("_", "-")
    part = ''
    if re.search('-CD\d+', filename):
        part = re.findall('-CD\d+', filename)[0]
    if re.search('-cd\d+', filename):
        part = re.findall('-cd\d+', filename)[0]
    filename = filename.replace(part, '')
    filename = str(re.sub("-\d{4}-\d{1,2}-\d{1,2}", "", filename))  # 去除文件名中时间
    filename = str(re.sub("\d{4}-\d{1,2}-\d{1,2}-", "", filename))  # 去除文件名中时间
    if re.search('^\D+.\d{2}.\d{2}.\d{2}', filename):  # 提取欧美番号 sexart.11.11.11
        try:
            file_number = re.search('\D+.\d{2}.\d{2}.\d{2}', filename).group()
            return file_number
        except:
            return os.path.splitext(filepath.split('/')[-1])[0]
    elif '-' in filename or '_' in filename:  # 普通提取番号 主要处理包含减号-和_的番号
        if 'FC2' or 'fc2' in filename:
            filename = filename.replace('-PPV', '').replace('PPV-', '').replace('-ppv', '').replace('ppv-', '')
        if re.search('\w+-\d+', filename):  # 提取类似mkbd-120番号
            file_number = re.search('\w+-\d+', filename).group()
        elif re.search('\d+[a-zA-Z]+-\d+', filename):  # 提取类似259luxu-1111番号
            file_number = re.search('\d+[a-zA-Z]+-\d+', filename).group()
        elif re.search('\w+-\w\d+', filename):  # 提取类似mkbd-s120番号
            file_number = re.search('\w+-\w\d+', filename).group()
        elif re.search('\d+-\w+', filename):  # 提取类似 111111-MMMM 番号
            file_number = re.search('\d+-\w+', filename).group()
        elif re.search('\d+-\d+', filename):  # 提取类似 111111-000 番号
            file_number = re.search('\d+-\d+', filename).group()
        elif re.search('\d+_\d+', filename):  # 提取类似 111111_000 番号
            file_number = re.search('\d+_\d+', filename).group()
        else:
            file_number = filename
        return file_number
    else:  # 提取不含减号-的番号，FANZA CID 保留ssni00644，将MIDE139改成MIDE-139
        try:
            file_number = os.path.splitext(filename.split('/')[-1])[0]
            find_num = re.findall(r'\d+', file_number)[0]
            find_char = re.findall(r'\D+', file_number)[0]
            if len(find_num) <= 4 and len(find_char) > 1:
                file_number = find_char + '-' + find_num
            return file_number
        except:
            return os.path.splitext(filepath.split('/')[-1])[0]


# ========================================================================去掉异常字符
def escapePath(path, Config):  # Remove escape literals
    escapeLiterals = Config['escape']['literals']
    backslash = '\\'
    for literal in escapeLiterals:
        path = path.replace(backslash + literal, '')
    return path


# ========================================================================根据番号获取数据
def getDataFromJSON(file_number, config, mode):  # 从JSON返回元数据
    # ================================================网站规则添加开始================================================
    json_data = {}
    if mode == 1:  # 从全部网站刮削
        # =======================================================================无码抓取:111111-111,n1111,HEYZO-1111
        if re.match('^\d{4,}', file_number) or re.match('n\d{4}', file_number) or 'HEYZO' in file_number.upper():
            json_data = json.loads(javbus.main_uncensored(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(javdb.main(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(avsox.main(file_number))
        # =======================================================================259LUXU-1111
        elif re.match('\d+[a-zA-Z]+-\d+', file_number) or 'SIRO' in file_number.upper():
            json_data = json.loads(mgstage.main(file_number))
            file_number = re.search('[a-zA-Z]+-\d+', file_number).group()
            if getDataState(json_data) == 0:
                json_data = json.loads(javdb.main(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(javbus.main(file_number))
        # =======================================================================FC2-111111
        elif 'FC2' in file_number.upper():
            json_data = json.loads(fc2fans_club.main(
                file_number.replace('fc2-', '').replace('fc2_', '').replace('FC2-', '').replace('fc2_', '')))
            if getDataState(json_data) == 0:
                json_data = json.loads(javdb.main(file_number))
        # =======================================================================ssni00321
        elif re.match('\D{2,}00\d{3,}', file_number) and '-' not in file_number and '_' not in file_number:
            json_data = json.loads(dmm.main(file_number))
        # =======================================================================sexart.15.06.14
        elif re.search('[a-zA-Z]+.\d{2}.\d{2}.\d{2}', file_number):
            json_data = json.loads(javdb.main_us(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(javbus.main_us(file_number))
        # =======================================================================MIDE-139
        else:
            json_data = json.loads(javbus.main(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(javlibrary.main(file_number, config['javlibrary_url']['url']))
            if getDataState(json_data) == 0:
                json_data = json.loads(javdb.main(file_number))
            if getDataState(json_data) == 0:
                json_data = json.loads(avsox.main(file_number))
    elif re.match('\D{2,}00\d{3,}', file_number) and mode != 8:
        json_data = {
            'title': '',
            'actor': '',
            'website': '',
        }
    elif mode == 2:  # 仅从javlibrary
        json_data = json.loads(javlibrary.main(file_number, config['javlibrary_url']['url']))
    elif mode == 3:  # 仅从mgstage
        json_data = json.loads(mgstage.main(file_number))
    elif mode == 4:  # 仅从fc2club
        json_data = json.loads(fc2fans_club.main(file_number))
    elif mode == 5:  # 仅从javbus
        if re.match('^\d{5,}', file_number) or re.match('n\d{4}', file_number) or 'HEYZO' in file_number.upper():
            json_data = json.loads(javbus.main_uncensored(file_number))
        elif re.search('\D+.\d{2}.\d{2}.\d{2}', file_number):
            json_data = json.loads(javbus.main_us(file_number))
        else:
            json_data = json.loads(javbus.main(file_number))
    elif mode == 6:  # 仅从javdb
        if re.search('\D+.\d{2}.\d{2}.\d{2}', file_number):
            json_data = json.loads(javdb.main_us(file_number))
        else:
            json_data = json.loads(javdb.main(file_number))
    elif mode == 7:  # 仅从avsox
        json_data = json.loads(avsox.main(file_number))
    elif mode == 8:  # 仅从dmm
        json_data = json.loads(dmm.main(file_number))

    # ================================================网站规则添加结束================================================
    # print(json_data)
    # ======================================超时或未找到
    if json_data['website'] == 'timeout':
        return json_data
    elif json_data['title'] == '':
        return json_data
    # ======================================处理得到的信息
    title = json_data['title']
    number = json_data['number']
    actor_list = str(json_data['actor']).strip("[ ]").replace("'", '').split(',')  # 字符串转列表
    release = json_data['release']
    try:
        cover_small = json_data['cover_small']
    except:
        cover_small = ''
    tag = str(json_data['tag']).strip("[ ]").replace("'", '').replace(" ", '').split(',')  # 字符串转列表 @
    actor = str(actor_list).strip("[ ]").replace("'", '').replace(" ", '')
    if actor == '':
        actor = 'Unknown'

    # ====================处理异常字符====================== #\/:*?"<>|
    title = title.replace('\\', '')
    title = title.replace('/', '')
    title = title.replace(':', '')
    title = title.replace('*', '')
    title = title.replace('?', '')
    title = title.replace('"', '')
    title = title.replace('<', '')
    title = title.replace('>', '')
    title = title.replace('|', '')
    title = title.replace(' ', '.')
    title = title.replace('【', '')
    title = title.replace('】', '')
    release = release.replace('/', '-')
    tmpArr = cover_small.split(',')
    if len(tmpArr) > 0:
        cover_small = tmpArr[0].strip('\"').strip('\'')
    for key, value in json_data.items():
        if key == 'title' or key == 'studio' or key == 'director' or key == 'series' or key == 'publisher':
            json_data[key] = str(value).replace('/', '')
    # ====================处理异常字符 END================== #\/:*?"<>|

    naming_media = config['Name_Rule']['naming_media']
    naming_file = config['Name_Rule']['naming_file']
    folder_name = config['Name_Rule']['folder_name']

    # 返回处理后的json_data
    json_data['title'] = title
    json_data['number'] = number
    json_data['actor'] = actor
    json_data['release'] = release
    json_data['cover_small'] = cover_small
    json_data['tag'] = tag
    json_data['naming_media'] = naming_media
    json_data['naming_file'] = naming_file
    json_data['folder_name'] = folder_name
    return json_data


# ========================================================================返回json里的数据
def get_info(json_data):
    for key, value in json_data.items():
        if value == '' or value == 'N/A':
            json_data[key] = 'unknown'
    title = json_data['title']
    studio = json_data['studio']
    publisher = json_data['publisher']
    year = json_data['year']
    outline = json_data['outline']
    runtime = json_data['runtime']
    director = json_data['director']
    actor_photo = json_data['actor_photo']
    actor = json_data['actor']
    release = json_data['release']
    tag = json_data['tag']
    number = json_data['number']
    cover = json_data['cover']
    website = json_data['website']
    series = json_data['series']
    return title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series


# ========================================================================保存配置到config.ini
def save_config(json_config):
    # json_config = json.loads(json_config)
    with open("config.ini", "wt", encoding='UTF-8') as code:
        print("[common]", file=code)
        print("main_mode = " + str(json_config['main_mode']), file=code)
        print("failed_output_folder = " + json_config['failed_output_folder'], file=code)
        print("success_output_folder = " + json_config['success_output_folder'], file=code)
        print("soft_link = " + str(json_config['soft_link']), file=code)
        print("website = " + json_config['website'], file=code)
        print("# all or javlibrary or mgstage or fc2club or javbus or javdb or avsox or dmm", file=code)
        print("", file=code)
        print("[proxy]", file=code)
        print("proxy = " + json_config['proxy'], file=code)
        print("timeout = " + str(json_config['timeout']), file=code)
        print("retry = " + str(json_config['retry']), file=code)
        print("", file=code)
        print("[Name_Rule]", file=code)
        print("folder_name = " + json_config['folder_name'], file=code)
        print("naming_media = " + json_config['naming_media'], file=code)
        print("naming_file = " + json_config['naming_file'], file=code)
        print("", file=code)
        print("[update]", file=code)
        print("update_check = " + str(json_config['update_check']), file=code)
        print("", file=code)
        print("[log]", file=code)
        print("save_log = " + str(json_config['save_log']), file=code)
        print("", file=code)
        print("[media]", file=code)
        print("media_warehouse = " + json_config['media_warehouse'], file=code)
        print("# emby or plex or kodi ,emby = jellyfin", file=code)
        print("", file=code)
        print("[escape]", file=code)
        print("literals = " + json_config['literals'], file=code)
        print("folders = " + json_config['folders'], file=code)
        print("", file=code)
        print("[debug_mode]", file=code)
        print("switch = " + str(json_config['switch_debug']), file=code)
        print("", file=code)
        print("[emby]", file=code)
        print("emby_url = " + json_config['emby_url'], file=code)
        print("api_key = " + json_config['api_key'], file=code)
        print("", file=code)
        print("[javlibrary_url]", file=code)
        print("url = " + json_config['javlib_url'], file=code)
    code.close()


# ========================================================================元数据获取失败检测
def getDataState(json_data):
    if json_data['title'] == '' or json_data['title'] == 'None' or json_data['title'] == 'null':
        return 0
    else:
        return 1
