#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import json
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTextCursor, QCursor
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QApplication
from PyQt5.QtCore import pyqtSignal, Qt
import sys
import time
import os.path
import requests
import shutil
import base64
import re
from aip import AipBodyAnalysis
from PIL import Image, ImageFilter
import os
from configparser import ConfigParser
from Ui.AVDC import Ui_AVDV
from Function.Function import save_config, movie_lists, get_info, getDataFromJSON, escapePath, getNumber, check_pic
from Function.getHtml import get_html, get_proxies, get_config


class MyMAinWindow(QMainWindow, Ui_AVDV):
    progressBarValue = pyqtSignal(int)  # 进度条信号量

    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.Ui = Ui_AVDV()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.Init_Ui()
        self.set_style()
        # 初始化需要的变量
        self.version = '3.964'
        self.m_drag = False
        self.m_DragPosition = 0
        self.count_claw = 0  # 批量刮削次数
        self.item_succ = self.Ui.treeWidget_number.topLevelItem(0)
        self.item_fail = self.Ui.treeWidget_number.topLevelItem(1)
        self.select_file_path = ''
        self.json_array = {}
        self.Init()
        self.Load_Config()
        self.show_version()
        # ========================================================================打开日志文件
        if self.Ui.radioButton_log_on.isChecked():
            if not os.path.exists('Log'):
                os.makedirs('Log')
            log_name = 'Log/' + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + '.txt'
            self.log_txt = open(log_name, "wb", buffering=0)
            self.add_text_main('[-]Created log file: ' + log_name)
            self.add_text_main("[*]======================================================")

    def Init_Ui(self):
        ico_path = ''
        if os.path.exists('AVDC-ico.png'):
            ico_path = 'AVDC-ico.png'
        elif os.path.exists('Img/AVDC-ico.png'):
            ico_path = 'Img/AVDC-ico.png'
        pix = QPixmap(ico_path)
        self.Ui.label_ico.setScaledContents(True)
        self.Ui.label_ico.setPixmap(pix)  # 添加图标
        self.Ui.progressBar_avdc.setValue(0)  # 进度条清0
        self.progressBarValue.connect(self.set_processbar)
        self.Ui.progressBar_avdc.setTextVisible(False)  # 不显示进度条文字
        self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.Ui.treeWidget_number.expandAll()

    def set_style(self):
        # 控件美化
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
            * {
                    font-size:15px;
            }            
            QWidget#centralwidget{
                    background:gray;
                    border:1px solid gray;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }            
            QTextBrowser{
                    border:1px solid gray;
                    background:white;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }
            QLineEdit{
                    background:white;
                    border:1px solid gray;
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
            QPushButton#pushButton_start_cap,#pushButton_move_mp4,#pushButton_select_file,#pushButton_select_thumb{
                    font-size:20px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_add_actor_pic,#pushButton_start_single_file{
                    font-size:20px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_save_config,#pushButton_show_pic_actor,#pushButton_init_config{
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:13px;
                    padding:2px 4px;
            }
            QProgressBar::chunk{
                    background-color: #2196F3;
                    width: 5px; /*区块宽度*/
                    margin: 0.5px;
            }
            ''')

    # ========================================================================按钮点击事件
    def Init(self):
        self.Ui.stackedWidget.setCurrentIndex(0)
        self.Ui.treeWidget_number.clicked.connect(self.treeWidget_number_clicked)
        self.Ui.pushButton_close.clicked.connect(self.close_win)
        self.Ui.pushButton_min.clicked.connect(self.min_win)
        self.Ui.pushButton_main.clicked.connect(self.pushButton_main_clicked)
        self.Ui.pushButton_tool.clicked.connect(self.pushButton_tool_clicked)
        self.Ui.pushButton_setting.clicked.connect(self.pushButton_setting_clicked)
        self.Ui.pushButton_select_file.clicked.connect(self.pushButton_select_file_clicked)
        self.Ui.pushButton_about.clicked.connect(self.pushButton_about_clicked)
        self.Ui.pushButton_start_cap.clicked.connect(self.pushButton_start_cap_clicked)
        self.Ui.pushButton_save_config.clicked.connect(self.pushButton_save_config_clicked)
        self.Ui.pushButton_init_config.clicked.connect(self.pushButton_init_config_clicked)
        self.Ui.pushButton_move_mp4.clicked.connect(self.move_file)
        self.Ui.pushButton_add_actor_pic.clicked.connect(self.pushButton_add_actor_pic_clicked)
        self.Ui.pushButton_show_pic_actor.clicked.connect(self.pushButton_show_pic_actor_clicked)
        self.Ui.pushButton_select_thumb.clicked.connect(self.pushButton_select_thumb_clicked)
        self.Ui.pushButton_log.clicked.connect(self.pushButton_show_log_clicked)
        self.Ui.pushButton_start_single_file.clicked.connect(self.pushButton_start_single_file_clicked)
        self.Ui.checkBox_cover.stateChanged.connect(self.cover_change)
        self.Ui.horizontalSlider_timeout.valueChanged.connect(self.lcdNumber_timeout_change)
        self.Ui.horizontalSlider_retry.valueChanged.connect(self.lcdNumber_retry_change)
        self.Ui.horizontalSlider_mark_size.valueChanged.connect(self.lcdNumber_mark_size_change)

    # ========================================================================显示版本号
    def show_version(self):
        self.Ui.textBrowser_log_main.append('[*]======================== AVDC ========================')
        self.Ui.textBrowser_log_main.append('[*]                     Version ' + self.version)
        self.Ui.textBrowser_log_main.append('[*]======================================================')

    # ========================================================================鼠标拖动窗口
    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 按下左键改变鼠标指针样式为手掌

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
            self.setCursor(QCursor(Qt.ArrowCursor))  # 释放左键改变鼠标指针样式为箭头

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

    def pushButton_show_log_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(4)

    def lcdNumber_timeout_change(self):
        timeout = self.Ui.horizontalSlider_timeout.value()
        self.Ui.lcdNumber_timeout.display(timeout)

    def lcdNumber_retry_change(self):
        retry = self.Ui.horizontalSlider_retry.value()
        self.Ui.lcdNumber_retry.display(retry)

    def lcdNumber_mark_size_change(self):
        mark_size = self.Ui.horizontalSlider_mark_size.value()
        self.Ui.lcdNumber_mark_size.display(mark_size)

    def cover_change(self):
        if not self.Ui.checkBox_cover.isChecked():
            self.Ui.label_poster.setText("封面图")
            self.Ui.label_thumb.setText("缩略图")

    def treeWidget_number_clicked(self, qmodeLindex):
        item = self.Ui.treeWidget_number.currentItem()
        if item.text(0) != '成功' and item.text(0) != '失败':
            try:
                index_json = str(item.text(0)).split('.')[0]
                self.add_label_info(self.json_array[str(index_json)])
            except:
                print(item.text(0) + ': No info!')

    def pushButton_start_cap_clicked(self):
        self.Ui.pushButton_start_cap.setEnabled(False)
        self.progressBarValue.emit(int(0))
        try:
            self.count_claw += 1
            t = threading.Thread(target=self.AVDC_Main)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_start_cap_clicked: ' + str(error_info))

    # ========================================================================恢复默认config.ini
    def pushButton_init_config_clicked(self):
        try:
            t = threading.Thread(target=self.init_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_save_config_clicked: ' + str(error_info))

    def init_config_clicked(self):
        json_config = {
            'show_poster': 1,
            'main_mode': 1,
            'soft_link': 0,
            'switch_debug': 1,
            'failed_file_move': 1,
            'update_check': 1,
            'save_log': 1,
            'website': 'all',
            'failed_output_folder': 'failed',
            'success_output_folder': 'JAV_output',
            'proxy': '',
            'timeout': 7,
            'retry': 3,
            'folder_name': 'actor/number-title-release',
            'naming_media': 'number-title',
            'naming_file': 'number',
            'literals': '\()',
            'folders': 'failed,JAV_output',
            'string': '1080p,720p,22-sht.me,-HD',
            'emby_url': 'localhost:8096',
            'api_key': '',
            'media_path': 'E:/TEMP',
            'media_type': '.mp4|.avi|.rmvb|.wmv|.mov|.mkv|.flv|.ts|.webm|.MP4|.AVI|.RMVB|.WMV|.MOV|.MKV|.FLV|.TS|.WEBM',
            'sub_type': '.smi|.srt|.idx|.sub|.sup|.psb|.ssa|.ass|.txt|.usf|.xss|.ssf|.rt|.lrc|.sbv|.vtt|.ttml',
            'poster_mark': 1,
            'thumb_mark': 1,
            'mark_size': 3,
            'mark_type': 'SUB,LEAK,UNCENSORED',
            'mark_pos': 'top_left',
            'uncensored_poster': 0,
            'uncensored_prefix': 'S2M|BT|LAF|SMD',
            'nfo_download': 1,
            'poster_download': 1,
            'fanart_download': 1,
            'thumb_download': 1,
            'extrafanart_download': 0,
            'extrafanart_folder': 'extrafanart',
        }
        save_config(json_config)
        self.Load_Config()

    # ========================================================================加载config
    def Load_Config(self):
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        # ========================================================================common
        if int(config['common']['main_mode']) == 1:
            self.Ui.radioButton_common.setChecked(True)
        elif int(config['common']['main_mode']) == 2:
            self.Ui.radioButton_sort.setChecked(True)
        if int(config['common']['soft_link']) == 1:
            self.Ui.radioButton_soft_on.setChecked(True)
        elif int(config['common']['soft_link']) == 0:
            self.Ui.radioButton_soft_off.setChecked(True)
        if int(config['common']['failed_file_move']) == 1:
            self.Ui.radioButton_fail_move_on.setChecked(True)
        elif int(config['common']['failed_file_move']) == 0:
            self.Ui.radioButton_fail_move_off.setChecked(True)
        if int(config['common']['show_poster']) == 1:
            self.Ui.checkBox_cover.setChecked(True)
        elif int(config['common']['show_poster']) == 0:
            self.Ui.checkBox_cover.setChecked(False)
        if config['common']['website'] == 'all':
            self.Ui.comboBox_website_all.setCurrentIndex(0)
        elif config['common']['website'] == 'mgstage':
            self.Ui.comboBox_website_all.setCurrentIndex(1)
        elif config['common']['website'] == 'javbus':
            self.Ui.comboBox_website_all.setCurrentIndex(2)
        elif config['common']['website'] == 'jav321':
            self.Ui.comboBox_website_all.setCurrentIndex(3)
        elif config['common']['website'] == 'javdb':
            self.Ui.comboBox_website_all.setCurrentIndex(4)
        elif config['common']['website'] == 'avsox':
            self.Ui.comboBox_website_all.setCurrentIndex(5)
        elif config['common']['website'] == 'xcity':
            self.Ui.comboBox_website_all.setCurrentIndex(6)
        elif config['common']['website'] == 'dmm':
            self.Ui.comboBox_website_all.setCurrentIndex(7)
        self.Ui.lineEdit_success.setText(config['common']['success_output_folder'])
        self.Ui.lineEdit_fail.setText(config['common']['failed_output_folder'])
        # ========================================================================proxy
        if config['proxy']['type'] == 'no' or config['proxy']['type'] == '':
            self.Ui.radioButton_proxy_nouse.setChecked(True)
        elif config['proxy']['type'] == 'http':
            self.Ui.radioButton_proxy_http.setChecked(True)
        elif config['proxy']['type'] == 'socks5':
            self.Ui.radioButton_proxy_socks5.setChecked(True)
        self.Ui.lineEdit_proxy.setText(config['proxy']['proxy'])
        self.Ui.horizontalSlider_timeout.setValue(int(config['proxy']['timeout']))
        self.Ui.horizontalSlider_retry.setValue(int(config['proxy']['retry']))
        # ========================================================================Name_Rule
        self.Ui.lineEdit_dir_name.setText(config['Name_Rule']['folder_name'])
        self.Ui.lineEdit_media_name.setText(config['Name_Rule']['naming_media'])
        self.Ui.lineEdit_local_name.setText(config['Name_Rule']['naming_file'])
        # ========================================================================update
        if int(config['update']['update_check']) == 1:
            self.Ui.radioButton_update_on.setChecked(True)
        elif int(config['update']['update_check']) == 0:
            self.Ui.radioButton_update_off.setChecked(True)
        # ========================================================================log
        if int(config['log']['save_log']) == 1:
            self.Ui.radioButton_log_on.setChecked(True)
        elif int(config['log']['save_log']) == 0:
            self.Ui.radioButton_log_off.setChecked(True)
        # ========================================================================media
        self.Ui.lineEdit_movie_type.setText(config['media']['media_type'])
        self.Ui.lineEdit_sub_type.setText(config['media']['sub_type'])
        self.Ui.lineEdit_movie_path.setText(str(config['media']['media_path']).replace('\\', '/'))
        # ========================================================================escape
        self.Ui.lineEdit_escape_dir.setText(config['escape']['folders'])
        self.Ui.lineEdit_escape_char.setText(config['escape']['literals'])
        self.Ui.lineEdit_escape_dir_move.setText(config['escape']['folders'])
        self.Ui.lineEdit_escape_string.setText(config['escape']['string'])
        # ========================================================================debug_mode
        if int(config['debug_mode']['switch']) == 1:
            self.Ui.radioButton_debug_on.setChecked(True)
        elif int(config['debug_mode']['switch']) == 0:
            self.Ui.radioButton_debug_off.setChecked(True)
        # ========================================================================emby
        self.Ui.lineEdit_emby_url.setText(config['emby']['emby_url'])
        self.Ui.lineEdit_api_key.setText(config['emby']['api_key'])
        # ========================================================================mark
        if int(config['mark']['poster_mark']) == 1:
            self.Ui.radioButton_poster_mark_on.setChecked(True)
        elif int(config['mark']['poster_mark']) == 0:
            self.Ui.radioButton_poster_mark_off.setChecked(True)
        if int(config['mark']['thumb_mark']) == 1:
            self.Ui.radioButton_thumb_mark_on.setChecked(True)
        elif int(config['mark']['thumb_mark']) == 0:
            self.Ui.radioButton_thumb_mark_off.setChecked(True)
        self.Ui.horizontalSlider_mark_size.setValue(int(config['mark']['mark_size']))
        if 'SUB' in str(config['mark']['mark_type']).upper():
            self.Ui.checkBox_sub.setChecked(True)
        if 'LEAK' in str(config['mark']['mark_type']).upper():
            self.Ui.checkBox_leak.setChecked(True)
        if 'UNCENSORED' in str(config['mark']['mark_type']).upper():
            self.Ui.checkBox_uncensored.setChecked(True)
        if 'top_left' == config['mark']['mark_pos']:
            self.Ui.radioButton_top_left.setChecked(True)
        elif 'bottom_left' == config['mark']['mark_pos']:
            self.Ui.radioButton_bottom_left.setChecked(True)
        elif 'top_right' == config['mark']['mark_pos']:
            self.Ui.radioButton_top_right.setChecked(True)
        elif 'bottom_right' == config['mark']['mark_pos']:
            self.Ui.radioButton_bottom_right.setChecked(True)
        # ========================================================================uncensored
        if int(config['uncensored']['uncensored_poster']) == 1:
            self.Ui.radioButton_poster_cut.setChecked(True)
        elif int(config['uncensored']['uncensored_poster']) == 0:
            self.Ui.radioButton_poster_official.setChecked(True)
        self.Ui.lineEdit_uncensored_prefix.setText(config['uncensored']['uncensored_prefix'])
        # ========================================================================file_download
        if int(config['file_download']['nfo']) == 1:
            self.Ui.checkBox_download_nfo.setChecked(True)
        elif int(config['file_download']['nfo']) == 0:
            self.Ui.checkBox_download_nfo.setChecked(False)
        if int(config['file_download']['poster']) == 1:
            self.Ui.checkBox_download_poster.setChecked(True)
        elif int(config['file_download']['poster']) == 0:
            self.Ui.checkBox_download_poster.setChecked(False)
        if int(config['file_download']['fanart']) == 1:
            self.Ui.checkBox_download_fanart.setChecked(True)
        elif int(config['file_download']['fanart']) == 0:
            self.Ui.checkBox_download_fanart.setChecked(False)
        if int(config['file_download']['thumb']) == 1:
            self.Ui.checkBox_download_thumb.setChecked(True)
        elif int(config['file_download']['thumb']) == 0:
            self.Ui.checkBox_download_thumb.setChecked(False)
        # ========================================================================extrafanart
        if int(config['extrafanart']['extrafanart_download']) == 1:
            self.Ui.radioButton_extrafanart_download_on.setChecked(True)
        elif int(config['extrafanart']['extrafanart_download']) == 0:
            self.Ui.radioButton_extrafanart_download_off.setChecked(True)
        self.Ui.lineEdit_extrafanart_dir.setText(config['extrafanart']['extrafanart_folder'])

    # ========================================================================读取设置页设置，保存在config.ini
    def pushButton_save_config_clicked(self):
        try:
            t = threading.Thread(target=self.save_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_save_config_clicked: ' + str(error_info))

    def save_config_clicked(self):
        main_mode = 1
        failed_file_move = 1
        soft_link = 0
        show_poster = 0
        switch_debug = 0
        update_check = 0
        save_log = 0
        website = ''
        add_mark = 1
        mark_size = 3
        mark_type = ''
        mark_pos = ''
        uncensored_poster = 0
        nfo_download = 0
        poster_download = 0
        fanart_download = 0
        thumb_download = 0
        extrafanart_download = 0
        extrafanart_folder = ''
        proxy_type = ''
        # ========================================================================common
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
        if self.Ui.radioButton_log_on.isChecked():  # 开启日志
            save_log = 1
        elif self.Ui.radioButton_log_off.isChecked():  # 关闭日志
            save_log = 0
        if self.Ui.checkBox_cover.isChecked():  # 显示封面
            show_poster = 1
        else:  # 关闭封面
            show_poster = 0
        if self.Ui.radioButton_fail_move_on.isChecked():  # 失败移动开
            failed_file_move = 1
        elif self.Ui.radioButton_fail_move_off.isChecked():  # 失败移动关
            failed_file_move = 0
        if self.Ui.comboBox_website_all.currentText() == 'All websites':  # all
            website = 'all'
        elif self.Ui.comboBox_website_all.currentText() == 'mgstage':  # mgstage
            website = 'mgstage'
        elif self.Ui.comboBox_website_all.currentText() == 'javbus':  # javbus
            website = 'javbus'
        elif self.Ui.comboBox_website_all.currentText() == 'jav321':  # jav321
            website = 'jav321'
        elif self.Ui.comboBox_website_all.currentText() == 'javdb':  # javdb
            website = 'javdb'
        elif self.Ui.comboBox_website_all.currentText() == 'avsox':  # avsox
            website = 'avsox'
        elif self.Ui.comboBox_website_all.currentText() == 'xcity':  # xcity
            website = 'xcity'
        elif self.Ui.comboBox_website_all.currentText() == 'dmm':  # dmm
            website = 'dmm'
        # ========================================================================proxy
        if self.Ui.radioButton_proxy_http.isChecked():  # http proxy
            proxy_type = 'http'
        elif self.Ui.radioButton_proxy_socks5.isChecked():  # socks5 proxy
            proxy_type = 'socks5'
        elif self.Ui.radioButton_proxy_nouse.isChecked():  # nouse proxy
            proxy_type = 'no'
        # ========================================================================水印
        if self.Ui.radioButton_poster_mark_on.isChecked():  # 封面添加水印
            poster_mark = 1
        else:  # 关闭封面添加水印
            poster_mark = 0
        if self.Ui.radioButton_thumb_mark_on.isChecked():  # 缩略图添加水印
            thumb_mark = 1
        else:  # 关闭缩略图添加水印
            thumb_mark = 0
        if self.Ui.checkBox_sub.isChecked():  # 字幕
            mark_type += ',SUB'
        if self.Ui.checkBox_leak.isChecked():  # 流出
            mark_type += ',LEAK'
        if self.Ui.checkBox_uncensored.isChecked():  # 无码
            mark_type += ',UNCENSORED'
        if self.Ui.radioButton_top_left.isChecked():  # 左上
            mark_pos = 'top_left'
        elif self.Ui.radioButton_bottom_left.isChecked():  # 左下
            mark_pos = 'bottom_left'
        elif self.Ui.radioButton_top_right.isChecked():  # 右上
            mark_pos = 'top_right'
        elif self.Ui.radioButton_bottom_right.isChecked():  # 右下
            mark_pos = 'bottom_right'
        if self.Ui.radioButton_poster_official.isChecked():  # 官方
            uncensored_poster = 0
        elif self.Ui.radioButton_poster_cut.isChecked():  # 裁剪
            uncensored_poster = 1
        # ========================================================================下载文件，剧照
        if self.Ui.checkBox_download_nfo.isChecked():
            nfo_download = 1
        else:
            nfo_download = 0
        if self.Ui.checkBox_download_poster.isChecked():
            poster_download = 1
        else:
            poster_download = 0
        if self.Ui.checkBox_download_fanart.isChecked():
            fanart_download = 1
        else:
            fanart_download = 0
        if self.Ui.checkBox_download_thumb.isChecked():
            thumb_download = 1
        else:
            thumb_download = 0
        if self.Ui.radioButton_extrafanart_download_on.isChecked():  # 下载剧照
            extrafanart_download = 1
        else:  # 关闭封面
            extrafanart_download = 0
        json_config = {
            'main_mode': main_mode,
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'show_poster': show_poster,
            'failed_file_move': failed_file_move,
            'update_check': update_check,
            'save_log': save_log,
            'website': website,
            'failed_output_folder': self.Ui.lineEdit_fail.text(),
            'success_output_folder': self.Ui.lineEdit_success.text(),
            'type': proxy_type,
            'proxy': self.Ui.lineEdit_proxy.text(),
            'timeout': self.Ui.horizontalSlider_timeout.value(),
            'retry': self.Ui.horizontalSlider_retry.value(),
            'folder_name': self.Ui.lineEdit_dir_name.text(),
            'naming_media': self.Ui.lineEdit_media_name.text(),
            'naming_file': self.Ui.lineEdit_local_name.text(),
            'literals': self.Ui.lineEdit_escape_char.text(),
            'folders': self.Ui.lineEdit_escape_dir.text(),
            'string': self.Ui.lineEdit_escape_string.text(),
            'emby_url': self.Ui.lineEdit_emby_url.text(),
            'api_key': self.Ui.lineEdit_api_key.text(),
            'media_path': self.Ui.lineEdit_movie_path.text(),
            'media_type': self.Ui.lineEdit_movie_type.text(),
            'sub_type': self.Ui.lineEdit_sub_type.text(),
            'poster_mark': poster_mark,
            'thumb_mark': thumb_mark,
            'mark_size': self.Ui.horizontalSlider_mark_size.value(),
            'mark_type': mark_type.strip(','),
            'mark_pos': mark_pos,
            'uncensored_poster': uncensored_poster,
            'uncensored_prefix': self.Ui.lineEdit_uncensored_prefix.text(),
            'nfo_download': nfo_download,
            'poster_download': poster_download,
            'fanart_download': fanart_download,
            'thumb_download': thumb_download,
            'extrafanart_download': extrafanart_download,
            'extrafanart_folder': self.Ui.lineEdit_extrafanart_dir.text(),
        }
        save_config(json_config)

    # ========================================================================小工具-单视频刮削
    def pushButton_select_file_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        filepath, filetype = QtWidgets.QFileDialog.getOpenFileName(self, "选取视频文件", path, "Movie Files(*.mp4 "
                                                                                         "*.avi *.rmvb *.wmv "
                                                                                         "*.mov *.mkv *.flv *.ts "
                                                                                         "*.webm *.MP4 *.AVI "
                                                                                         "*.RMVB *.WMV *.MOV "
                                                                                         "*.MKV *.FLV *.TS "
                                                                                         "*.WEBM);;All Files(*)")
        self.select_file_path = filepath

    def pushButton_start_single_file_clicked(self):
        if self.select_file_path != '':
            self.Ui.stackedWidget.setCurrentIndex(0)
            try:
                t = threading.Thread(target=self.select_file_thread)
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_start_single_file_clicked: ' + str(error_info))

    def select_file_thread(self):
        file_name = self.select_file_path
        file_root = os.getcwd().replace("\\\\", "/").replace("\\", "/")
        file_path = file_name.replace(file_root, '.').replace("\\\\", "/").replace("\\", "/")
        # 获取去掉拓展名的文件名做为番号
        file_name = os.path.splitext(file_name.split('/')[-1])[0]
        mode = self.Ui.comboBox_website.currentIndex() + 1
        # 指定的网址
        appoint_url = self.Ui.lineEdit_appoint_url.text()
        appoint_number = self.Ui.lineEdit_movie_number.text()
        try:
            if appoint_number:
                file_name = appoint_number
            else:
                if '-CD' in file_name or '-cd' in file_name:
                    part = ''
                    if re.search('-CD\d+', file_name):
                        part = re.findall('-CD\d+', file_name)[0]
                    elif re.search('-cd\d+', file_name):
                        part = re.findall('-cd\d+', file_name)[0]
                    file_name = file_name.replace(part, '')
                if '-c.' in file_path or '-C.' in file_path:
                    file_name = file_name[0:-2]
            self.add_text_main("[!]Making Data for   [" + file_path + "], the number is [" + file_name + "]")
            self.Core_Main(file_path, file_name, mode, 0, appoint_url)
        except Exception as error_info:
            self.add_text_main('[-]Error in select_file_thread: ' + str(error_info))
        self.add_text_main("[*]======================================================")

    # ========================================================================小工具-裁剪封面图
    def pushButton_select_thumb_clicked(self):
        path = self.Ui.lineEdit_movie_path.text()
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取缩略图", path,
                                                                   "Picture Files(*.jpg);;All Files(*)")
        if filePath != '':
            self.Ui.stackedWidget.setCurrentIndex(0)
            try:
                t = threading.Thread(target=self.select_thumb_thread, args=(filePath,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_select_thumb_clicked: ' + str(error_info))

    def select_thumb_thread(self, file_path):
        file_name = file_path.split('/')[-1]
        file_path = file_path.replace('/' + file_name, '')
        self.image_cut(file_path, file_name, 2)
        self.add_text_main("[*]======================================================")

    def image_cut(self, path, file_name, mode=1):
        png_name = file_name.replace('-thumb.jpg', '-poster.jpg')
        file_path = os.path.join(path, file_name)
        png_path = os.path.join(path, png_name)
        try:
            if os.path.exists(png_path):
                os.remove(png_path)
        except Exception as error_info:
            self.add_text_main('[-]Error in image_cut: ' + str(error_info))
            return

        """ 你的 APPID AK SK """
        APP_ID = '17013175'
        API_KEY = 'IQs1mkG4FerdtmNh6qKDI4fW'
        SECRET_KEY = 'dLr9GTqqutqP9nWKKRaEinVDhxYlPbnD'

        client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

        """ 获取图片分辨率 """
        im = Image.open(file_path)  # 返回一个Image对象
        width, height = im.size

        """ 读取图片 """
        with open(file_path, 'rb') as fp:
            image = fp.read()
        ex, ey, ew, eh = 0, 0, 0, 0
        """ 获取裁剪区域 """
        if height / width <= 1.5:  # 长宽比大于1.5，太宽
            """ 调用人体检测与属性识别 """
            result = client.bodyAnalysis(image)
            ewidth = int(height / 1.5)
            ex = int(result["person_info"][0]['body_parts']['nose']['x'])
            if width - ex < ewidth / 2:
                ex = width - ewidth
            else:
                ex -= int(ewidth / 2)
            if ex < 0:
                ex = 0
            ey = 0
            eh = height
            if ewidth > width:
                ew = width
            else:
                ew = ewidth
        elif height / width > 1.5:  # 长宽比小于1.5，太窄
            ex = 0
            ey = 0
            ew = int(width)
            eh = ew * 1.5
        fp = open(file_path, 'rb')
        img = Image.open(fp)
        img_new_png = img.crop((ex, ey, ew + ex, eh + ey))
        fp.close()
        img_new_png.save(png_path)
        self.add_text_main('[+]Poster Cut         ' + png_name + ' from ' + file_name + '!')
        if mode == 2:
            pix = QPixmap(file_path)
            self.Ui.label_thumb.setScaledContents(True)
            self.Ui.label_thumb.setPixmap(pix)  # 添加图标
            pix = QPixmap(png_path)
            self.Ui.label_poster.setScaledContents(True)
            self.Ui.label_poster.setPixmap(pix)  # 添加图标

    # ========================================================================小工具-视频移动
    def move_file(self):
        self.Ui.stackedWidget.setCurrentIndex(4)
        try:
            t = threading.Thread(target=self.move_file_thread)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in move_file: ' + str(error_info))

    def move_file_thread(self):
        escape_dir = self.Ui.lineEdit_escape_dir_move.text()
        sub_type = self.Ui.lineEdit_sub_type.text().split('|')
        movie_path = self.Ui.lineEdit_movie_path.text()
        movie_type = self.Ui.lineEdit_movie_type.text()
        movie_list = movie_lists(escape_dir, movie_type, movie_path)
        des_path = movie_path + '/Movie_moved'
        if not os.path.exists(des_path):
            self.add_text_main('[+]Created folder Movie_moved!')
            os.makedirs(des_path)
        self.add_text_main('[+]Move Movies Start!')
        for movie in movie_list:
            if des_path in movie:
                continue
            sour = movie
            des = des_path + '/' + sour.split('/')[-1]
            try:
                shutil.move(sour, des)
                self.add_text_main('   [+]Move ' + sour.split('/')[-1] + ' to Movie_moved Success!')
                path_old = sour.replace(sour.split('/')[-1], '')
                filename = sour.split('/')[-1].split('.')[0]
                for sub in sub_type:
                    if os.path.exists(path_old + '/' + filename + sub):  # 字幕移动
                        shutil.move(path_old + '/' + filename + sub, des_path + '/' + filename + sub)
                        self.add_text_main('   [+]Sub moved! ' + filename + sub)
            except Exception as error_info:
                self.add_text_main('[-]Error in move_file_thread: ' + str(error_info))
        self.add_text_main("[+]Move Movies All Finished!!!")
        self.add_text_main("[*]======================================================")

    # ========================================================================小工具-emby女优头像
    def pushButton_add_actor_pic_clicked(self):  # 添加头像按钮响应
        self.Ui.stackedWidget.setCurrentIndex(4)
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.add_text_main('[-]The emby_url is empty!')
            self.add_text_main("[*]======================================================")
            return
        elif api_key == '':
            self.add_text_main('[-]The api_key is empty!')
            self.add_text_main("[*]======================================================")
            return
        try:
            t = threading.Thread(target=self.found_profile_picture, args=(1,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_add_actor_pic_clicked: ' + str(error_info))

    def pushButton_show_pic_actor_clicked(self):  # 查看按钮响应
        self.Ui.stackedWidget.setCurrentIndex(4)
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        if emby_url == '':
            self.add_text_main('[-]The emby_url is empty!')
            self.add_text_main("[*]======================================================")
            return
        elif api_key == '':
            self.add_text_main('[-]The api_key is empty!')
            self.add_text_main("[*]======================================================")
            return
        if self.Ui.comboBox_pic_actor.currentIndex() == 0:  # 可添加头像的女优
            try:
                t = threading.Thread(target=self.found_profile_picture, args=(2,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_show_pic_actor_clicked: ' + str(error_info))
        else:
            try:
                t = threading.Thread(target=self.show_actor, args=(self.Ui.comboBox_pic_actor.currentIndex(),))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_show_pic_actor_clicked: ' + str(error_info))

    def show_actor(self, mode):  # 按模式显示相应列表
        if mode == 1:  # 没有头像的女优
            self.add_text_main('[+]没有头像的女优!')
        elif mode == 2:  # 有头像的女优
            self.add_text_main('[+]有头像的女优!')
        elif mode == 3:  # 所有女优
            self.add_text_main('[+]所有女优!')
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.add_text_main("[*]======================================================")
            return
        count = 1
        actor_list_temp = ''
        for actor in actor_list['Items']:
            if mode == 3:  # 所有女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 2 and actor['ImageTags'] != {}:  # 有头像的女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            elif mode == 1 and actor['ImageTags'] == {}:  # 没有头像的女优
                actor_list_temp += str(count) + '.' + actor['Name'] + ','
                count += 1
            if (count - 1) % 5 == 0 and actor_list_temp != '':
                self.add_text_main('[+]' + actor_list_temp)
                actor_list_temp = ''
        self.add_text_main("[*]======================================================")

    def get_emby_actor_list(self):  # 获取emby的演员列表
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':')
        url = 'http://' + emby_url + '/emby/Persons?api_key=' + api_key
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/60.0.3100.0 Safari/537.36'}
        actor_list = {}
        try:
            getweb = requests.get(str(url), headers=headers, timeout=10)
            getweb.encoding = 'utf-8'
            actor_list = json.loads(getweb.text)
        except:
            self.add_text_main('[-]Error! Check your emby_url or api_key!')
            actor_list['TotalRecordCount'] = 0
        return actor_list

    def found_profile_picture(self, mode):  # mode=1，上传头像，mode=2，显示可添加头像的女优
        if mode == 1:
            self.add_text_main('[+]Start upload profile pictures!')
        elif mode == 2:
            self.add_text_main('[+]可添加头像的女优!')
        path = 'Actor'
        if not os.path.exists(path):
            self.add_text_main('[+]Actor folder not exist!')
            self.add_text_main("[*]======================================================")
            return
        path_success = 'Actor/Success'
        if not os.path.exists(path_success):
            os.makedirs(path_success)
        profile_pictures = os.listdir(path)
        actor_list = self.get_emby_actor_list()
        if actor_list['TotalRecordCount'] == 0:
            self.add_text_main("[*]======================================================")
            return
        count = 1
        for actor in actor_list['Items']:
            flag = 0
            pic_name = ''
            if actor['Name'] + '.jpg' in profile_pictures:
                flag = 1
                pic_name = actor['Name'] + '.jpg'
            elif actor['Name'] + '.png' in profile_pictures:
                flag = 1
                pic_name = actor['Name'] + '.png'
            if flag == 0:
                byname_list = re.split('[,，()（）]', actor['Name'])
                for byname in byname_list:
                    if byname + '.jpg' in profile_pictures:
                        pic_name = byname + '.jpg'
                        flag = 1
                        break
                    elif byname + '.png' in profile_pictures:
                        pic_name = byname + '.png'
                        flag = 1
                        break
            if flag == 1 and (actor['ImageTags'] == {} or not os.path.exists(path_success + '/' + pic_name)):
                if mode == 1:
                    try:
                        self.upload_profile_picture(count, actor, path + '/' + pic_name)
                        shutil.copy(path + '/' + pic_name, path_success + '/' + pic_name)
                    except Exception as error_info:
                        self.add_text_main('[-]Error in found_profile_picture! ' + str(error_info))
                else:
                    self.add_text_main('[+]' + "%4s" % str(count) + '.Actor name: ' + actor['Name'] + '  Pic name: '
                                       + pic_name)
                count += 1
        if count == 1:
            self.add_text_main('[-]NO profile picture can be uploaded!')
        self.add_text_main("[*]======================================================")

    def upload_profile_picture(self, count, actor, pic_path):  # 上传头像
        emby_url = self.Ui.lineEdit_emby_url.text()
        api_key = self.Ui.lineEdit_api_key.text()
        emby_url = emby_url.replace('：', ':')
        try:
            f = open(pic_path, 'rb')  # 二进制方式打开图文件
            b6_pic = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
            f.close()
            url = 'http://' + emby_url + '/emby/Items/' + actor['Id'] + '/Images/Primary?api_key=' + api_key
            if pic_path.endswith('jpg'):
                header = {"Content-Type": 'image/png', }
            else:
                header = {"Content-Type": 'image/jpeg', }
            requests.post(url=url, data=b6_pic, headers=header)
            self.add_text_main(
                '[+]' + "%4s" % str(count) + '.Success upload profile picture for ' + actor['Name'] + '!')
        except Exception as error_info:
            self.add_text_main('[-]Error in upload_profile_picture! ' + str(error_info))

    # ========================================================================自定义文件名
    def get_naming_rule(self, json_data):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        name_file = json_data['naming_file'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                       year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        name_file = name_file.replace('//', '/').replace('--', '-').strip('-')
        if len(name_file) > 100:  # 文件名过长 取标题前70个字符
            self.add_text_main('[-]Error in Length of Path! Cut title!')
            name_file = name_file.replace(title, title[0:70])
        return name_file

    # ========================================================================语句添加到日志框
    def add_text_main(self, text):
        try:
            time.sleep(0.1)
            if self.Ui.radioButton_log_on.isChecked():
                self.log_txt.write((str(text) + '\n').encode('utf8'))
            self.Ui.textBrowser_log_main.append(text)
            self.Ui.textBrowser_log_main.moveCursor(QTextCursor.End)
        except Exception as error_info:
            self.Ui.textBrowser_log_main.append('[-]Error in add_text_main' + str(error_info))

    # ========================================================================移动到失败文件夹
    def moveFailedFolder(self, filepath, failed_folder):
        if self.Ui.radioButton_fail_move_on.isChecked():
            if self.Ui.radioButton_soft_off.isChecked():
                try:
                    shutil.move(filepath, failed_folder + '/')
                    self.add_text_main('[-]Move ' + os.path.split(filepath)[1] + ' to Failed output folder Success!')
                except Exception as error_info:
                    self.add_text_main('[-]Error in moveFailedFolder! ' + str(error_info))

    # ========================================================================下载文件
    def DownloadFileWithFilename(self, url, filename, path, Config, filepath, failed_folder):
        proxy_type = ''
        retry_count = 0
        proxy = ''
        timeout = 0
        try:
            proxy_type, proxy, timeout, retry_count = get_config()
        except Exception as error_info:
            print('[-]Error in DownloadFileWithFilename! ' + str(error_info))
            self.add_text_main('[-]Error in DownloadFileWithFilename! Proxy config error! Please check the config.')
        proxies = get_proxies(proxy_type, proxy)
        i = 0
        while i < retry_count:
            try:
                if not os.path.exists(path):
                    os.makedirs(path)
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/68.0.3440.106 Safari/537.36'}
                result = requests.get(str(url), headers=headers, timeout=timeout, proxies=proxies)
                with open(str(path) + "/" + filename, "wb") as code:
                    code.write(result.content)
                code.close()
                return
            except Exception as error_info:
                i += 1
                print('[-]Error in DownloadFileWithFilename! ' + str(error_info))
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
        self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
        self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================下载缩略图
    def thumbDownload(self, json_data, path, naming_rule, Config, filepath, failed_folder):
        thumb_name = naming_rule + '-thumb.jpg'
        if os.path.exists(path + '/' + thumb_name):
            self.add_text_main('[+]Thumb Existed!     ' + thumb_name)
            return
        i = 1
        while i <= int(Config['proxy']['retry']):
            self.DownloadFileWithFilename(json_data['cover'], thumb_name, path, Config, filepath,
                                          failed_folder)
            if not check_pic(path + '/' + thumb_name):
                print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                i = i + 1
            else:
                break
        if check_pic(path + '/' + thumb_name):
            self.add_text_main('[+]Thumb Downloaded!  ' + thumb_name)
        else:
            os.remove(path + '/' + thumb_name)
            raise Exception("The Size of Thumb is Error! Deleted " + thumb_name + '!')

    def deletethumb(self, path, naming_rule):
        try:
            thumb_path = path + '/' + naming_rule + '-thumb.jpg'
            if (not self.Ui.checkBox_download_thumb.isChecked()) and os.path.exists(thumb_path):
                os.remove(thumb_path)
                self.add_text_main('[+]Thumb Delete!      ' + naming_rule + '-thumb.jpg')
        except Exception as error_info:
            self.add_text_main('[-]Error in deletethumb: ' + str(error_info))

    # ========================================================================无码片下载封面图
    def smallCoverDownload(self, path, naming_rule, json_data, Config, filepath, failed_folder):
        if json_data['imagecut'] == 3:
            if json_data['cover_small'] == '':
                return 'small_cover_error'
            is_pic_open = 0
            poster_name = naming_rule + '-poster.jpg'
            if os.path.exists(path + '/' + poster_name):
                self.add_text_main('[+]Poster Existed!    ' + poster_name)
                return
            self.DownloadFileWithFilename(json_data['cover_small'], 'cover_small.jpg', path, Config, filepath,
                                          failed_folder)
            try:
                if not check_pic(path + '/cover_small.jpg'):
                    raise Exception("The Size of smallcover is Error! Deleted cover_small.jpg!")
                fp = open(path + '/cover_small.jpg', 'rb')
                is_pic_open = 1
                img = Image.open(fp)
                w = img.width
                h = img.height
                if not (1.4 <= h / w <= 1.6):
                    self.add_text_main('[-]The size of cover_small.jpg is unfit, Try to cut thumb!')
                    fp.close()
                    os.remove(path + '/cover_small.jpg')
                    return 'small_cover_error'
                img.save(path + '/' + poster_name)
                self.add_text_main('[+]Poster Downloaded! ' + poster_name)
                fp.close()
                os.remove(path + '/cover_small.jpg')
            except Exception as error_info:
                self.add_text_main('[-]Error in smallCoverDownload: ' + str(error_info))
                if is_pic_open:
                    fp.close()
                os.remove(path + '/cover_small.jpg')
                self.add_text_main('[+]Try to cut cover!')
                return 'small_cover_error'

    # ========================================================================下载剧照
    def extrafanartDownload(self, json_data, path, Config, filepath, failed_folder):
        if len(json_data['extrafanart']) == 0:
            json_data['extrafanart'] = ''
        if self.Ui.radioButton_extrafanart_download_on.isChecked() and str(json_data['extrafanart']) != '':
            self.add_text_main('[+]ExtraFanart Downloading!')
            extrafanart_folder = self.Ui.lineEdit_extrafanart_dir.text()
            if extrafanart_folder == '':
                extrafanart_folder = 'extrafanart'
            extrafanart_path = path + '/' + extrafanart_folder
            extrafanart_list = json_data['extrafanart']
            if not os.path.exists(extrafanart_path):
                os.makedirs(extrafanart_path)
            extrafanart_count = 0
            for extrafanart_url in extrafanart_list:
                extrafanart_count += 1
                if not os.path.exists(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                    i = 1
                    while i <= int(Config['proxy']['retry']):
                        self.DownloadFileWithFilename(extrafanart_url, 'fanart' + str(extrafanart_count) + '.jpg',
                                                      extrafanart_path, Config, filepath, failed_folder)
                        if not check_pic(extrafanart_path + '/fanart' + str(extrafanart_count) + '.jpg'):
                            print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                            i = i + 1
                        else:
                            break

    # ========================================================================打印NFO
    def PrintFiles(self, path, name_file, cn_sub, leak, json_data, filepath, failed_folder):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        name_media = json_data['naming_media'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                         year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            if os.path.exists(path + "/" + name_file + ".nfo"):
                self.add_text_main('[+]Nfo Existed!       ' + name_file + ".nfo")
                return
            with open(path + "/" + name_file + ".nfo", "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                print("  <title>" + name_media + "</title>", file=code)
                print("  <set>", file=code)
                print("  </set>", file=code)
                try:
                    if str(json_data['score']) != 'unknown' and str(json_data['score']) != '' and float(
                            json_data['score']) != 0.0:
                        print("  <rating>" + str(json_data['score']) + "</rating>", file=code)
                except Exception as err:
                    print("Error in json_data score!" + str(err))
                if studio != 'unknown':
                    print("  <studio>" + studio + "</studio>", file=code)
                if str(year) != 'unknown':
                    print("  <year>" + year + "</year>", file=code)
                if outline != 'unknown':
                    print("  <outline>" + outline + "</outline>", file=code)
                    print("  <plot>" + outline + "</plot>", file=code)
                if str(runtime) != 'unknown':
                    print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                if director != 'unknown':
                    print("  <director>" + director + "</director>", file=code)
                print("  <poster>" + name_file + "-poster.jpg</poster>", file=code)
                print("  <thumb>" + name_file + "-thumb.jpg</thumb>", file=code)
                print("  <fanart>" + name_file + "-fanart.jpg</fanart>", file=code)
                try:
                    for key, value in actor_photo.items():
                        if str(key) != 'unknown' and str(key) != '':
                            print("  <actor>", file=code)
                            print("   <name>" + key + "</name>", file=code)
                            if not value == '':  # or actor_photo == []:
                                print("   <thumb>" + value + "</thumb>", file=code)
                            print("  </actor>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in actor_photo: ' + str(error_info))
                if studio != 'unknown':
                    print("  <maker>" + studio + "</maker>", file=code)
                if publisher != 'unknown':
                    print("  <maker>" + publisher + "</maker>", file=code)
                print("  <label>", file=code)
                print("  </label>", file=code)
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <tag>" + i + "</tag>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in tag: ' + str(error_info))
                if json_data['imagecut'] == 3:
                    print("  <tag>無碼</tag>", file=code)
                if leak == 1:
                    print("  <tag>流出</tag>", file=code)
                if cn_sub == 1:
                    print("  <tag>中文字幕</tag>", file=code)
                if series != 'unknown':
                    print("  <tag>" + '系列:' + series + "</tag>", file=code)
                if studio != 'unknown':
                    print("  <tag>" + '製作:' + studio + "</tag>", file=code)
                if publisher != 'unknown':
                    print("  <tag>" + '發行:' + publisher + "</tag>", file=code)
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <genre>" + i + "</genre>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in genre: ' + str(error_info))
                if json_data['imagecut'] == 3:
                    print("  <genre>無碼</genre>", file=code)
                if leak == 1:
                    print("  <genre>流出</genre>", file=code)
                if cn_sub == 1:
                    print("  <genre>中文字幕</genre>", file=code)
                if series != 'unknown':
                    print("  <genre>" + '系列:' + series + "</genre>", file=code)
                if studio != 'unknown':
                    print("  <genre>" + '製作:' + studio + "</genre>", file=code)
                if publisher != 'unknown':
                    print("  <genre>" + '發行:' + publisher + "</genre>", file=code)
                print("  <num>" + number + "</num>", file=code)
                if release != 'unknown':
                    print("  <premiered>" + release + "</premiered>", file=code)
                    print("  <release>" + release + "</release>", file=code)
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                self.add_text_main("[+]Nfo Wrote!         " + name_file + ".nfo")
        except Exception as error_info:
            self.add_text_main("[-]Write Failed!")
            self.add_text_main('[-]Error in PrintFiles: ' + str(error_info))
            self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================thumb复制为fanart
    def copyRenameJpgToFanart(self, path, naming_rule):
        try:
            if not os.path.exists(path + '/' + naming_rule + '-fanart.jpg'):
                shutil.copy(path + '/' + naming_rule + '-thumb.jpg', path + '/' + naming_rule + '-fanart.jpg')
                self.add_text_main('[+]Fanart Copied!     ' + naming_rule + '-fanart.jpg')
            else:
                self.add_text_main('[+]Fanart Existed!    ' + naming_rule + '-fanart.jpg')
        except Exception as error_info:
            self.add_text_main('[-]Error in copyRenameJpgToFanart: ' + str(error_info))

    # ========================================================================移动视频、字幕
    def pasteFileToFolder(self, filepath, path, naming_rule, failed_folder):
        type = str(os.path.splitext(filepath)[1])
        try:
            if os.path.exists(path + '/' + naming_rule + type):
                raise FileExistsError
            if self.Ui.radioButton_soft_on.isChecked():  # 如果使用软链接
                os.symlink(filepath, path + '/' + naming_rule + type)
                self.add_text_main('[+]Movie Linked!     ' + naming_rule + type)
            else:
                shutil.move(filepath, path + '/' + naming_rule + type)
                self.add_text_main('[+]Movie Moved!       ' + naming_rule + type)
            path_old = filepath.replace(filepath.split('/')[-1], '')
            filename = filepath.split('/')[-1].split('.')[0]
            sub_type = self.Ui.lineEdit_sub_type.text().split('|')
            for sub in sub_type:
                if os.path.exists(path_old + '/' + filename + sub):  # 字幕移动
                    shutil.move(path_old + '/' + filename + sub, path + '/' + naming_rule + sub)
                    self.add_text_main('[+]Sub moved!         ' + naming_rule + sub)
                    return True
        except FileExistsError:
            self.add_text_main('[+]Movie Existed!     ' + naming_rule + type)
            if os.path.split(filepath)[0] != path:
                self.moveFailedFolder(filepath, failed_folder)
        except PermissionError:
            self.add_text_main('[-]PermissionError! Please run as Administrator!')
        except Exception as error_info:
            self.add_text_main('[-]Error in pasteFileToFolder: ' + str(error_info))
        return False

    # ========================================================================有码片裁剪封面
    def cutImage(self, imagecut, path, naming_rule):
        if imagecut != 3:
            thumb_name = naming_rule + '-thumb.jpg'
            poster_name = naming_rule + '-poster.jpg'
            if os.path.exists(path + '/' + poster_name):
                self.add_text_main('[+]Poster Existed!    ' + poster_name)
                return
            if imagecut == 0:
                self.image_cut(path, thumb_name)
            else:
                try:
                    img = Image.open(path + '/' + thumb_name)
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + poster_name)
                    self.add_text_main('[+]Poster Cut!        ' + poster_name)
                except:
                    self.add_text_main('[-]Thumb cut failed!')

    def fix_size(self, path, naming_rule):
        try:
            poster_path = path + '/' + naming_rule + '-poster.jpg'
            pic = Image.open(poster_path)
            (width, height) = pic.size
            if not 2 / 3 - 0.05 <= width / height <= 2 / 3 + 0.05:  # 仅处理会过度拉伸的图片
                fixed_pic = pic.resize((int(width), int(3 / 2 * width)))  # 拉伸图片
                fixed_pic = fixed_pic.filter(ImageFilter.GaussianBlur(radius=50))  # 高斯模糊
                fixed_pic.paste(pic, (0, int((3 / 2 * width - height) / 2)))  # 粘贴原图
                fixed_pic.save(poster_path)
        except Exception as error_info:
            self.add_text_main('[-]Error in fix_size: ' + str(error_info))

    # ========================================================================加水印
    def add_mark(self, poster_path, thumb_path, cn_sub, leak, uncensored, config):
        mark_type = ''
        if self.Ui.checkBox_sub.isChecked() and cn_sub:
            mark_type += ',字幕'
        if self.Ui.checkBox_leak.isChecked() and leak:
            mark_type += ',流出'
        if self.Ui.checkBox_uncensored.isChecked() and uncensored:
            mark_type += ',无码'
        if self.Ui.radioButton_thumb_mark_on.isChecked() and mark_type != '' and self.Ui.checkBox_download_thumb.isChecked() and os.path.exists(thumb_path):
            self.add_mark_thread(thumb_path, cn_sub, leak, uncensored)
            self.add_text_main('[+]Thumb Add Mark:    ' + mark_type.strip(','))
        if self.Ui.radioButton_poster_mark_on.isChecked() and mark_type != '' and self.Ui.checkBox_download_poster.isChecked() and os.path.exists(poster_path):
            self.add_mark_thread(poster_path, cn_sub, leak, uncensored)
            self.add_text_main('[+]Poster Add Mark:   ' + mark_type.strip(','))

    def add_mark_thread(self, pic_path, cn_sub, leak, uncensored):
        size = 14 - int(self.Ui.horizontalSlider_mark_size.value())  # 获取自定义大小的值
        img_pic = Image.open(pic_path)
        count = 0  # 获取自定义位置，取余配合pos达到顺时针添加的效果
        if self.Ui.radioButton_top_left.isChecked():
            count = 0
        elif self.Ui.radioButton_top_right.isChecked():
            count = 1
        elif self.Ui.radioButton_bottom_right.isChecked():
            count = 2
        elif self.Ui.radioButton_bottom_left.isChecked():
            count = 3
        if self.Ui.checkBox_sub.isChecked() and cn_sub == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 1)  # 添加
            count = (count + 1) % 4
        if self.Ui.checkBox_leak.isChecked() and leak == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 2)
            count = (count + 1) % 4
        if self.Ui.checkBox_uncensored.isChecked() and uncensored == 1:
            self.add_to_pic(pic_path, img_pic, size, count, 3)
        img_pic.close()

    def add_to_pic(self, pic_path, img_pic, size, count, mode):
        mark_pic_path = ''
        if mode == 1:
            mark_pic_path = 'Img/SUB.png'
        elif mode == 2:
            mark_pic_path = 'Img/LEAK.png'
        elif mode == 3:
            mark_pic_path = 'Img/UNCENSORED.png'
        img_subt = Image.open(mark_pic_path)
        scroll_high = int(img_pic.height / size)
        scroll_wide = int(scroll_high * img_subt.width / img_subt.height)
        img_subt = img_subt.resize((scroll_wide, scroll_high), Image.ANTIALIAS)
        r, g, b, a = img_subt.split()  # 获取颜色通道，保持png的透明性
        # 封面四个角的位置
        pos = [
            {'x': 0, 'y': 0},
            {'x': img_pic.width - scroll_wide, 'y': 0},
            {'x': img_pic.width - scroll_wide, 'y': img_pic.height - scroll_high},
            {'x': 0, 'y': img_pic.height - scroll_high},
        ]
        img_pic.paste(img_subt, (pos[count]['x'], pos[count]['y']), mask=a)
        img_pic.save(pic_path, quality=95)

    # ========================================================================获取分集序号
    def get_part(self, filepath, failed_folder):
        try:
            if re.search('-CD\d+', filepath):
                return re.findall('-CD\d+', filepath)[0]
            if re.search('-cd\d+', filepath):
                return re.findall('-cd\d+', filepath)[0]
        except Exception as error_info:
            self.add_text_main('[-]Error in get_part: ' + str(error_info))
            self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================更新进度条
    def set_processbar(self, value):
        self.Ui.progressBar_avdc.setProperty("value", value)
        self.Ui.label_percent.setText(str(value) + '%')

    # ========================================================================输出调试信息
    def debug_mode(self, json_data):
        try:
            self.add_text_main('[+] ---Debug info---')
            for key, value in json_data.items():
                if value == '' or key == 'actor_photo' or key == 'extrafanart':
                    continue
                if key == 'tag' and len(value) == 0:
                    continue
                elif key == 'tag':
                    value = str(json_data['tag']).strip(" ['']").replace('\'', '')
                self.add_text_main('   [+]-' + "%-13s" % key + ': ' + str(value))
            self.add_text_main('[+] ---Debug info---')
        except Exception as error_info:
            self.add_text_main('[-]Error in debug_mode: ' + str(error_info))

    # ========================================================================创建输出文件夹
    def creatFolder(self, success_folder, json_data, config):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        if len(actor.split(',')) >= 10:  # 演员过多取前五个
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        folder_name = json_data['folder_name']
        path = folder_name.replace('title', title).replace('studio', studio).replace('year', year).replace('runtime',
                                                                                                           runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)  # 生成文件夹名
        path = path.replace('--', '-').strip('-')
        if len(path) > 100:  # 文件夹名过长 取标题前70个字符
            self.add_text_main('[-]Error in Length of Path! Cut title!')
            path = path.replace(title, title[0:70])
        path = success_folder + '/' + path
        path = path.replace('--', '-').strip('-')
        if not os.path.exists(path):
            path = escapePath(path, config)
            os.makedirs(path)
        return path

    # ========================================================================从指定网站获取json_data
    def get_json_data(self, mode, number, config, appoint_url):
        if mode == 5:  # javdb模式
            self.add_text_main('[!]Please Wait Three Seconds！')
            time.sleep(3)
        json_data = getDataFromJSON(number, config, mode, appoint_url)
        return json_data

    # ========================================================================json_data添加到主界面
    def add_label_info(self, json_data):
        try:
            t = threading.Thread(target=self.add_label_info_Thread, args=(json_data,))
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_start_cap_clicked: ' + str(error_info))

    def add_label_info_Thread(self, json_data):
        self.Ui.label_number.setText(json_data['number'])
        self.Ui.label_release.setText(json_data['release'])
        self.Ui.label_director.setText(json_data['director'])
        self.Ui.label_label.setText(json_data['series'])
        self.Ui.label_studio.setText(json_data['studio'])
        self.Ui.label_publish.setText(json_data['publisher'])
        self.Ui.label_title.setText(json_data['title'])
        self.Ui.label_actor.setText(json_data['actor'])
        self.Ui.label_outline.setText(json_data['outline'])
        self.Ui.label_tag.setText(str(json_data['tag']).strip(" [',']").replace('\'', ''))
        if self.Ui.checkBox_cover.isChecked():
            poster_path = json_data['poster_path']
            thumb_path = json_data['thumb_path']
            if os.path.exists(poster_path):
                pix = QPixmap(poster_path)
                self.Ui.label_poster.setScaledContents(True)
                self.Ui.label_poster.setPixmap(pix)  # 添加封面图
            if os.path.exists(thumb_path):
                pix = QPixmap(thumb_path)
                self.Ui.label_thumb.setScaledContents(True)
                self.Ui.label_thumb.setPixmap(pix)  # 添加缩略图

    # ========================================================================检查更新
    def UpdateCheck(self):
        if self.Ui.radioButton_update_on.isChecked():
            self.add_text_main('[!]Update Checking!')
            html2 = get_html('https://raw.githubusercontent.com/moyy996/AVDC/master/update_check.json')
            if html2 == 'ProxyError':
                return 'ProxyError'
            html = json.loads(str(html2))
            if float(self.version) < float(html['version']):
                self.add_text_main('[*]                  * New update ' + html['version'] + ' *')
                self.add_text_main('[*]                     ↓ Download ↓')
                self.add_text_main('[*] ' + html['download'])
            else:
                self.add_text_main('[!]No Newer Version Available!')
            self.add_text_main("[*]======================================================")
        return 'True'

    # ========================================================================新建失败输出文件夹
    def CreatFailedFolder(self, failed_folder):
        if self.Ui.radioButton_fail_move_on.isChecked() and not os.path.exists(failed_folder):
            try:
                os.makedirs(failed_folder + '/')
                self.add_text_main('[+]Created folder named ' + failed_folder + '!')
            except Exception as error_info:
                self.add_text_main('[-]Error in CreatFailedFolder: ' + str(error_info))

    # ========================================================================删除空目录
    def CEF(self, path):
        if os.path.exists(path):
            for root, dirs, files in os.walk(path):
                for dir in dirs:
                    try:
                        os.removedirs(root.replace('\\', '/') + '/' + dir)  # 删除这个空文件夹
                        self.add_text_main('[+]Deleting empty folder ' + root.replace('\\', '/') + '/' + dir)
                    except:
                        delete_empty_folder_failed = ''

    def Core_Main(self, filepath, number, mode, count, appoint_url=''):
        # =======================================================================初始化所需变量
        leak = 0
        uncensored = 0
        cn_sub = 0
        c_word = ''
        multi_part = 0
        part = ''
        program_mode = 0
        config_file = 'config.ini'
        Config = ConfigParser()
        Config.read(config_file, encoding='UTF-8')
        if self.Ui.radioButton_common.isChecked():
            program_mode = 1
        elif self.Ui.radioButton_sort.isChecked():
            program_mode = 2
        movie_path = self.Ui.lineEdit_movie_path.text()
        if movie_path == '':
            movie_path = os.getcwd().replace('\\', '/')
        failed_folder = movie_path + '/' + self.Ui.lineEdit_fail.text()  # 失败输出目录
        success_folder = movie_path + '/' + self.Ui.lineEdit_success.text()  # 成功输出目录
        # =======================================================================获取json_data
        json_data = self.get_json_data(mode, number, Config, appoint_url)
        # =======================================================================调试模式
        if self.Ui.radioButton_debug_on.isChecked():
            self.debug_mode(json_data)
        # =======================================================================是否找到影片信息
        if json_data['website'] == 'timeout':
            self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
            return 'error'
        elif json_data['title'] == '':
            self.add_text_main('[-]Movie Data not found!')
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0,
                         str(self.count_claw) + '-' + str(count) + '.' + os.path.splitext(filepath.split('/')[-1])[0])
            self.item_fail.addChild(node)
            self.moveFailedFolder(filepath, failed_folder)
            return 'not found'
        elif 'http' not in json_data['cover']:
            raise Exception('Cover Url is None!')
        elif json_data['imagecut'] == 3 and 'http' not in json_data['cover_small']:
            raise Exception('Cover_small Url is None!')
        # =======================================================================判断-C,-CD后缀,无码,流出
        if '-CD' in filepath or '-cd' in filepath:
            multi_part = 1
            part = self.get_part(filepath, failed_folder)
        if '-c.' in filepath or '-C.' in filepath or '中文' in filepath or '字幕' in filepath:
            cn_sub = 1
            c_word = '-C'  # 中文字幕影片后缀
        if json_data['imagecut'] == 3:  # imagecut=3为无码
            uncensored = 1
        if '流出' in os.path.split(filepath)[1]:
            leak = 1
        # =======================================================================创建输出文件夹
        path = self.creatFolder(success_folder, json_data, Config)
        self.add_text_main('[+]Folder : ' + path)
        self.add_text_main('[+]From   : ' + json_data['website'])
        # =======================================================================文件命名规则
        number = json_data['number']
        naming_rule = str(self.get_naming_rule(json_data)).replace('--', '-').strip('-')
        if leak == 1:
            naming_rule += '-流出'
        if multi_part == 1:
            naming_rule += part
        if cn_sub == 1:
            naming_rule += c_word
        # =======================================================================封面路径
        thumb_path = path + '/' + naming_rule + '-thumb.jpg'
        poster_path = path + '/' + naming_rule + '-poster.jpg'
        # =======================================================================无码封面获取方式
        if json_data['imagecut'] == 3 and self.Ui.radioButton_poster_cut.isChecked():
            json_data['imagecut'] = 0
        # =======================================================================刮削模式
        if program_mode == 1:
            # imagecut 0 判断人脸位置裁剪缩略图为封面，1 裁剪右半面，3 下载小封面
            self.thumbDownload(json_data, path, naming_rule, Config, filepath, failed_folder)
            if self.Ui.checkBox_download_poster.isChecked():
                if self.smallCoverDownload(path, naming_rule, json_data, Config, filepath,
                                           failed_folder) == 'small_cover_error':  # 下载小封面
                    json_data['imagecut'] = 0
                self.cutImage(json_data['imagecut'], path, naming_rule)  # 裁剪图
                self.fix_size(path, naming_rule)
            if self.Ui.checkBox_download_fanart.isChecked():
                self.copyRenameJpgToFanart(path, naming_rule)
            self.deletethumb(path, naming_rule)
            if self.pasteFileToFolder(filepath, path, naming_rule, failed_folder):  # 移动文件,True 为有外挂字幕
                cn_sub = 1
            if self.Ui.checkBox_download_nfo.isChecked():
                self.PrintFiles(path, naming_rule, cn_sub, leak, json_data, filepath, failed_folder)  # 打印文件
            if self.Ui.radioButton_extrafanart_download_on.isChecked():
                self.extrafanartDownload(json_data, path, Config, filepath, failed_folder)
            self.add_mark(poster_path, thumb_path, cn_sub, leak, uncensored, Config)
        # =======================================================================整理模式
        elif program_mode == 2:
            self.pasteFileToFolder(filepath, path, naming_rule, failed_folder)  # 移动文件
        # =======================================================================json添加封面项
        json_data['thumb_path'] = thumb_path
        json_data['poster_path'] = poster_path
        json_data['number'] = number
        self.add_label_info(json_data)
        self.json_array[str(self.count_claw) + '-' + str(count)] = json_data
        return part + c_word

    def AVDC_Main(self):
        # =======================================================================初始化所需变量
        os.chdir(os.getcwd())
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        movie_path = self.Ui.lineEdit_movie_path.text()
        if movie_path == '':
            movie_path = os.getcwd().replace('\\', '/')
        failed_folder = movie_path + '/' + self.Ui.lineEdit_fail.text()  # 失败输出目录
        escape_folder = self.Ui.lineEdit_escape_dir.text()  # 多级目录刮削需要排除的目录
        mode = self.Ui.comboBox_website_all.currentIndex() + 1
        movie_type = self.Ui.lineEdit_movie_type.text()
        escape_string = self.Ui.lineEdit_escape_string.text()
        # =======================================================================检测更新,判断网络情况,新建failed目录,获取影片列表
        if self.UpdateCheck() == 'ProxyError':
            self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
            self.Ui.pushButton_start_cap.setEnabled(True)
            self.add_text_main("[*]======================================================")
            return
        if self.Ui.radioButton_fail_move_on.isChecked():
            self.CreatFailedFolder(failed_folder)  # 新建failed文件夹
        movie_list = movie_lists(escape_folder, movie_type, movie_path)  # 获取所有需要刮削的影片列表
        count = 0
        count_all = str(len(movie_list))
        self.add_text_main('[+]Find ' + count_all + ' movies')
        if count_all == 0:
            self.progressBarValue.emit(int(100))
        if config['common']['soft_link'] == '1':
            self.add_text_main('[!] --- Soft link mode is ENABLE! ----')
        # =======================================================================遍历电影列表 交给core处理
        for movie in movie_list:  # 遍历电影列表 交给core处理
            count += 1
            self.Ui.label_progress.setText('当前: ' + str(count) + '/' + str(count_all))
            percentage = str(count / int(count_all) * 100)[:4] + '%'
            value = int(count / int(count_all) * 100)
            self.add_text_main(
                '[!] - ' + str(self.count_claw) + ' - ' + percentage + ' - [' + str(count) + '/' + count_all + '] -')
            try:
                movie_number = getNumber(movie, escape_string)
                self.add_text_main("[!]Making Data for   [" + movie + "], the number is [" + movie_number + "]")
                result = self.Core_Main(movie, movie_number, mode, count)
                if result != 'not found' and movie_number != '' and result != 'error':
                    node = QTreeWidgetItem(self.item_succ)
                    node.setText(0, str(self.count_claw) + '-' + str(count) + '.' + movie_number + result)
                    self.item_succ.addChild(node)
                elif result == 'error':
                    break
                self.add_text_main("[*]======================================================")
            except Exception as error_info:
                node = QTreeWidgetItem(self.item_fail)
                node.setText(0,
                             str(self.count_claw) + '-' + str(count) + '.' + os.path.splitext(movie.split('/')[-1])[0])
                self.item_fail.addChild(node)
                self.add_text_main('[-]Error in AVDC_Main: ' + str(error_info))
                if self.Ui.radioButton_fail_move_on.isChecked() and not os.path.exists(
                        failed_folder + '/' + os.path.split(movie)[1]):
                    if config['common']['soft_link'] == '0':
                        try:
                            shutil.move(movie, failed_folder + '/')
                            self.add_text_main('[-]Move ' + movie + ' to failed folder')
                        except shutil.Error as error_info:
                            self.add_text_main('[-]Error in AVDC_Main: ' + str(error_info))
                self.add_text_main("[*]======================================================")
            self.progressBarValue.emit(int(value))
        self.Ui.pushButton_start_cap.setEnabled(True)
        self.CEF(movie_path)
        self.add_text_main("[+]All finished!!!")
        self.add_text_main("[*]======================================================")


if __name__ == '__main__':
    '''
    主函数
    '''
    app = QApplication(sys.argv)
    ui = MyMAinWindow()
    ui.show()
    sys.exit(app.exec_())
