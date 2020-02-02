#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTextCursor, QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QThread, Qt
from AVDC import *
from AVDC_EACH import *
import os
import sys
import time
import os.path
from PIL import Image
import json
from configparser import ConfigParser
from AV_Data_Capture import *
from core import *
from fanza import *
import requests


class MyMAinWindow(QMainWindow, Ui_AVDV):
    progressBarValue = pyqtSignal(int)

    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.Ui = Ui_AVDV()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.Init_Ui()
        self.Init()
        self.Load_Config()
        self.update_version()

    def Init_Ui(self):
        pix = QPixmap('AVDC-ico.png')
        self.Ui.label_ico.setScaledContents(True)
        self.Ui.label_ico.setPixmap(pix)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.Ui.widget_setting.setStyleSheet(
            '''
            QWidget#widget_setting{
                    background:#F0F8FF;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton{
                    font-size:15px;
                    background:gray;
                    border:9px solid gray;
                    border-radius:15px;
                    padding:2px 4px;
            }
            
            ''')
        self.Ui.centralwidget.setStyleSheet(
            '''
            QWidget#centralwidget{
                    background:gray;
                    border:1px solid gray;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }            
            QLineEdit{
                    background:white;
                    border:1px solid white;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }            
            QTextBrowser#textBrowser_about{
                    background:white;
                    border:1px solid white;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }            
            QTextBrowser#textBrowser_warning{
                    background:gray;
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }            
            QPushButton#pushButton_start_cap,#pushButton_javdb_sp,#pushButton_move_mp4,#pushButton_select_file{
                    font-size:20px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_save_config, #pushButton_start_javdb{
                    font-size:18px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:13px;
                    padding:2px 4px;
            }
            ''')

    def Init(self):
        self.Ui.stackedWidget.setCurrentIndex(0)
        self.Ui.pushButton_close.clicked.connect(self.close_win)
        self.Ui.pushButton_min.clicked.connect(self.min_win)
        self.Ui.pushButton_main.clicked.connect(self.pushButton_main_clicked)
        self.Ui.pushButton_tool.clicked.connect(self.pushButton_tool_clicked)
        self.Ui.pushButton_setting.clicked.connect(self.pushButton_setting_clicked)
        self.Ui.pushButton_select_file.clicked.connect(self.pushButton_select_file_clicked)
        self.Ui.pushButton_about.clicked.connect(self.pushButton_about_clicked)
        self.Ui.pushButton_start_cap.clicked.connect(self.pushButton_start_cap_clicked)
        self.Ui.pushButton_save_config.clicked.connect(self.pushButton_save_config_clicked)
        self.Ui.pushButton_move_mp4.clicked.connect(self.move_file)

    # ========================================================================加载config
    def Load_Config(self):
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        if int(config['common']['main_mode']) == 1:
            self.Ui.radioButton_common.setChecked(True)
        elif int(config['common']['main_mode']) == 2:
            self.Ui.radioButton_sort.setChecked(True)
        if int(config['common']['soft_link']) == 1:
            self.Ui.radioButton_soft_on.setChecked(True)
        elif int(config['common']['soft_link']) == 0:
            self.Ui.radioButton_soft_off.setChecked(True)
        if int(config['update']['update_check']) == 1:
            self.Ui.radioButton_update_on.setChecked(True)
        elif int(config['update']['update_check']) == 0:
            self.Ui.radioButton_update_off.setChecked(True)
        if int(config['debug_mode']['switch']) == 1:
            self.Ui.radioButton_debug_on.setChecked(True)
        elif int(config['debug_mode']['switch']) == 0:
            self.Ui.radioButton_debug_off.setChecked(True)
        if config['media']['media_warehouse'] == 'emby' or config['media']['media_warehouse'] == 'jellyfin':
            self.Ui.radioButton_emby.setChecked(True)
        elif config['media']['media_warehouse'] == 'plex':
            self.Ui.radioButton_plex.setChecked(True)
        elif config['media']['media_warehouse'] == 'kodi':
            self.Ui.radioButton_kodi.setChecked(True)
        self.Ui.lineEdit_success.setText(config['common']['success_output_folder'])
        self.Ui.lineEdit_fail.setText(config['common']['failed_output_folder'])
        self.Ui.lineEdit_escape_dir.setText(config['escape']['folders'])
        self.Ui.lineEdit_escape_char.setText(config['escape']['literals'])
        self.Ui.lineEdit_proxy.setText(config['proxy']['proxy'])
        self.Ui.lineEdit_timeout.setText(config['proxy']['timeout'])
        self.Ui.lineEdit_retry.setText(config['proxy']['retry'])
        self.Ui.lineEdit_dir_name.setText(config['Name_Rule']['location_rule'])
        self.Ui.lineEdit_media_name.setText(config['Name_Rule']['naming_rule'])
        self.Ui.lineEdit_escape_dir_move.setText(config['escape']['folders'])

    # ========================================================================检测更新
    def update_version(self):
        version = '3.1'
        self.add_text_main('[*]================== AV Data Capture ===================')
        self.add_text_main('[*]                     Version ' + version)
        self.add_text_main('[*]======================================================')
        self.UpdateCheck(version)

    # ========================================================================鼠标拖动窗口
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_drag:
            self.move(e.globalPos() - self.m_DragPosition)
            e.accept()

    # ========================================================================左侧按钮点击事件响应函数
    def close_win(self):
        os._exit(0)

    def min_win(self):
        self.setWindowState(Qt.WindowMinimized)

    def pushButton_main_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(0)

    def pushButton_tool_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(1)

    def pushButton_setting_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(2)

    def pushButton_about_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(3)

    def pushButton_start_cap_clicked(self):
        try:
            t = threading.Thread(target=self.AVDC_Main)
            t.start()  # 启动线程,即让线程开始执行
        except Exception:
            self.add_text_main('[-]Thread Exist Error!')

    def pushButton_save_config_clicked(self):
        try:
            t = threading.Thread(target=self.save_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception:
            self.add_text_main('[-]Thread Save Config Error!')

    # ========================================================================读取设置页设置，保存在config.ini
    def save_config_clicked(self):
        main_mode = 1
        soft_link = 0
        switch_debug = 0
        update_check = 0
        media_warehouse = ''
        if self.Ui.radioButton_common.isChecked():  # 普通模式
            main_mode = 1
        elif self.Ui.radioButton_sort.isChecked():  # 整理模式
            main_mode = 2
        if self.Ui.radioButton_soft_on.isChecked():  # 软链接开
            soft_link = 1
        elif self.Ui.radioButton_soft_off.isChecked():  # 软链接关
            soft_link = 0
        if self.Ui.radioButton_debug_on.isChecked():  # 调试模式开
            switch_debug = 1
        elif self.Ui.radioButton_debug_off.isChecked():  # 调试模式关
            switch_debug = 0
        if self.Ui.radioButton_update_on.isChecked():  # 检查更新
            update_check = 1
        elif self.Ui.radioButton_update_off.isChecked():  # 不检查更新
            update_check = 0
        if self.Ui.radioButton_emby.isChecked():  # emby/jellyfin
            media_warehouse = 'emby'
        elif self.Ui.radioButton_plex.isChecked():  # plex
            media_warehouse = 'plex'
        elif self.Ui.radioButton_kodi.isChecked():  # kodi
            media_warehouse = 'kodi'
        json_config = {
            'main_mode': main_mode,
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'update_check': update_check,
            'media_warehouse': media_warehouse,
            'failed_output_folder': self.Ui.lineEdit_fail.text(),
            'success_output_folder': self.Ui.lineEdit_success.text(),
            'proxy': self.Ui.lineEdit_proxy.text(),
            'timeout': self.Ui.lineEdit_timeout.text(),
            'retry': self.Ui.lineEdit_retry.text(),
            'location_rule': self.Ui.lineEdit_dir_name.text(),
            'naming_rule': self.Ui.lineEdit_media_name.text(),
            'literals': self.Ui.lineEdit_escape_char.text(),
            'folders': self.Ui.lineEdit_escape_dir.text(),
        }
        save_config(json_config)

    # ========================================================================小工具-单视频刮削
    def pushButton_select_file_clicked(self):
        fileName, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "Movie Files(*.mp4 *.avi *.rmvb "
                                                                   "*.wmv *.mov *.mkv *.flv *.ts *.MP4 *.AVI *.RMVB "
                                                                   "*.WMV *.MOV *.MKV *.FLV *.TS);;All Files(*)")

        self.Ui.stackedWidget.setCurrentIndex(0)
        try:
            t = threading.Thread(target=self.select_file_thread, args=(fileName,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception:
            self.add_text_main('[-]Thread Select File Error!')

    def select_file_thread(self, file_name):
        file_root = os.getcwd().replace("\\\\", "/").replace("\\", "/")
        file_path = file_name.replace(file_root, '.').replace("\\\\", "/").replace("\\", "/")
        file_name = os.path.splitext(file_name.split('/')[-1])[0]
        print(file_name, file_path, file_root)
        self.add_text_main("[!]Making Data for   [" + file_path + "], the number is [" + file_name + "]")
        self.core_main(file_path, file_name)
        self.add_text_main("[*]======================================================")

    # ========================================================================小工具-视频移动
    def move_file(self):
        self.Ui.stackedWidget.setCurrentIndex(0)
        try:
            t = threading.Thread(target=self.move_file_thread)
            t.start()  # 启动线程,即让线程开始执行
        except Exception:
            self.add_text_main('[-]Thread Save Config Error!')

    def move_file_thread(self):
        escape_dir = self.Ui.lineEdit_escape_dir_move.text()
        movie_list = movie_lists(escape_dir)
        self.add_text_main('[+]Move Movies Start! Find ' + str(len(movie_list)) + ' Movies')
        for movie in movie_list:
            sour = movie
            lenth = len(sour.split('/'))
            des = os.getcwd() + '/' + sour.split('/')[lenth - 1]
            try:
                if len(sour.split('/')) > 2:
                    shutil.move(sour, des)
                    self.add_text_main('   [+]Move ' + sour.split('/')[lenth - 1] + ' Success!')
            except:
                self.add_text_main('[-]   Move ' + sour.split('/')[lenth - 1] + ' Error!')
        self.add_text_main("[+]Move Movies All Finished!!!")
        self.add_text_main("[*]======================================================")

    # ========================================================================core.py
    def add_text_main(self, text):
        time.sleep(0.1)
        self.Ui.textBrowser_log_main.append(text)
        self.Ui.textBrowser_log_main.moveCursor(QTextCursor.End)

    def moveFailedFolder(self, filepath, failed_folder):
        self.add_text_main('[-]Move to Failed output folder')
        shutil.move(filepath, str(os.getcwd()) + '/' + failed_folder + '/')
        # os._exit(0)

    # =====================资源下载部分===========================
    def DownloadFileWithFilename(self, url, filename, path, Config, filepath,
                                 failed_folder):  # path = examle:photo , video.in the Project Folder!
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy = Config['proxy']['proxy']
            timeout = int(Config['proxy']['timeout'])
            retry_count = int(Config['proxy']['retry'])
        except:
            self.add_text_main('[-]Proxy config error! Please check the config.')
        i = 0

        while i < retry_count:
            try:
                if not proxy == '':
                    if not os.path.exists(path):
                        os.makedirs(path)
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
                    r = requests.get(url, headers=headers, timeout=timeout,
                                     proxies={"http": "http://" + str(proxy), "https": "https://" + str(proxy)})
                    if r == '':
                        self.add_text_main('[-]Movie Data not found!')
                        # os._exit(0)
                    with open(str(path) + "/" + filename, "wb") as code:
                        code.write(r.content)
                    return
                else:
                    if not os.path.exists(path):
                        os.makedirs(path)
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
                    r = requests.get(url, timeout=timeout, headers=headers)
                    if r == '':
                        self.add_text_main('[-]Movie Data not found!')
                        # os._exit(0)
                    with open(str(path) + "/" + filename, "wb") as code:
                        code.write(r.content)
                    return
            except requests.exceptions.RequestException:
                i += 1
                self.add_text_main('[-]Image Download :  Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ConnectionError:
                i += 1
                self.add_text_main('[-]Image Download :  Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ProxyError:
                i += 1
                self.add_text_main('[-]Image Download :  Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ConnectTimeout:
                i += 1
                self.add_text_main('[-]Image Download :  Connect retry ' + str(i) + '/' + str(retry_count))
        self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
        self.moveFailedFolder(filepath, failed_folder)

    def imageDownload(self, option, cover, number, c_word, path, multi_part, Config, filepath,
                      failed_folder):  # 封面是否下载成功，否则移动到failed
        if option == 'emby':
            if self.DownloadFileWithFilename(cover, number + c_word + '.jpg', path, Config, filepath,
                                             failed_folder) == 'failed':
                self.moveFailedFolder(filepath, failed_folder)
            self.DownloadFileWithFilename(cover, number + c_word + '.jpg', path, Config, filepath, failed_folder)
            if not os.path.getsize(path + '/' + number + c_word + '.jpg') == 0:
                self.add_text_main('[+]Image Downloaded! ' + number + c_word + '.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/' + number + c_word + '.jpg') == 0:
                    self.add_text_main('[!]Image Download Failed! Trying again. [' + Config['proxy']['retry'] + '/3]')
                    self.DownloadFileWithFilename(cover, number + c_word + '.jpg', path, Config, filepath,
                                                  failed_folder)
                    i = i + 1
                    continue
                else:
                    break
            if multi_part == 1:
                old_name = os.path.join(path, number + c_word + '.jpg')
                new_name = os.path.join(path, number + c_word + '.jpg')
                os.rename(old_name, new_name)
                self.add_text_main('[+]Image Downloaded! ' + number + c_word + '.jpg')
            else:
                self.add_text_main('[+]Image Downloaded! ' + number + c_word + '.jpg')
        elif option == 'plex':
            if self.DownloadFileWithFilename(cover, 'fanart.jpg', path, Config, filepath, failed_folder) == 'failed':
                self.moveFailedFolder(filepath, failed_folder)
            self.DownloadFileWithFilename(cover, 'fanart.jpg', path, Config, filepath, failed_folder)
            if not os.path.getsize(path + '/fanart.jpg') == 0:
                self.add_text_main('[+]Image Downloaded! fanart.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/fanart.jpg') == 0:
                    self.add_text_main('[!]Image Download Failed! Trying again. [' + Config['proxy']['retry'] + '/3]')
                    self.DownloadFileWithFilename(cover, 'fanart.jpg', path, Config, filepath, failed_folder)
                    i = i + 1
                    continue
                else:
                    break
            if not os.path.getsize(path + '/' + number + c_word + '.jpg') == 0:
                self.add_text_main('[!]Image Download Failed! Trying again.')
                self.DownloadFileWithFilename(cover, number + c_word + '.jpg', path, Config, filepath, failed_folder)
            self.add_text_main('[+]Image Downloaded! fanart.jpg')
        elif option == 'kodi':
            if self.DownloadFileWithFilename(cover, number + c_word + '-fanart.jpg', path, Config, filepath,
                                             failed_folder) == 'failed':
                self.moveFailedFolder(filepath, failed_folder)
            self.DownloadFileWithFilename(cover, number + c_word + '-fanart.jpg', path, Config, filepath, failed_folder)
            if not os.path.getsize(path + '/' + number + c_word + '-fanart.jpg') == 0:
                self.add_text_main('[+]Image Downloaded! ' + number + c_word + '-fanart.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/' + number + c_word + '-fanart.jpg') == 0:
                    self.add_text_main('[!]Image Download Failed! Trying again. [' + Config['proxy']['retry'] + '/3]')
                    self.DownloadFileWithFilename(cover, number + c_word + '-fanart.jpg', path, Config, filepath,
                                                  failed_folder)
                    i = i + 1
                    continue
                else:
                    break
            self.add_text_main('[+]Image Downloaded! ' + number + c_word + '-fanart.jpg')

    def smallCoverCheck(self, path, number, imagecut, cover_small, c_word, option, Config, filepath, failed_folder):
        if imagecut == 3:
            if option == 'emby':
                self.DownloadFileWithFilename(cover_small, '1.jpg', path, Config, filepath, failed_folder)
                try:
                    img = Image.open(path + '/1.jpg')
                except Exception:
                    img = Image.open('1.jpg')
                w = img.width
                h = img.height
                img.save(path + '/' + number + c_word + '.png')
                time.sleep(1)
                os.remove(path + '/1.jpg')
            if option == 'kodi':
                self.DownloadFileWithFilename(cover_small, '1.jpg', path, Config, filepath, failed_folder)
                try:
                    img = Image.open(path + '/1.jpg')
                except Exception:
                    img = Image.open('1.jpg')
                w = img.width
                h = img.height
                img.save(path + '/' + number + c_word + '-poster.jpg')
                time.sleep(1)
                os.remove(path + '/1.jpg')
            if option == 'plex':
                self.DownloadFileWithFilename(cover_small, '1.jpg', path, Config, filepath, failed_folder)
                try:
                    img = Image.open(path + '/1.jpg')
                except Exception:
                    img = Image.open('1.jpg')
                w = img.width
                h = img.height
                img.save(path + '/poster.png')
                os.remove(path + '/1.jpg')

    def PrintFiles(self, option, path, c_word, naming_rule, part, cn_sub, json_data, filepath, failed_folder, tag):
        title, studio, year, outline, runtime, director, actor_photo, actor, release, number, cover, website = get_info(
            json_data)
        naming_rule = naming_rule.split('-')
        name_title = ''
        count = 0
        for rule in naming_rule:
            if count == 0:
                name_title += json_data[rule]
            else:
                name_title += '-' + json_data[rule]
            count += 1
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path + "/" + number + c_word + ".nfo", "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                print(" <title>" + name_title + part + "</title>", file=code)
                print("  <set>", file=code)
                print("  </set>", file=code)
                print("  <studio>" + studio + "+</studio>", file=code)
                print("  <year>" + year + "</year>", file=code)
                print("  <outline>" + outline + "</outline>", file=code)
                print("  <plot>" + outline + "</plot>", file=code)
                print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                print("  <director>" + director + "</director>", file=code)
                if option == 'emby':
                    print("  <poster>" + number + c_word + ".png</poster>", file=code)
                    print("  <thumb>" + number + c_word + ".png</thumb>", file=code)
                    print("  <fanart>" + number + c_word + '.jpg' + "</fanart>", file=code)
                elif option == 'kodi':
                    print("  <poster>" + number + c_word + "-poster.jpg</poster>", file=code)
                    print("  <fanart>" + number + c_word + '-fanart.jpg' + "</fanart>", file=code)
                elif option == 'plex':
                    print("  <poster>poster.png</poster>", file=code)
                    print("  <thumb>thumb.png</thumb>", file=code)
                    print("  <fanart>fanart.jpg</fanart>", file=code)
                try:
                    for key, value in actor_photo.items():
                        print("  <actor>", file=code)
                        print("   <name>" + key + "</name>", file=code)
                        if not value == '':  # or actor_photo == []:
                            print("   <thumb>" + value + "</thumb>", file=code)
                        print("  </actor>", file=code)
                except:
                    aaaa = ''
                print("  <maker>" + studio + "</maker>", file=code)
                print("  <label>", file=code)
                print("  </label>", file=code)
                if cn_sub == '1':
                    print("  <tag>中文字幕</tag>", file=code)
                try:
                    for i in tag:
                        print("  <tag>" + i + "</tag>", file=code)
                except:
                    aaaaa = ''
                try:
                    for i in tag:
                        print("  <genre>" + i + "</genre>", file=code)
                except:
                    aaaaaaaa = ''
                if cn_sub == '1':
                    print("  <genre>中文字幕</genre>", file=code)
                print("  <num>" + number + "</num>", file=code)
                if option == 'emby':
                    print("  <premiered>" + release + "</premiered>", file=code)
                elif option == 'kodi' or option == 'plex':
                    print("  <release>" + release + "</release>", file=code)
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                self.add_text_main("[+]Writeed!          " + number + c_word + ".nfo")
        except IOError as e:
            self.add_text_main("[-]Write Failed!")
            self.add_text_main(e)
            self.moveFailedFolder(filepath, failed_folder)
        except Exception as e1:
            self.add_text_main(e1)
            self.add_text_main("[-]Write Failed!")
            self.moveFailedFolder(filepath, failed_folder)

    def cutImage(self, option, imagecut, path, number, c_word):
        if option == 'plex':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/fanart.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/poster.png')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                img = Image.open(path + '/fanart.jpg')
                w = img.width
                h = img.height
                img.save(path + '/poster.png')
        elif option == 'emby':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/' + number + c_word + '.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + number + c_word + '.png')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                img = Image.open(path + '/' + number + c_word + '.jpg')
                w = img.width
                h = img.height
                img.save(path + '/' + number + c_word + '.png')
        elif option == 'kodi':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/' + number + c_word + '-fanart.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + number + c_word + '-poster.jpg')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                img = Image.open(path + '/' + number + c_word + '-fanart.jpg')
                w = img.width
                h = img.height
                try:
                    img = img.convert('RGB')
                    img.save(path + '/' + number + c_word + '-poster.jpg')
                except:
                    img = img.convert('RGB')
                    img.save(path + '/' + number + c_word + '-poster.jpg')

    def pasteFileToFolder(self, filepath, path, number, c_word, config):  # 文件路径，番号，后缀，要移动至的位置
        houzhui = str(
            re.search('[.](AVI|RMVB|WMV|MOV|MP4|MKV|FLV|TS|avi|rmvb|wmv|mov|mp4|mkv|flv|ts)$', filepath).group())
        try:
            if config['common']['soft_link'] == '1':  # 如果soft_link=1 使用软链接
                os.symlink(filepath, path + '/' + number + c_word + houzhui)
            else:
                os.rename(filepath, path + '/' + number + c_word + houzhui)
            if os.path.exists(os.getcwd() + '/' + number + c_word + '.srt'):  # 字幕移动
                os.rename(os.getcwd() + '/' + number + c_word + '.srt', path + '/' + number + c_word + '.srt')
                self.add_text_main('[+]Sub moved!')
            elif os.path.exists(os.getcwd() + '/' + number + c_word + '.ssa'):
                os.rename(os.getcwd() + '/' + number + c_word + '.ssa', path + '/' + number + c_word + '.ssa')
                self.add_text_main('[+]Sub moved!')
            elif os.path.exists(os.getcwd() + '/' + number + c_word + '.sub'):
                os.rename(os.getcwd() + '/' + number + c_word + '.sub', path + '/' + number + c_word + '.sub')
                self.add_text_main('[+]Sub moved!')
        except FileExistsError:
            self.add_text_main('[-]File Exists! Please check your movie!')
            self.add_text_main('[-]move to the root folder of the program.')
            # os._exit(0)
        except PermissionError:
            self.add_text_main('[-]Error! Please run as administrator!')
            # os._exit(0)

    def pasteFileToFolder_mode2(self, filepath, path, multi_part, number, part, c_word, config):  # 文件路径，番号，后缀，要移动至的位置
        if multi_part == 1:
            number += part  # 这时number会被附加上CD1后缀
        houzhui = str(
            re.search('[.](AVI|RMVB|WMV|MOV|MP4|MKV|FLV|TS|avi|rmvb|wmv|mov|mp4|mkv|flv|ts)$', filepath).group())
        try:
            if config['common']['soft_link'] == '1':
                os.symlink(filepath, path + '/' + number + part + c_word + houzhui)
            else:
                os.rename(filepath, path + '/' + number + part + c_word + houzhui)
            if os.path.exists(number + '.srt'):  # 字幕移动
                os.rename(number + part + c_word + '.srt', path + '/' + number + part + c_word + '.srt')
                self.add_text_main('[+]Sub moved!')
            elif os.path.exists(number + part + c_word + '.ass'):
                os.rename(number + part + c_word + '.ass', path + '/' + number + part + c_word + '.ass')
                self.add_text_main('[+]Sub moved!')
            elif os.path.exists(number + part + c_word + '.sub'):
                os.rename(number + part + c_word + '.sub', path + '/' + number + part + c_word + '.sub')
                self.add_text_main('[+]Sub moved!')
            self.add_text_main('[!]Success')
        except FileExistsError:
            self.add_text_main('[-]File Exists! Please check your movie!')
            self.add_text_main('[-]move to the root folder of the program.')
            # os._exit(0)
        except PermissionError:
            self.add_text_main('[-]Error! Please run as administrator!')
            # os._exit(0)

    def get_part(self, filepath, failed_folder):
        try:
            if re.search('-CD\d+', filepath):
                return re.findall('-CD\d+', filepath)[0]
            if re.search('-cd\d+', filepath):
                return re.findall('-cd\d+', filepath)[0]
        except:
            self.add_text_main("[-]failed!Please rename the filename again!")
            self.moveFailedFolder(filepath, failed_folder)

    def debug_mode(self, json_data, config):  # 输出调试信息
        try:
            if config['debug_mode']['switch'] == '1':
                self.add_text_main('[+] ---Debug info---')
                for key, value in json_data.items():
                    if value == '' or key == 'actor_photo' or key == 'year' or key == 'imagecut':
                        continue
                    self.add_text_main('   [+]-' + "%-13s" % key + ': ' + str(value))
                self.add_text_main('[+] ---Debug info---')
        except:
            self.add_text_main('[-] ---Debug error---')

    def creatFolder(self, success_folder, json_data, Config):  # 创建文件夹
        location_rule = json_data['location_rule'].split('/')[-1].split('-')
        path = ''
        count = 0
        for rule in location_rule:
            if count == 0:
                path += json_data[rule]
            else:
                path += '-' + json_data[rule]
            count += 1
        if len(path) > 240:
            self.add_text_main('[-]Error in Length of Path! Repleaced with Number')
            path = json_data['number']
        path = success_folder + '/' + json_data['actor'] + '/' + path
        if not os.path.exists(path):
            path = escapePath(path, Config)
            try:
                os.makedirs(path)
            except:
                self.add_text_main('[-]Error in Makedir Path')
                return 'error'
        return path

    def core_main(self, file_path, number_th):
        # =======================================================================初始化所需变量
        multi_part = 0
        part = ''
        c_word = ''
        option = ''
        cn_sub = ''
        config_file = 'config.ini'
        Config = ConfigParser()
        Config.read(config_file, encoding='UTF-8')
        try:
            option = ReadMediaWarehouse(Config)
        except:
            self.add_text_main('[-]Config media_warehouse read failed!')
        program_mode = Config['common']['main_mode']  # 运行模式
        failed_folder = Config['common']['failed_output_folder']  # 失败输出目录
        success_folder = Config['common']['success_output_folder']  # 成功输出目录
        filepath = file_path  # 影片的路径
        number = number_th
        json_data = getDataFromJSON(number, filepath, failed_folder, Config)  # 定义番号
        self.debug_mode(json_data, Config)  # 调试模式检测
        imagecut = json_data['imagecut']
        tag = json_data['tag']
        if json_data['title'] == '' or number == '':
            self.add_text_main('[-]Movie Data not found!')
            self.moveFailedFolder(filepath, failed_folder)
        # =======================================================================判断-C,-CD后缀
        if '-CD' in filepath or '-cd' in filepath:
            multi_part = 1
            part = self.get_part(filepath, failed_folder)
        if '-c.' in filepath or '-C.' in filepath or '中文' in filepath or '字幕' in filepath:
            cn_sub = '1'
            c_word = '-C'  # 中文字幕影片后缀

        self.CreatFailedFolder(failed_folder)  # 创建输出失败目录
        path = self.creatFolder(success_folder, json_data, Config)  # 创建文件夹
        if path == 'error':
            self.add_text_main('[-]Move ' + file_path + ' to failed folder')
            shutil.move(file_path, str(os.getcwd()) + '/' + 'failed/')
            return
        self.add_text_main('[+]Folder : ' + path)
        # =======================================================================刮削模式
        if program_mode == '1':
            if multi_part == 1:
                number += part  # 这时number会被附加上CD1后缀
            self.smallCoverCheck(path, number, imagecut, json_data['cover_small'], c_word, option, Config, filepath,
                                 failed_folder)  # 检查小封面
            self.imageDownload(option, json_data['cover'], number, c_word, path, multi_part, Config, filepath,
                               failed_folder)  # creatFoder会返回番号路径
            self.cutImage(option, imagecut, path, number, c_word)  # 裁剪图
            copyRenameJpgToBackdrop(option, path, number, c_word)
            self.PrintFiles(option, path, c_word, json_data['naming_rule'], part, cn_sub, json_data, filepath,
                            failed_folder,
                            tag)  # 打印文件
            self.pasteFileToFolder(filepath, path, number, c_word, Config)  # 移动文件
            # =======================================================================整理模式
        elif program_mode == '2':
            self.pasteFileToFolder_mode2(filepath, path, multi_part, number, part, c_word, Config)  # 移动文件

    # ========================================================================AVDC刮削主功能
    def UpdateCheck(self, version):
        if self.Ui.radioButton_update_on.isChecked():
            check = 1
        else:
            check = 0
        if UpdateCheckSwitch(check) == '1':
            html2 = get_html('https://raw.githubusercontent.com/moyy996/AVDC/master/update_check.json')
            html = json.loads(str(html2))

            if float(version) < float(html['version']):
                self.add_text_main('[*]                  * New update ' + html['version'] + ' *')
                self.add_text_main('[*]                     ↓ Download ↓')
                self.add_text_main('[*] ' + html['download'])
                self.add_text_main('[*]======================================================')

    def CreatFailedFolder(self, failed_folder):
        if not os.path.exists(failed_folder + '/'):  # 新建failed文件夹
            try:
                os.makedirs(failed_folder + '/')
            except:
                self.add_text_main("[-]failed!can not be make Failed output folder\n[-](Please run as Administrator)")
                # os._exit(0)

    def CEF(self, path):
        try:
            files = os.listdir(path)  # 获取路径下的子文件(夹)列表
            for file in files:
                os.removedirs(path + '/' + file)  # 删除这个空文件夹
                self.add_text_main('[+]Deleting empty folder' + path + '/' + file)
        except:
            self.add_text_main('[+]Deleting empty folder error!')

    def AVDC_Main(self):
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        success_folder = config['common']['success_output_folder']
        failed_folder = config['common']['failed_output_folder']  # 失败输出目录
        escape_folder = config['escape']['folders']  # 多级目录刮削需要排除的目录

        self.CreatFailedFolder(failed_folder)
        os.chdir(os.getcwd())
        movie_list = movie_lists(escape_folder)

        count = 0
        count_all = str(len(movie_list))
        self.add_text_main('[+]Find ' + count_all + ' movies')
        if config['common']['soft_link'] == '1':
            self.add_text_main('[!] --- Soft link mode is ENABLE! ----')
        for movie in movie_list:  # 遍历电影列表 交给core处理
            count = count + 1
            percentage = str(count / int(count_all) * 100)[:4] + '%'
            self.add_text_main('[!] - ' + percentage + ' [' + str(count) + '/' + count_all + '] -')
            try:
                self.add_text_main("[!]Making Data for   [" + movie + "], the number is [" + getNumber(movie) + "]")
                self.core_main(movie, getNumber(movie))
                self.add_text_main("[*]======================================================")
            except:  # 番号提取异常
                self.add_text_main('[-]' + movie + ' Cannot catch the number :')
                curr_path = str(os.getcwd()).replace('\\', '/')
                if config['common']['soft_link'] == '1':
                    self.add_text_main('[-]Link ' + movie + ' to failed folder')
                    try:
                        os.symlink(movie, curr_path + '/' + 'failed/')
                    except:
                        self.add_text_main('[-]Link ' + movie + ' failed! Please run as Administrator!')
                else:
                    self.add_text_main('[-]Move ' + movie + ' to failed folder')
                    shutil.move(movie, curr_path + '/' + 'failed/')
                continue
        self.CEF(success_folder)
        self.CEF(failed_folder)
        self.add_text_main("[+]All finished!!!")


if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    ui = MyMAinWindow()
    ui.show()
    sys.exit(app.exec_())
