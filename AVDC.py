# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AVDC.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AVDV(object):
    def setupUi(self, AVDV):
        AVDV.setObjectName("AVDV")
        AVDV.resize(1017, 722)
        self.centralwidget = QtWidgets.QWidget(AVDV)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(230, 0, 811, 721))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_avdc = QtWidgets.QWidget()
        self.page_avdc.setObjectName("page_avdc")
        self.pushButton_start_cap = QtWidgets.QPushButton(self.page_avdc)
        self.pushButton_start_cap.setGeometry(QtCore.QRect(640, 30, 121, 61))
        self.pushButton_start_cap.setObjectName("pushButton_start_cap")
        self.textBrowser_log_main = QtWidgets.QTextBrowser(self.page_avdc)
        self.textBrowser_log_main.setGeometry(QtCore.QRect(10, 100, 761, 601))
        self.textBrowser_log_main.setObjectName("textBrowser_log_main")
        self.stackedWidget.addWidget(self.page_avdc)
        self.page_javdb = QtWidgets.QWidget()
        self.page_javdb.setObjectName("page_javdb")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.page_javdb)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 410, 160, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_page = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_page.setFrameShape(QtWidgets.QFrame.Box)
        self.label_page.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_page.setObjectName("label_page")
        self.verticalLayout_2.addWidget(self.label_page)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_number = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_number.setFrameShape(QtWidgets.QFrame.Box)
        self.label_number.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_number.setObjectName("label_number")
        self.verticalLayout_2.addWidget(self.label_number)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_actor = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_actor.setFrameShape(QtWidgets.QFrame.Box)
        self.label_actor.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_actor.setObjectName("label_actor")
        self.verticalLayout_2.addWidget(self.label_actor)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page_javdb)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_site = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_site.setObjectName("label_site")
        self.horizontalLayout_4.addWidget(self.label_site)
        self.lineEdit_site = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_site.setInputMask("")
        self.lineEdit_site.setText("")
        self.lineEdit_site.setMaxLength(32767)
        self.lineEdit_site.setObjectName("lineEdit_site")
        self.horizontalLayout_4.addWidget(self.lineEdit_site)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.page_javdb)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(540, 10, 211, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_path = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_path.setObjectName("label_path")
        self.horizontalLayout_3.addWidget(self.label_path)
        self.lineEdit_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_path.setInputMask("")
        self.lineEdit_path.setText("")
        self.lineEdit_path.setMaxLength(32767)
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout_3.addWidget(self.lineEdit_path)
        self.progressBar = QtWidgets.QProgressBar(self.page_javdb)
        self.progressBar.setGeometry(QtCore.QRect(10, 680, 741, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.page_javdb)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 741, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox_page = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_page.setObjectName("comboBox_page")
        self.comboBox_page.addItem("")
        self.comboBox_page.addItem("")
        self.comboBox_page.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_page)
        self.lineEdit_page_num = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_page_num.setObjectName("lineEdit_page_num")
        self.horizontalLayout_2.addWidget(self.lineEdit_page_num)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox_single = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_single.setObjectName("checkBox_single")
        self.horizontalLayout_2.addWidget(self.checkBox_single)
        self.checkBox_cover = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox_cover.setObjectName("checkBox_cover")
        self.horizontalLayout_2.addWidget(self.checkBox_cover)
        self.pushButton_start_javdb = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_start_javdb.setMouseTracking(False)
        self.pushButton_start_javdb.setObjectName("pushButton_start_javdb")
        self.horizontalLayout_2.addWidget(self.pushButton_start_javdb)
        self.textEdit_log = QtWidgets.QTextEdit(self.page_javdb)
        self.textEdit_log.setGeometry(QtCore.QRect(10, 90, 741, 311))
        self.textEdit_log.setReadOnly(True)
        self.textEdit_log.setObjectName("textEdit_log")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.page_javdb)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(220, 640, 160, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_grade_fan = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        self.label_grade_fan.setFrameShape(QtWidgets.QFrame.Box)
        self.label_grade_fan.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_grade_fan.setObjectName("label_grade_fan")
        self.horizontalLayout_5.addWidget(self.label_grade_fan)
        self.gridLayoutWidget = QtWidgets.QWidget(self.page_javdb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(420, 410, 331, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_cover = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_cover.setEnabled(True)
        self.label_cover.setFrameShape(QtWidgets.QFrame.Box)
        self.label_cover.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cover.setObjectName("label_cover")
        self.gridLayout.addWidget(self.label_cover, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.page_javdb)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(220, 410, 161, 221))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_pic = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_pic.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pic.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pic.setObjectName("label_pic")
        self.gridLayout_2.addWidget(self.label_pic, 0, 0, 1, 1)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.page_javdb)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(500, 640, 160, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_grade_pos = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.label_grade_pos.setFrameShape(QtWidgets.QFrame.Box)
        self.label_grade_pos.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_grade_pos.setObjectName("label_grade_pos")
        self.horizontalLayout_6.addWidget(self.label_grade_pos)
        self.stackedWidget.addWidget(self.page_javdb)
        self.page_tool = QtWidgets.QWidget()
        self.page_tool.setObjectName("page_tool")
        self.pushButton_javdb_sp = QtWidgets.QPushButton(self.page_tool)
        self.pushButton_javdb_sp.setGeometry(QtCore.QRect(20, 10, 201, 71))
        self.pushButton_javdb_sp.setObjectName("pushButton_javdb_sp")
        self.label_7 = QtWidgets.QLabel(self.page_tool)
        self.label_7.setGeometry(QtCore.QRect(240, 10, 521, 101))
        self.label_7.setObjectName("label_7")
        self.pushButton_move_mp4 = QtWidgets.QPushButton(self.page_tool)
        self.pushButton_move_mp4.setGeometry(QtCore.QRect(20, 120, 201, 71))
        self.pushButton_move_mp4.setObjectName("pushButton_move_mp4")
        self.lineEdit_escape_dir_move = QtWidgets.QLineEdit(self.page_tool)
        self.lineEdit_escape_dir_move.setGeometry(QtCore.QRect(320, 120, 431, 24))
        self.lineEdit_escape_dir_move.setObjectName("lineEdit_escape_dir_move")
        self.label_41 = QtWidgets.QLabel(self.page_tool)
        self.label_41.setGeometry(QtCore.QRect(240, 120, 81, 24))
        self.label_41.setObjectName("label_41")
        self.label_8 = QtWidgets.QLabel(self.page_tool)
        self.label_8.setGeometry(QtCore.QRect(240, 150, 421, 41))
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_tool)
        self.page_setting = QtWidgets.QWidget()
        self.page_setting.setObjectName("page_setting")
        self.pushButton_save_config = QtWidgets.QPushButton(self.page_setting)
        self.pushButton_save_config.setGeometry(QtCore.QRect(170, 630, 361, 28))
        self.pushButton_save_config.setObjectName("pushButton_save_config")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.page_setting)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 370, 751, 121))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.lineEdit_proxy = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_proxy.setObjectName("lineEdit_proxy")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_proxy)
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.lineEdit_timeout = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_timeout.setObjectName("lineEdit_timeout")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_timeout)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_27.setObjectName("label_27")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.lineEdit_retry = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.lineEdit_retry.setObjectName("lineEdit_retry")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_retry)
        self.formLayoutWidget = QtWidgets.QWidget(self.page_setting)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 510, 751, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_34 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_34.setObjectName("label_34")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.label_35 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_35.setObjectName("label_35")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.lineEdit_dir_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_dir_name.setObjectName("lineEdit_dir_name")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_dir_name)
        self.label_36 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_36.setObjectName("label_36")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_36)
        self.lineEdit_media_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_media_name.setObjectName("lineEdit_media_name")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_media_name)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_setting)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 0, 751, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_3.addWidget(self.label_33)
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName("groupBox")
        self.radioButton_common = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_common.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_common.setObjectName("radioButton_common")
        self.radioButton_sort = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_sort.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_sort.setObjectName("radioButton_sort")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_soft_on = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_soft_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_soft_on.setObjectName("radioButton_soft_on")
        self.radioButton_soft_off = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_soft_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_soft_off.setObjectName("radioButton_soft_off")
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.radioButton_debug_on = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_debug_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_debug_on.setObjectName("radioButton_debug_on")
        self.radioButton_debug_off = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_debug_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_debug_off.setObjectName("radioButton_debug_off")
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton_update_on = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_update_on.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_update_on.setObjectName("radioButton_update_on")
        self.radioButton_update_off = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_update_off.setGeometry(QtCore.QRect(490, 10, 181, 19))
        self.radioButton_update_off.setObjectName("radioButton_update_off")
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.radioButton_emby = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_emby.setGeometry(QtCore.QRect(190, 10, 181, 19))
        self.radioButton_emby.setObjectName("radioButton_emby")
        self.radioButton_plex = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_plex.setGeometry(QtCore.QRect(420, 10, 181, 19))
        self.radioButton_plex.setObjectName("radioButton_plex")
        self.radioButton_kodi = QtWidgets.QRadioButton(self.groupBox_5)
        self.radioButton_kodi.setGeometry(QtCore.QRect(600, 10, 115, 19))
        self.radioButton_kodi.setObjectName("radioButton_kodi")
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.page_setting)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 230, 751, 121))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_37 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.lineEdit_fail = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_fail.setObjectName("lineEdit_fail")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_fail)
        self.label_39 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_39.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.lineEdit_success = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_success.setObjectName("lineEdit_success")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_success)
        self.label_40 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.lineEdit_escape_dir = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_dir.setObjectName("lineEdit_escape_dir")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_escape_dir)
        self.label_38 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.lineEdit_escape_char = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.lineEdit_escape_char.setObjectName("lineEdit_escape_char")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_escape_char)
        self.stackedWidget.addWidget(self.page_setting)
        self.page_about = QtWidgets.QWidget()
        self.page_about.setObjectName("page_about")
        self.textBrowser_about = QtWidgets.QTextBrowser(self.page_about)
        self.textBrowser_about.setGeometry(QtCore.QRect(30, 20, 721, 681))
        self.textBrowser_about.setObjectName("textBrowser_about")
        self.stackedWidget.addWidget(self.page_about)
        self.widget_setting = QtWidgets.QWidget(self.centralwidget)
        self.widget_setting.setGeometry(QtCore.QRect(0, 0, 221, 721))
        self.widget_setting.setObjectName("widget_setting")
        self.label_ico = QtWidgets.QLabel(self.widget_setting)
        self.label_ico.setGeometry(QtCore.QRect(10, 380, 201, 321))
        self.label_ico.setObjectName("label_ico")
        self.layoutWidget = QtWidgets.QWidget(self.widget_setting)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 201, 360))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.pushButton_min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_min.setObjectName("pushButton_min")
        self.horizontalLayout.addWidget(self.pushButton_min)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_main = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_main.setObjectName("pushButton_main")
        self.verticalLayout.addWidget(self.pushButton_main)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_tool = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_tool.setObjectName("pushButton_tool")
        self.verticalLayout.addWidget(self.pushButton_tool)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_setting = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_setting.setObjectName("pushButton_setting")
        self.verticalLayout.addWidget(self.pushButton_setting)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_about = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_about.setObjectName("pushButton_about")
        self.verticalLayout.addWidget(self.pushButton_about)
        AVDV.setCentralWidget(self.centralwidget)

        self.retranslateUi(AVDV)
        self.stackedWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(AVDV)

    def retranslateUi(self, AVDV):
        _translate = QtCore.QCoreApplication.translate
        AVDV.setWindowTitle(_translate("AVDV", "AVDC-3.0"))
        self.pushButton_start_cap.setText(_translate("AVDV", "开始"))
        self.label_9.setText(_translate("AVDV", "页数："))
        self.label_page.setText(_translate("AVDV", "None"))
        self.label.setText(_translate("AVDV", "番号："))
        self.label_number.setText(_translate("AVDV", "None"))
        self.label_2.setText(_translate("AVDV", "演员："))
        self.label_actor.setText(_translate("AVDV", "None"))
        self.label_site.setText(_translate("AVDV", "网址："))
        self.label_path.setText(_translate("AVDV", "路径："))
        self.comboBox_page.setItemText(0, _translate("AVDV", "只本页"))
        self.comboBox_page.setItemText(1, _translate("AVDV", "此页及以后"))
        self.comboBox_page.setItemText(2, _translate("AVDV", "此页及以前"))
        self.label_5.setText(_translate("AVDV", "页"))
        self.checkBox_single.setText(_translate("AVDV", "单体作品"))
        self.checkBox_cover.setText(_translate("AVDV", "显示封面"))
        self.pushButton_start_javdb.setText(_translate("AVDV", "开始"))
        self.label_3.setText(_translate("AVDV", "颜值："))
        self.label_grade_fan.setText(_translate("AVDV", "None"))
        self.label_cover.setText(_translate("AVDV", "缩略图"))
        self.label_pic.setText(_translate("AVDV", "封面图"))
        self.label_4.setText(_translate("AVDV", "颜值："))
        self.label_grade_pos.setText(_translate("AVDV", "None"))
        self.pushButton_javdb_sp.setText(_translate("AVDV", "JAVDB-爬虫"))
        self.label_7.setText(_translate("AVDV", "1、支持爬取-----仅本页，此页及之后几页，此页及前几页\n"
"2、支持过滤多女优作品，仅保留单体作品\n"
"3、显示封面可选，（不方便或者有他人的时候，\n"
"     把勾去掉，立即关闭封面显示，替换成安全的图片）\n"
"4、有颜值过滤，把阈值设置了75，颜值75以上的保存在beauty的同名路径下"))
        self.pushButton_move_mp4.setText(_translate("AVDV", "视频移动"))
        self.label_41.setText(_translate("AVDV", "排除目录："))
        self.label_8.setText(_translate("AVDV", "程序所在目录的所有子目录下的视频移动到当前目录下"))
        self.pushButton_save_config.setText(_translate("AVDV", "保存"))
        self.label_24.setText(_translate("AVDV", "代理设置"))
        self.label_25.setText(_translate("AVDV", "   代理:                 "))
        self.label_26.setText(_translate("AVDV", "   超时重试时间：         "))
        self.label_27.setText(_translate("AVDV", "   重试次数：             "))
        self.label_34.setText(_translate("AVDV", "命名规则"))
        self.label_35.setText(_translate("AVDV", "   目录命名：             "))
        self.label_36.setText(_translate("AVDV", "   视频标题(媒体库中)：   "))
        self.label_33.setText(_translate("AVDV", "普通设定"))
        self.groupBox.setTitle(_translate("AVDV", "   模式："))
        self.radioButton_common.setText(_translate("AVDV", "普通模式"))
        self.radioButton_sort.setText(_translate("AVDV", "整理模式"))
        self.groupBox_2.setTitle(_translate("AVDV", "   软链接模式："))
        self.radioButton_soft_on.setText(_translate("AVDV", "开"))
        self.radioButton_soft_off.setText(_translate("AVDV", "关"))
        self.groupBox_3.setTitle(_translate("AVDV", "   调试模式："))
        self.radioButton_debug_on.setText(_translate("AVDV", "开"))
        self.radioButton_debug_off.setText(_translate("AVDV", "关"))
        self.groupBox_4.setTitle(_translate("AVDV", "   检测更新："))
        self.radioButton_update_on.setText(_translate("AVDV", "开"))
        self.radioButton_update_off.setText(_translate("AVDV", "关"))
        self.groupBox_5.setTitle(_translate("AVDV", "   媒体库："))
        self.radioButton_emby.setText(_translate("AVDV", "emby/jellyfin"))
        self.radioButton_plex.setText(_translate("AVDV", "plex"))
        self.radioButton_kodi.setText(_translate("AVDV", "kodi"))
        self.label_37.setText(_translate("AVDV", "   失败输出目录：         "))
        self.label_39.setText(_translate("AVDV", "   成功输出目录：         "))
        self.label_40.setText(_translate("AVDV", "   排除目录："))
        self.label_38.setText(_translate("AVDV", "   异常字符：             "))
        self.textBrowser_about.setHtml(_translate("AVDV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt;\">gui made by </span><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ff0000;\">moy</span><span style=\" font-family:\'宋体\'; font-size:12pt; color:#ff0000;\">y</span><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ff0000;\">996</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">，</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">core made by </span><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ff0000;\">yoshiko2</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt;\">tg</span><span style=\" font-family:\'宋体\'; font-size:12pt;\">官方电报群</span><span style=\" font-family:\'Calibri\'; font-size:12pt;\">:</span><a href=\"https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ\"><span style=\" font-family:\'Calibri\'; font-size:12pt; text-decoration: underline; color:#0000ff;\"> https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:12pt;\">项目地址：</span><a href=\"https://github.com/yoshiko2/AV_Data_Capture\"><span style=\" font-family:\'Calibri\'; font-size:12pt; text-decoration: underline; color:#0000ff;\">https://github.com/yoshiko2/AV_Data_Capture</span></a></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/2.3\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">2.3</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2020.1.27 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">祝大家农历新年快乐！</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增了</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FANZA/DMM cid</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">番号抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">取消</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">config.ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">原有的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">movie_location</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，取而代之的是更强大的多级目录影片扫描功能 （此代码提交来自</span><a href=\"https://github.com/moyy996\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; font-weight:600; text-decoration: underline; color:#0000ff;\">moyy996</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复了无码封面下载</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">0KB</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">封面的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">暂不支持多级目录下的字幕文件整理功能，如果有需要请将影片与字幕文件的前缀重命名一致，并放到与程序同一目录下</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/2.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">2.2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.1.22 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">感谢</span><a href=\"https://github.com/moyy996\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; font-weight:600; text-decoration: underline; color:#0000ff;\">moyy996</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">提交的代码</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">javdb</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取标题、番号、演员</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">bug</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，使用小封面。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">DV-0000,LUXU-0000</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">类似的番号可以通过</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">javdb</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取。</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">release</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">/</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">导致多级目录问题。</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/2.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">2.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.1.19 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">avsox</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">无码抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">导出</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">emby/jellyfin</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">nfo</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件中日期标签修改为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&lt;premiered&gt;</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/2.0\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">2.0</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2020.1.19 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复了</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.9</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">版本乱码问题</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取恢复为优先从</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">fc2club</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><a href=\"#%E8%BD%AF%E9%93%BE%E6%8E%A5\"><span style=\" font-family:\'宋体\'; font-size:10.5pt; text-decoration: underline; color:#0000ff;\">软链接</span></a><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">功能</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><a href=\"#%E5%85%B3%E4%BA%8E%E5%AD%97%E5%B9%95%E6%96%87%E4%BB%B6%E7%A7%BB%E5%8A%A8%E5%8A%9F%E8%83%BD\"><span style=\" font-family:\'宋体\'; font-size:10.5pt; text-decoration: underline; color:#0000ff;\">字幕文件移动</span></a><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">功能</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.9\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.9</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.12.17 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">出现乱码问题</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.8\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.8</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.12.15 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">和素人抓取失效</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.7\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.7</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.11.24 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复了带</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">-C.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">后缀的中文字幕影片在</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">EMBY</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中的封面显示异常问题</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.6\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.6</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.11.6 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">kodi</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">模式下带中文字幕后缀影片处理后图片不显示中文字幕后缀</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">-C</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.4\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.4</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.11.4 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修正封面读取失败，增加路径</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">escape</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">字符，在</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> config.ini [escape] literals </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增指定字符删除功能（感谢</span><a href=\"https://github.com/ninjadogz\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; font-weight:600; text-decoration: underline; color:#0000ff;\">ninjadogz</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修正某些情况下网站数据导致的错误</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">（感谢</span><a href=\"https://github.com/biaji\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; font-weight:600; text-decoration: underline; color:#0000ff;\">biaji</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">增加</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">kodi</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">选项，完善</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">kodi</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">图片显示与分集处理 （感谢</span><a href=\"https://github.com/lhiqwj173\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt; font-weight:600; text-decoration: underline; color:#0000ff;\">lhiqwj173</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改进分集机制</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">带中文字幕影片在处理后文件仍会有</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">-C</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">结尾，不影响</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">NFO</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件的标题</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">程序更稳定</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">配置文件</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> config.ini </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中的 </span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">[directory_capture] </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改为 </span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">[move_location] path=</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，取消了星号</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">*</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">功能，会移动指定目录下的影片到与程序同一目录下</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.3\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.3</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.10.6 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，提高稳定性（作者断断续续写也不清楚修复了什么，反正能用就对了）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><a href=\"#%E8%B0%83%E8%AF%95%E6%A8%A1%E5%BC%8F\"><span style=\" font-family:\'宋体\'; font-size:10.5pt; text-decoration: underline; color:#0000ff;\">调试模式</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改进程序代码结构</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.8.29 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复素人抓取</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改进部分功能</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/1.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">1.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.8.18 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">项目进入正式版</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增网站</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">avsox</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，无码影片抓取成功率提高至少</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">50%</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改进无码影片小封面抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改进了元数据获取失败，请求番号至其他网站抓取的过程</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.9\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.9 更新</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.8.12 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">siro</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复部分小</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">config.ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">[directory_capture]</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">下的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">directory= </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，如果为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">*</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">就遍历程序目录下所有子目录下的影片，推荐用于</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BT</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">下载后多个文件夹下的影片抓取</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.8\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.8 更新</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.8.10</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">支持修改失败输出目录名称和成功输出目录名称</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改善对</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">linux</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">和</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">macos</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">的支持、</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">siro</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">系列抓取失败</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">bug</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改善程序源码</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.6\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.6</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.7.14 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：程序目录下</span><a href=\"#%E6%8A%93%E5%8F%96%E7%9B%AE%E5%BD%95%E9%80%89%E6%8B%A9\"><span style=\" font-family:\'宋体\'; font-size:10.5pt; text-decoration: underline; color:#0000ff;\">抓取目录的选择</span></a></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：本地</span><a href=\"#%E5%AA%92%E4%BD%93%E5%BA%93%E9%80%89%E6%8B%A9\"><span style=\" font-family:\'宋体\'; font-size:10.5pt; text-decoration: underline; color:#0000ff;\">媒体库选择</span></a><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">（</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">NFO</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件内容类型），可选择</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">emby</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">和</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">plex</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，不建议修改为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">PLEX</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">PLEX</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">未完善</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复：完善错误提示</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.5\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.5</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.7.9 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">config.ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">不存在时写入错误导致的闪退问题</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复若干</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.4\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.4</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.7.4 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更名</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">proxy.ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">config.ini</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复无码抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修改封面图为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">poster.png, fanart.jpg</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">如果文件名存在</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">”</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中文</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">“</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">”</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">字幕</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">“</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&quot;-c.&quot;</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，会给电影新增中文字幕标签</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.29 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修改</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件夹下</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">location_rule</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">\'JAV_output/\'+actor+\'/\'+number (</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">由于</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">Windows API</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">最长路径字符限制问题</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">)</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复素人系列抓取异常</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.11.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 11.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.29 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">大更新 </span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">Big Update</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：中文字幕标签（文件名需包含</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&quot;-c.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">后缀</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&quot;</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">或</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&quot;-C.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">后缀</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">&quot;</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">）</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：延迟设置</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：连接重试机制</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：抓取时显示总抓取进度，完成百分比</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：抓取网站</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:javdb</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增：野鸡番号可拖到</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">core.py/exe</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">处理</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复：标题的非法字符导致文件夹和文件创建失败的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复：无码抓取</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.6\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.6</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.22 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复素人系列抓取</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复标题导致的文件夹和文件新建失败的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG </span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.5\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.5</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.22</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">凌晨更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">6.22</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">中午重新上传</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修改</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">ini</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">紧急修复奇葩文件名导致无法新建文件和文件夹的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">之所以有部分</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">元数据不能正确获取，是因为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">属于半野鸡系列</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">AV</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，元数据杂乱或缺失的现象很常见</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">由于网站原因，素人系列元数据抓取易混淆</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.4\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.4</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.21</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修改东京热</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">N</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">系列番号内嵌在标题的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG<br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修改获取的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">JPG</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件名为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">Backdrop.jpg</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">，针对</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">EMBY<br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取异常（因外部网站原因，元数据可能不完整）</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.3\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.3</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.20</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增更新检测，版本显示</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增去除</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件名中的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">PPV</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">功能</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">适配更多的素人系列视频番号前缀，扩大素人视频系列搜索范围</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">仍然有部分素人系列视频元数据无法正确抓取（数据混淆）</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.19</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复代理无法访问</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG<br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">TS</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">媒体格式适配</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">提高程序稳定性</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">素人系列爬取的数据容易混淆</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.18</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">元数据抓取异常</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.10\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 10</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.17</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增自定义目录规则功能</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增自定义命名规则功能</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.8\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 8</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.11</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:<br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">几乎无敌的番号提取</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">增加对东京热</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">(n1xxx)</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">番号的支持</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增自定义</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">http</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">代理设置，支持</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">shadowsocks/R,V2RAY</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">本地代理连接</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.7\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 7</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.9</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更叼的错误处理和错误提示 例如：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">(</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">程序最后需要按回车键结束程序，在此之前可以检查错误信息</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">)<br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">300MAAN,326SCP,326URF</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">系列电影元数据抓取的支持</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.6.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 6.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.4</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.6\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 6</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.2 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:<br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">在</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">JAVBUS</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">抓取的影片数据支持标签功能</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">多演员标签</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.5\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 5</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.6.1 </span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">重大更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:<br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增对</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">FC2</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">系列视频抓取的支持</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增对</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">SIRO 259LUXU</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">系列视频抓取的支持</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">大幅度优化无码视频抓取（个别例外）</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.4\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 4</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.30</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增重命名文件时替换</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">\'_\'</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">为</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">\'-\'</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">的功能</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">完善错误提示</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.3.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 3.2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.29</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">午时更新：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">完善错误提示</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.3.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 3.1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.29</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复无法输出</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">NFO</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">文件和影片介绍的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.3\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 3</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.28</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:<br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更便于阅读的源码</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">core.py</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">（不影响程序本体）</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">新增</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">删除番号获取失败形成的空目录</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.2.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 2.1 紧急修复</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.28</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">:<br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">修复</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">EXE</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">版程序无法运行的</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">BUG</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.2\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 2</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">2019.5.27</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更新：</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />1.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">支持</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\">MP4,AVI,RMVB,WMV,MOV,MKV,FLV</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">格式</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />2.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">更智能的程序终止机制</span><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"><br />3.</span><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">改善程序源码结构，更便于阅读</span></p>\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/yoshiko2/AV_Data_Capture/releases/tag/0.1\"><span style=\" font-family:\'宋体\'; font-size:13.5pt; font-weight:600; text-decoration: underline; color:#ff0000;\">Beta 1</span></a></h3>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">2019.5.26更新</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\'; font-size:10.5pt;\">第一个版本</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:10.5pt;\"> </span></p></body></html>"))
        self.label_ico.setText(_translate("AVDV", "图标"))
        self.pushButton_close.setText(_translate("AVDV", "X"))
        self.pushButton_min.setText(_translate("AVDV", "-"))
        self.pushButton_main.setText(_translate("AVDV", "主界面"))
        self.pushButton_tool.setText(_translate("AVDV", "工具"))
        self.pushButton_setting.setText(_translate("AVDV", "设置"))
        self.pushButton_about.setText(_translate("AVDV", "关于"))
