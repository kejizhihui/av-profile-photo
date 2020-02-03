#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from core import *



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


def getNumber(filepath):
    filepath = filepath.replace('./', '')
    if '-' in filepath or '_' in filepath:  # 普通提取番号 主要处理包含减号-和_的番号
        filepath = filepath.replace("_", "-")
        filepath.strip('22-sht.me').strip('-HD').strip('-hd')
        filename = str(re.sub("\[\d{4}-\d{1,2}-\d{1,2}\] - ", "", filepath))  # 去除文件名中时间
        if 'FC2' or 'fc2' in filename:
            filename = filename.replace('-PPV', '').replace('PPV-', '').replace('-ppv', '').replace('ppv-', '')
        try:
            file_number = re.search('\w+-\d+', filename).group()
        except:  # 提取类似mkbd-s120番号
            file_number = re.search('\w+-\w+\d+', filename).group()
        return file_number
    else:  # 提取不含减号-的番号，FANZA CID
        try:
            return str(
                re.findall(r'(.+?)\.', str(re.search('([^<>/\\\\|:""\\*\\?]+)\\.\\w+$', filepath).group()))).strip(
                "['']").replace('_', '-')
        except:
            return re.search(r'(.+?)\.', filepath)[0]
