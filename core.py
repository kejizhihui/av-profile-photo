# -*- coding: utf-8 -*-

import re
import os
import os.path
import shutil
from PIL import Image
import time
import json
from ADC_function import *
from configparser import ConfigParser
import argparse
# =========website========
import fc2fans_club
import siro
import avsox
import javbus
import javdb
import fanza
import requests


# =====================本地文件处理===========================

def escapePath(path, Config):  # Remove escape literals
    escapeLiterals = Config['escape']['literals']
    backslash = '\\'
    for literal in escapeLiterals:
        path = path.replace(backslash + literal, '')
    return path



def getDataFromJSON(file_number, filepath, failed_folder, config):  # 从JSON返回元数据
    # ================================================网站规则添加开始================================================

    if re.match('^\d{5,}', file_number):
        json_data = json.loads(avsox.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javdb.main(file_number))
    # ==
    elif re.match('\d+\D+', file_number):
        json_data = json.loads(siro.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javbus.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javdb.main(file_number))
    # ==
    elif 'fc2' in file_number or 'FC2' in file_number:
        json_data = json.loads(fc2fans_club.main(
            file_number.replace('fc2-', '').replace('fc2_', '').replace('FC2-', '').replace('fc2_', '')))
    # ==
    elif 'HEYZO' in file_number or 'heyzo' in file_number or 'Heyzo' in file_number:
        json_data = json.loads(avsox.main(file_number))
    # ==
    elif 'siro' in file_number or 'SIRO' in file_number or 'Siro' in file_number:
        json_data = json.loads(siro.main(file_number))
    elif not '-' in file_number or '_' in file_number:
        json_data = json.loads(fanza.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javbus.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(avsox.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javdb.main(file_number))
    # ==
    else:
        json_data = json.loads(javbus.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(avsox.main(file_number))
        if getDataState(json_data) == 0:  # 如果元数据获取失败，请求番号至其他网站抓取
            json_data = json.loads(javdb.main(file_number))

    # ================================================网站规则添加结束================================================

    title = json_data['title']
    actor_list = str(json_data['actor']).strip("[ ]").replace("'", '').split(',')  # 字符串转列表
    release = json_data['release']
    number = json_data['number']
    try:
        cover_small = json_data['cover_small']
    except:
        cover_small = ''
    tag = str(json_data['tag']).strip("[ ]").replace("'", '').replace(" ", '').split(',')  # 字符串转列表 @
    actor = str(actor_list).strip("[ ]").replace("'", '').replace(" ", '')

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
    release = release.replace('/', '-')
    tmpArr = cover_small.split(',')
    if len(tmpArr) > 0:
        cover_small = tmpArr[0].strip('\"').strip('\'')
    # ====================处理异常字符 END================== #\/:*?"<>|

    naming_rule = eval(config['Name_Rule']['naming_rule'])
    location_rule = eval(config['Name_Rule']['location_rule'])

    # 返回处理后的json_data
    json_data['title'] = title
    json_data['actor'] = actor
    json_data['release'] = release
    json_data['cover_small'] = cover_small
    json_data['tag'] = tag
    json_data['naming_rule'] = naming_rule
    json_data['location_rule'] = location_rule
    return json_data


def get_info(json_data):  # 返回json里的数据
    title = json_data['title']
    studio = json_data['studio']
    year = json_data['year']
    outline = json_data['outline']
    runtime = json_data['runtime']
    director = json_data['director']
    actor_photo = json_data['actor_photo']
    release = json_data['release']
    number = json_data['number']
    cover = json_data['cover']
    website = json_data['website']
    return title, studio, year, outline, runtime, director, actor_photo, release, number, cover, website


def creatFolder(success_folder, location_rule, json_data, Config):  # 创建文件夹
    title, studio, year, outline, runtime, director, actor_photo, release, number, cover, website = get_info(json_data)
    if len(location_rule) > 240:  # 新建成功输出文件夹
        path = success_folder + '/' + location_rule.replace("'actor'", "'manypeople'", 3).replace("actor",
                                                                                                  "'manypeople'",
                                                                                                  3)  # path为影片+元数据所在目录
    else:
        path = success_folder + '/' + location_rule
    if not os.path.exists(path):
        path = escapePath(path, Config)
        try:
            os.makedirs(path)
        except:
            path = success_folder + '/' + location_rule.replace('/[' + number + ']-' + title, "/number")
            path = escapePath(path, Config)
            os.makedirs(path)
    return path


def copyRenameJpgToBackdrop(option, path, number, c_word):
    if option == 'plex':
        shutil.copy(path + '/fanart.jpg', path + '/Backdrop.jpg')
        shutil.copy(path + '/poster.png', path + '/thumb.png')
    if option == 'emby':
        shutil.copy(path + '/' + number + c_word + '.jpg', path + '/Backdrop.jpg')
    if option == 'kodi':
        shutil.copy(path + '/' + number + c_word + '-fanart.jpg', path + '/Backdrop.jpg')


