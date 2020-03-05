#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QTextCursor, QCursor
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, Qt
from Ui.AVDC import *
import sys
import time
import os.path
from Function.Function import *
from Function.getHtml import *
import requests
import shutil
import base64
import re
from aip import AipBodyAnalysis
from PIL import Image
import os


class MyMAinWindow(QMainWindow, Ui_AVDV):
    progressBarValue = pyqtSignal(int)  # 进度条信号量

    def __init__(self, parent=None):
        super(MyMAinWindow, self).__init__(parent)
        self.Ui = Ui_AVDV()  # 实例化 Ui
        self.Ui.setupUi(self)  # 初始化Ui
        self.Init_Ui()
        self.set_style()
        # 初始化需要的变量
        self.version = '3.81'
        self.m_drag = False
        self.m_DragPosition = 0
        self.item_succ = self.Ui.treeWidget_number.topLevelItem(0)
        self.item_fail = self.Ui.treeWidget_number.topLevelItem(1)
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
        elif os.path.exists('Ui/AVDC-ico.png'):
            ico_path = 'Ui/AVDC-ico.png'
        pix = QPixmap(ico_path)
        self.Ui.label_ico.setScaledContents(True)
        self.Ui.label_ico.setPixmap(pix)  # 添加图标
        self.Ui.progressBar_avdc.setValue(0)  # 进度条清0
        self.progressBarValue.connect(self.set_processbar)
        self.Ui.progressBar_avdc.setTextVisible(False)  # 不显示进度条文字
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.Ui.treeWidget_number.expandAll()
        self.Ui.checkBox_cover.setChecked(True)

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
            QPushButton#pushButton_start_cap,#pushButton_move_mp4,#pushButton_select_file,#pushButton_select_fanart{
                    font-size:20px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_add_actor_pic{
                    font-size:20px;
                    background:#F0F8FF;
                    border:2px solid white;
                    width:300px;
                    border-radius:20px;
                    padding:2px 4px;
            }
            QPushButton#pushButton_save_config,#pushButton_show_pic_actor{
                    font-size:20px;
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
        self.Ui.pushButton_move_mp4.clicked.connect(self.move_file)
        self.Ui.pushButton_add_actor_pic.clicked.connect(self.pushButton_add_actor_pic_clicked)
        self.Ui.pushButton_show_pic_actor.clicked.connect(self.pushButton_show_pic_actor_clicked)
        self.Ui.pushButton_select_fanart.clicked.connect(self.pushButton_select_fanart_clicked)
        self.Ui.pushButton_log.clicked.connect(self.pushButton_show_log_clicked)
        self.Ui.checkBox_cover.stateChanged.connect(self.cover_change)
        self.Ui.horizontalSlider_timeout.valueChanged.connect(self.lcdNumber_timeout_change)
        self.Ui.horizontalSlider_retry.valueChanged.connect(self.lcdNumber_retry_change)

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
        if int(config['log']['save_log']) == 1:
            self.Ui.radioButton_log_on.setChecked(True)
        elif int(config['log']['save_log']) == 0:
            self.Ui.radioButton_log_off.setChecked(True)
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
        if config['common']['website'] == 'all':
            self.Ui.comboBox_website_all.setCurrentIndex(0)
        elif config['common']['website'] == 'javlibrary':
            self.Ui.comboBox_website_all.setCurrentIndex(1)
        elif config['common']['website'] == 'mgstage':
            self.Ui.comboBox_website_all.setCurrentIndex(2)
        elif config['common']['website'] == 'fc2club':
            self.Ui.comboBox_website_all.setCurrentIndex(3)
        elif config['common']['website'] == 'javbus':
            self.Ui.comboBox_website_all.setCurrentIndex(4)
        elif config['common']['website'] == 'javdb':
            self.Ui.comboBox_website_all.setCurrentIndex(5)
        elif config['common']['website'] == 'avsox':
            self.Ui.comboBox_website_all.setCurrentIndex(6)
        elif config['common']['website'] == 'dmm':
            self.Ui.comboBox_website_all.setCurrentIndex(7)
        self.Ui.lineEdit_success.setText(config['common']['success_output_folder'])
        self.Ui.lineEdit_fail.setText(config['common']['failed_output_folder'])
        self.Ui.lineEdit_escape_dir.setText(config['escape']['folders'])
        self.Ui.lineEdit_escape_char.setText(config['escape']['literals'])
        self.Ui.lineEdit_proxy.setText(config['proxy']['proxy'])
        self.Ui.horizontalSlider_timeout.setValue(int(config['proxy']['timeout']))
        self.Ui.horizontalSlider_retry.setValue(int(config['proxy']['retry']))
        self.Ui.lineEdit_dir_name.setText(config['Name_Rule']['folder_name'])
        self.Ui.lineEdit_media_name.setText(config['Name_Rule']['naming_media'])
        self.Ui.lineEdit_local_name.setText(config['Name_Rule']['naming_file'])
        self.Ui.lineEdit_escape_dir_move.setText(config['escape']['folders'])
        self.Ui.lineEdit_emby_url.setText(config['emby']['emby_url'])
        self.Ui.lineEdit_api_key.setText(config['emby']['api_key'])
        self.Ui.lineEdit_javlibrary_url.setText(config['javlibrary_url']['url'])

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

    def pushButton_show_log_clicked(self):
        self.Ui.stackedWidget.setCurrentIndex(4)

    def lcdNumber_timeout_change(self):
        timeout = self.Ui.horizontalSlider_timeout.value()
        self.Ui.lcdNumber_timeout.display(timeout)

    def lcdNumber_retry_change(self):
        retry = self.Ui.horizontalSlider_retry.value()
        self.Ui.lcdNumber_retry.display(retry)

    def cover_change(self):
        if not self.Ui.checkBox_cover.isChecked():
            self.Ui.label_poster.setText("封面图")
            self.Ui.label_fanart.setText("缩略图")

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
            t = threading.Thread(target=self.AVDC_Main)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_start_cap_clicked: ' + str(error_info))

    def pushButton_save_config_clicked(self):
        try:
            t = threading.Thread(target=self.save_config_clicked)
            t.start()  # 启动线程,即让线程开始执行
        except Exception as error_info:
            self.add_text_main('[-]Error in pushButton_save_config_clicked: ' + str(error_info))

    # ========================================================================读取设置页设置，保存在config.ini
    def save_config_clicked(self):
        main_mode = 1
        soft_link = 0
        switch_debug = 0
        update_check = 0
        save_log = 0
        media_warehouse = ''
        website = ''
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
        if self.Ui.radioButton_emby.isChecked():  # emby/jellyfin
            media_warehouse = 'emby'
        elif self.Ui.radioButton_plex.isChecked():  # plex
            media_warehouse = 'plex'
        elif self.Ui.radioButton_kodi.isChecked():  # kodi
            media_warehouse = 'kodi'
        if self.Ui.comboBox_website_all.currentText() == 'All websites':  # all
            website = 'all'
        elif self.Ui.comboBox_website_all.currentText() == 'javlibrary':  # javlibrary
            website = 'javlibrary'
        elif self.Ui.comboBox_website_all.currentText() == 'mgstage':  # mgstage
            website = 'mgstage'
        elif self.Ui.comboBox_website_all.currentText() == 'fc2club':  # fc2club
            website = 'fc2club'
        elif self.Ui.comboBox_website_all.currentText() == 'javbus':  # javbus
            website = 'javbus'
        elif self.Ui.comboBox_website_all.currentText() == 'javdb':  # javdb
            website = 'javdb'
        elif self.Ui.comboBox_website_all.currentText() == 'avsox':  # avsox
            website = 'avsox'
        elif self.Ui.comboBox_website_all.currentText() == 'dmm':  # dmm
            website = 'dmm'
        json_config = {
            'main_mode': main_mode,
            'soft_link': soft_link,
            'switch_debug': switch_debug,
            'update_check': update_check,
            'save_log': save_log,
            'media_warehouse': media_warehouse,
            'website': website,
            'failed_output_folder': self.Ui.lineEdit_fail.text(),
            'success_output_folder': self.Ui.lineEdit_success.text(),
            'proxy': self.Ui.lineEdit_proxy.text(),
            'timeout': self.Ui.horizontalSlider_timeout.value(),
            'retry': self.Ui.horizontalSlider_retry.value(),
            'folder_name': self.Ui.lineEdit_dir_name.text(),
            'naming_media': self.Ui.lineEdit_media_name.text(),
            'naming_file': self.Ui.lineEdit_local_name.text(),
            'literals': self.Ui.lineEdit_escape_char.text(),
            'folders': self.Ui.lineEdit_escape_dir.text(),
            'emby_url': self.Ui.lineEdit_emby_url.text(),
            'api_key': self.Ui.lineEdit_api_key.text(),
            'javlib_url': self.Ui.lineEdit_javlibrary_url.text(),
        }
        save_config(json_config)

    # ========================================================================小工具-单视频刮削
    def pushButton_select_file_clicked(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "Movie Files(*.mp4 *.avi *.rmvb "
                                                                   "*.wmv *.mov *.mkv *.flv *.ts *.MP4 *.AVI *.RMVB "
                                                                   "*.WMV *.MOV *.MKV *.FLV *.TS);;All Files(*)")
        if filePath != '':
            self.Ui.stackedWidget.setCurrentIndex(0)
            try:
                t = threading.Thread(target=self.select_file_thread, args=(filePath,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_select_file_clicked: ' + str(error_info))

    def select_file_thread(self, file_name):
        file_root = os.getcwd().replace("\\\\", "/").replace("\\", "/")
        file_path = file_name.replace(file_root, '.').replace("\\\\", "/").replace("\\", "/")
        file_name = os.path.splitext(file_name.split('/')[-1])[0]
        mode = self.Ui.comboBox_website.currentIndex() + 1
        try:
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
            self.Core_Main(file_path, file_name, mode, 0)
        except Exception as error_info:
            self.add_text_main('[-]Error in select_file_thread: ' + str(error_info))
        self.add_text_main("[*]======================================================")

    # ========================================================================小工具-裁剪封面图
    def pushButton_select_fanart_clicked(self):
        filePath, fileType = QtWidgets.QFileDialog.getOpenFileName(self, "选取文件", os.getcwd(),
                                                                   "Picture Files(*.jpg);;All Files(*)")
        if filePath != '':
            self.Ui.stackedWidget.setCurrentIndex(0)
            try:
                t = threading.Thread(target=self.select_fanart_thread, args=(filePath,))
                t.start()  # 启动线程,即让线程开始执行
            except Exception as error_info:
                self.add_text_main('[-]Error in pushButton_select_fanart_clicked: ' + str(error_info))

    def select_fanart_thread(self, file_path):
        file_name = file_path.split('/')[-1]
        file_path = file_path.replace('/' + file_name, '')
        self.image_cut(file_path, file_name)
        self.add_text_main("[*]======================================================")

    def image_cut(self, path, file_name):
        file_path = os.path.join(path, file_name)
        png_name = ''
        if self.Ui.radioButton_emby.isChecked():  # emby/jellyfin
            png_name = os.path.splitext(file_name)[0] + '.png'
        elif self.Ui.radioButton_plex.isChecked():  # plex
            png_name = 'poster.jpg'
        elif self.Ui.radioButton_kodi.isChecked():  # kodi
            png_name = file_name.replace('-fanart.jpg', '-poster.jpg')
        try:
            if os.path.exists(os.path.join(path, png_name)):
                os.remove(os.path.join(path, png_name))
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

        """ 调用人体检测与属性识别 """
        result = client.bodyAnalysis(image)
        ewidth = int(0.661538 * height)
        ex = int(result["person_info"][0]['body_parts']['nose']['x'])
        if width - ex < ewidth / 2:
            ex = width - ewidth
        else:
            ex -= int(ewidth / 2)
        ey = 0
        ew = ewidth
        eh = height
        fp = open(file_path, 'rb')
        img = Image.open(fp)
        img_new_png = img.crop((ex, ey, ew + ex, eh + ey))
        fp.close()
        img_new_png.save(path + '/' + png_name)
        self.add_text_main('[+]Poster Cut         ' + png_name + ' from ' + file_name + '!')
        pix = QPixmap(file_path)
        self.Ui.label_fanart.setScaledContents(True)
        self.Ui.label_fanart.setPixmap(pix)  # 添加图标
        pix = QPixmap(path + '/' + png_name)
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
        sub_type = ['.srt', '.ass', '.sub']
        des_path = 'Movie_moved'
        movie_list = movie_lists(escape_dir)
        if not os.path.exists(des_path):
            self.add_text_main('[+]Created folder Movie_moved!')
            os.makedirs(des_path)
        self.add_text_main('[+]Move Movies Start!')
        for movie in movie_list:
            if des_path in movie:
                continue
            sour = movie
            lenth = len(sour.split('/'))
            des = des_path + '/' + sour.split('/')[lenth - 1]
            try:
                if len(sour.split('/')) > 2:
                    shutil.move(sour, des)
                    self.add_text_main('   [+]Move ' + sour.split('/')[lenth - 1] + ' to Movie_moved Success!')
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
            respones = requests.post(url=url, data=b6_pic, headers=header)
            self.add_text_main(
                '[+]' + "%4s" % str(count) + '.Success upload profile picture for ' + actor['Name'] + '!')
        except Exception as error_info:
            self.add_text_main('[-]Error in upload_profile_picture! ' + str(error_info))

    # ========================================================================自定义文件名
    def get_naming_rule(self, json_data):
        title, studio, publisher, year, outline, runtime, director, actor_photo, actor, release, tag, number, cover, website, series = get_info(
            json_data)
        name_file = json_data['naming_file'].replace('title', title).replace('studio', studio).replace('year',
                                                                                                       year).replace(
            'runtime',
            runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        return name_file

    # ========================================================================语句添加到日志框
    def add_text_main(self, text):
        time.sleep(0.1)
        if self.Ui.radioButton_log_on.isChecked():
            self.log_txt.write((str(text) + '\n').encode('utf8'))
        self.Ui.textBrowser_log_main.append(text)
        self.Ui.textBrowser_log_main.moveCursor(QTextCursor.End)

    # ========================================================================移动到失败文件夹
    def moveFailedFolder(self, filepath, failed_folder):
        self.add_text_main('[-]Move to Failed output folder')
        shutil.move(filepath, failed_folder + '/')

    # ========================================================================下载文件
    def DownloadFileWithFilename(self, url, filename, path, Config, filepath, failed_folder):
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
                    code.close()
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
                    code.close()
                    return
            except requests.exceptions.RequestException:
                i += 1
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ConnectionError:
                i += 1
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ProxyError:
                i += 1
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
            except requests.exceptions.ConnectTimeout:
                i += 1
                print('[-]Image Download :   Connect retry ' + str(i) + '/' + str(retry_count))
        self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
        self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================下载缩略图
    def fanartDownload(self, option, json_data, path, naming_rule, Config, filepath, failed_folder):
        if option == 'emby':
            self.DownloadFileWithFilename(json_data['cover'], naming_rule + '.jpg', path, Config, filepath,
                                          failed_folder)
            if not os.path.getsize(path + '/' + naming_rule + '.jpg') == 0:
                self.add_text_main('[+]Fanart Downloaded! ' + naming_rule + '.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/' + naming_rule + '.jpg') == 0:
                    print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                    self.DownloadFileWithFilename(json_data['cover'], naming_rule + '.jpg', path, Config, filepath,
                                                  failed_folder)
                    i = i + 1
                else:
                    break
            self.add_text_main('[+]Fanart Downloaded! ' + naming_rule + '.jpg')
        elif option == 'plex':
            self.DownloadFileWithFilename(json_data['cover'], 'fanart.jpg', path, Config, filepath, failed_folder)
            if not os.path.getsize(path + '/fanart.jpg') == 0:
                self.add_text_main('[+]Fanart Downloaded! fanart.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/fanart.jpg') == 0:
                    print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                    self.DownloadFileWithFilename(json_data['cover'], 'fanart.jpg', path, Config, filepath,
                                                  failed_folder)
                    i = i + 1
                    continue
                else:
                    break
            self.add_text_main('[+]Fanart Downloaded! fanart.jpg')
        elif option == 'kodi':
            self.DownloadFileWithFilename(json_data['cover'], naming_rule + '-fanart.jpg', path, Config, filepath,
                                          failed_folder)
            if not os.path.getsize(path + '/' + naming_rule + '-fanart.jpg') == 0:
                self.add_text_main('[+]Fanart Downloaded! ' + naming_rule + '-fanart.jpg')
                return
            i = 1
            while i <= int(Config['proxy']['retry']):
                if os.path.getsize(path + '/' + naming_rule + '-fanart.jpg') == 0:
                    print('[!]Image Download Failed! Trying again. ' + str(i) + '/' + Config['proxy']['retry'])
                    self.DownloadFileWithFilename(json_data['cover'], naming_rule + '-fanart.jpg', path, Config,
                                                  filepath,
                                                  failed_folder)
                    i = i + 1
                    continue
                else:
                    break
            self.add_text_main('[+]Fanart Downloaded! ' + naming_rule + '-fanart.jpg')

    # ========================================================================无码片下载封面图
    def smallCoverDownload(self, path, naming_rule, json_data, option, Config, filepath, failed_folder):
        if json_data['imagecut'] == 3:
            self.DownloadFileWithFilename(json_data['cover_small'], 'cover_small.jpg', path, Config, filepath,
                                          failed_folder)
            try:
                fp = open(path + '/cover_small.jpg', 'rb')
                img = Image.open(fp)
                w = img.width
                h = img.height
                if not (1.45 <= h/w <= 1.55):
                    self.add_text_main('[-]The size of cover_small.jpg is wrong, Try to cut fanart!')
                    fp.close()
                    os.remove(path + '/cover_small.jpg')
                    return 'small_cover_error'
                if option == 'emby':
                    img.save(path + '/' + naming_rule + '.png')
                    self.add_text_main('[+]Poster Downloaded! ' + naming_rule + '.png')
                elif option == 'kodi':
                    img.save(path + '/' + naming_rule + '-poster.jpg')
                    self.add_text_main('[+]Poster Downloaded! ' + naming_rule + '-poster.jpg')
                elif option == 'plex':
                    img.save(path + '/poster.jpg')
                    self.add_text_main('[+]Poster Downloaded! poster.jpg')
                fp.close()
                os.remove(path + '/cover_small.jpg')
            except Exception as error_info:
                self.add_text_main('[-]Error in smallCoverDownload: ' + str(error_info))
                fp.close()
                os.remove(path + '/cover_small.jpg')
                self.add_text_main('[+]Try to cut fanart!')
                return 'small_cover_error'

    # ========================================================================打印NFO
    def PrintFiles(self, option, path, name_file, cn_sub, json_data, filepath, failed_folder):
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
            with open(path + "/" + name_file + ".nfo", "wt", encoding='UTF-8') as code:
                print('<?xml version="1.0" encoding="UTF-8" ?>', file=code)
                print("<movie>", file=code)
                print(" <title>" + name_media + "</title>", file=code)
                print("  <set>", file=code)
                print("  </set>", file=code)
                if studio != 'unknown':
                    print("  <studio>" + studio + "+</studio>", file=code)
                if str(year) != 'unknown':
                    print("  <year>" + year + "</year>", file=code)
                if outline != 'unknown':
                    print("  <outline>" + outline + "</outline>", file=code)
                    print("  <plot>" + outline + "</plot>", file=code)
                if str(runtime) != 'unknown':
                    print("  <runtime>" + str(runtime).replace(" ", "") + "</runtime>", file=code)
                if director != 'unknown':
                    print("  <director>" + director + "</director>", file=code)
                if option == 'emby':
                    print("  <poster>" + name_file + ".png</poster>", file=code)
                    print("  <thumb>" + name_file + ".png</thumb>", file=code)
                    print("  <fanart>" + name_file + '.jpg' + "</fanart>", file=code)
                elif option == 'kodi':
                    print("  <poster>" + name_file + "-poster.jpg</poster>", file=code)
                    print("  <fanart>" + name_file + '-fanart.jpg' + "</fanart>", file=code)
                elif option == 'plex':
                    print("  <poster>poster.jpg</poster>", file=code)
                    print("  <thumb>thumb.png</thumb>", file=code)
                    print("  <fanart>fanart.jpg</fanart>", file=code)
                try:
                    for key, value in actor_photo.items():
                        if str(key) != 'unknown':
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
                if re.match('^\d{4,}', number) or re.match('n\d{4}', number) or 'HEYZO' in number.upper():
                    print("  <tag>無碼</tag>", file=code)
                if series != 'unknown':
                    print("  <tag>" + '系列:' + series + "</tag>", file=code)
                if studio != 'unknown':
                    print("  <tag>" + '製作:' + studio + "</tag>", file=code)
                if publisher != 'unknown':
                    print("  <tag>" + '發行:' + publisher + "</tag>", file=code)
                if cn_sub == 1:
                    print("  <tag>中文字幕</tag>", file=code)
                try:
                    for i in tag:
                        if i != 'unknown':
                            print("  <genre>" + i + "</genre>", file=code)
                except Exception as error_info:
                    self.add_text_main('[-]Error in genre: ' + str(error_info))
                if re.match('^\d{4,}', number) or re.match('n\d{4}', number) or 'HEYZO' in number.upper():
                    print("  <genre>無碼</genre>", file=code)
                if series != 'unknown':
                    print("  <genre>" + '系列:' + series + "</genre>", file=code)
                if studio != 'unknown':
                    print("  <genre>" + '製作:' + studio + "</genre>", file=code)
                if publisher != 'unknown':
                    print("  <genre>" + '發行:' + publisher + "</genre>", file=code)
                if cn_sub == 1:
                    print("  <genre>中文字幕</genre>", file=code)
                print("  <num>" + number + "</num>", file=code)
                if release != 'unknown':
                    if option == 'emby':
                        print("  <premiered>" + release + "</premiered>", file=code)
                    elif option == 'kodi' or option == 'plex':
                        print("  <release>" + release + "</release>", file=code)
                print("  <cover>" + cover + "</cover>", file=code)
                print("  <website>" + website + "</website>", file=code)
                print("</movie>", file=code)
                self.add_text_main("[+]Nfo Writed!        " + name_file + ".nfo")
        except Exception as error_info:
            self.add_text_main("[-]Write Failed!")
            self.add_text_main('[-]Error in PrintFiles: ' + str(error_info))
            self.moveFailedFolder(filepath, failed_folder)

    # ========================================================================有码片裁剪封面
    def cutImage(self, option, imagecut, path, naming_rule):
        if option == 'plex':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/fanart.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/poster.jpg')
                    self.add_text_main('[+]Poster Cut!        ' + 'poster.jpg')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                self.image_cut(path, 'fanart.jpg')
        elif option == 'emby':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/' + naming_rule + '.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + naming_rule + '.png')
                    self.add_text_main('[+]Poster Cut!        ' + naming_rule + '.png')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                self.image_cut(path, naming_rule + '.jpg')
        elif option == 'kodi':
            if imagecut == 1:
                try:
                    img = Image.open(path + '/' + naming_rule + '-fanart.jpg')
                    imgSize = img.size
                    w = img.width
                    h = img.height
                    img2 = img.crop((w / 1.9, 0, w, h))
                    img2.save(path + '/' + naming_rule + '-poster.jpg')
                    self.add_text_main('[+]Poster Cut!        ' + naming_rule + '-poster.jpg')
                except:
                    self.add_text_main('[-]Cover cut failed!')
            elif imagecut == 0:
                self.image_cut(path, naming_rule + '-fanart.jpg')

    # ========================================================================jpg复制为Backdrop
    def copyRenameJpgToBackdrop(self, option, path, naming_rule):
        if option == 'plex':
            shutil.copy(path + '/fanart.jpg', path + '/Backdrop.jpg')
            shutil.copy(path + '/poster.jpg', path + '/thumb.png')
        if option == 'emby':
            shutil.copy(path + '/' + naming_rule + '.jpg', path + '/Backdrop.jpg')
        if option == 'kodi':
            shutil.copy(path + '/' + naming_rule + '-fanart.jpg', path + '/Backdrop.jpg')

    # ========================================================================移动文件、字幕
    def pasteFileToFolder(self, filepath, path, naming_rule):
        try:
            type = str(os.path.splitext(filepath)[1])
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
            sub_type = ['.srt', '.ass', '.sub']
            for sub in sub_type:
                if os.path.exists(path_old + '/' + filename + sub):  # 字幕移动
                    shutil.move(path_old + '/' + filename + sub, path + '/' + naming_rule + sub)
                    self.add_text_main('[+]Sub moved!         ' + naming_rule + sub)
                    break
        except FileExistsError:
            failed_folder = self.Ui.lineEdit_fail.text()
            self.moveFailedFolder(filepath, failed_folder)
            self.add_text_main('[-]' + os.path.split(filepath)[1] + ' already exists!')
        except PermissionError:
            self.add_text_main('[-]PermissionError! Please run as Administrator!')
        except Exception as error_info:
            self.add_text_main('[-]Error in pasteFileToFolder: ' + str(error_info))

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
                if key == 'title' and value == '':
                    self.add_text_main('   [+]Title is None, Not Find Info!')
                    break
                if value == '' or key == 'actor_photo':
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
        if len(actor.split(',')) >= 15:
            actor = actor.split(',')[0] + ',' + actor.split(',')[1] + ',' + actor.split(',')[2] + '等演员'
        folder_name = json_data['folder_name']
        path = folder_name.replace('title', title).replace('studio', studio).replace('year', year).replace('runtime',
                                                                                                           runtime).replace(
            'director', director).replace('actor', actor).replace('release', release).replace('number', number).replace(
            'series', series).replace('publisher', publisher)
        path = path.replace('//', '/').replace('--', '-').strip('-')
        if len(path) > 200:
            self.add_text_main('[-]Error in Length of Path! Repleaced with actor/number')
            path = actor + '/' + json_data['number']
        path = success_folder + '/' + path
        path = path.replace('//', '/').replace('--', '-').strip('-')
        if not os.path.exists(path):
            path = escapePath(path, config)
            try:
                os.makedirs(path)
            except Exception as error_info:
                self.add_text_main('[-]Error in creatFolder: ' + str(error_info))
                return 'error'
        return path

    # ========================================================================从指定网站获取json_data
    def get_json_data(self, mode, number, config):
        if mode == 6:  # javdb模式
            self.add_text_main('[!]Please Wait Three Seconds！')
            time.sleep(3)
            json_data = getDataFromJSON(number, config, 6)
        else:
            json_data = getDataFromJSON(number, config, mode)
        return json_data

    # ========================================================================json_data添加到主界面
    def add_label_info(self, json_data):
        self.Ui.label_number.setText(json_data['number'])
        self.Ui.label_release.setText(json_data['release'])
        self.Ui.label_director.setText(json_data['director'])
        self.Ui.label_publish.setText(json_data['publisher'])
        self.Ui.label_studio.setText(json_data['studio'])
        self.Ui.label_label.setText(json_data['series'])
        self.Ui.label_title.setText(json_data['title'])
        self.Ui.label_actor.setText(json_data['actor'])
        self.Ui.label_outline.setText(json_data['outline'])
        self.Ui.label_tag.setText(str(json_data['tag']).strip(" [',']").replace('\'', ''))
        if self.Ui.checkBox_cover.isChecked():
            fanart_path = json_data['fanart_path']
            poster_path = json_data['poster_path']
            if os.path.exists(fanart_path):
                pix = QPixmap(fanart_path)
                self.Ui.label_fanart.setScaledContents(True)
                self.Ui.label_fanart.setPixmap(pix)  # 添加缩略图
            if os.path.exists(poster_path):
                pix = QPixmap(poster_path)
                self.Ui.label_poster.setScaledContents(True)
                self.Ui.label_poster.setPixmap(pix)  # 添加封面图

    def Core_Main(self, file_path, number_th, mode, count):
        # =======================================================================初始化所需变量
        multi_part = 0
        part = ''
        c_word = ''
        option = ''
        cn_sub = 0
        filepath = file_path  # 影片的路径
        number = number_th
        config_file = 'config.ini'
        Config = ConfigParser()
        Config.read(config_file, encoding='UTF-8')
        if self.Ui.radioButton_emby.isChecked():  # emby/jellyfin
            option = 'emby'
        elif self.Ui.radioButton_plex.isChecked():  # plex
            option = 'plex'
        elif self.Ui.radioButton_kodi.isChecked():  # kodi
            option = 'kodi'
        program_mode = Config['common']['main_mode']  # 运行模式
        failed_folder = Config['common']['failed_output_folder']  # 失败输出目录
        success_folder = Config['common']['success_output_folder']  # 成功输出目录
        # =======================================================================获取json_data
        json_data = self.get_json_data(mode, number, Config)
        # =======================================================================是否找到影片信息
        if json_data['website'] == 'timeout':
            self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
            return ''
        elif mode == 6 and json_data['actor'] == 'N/A':
            self.add_text_main('[-]Your IP Has Been Blocked By JAVDB!')
            return ''
        elif json_data['title'] == '':
            self.add_text_main('[-]Movie Data not found!')
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0, str(count) + '.' + os.path.splitext(filepath.split('/')[-1])[0])
            self.item_fail.addChild(node)
            self.moveFailedFolder(filepath, failed_folder)
            return 'not found'
        # =======================================================================调试模式
        if self.Ui.radioButton_debug_on.isChecked():
            self.debug_mode(json_data)
        # =======================================================================判断-C,-CD后缀
        if '-CD' in filepath or '-cd' in filepath:
            multi_part = 1
            part = self.get_part(filepath, failed_folder)
        if '-c.' in filepath or '-C.' in filepath or '中文' in filepath or '字幕' in filepath:
            cn_sub = 1
            c_word = '-C'  # 中文字幕影片后缀
        # =======================================================================创建输出文件夹
        self.CreatFailedFolder(failed_folder)  # 创建输出失败目录
        path = self.creatFolder(success_folder, json_data, Config)  # 创建文件夹
        if path == 'error':
            node = QTreeWidgetItem(self.item_fail)
            node.setText(0, str(count) + '.' + os.path.splitext(filepath.split('/')[-1])[0])
            self.item_fail.addChild(node)
            self.moveFailedFolder(filepath, failed_folder)
            return
        self.add_text_main('[+]Folder : ' + path)
        self.add_text_main('[+]From : ' + json_data['website'])
        # =======================================================================刮削模式
        number = json_data['number']
        naming_rule = str(self.get_naming_rule(json_data)).replace('--', '-').strip('-')
        if multi_part == 1:
            naming_rule += part
        if cn_sub == 1:
            naming_rule += c_word
        if program_mode == '1':
            # imagecut 1 裁剪右半面，0 裁剪缩略图为封面，3 下载小封面
            self.fanartDownload(option, json_data, path, naming_rule, Config, filepath, failed_folder)
            if self.smallCoverDownload(path, naming_rule, json_data, option, Config, filepath,
                                       failed_folder) == 'small_cover_error':  # 下载小封面
                json_data['imagecut'] = 0
            self.cutImage(option, json_data['imagecut'], path, naming_rule)  # 裁剪图
            self.copyRenameJpgToBackdrop(option, path, naming_rule)
            self.PrintFiles(option, path, naming_rule, cn_sub, json_data, filepath, failed_folder)  # 打印文件
            self.pasteFileToFolder(filepath, path, naming_rule)  # 移动文件
            # =======================================================================整理模式
        elif program_mode == '2':
            self.pasteFileToFolder(filepath, path, naming_rule)  # 移动文件
        # =======================================================================json添加封面项
        fanart_path = ''
        poster_path = ''
        if self.Ui.radioButton_emby.isChecked():  # emby/jellyfin
            fanart_path = path + '/' + naming_rule + '.jpg'
            poster_path = path + '/' + naming_rule + '.png'
        elif self.Ui.radioButton_plex.isChecked():  # plex
            fanart_path = path + '/fanart.jpg'
            poster_path = path + '/poster.jpg'
        elif self.Ui.radioButton_kodi.isChecked():  # kodi
            fanart_path = path + '/' + naming_rule + '-fanart.jpg'
            poster_path = path + '/' + naming_rule + '-poster.jpg'
        json_data['fanart_path'] = fanart_path
        json_data['poster_path'] = poster_path
        json_data['number'] = number
        self.add_label_info(json_data)
        self.json_array[str(count)] = json_data
        return part + c_word

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
        if not os.path.exists(failed_folder + '/'):
            try:
                os.makedirs(failed_folder + '/')
                self.add_text_main('[+]Created folder named' + failed_folder + '!')
            except Exception as error_info:
                self.add_text_main('[-]Error in CreatFailedFolder: ' + str(error_info))

    # ========================================================================删除空目录
    def CEF(self, path):
        dirs = os.listdir(path)  # 获取路径下的子文件(夹)列表
        for dir in dirs:
            try:
                os.removedirs(path + '/' + dir)  # 删除这个空文件夹
                self.add_text_main('[+]Deleting empty folder ' + path + '/' + dir)
            except:
                delete_empty_folder_failed = ''

    def AVDC_Main(self):
        # =======================================================================初始化所需变量
        config_file = 'config.ini'
        config = ConfigParser()
        config.read(config_file, encoding='UTF-8')
        success_folder = self.Ui.lineEdit_success.text()
        failed_folder = self.Ui.lineEdit_fail.text()  # 失败输出目录
        escape_folder = self.Ui.lineEdit_escape_dir.text()  # 多级目录刮削需要排除的目录
        mode = self.Ui.comboBox_website_all.currentIndex() + 1
        # =======================================================================检测更新,判断网络情况,新建failed目录,获取影片列表
        os.chdir(os.getcwd())
        if self.UpdateCheck() == 'ProxyError':
            self.add_text_main('[-]Connect Failed! Please check your Proxy or Network!')
            self.Ui.pushButton_start_cap.setEnabled(True)
            self.add_text_main("[*]======================================================")
            return
        self.CreatFailedFolder(failed_folder)  # 新建failed文件夹
        movie_list = movie_lists(escape_folder)  # 获取所有需要刮削的影片列表
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
            self.add_text_main('[!] - ' + percentage + ' [' + str(count) + '/' + count_all + '] -')
            try:
                self.add_text_main("[!]Making Data for   [" + movie + "], the number is [" + getNumber(movie) + "]")
                result = self.Core_Main(movie, getNumber(movie), mode, count)
                if result != 'not found' and getNumber(movie) != '':
                    node = QTreeWidgetItem(self.item_succ)
                    node.setText(0, str(count) + '.' + getNumber(movie) + result)
                    self.item_succ.addChild(node)
                self.add_text_main("[*]======================================================")
            except Exception as error_info:
                node = QTreeWidgetItem(self.item_fail)
                node.setText(0, str(count) + '.' + os.path.splitext(movie.split('/')[-1])[0])
                self.item_fail.addChild(node)
                self.add_text_main('[-]Error in AVDC_Main: ' + str(error_info))
                if config['common']['soft_link'] == '1':
                    self.add_text_main('[-]Link ' + movie + ' to failed folder')
                    try:
                        os.symlink(movie, failed_folder + '/')
                    except Exception as error_info:
                        self.add_text_main('[-]Error in AVDC_Main: ' + str(error_info))
                else:
                    try:
                        shutil.move(movie, failed_folder + '/')
                        self.add_text_main('[-]Move ' + movie + ' to failed folder')
                    except shutil.Error as error_info:
                        self.add_text_main('[-]Error in AVDC_Main: ' + str(error_info))
                self.add_text_main("[*]======================================================")
            self.progressBarValue.emit(int(value))
        self.Ui.pushButton_start_cap.setEnabled(True)
        self.CEF(success_folder)
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
