# AVDC


# 目录
* [简介](#简介)
* [声明](#声明)
* [FAQ](#FAQ)
* [故事](#故事)
* [GUI运行截图](#GUI运行截图)
* [效果图](#效果图)
* [如何使用](#如何使用)
* [下载](#下载)
* [简明教程](#简要教程)
* [模块安装](#1模块安装)
* [配置](#2配置configini)
* [多目录影片处理](#4多目录影片处理)
* [多集影片处理](#多集影片处理)
* [(可选)设置自定义目录和影片重命名规则](#3可选设置自定义目录和影片重命名规则)
* [运行软件](#5运行-av_data_capturepyexe)
* [影片原路径处理](#4建议把软件拷贝和电影的统一目录下)
* [异常处理（重要）](#51异常处理重要)
* [导入至媒体库](#7把jav_output文件夹导入到embykodi中等待元数据刷新完成)
* [关于群晖NAS](#8关于群晖NAS)
* [写在后面](#9写在后面)


# 简介
**命令行版(原作者)**：https://github.com/yoshiko2/AV_Data_Capture<br>
<a title="Hits" target="_blank" href="https://github.com/yoshiko2/AV_Data_Capture"><img src="https://hits.b3log.org/yoshiko2/AV_Data_Capture.svg"></a>
![](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square)
![](https://img.shields.io/github/downloads/yoshiko2/av_data_capture/total.svg?style=flat-square)
![](https://img.shields.io/github/license/yoshiko2/av_data_capture.svg?style=flat-square)
![](https://img.shields.io/github/release/yoshiko2/av_data_capture.svg?style=flat-square)
![](https://img.shields.io/badge/Python-3.7-yellow.svg?style=flat-square&logo=python)<br>
**GUI版(本项目)**：<br>
<a title="Hits" target="_blank" href="https://github.com/moyy996/avdc"><img src="https://hits.b3log.org/moyy996/AVDC.svg"></a>
![](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square)
![](https://img.shields.io/github/downloads/moyy996/avdc/total.svg?style=flat-square)
![](https://img.shields.io/github/license/moyy996/avdc.svg?style=flat-square)
![](https://img.shields.io/github/release/moyy996/avdc.svg?style=flat-square)
![](https://img.shields.io/badge/Python-3.6-yellow.svg?style=flat-square&logo=python)
![](https://img.shields.io/badge/Pyqt-5-blue.svg?style=flat-square)<br>

### 主要功能
* **日本电影元数据 抓取工具 | 刮削器**，配合本地影片管理软件EMBY,KODI，PLEX等管理本地影片，该软件起到分类与元数据抓取作用，利用元数据信息来分类，供本地影片分类整理使用。<br>
* 可**批量抓取**，也可**单个抓取**。可抓取**子目录下视频**，**多集视频**（-cd1/-cd2）。<br>
* 目前可抓取网站：**javbus,javdb,avsox,fc2club,fanza**。<br>
### 反馈
* 欢迎使用体验,有**程序BUG问题、功能建议**,可进**电报群**反馈    [点击进群](https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ)<br>

# 声明
* 本软件仅供**技术交流，学术交流**使用<br>
* 本软件作者编写出该软件旨在学习Python3，提高编程水平<br>
* 用户在使用该软件前，请用户自觉遵守当地法律法规，如果该软件使用过程中存在违反当地法律法规的行为，请勿使用该软件<br>
* 用户使用该软件时，若产生一切违法行为由用户承担<br>
* 严禁用户使用于商业和个人其他意图<br>
* 本软件作者保留最终决定权和最终解释权<br>

**若用户不同意上述条款任意一条，请勿使用该软件**<br>

# FAQ
### 这软件能下片吗？
* 该软件不提供任何影片下载地址，仅供本地影片分类整理使用。
### 什么是元数据？
* 元数据包括了影片的：封面，导演，演员，简介，类型......
### 软件收费吗？
* 软件永久免费。**除了作者钦点以外**
### 软件运行异常怎么办？
* 认真看 [异常处理（重要）](#5异常处理重要)

# 故事
[点击跳转至原作者博客文章](https://yoshiko2.github.io/2019/10/18/AVDC/)

# GUI运行截图

## **主界面，设置，工具，关于**

<div align="center">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/main_window.png" height="300">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/setting.png" height="300">
</div>
<div align="center">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/tool.png" height="300">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/about.png" height="300">
</div>

# 效果图
### **1、输出目录文件结构**<br>

<div>
<img src="https://github.com/moyy996/AVDC/blob/master/readme/tree-jav-output.png" height="700">
</div>

### **2、媒体库：以下为刮削、导入后的EMBY**<br>

<div>
<img src="https://github.com/moyy996/AVDC/blob/master/readme/emby.png" height="400">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/emby_each.png" height="400">
</div>

# 如何使用
### 下载
* **Release** 的程序可脱离**python环境**运行，源码包需要 [安装模块](#1模块安装)<br>
* **Release** 下载地址(**仅限Windows**): [点击下载](https://github.com/moyy996/AVDC/releases)<br>
* **源码包** 下载地址(**Windows,Linux,MacOS**): [点击下载](https://github.com/moyy996/AVDC/archive/master.zip)<br>

* Windows Python环境: [点击前往](https://www.python.org/downloads/windows/) 选中executable installer下载
* MacOS Python环境： [点击前往](https://www.python.org/downloads/mac-osx/)
* Linux Python环境：Linux用户懂的吧，不解释下载地址

### 简要教程:<br>
* **1.把软件拉到和电影的同一目录或者上级目录**<br>
* **2.运行AVDC.exe，配置设置页各项（配置方法请看以下教程）**<br>
* **3.点击开始等待完成(出错请开调试模式后截图)**<br>
* **4.把JAV_output导入至KODI,EMBY,PLEX中。**<br>
* **详细请看以下教程**<br>

## 1.模块安装
如果运行**源码**版，运行前请安装**Python环境**和安装以下**模块**<br>  
在终端/cmd/Powershell中输入以下代码来安装模块<br>
**1、批量**从py-require.txt安装<br>
>pip install -r py-require.txt<br>

**2、单个**按需安装<br>
>pip install requests<br>
>pip install pyquery<br>
>pip install lxml<br>
>pip install Beautifulsoup4<br>
>pip install pillow<br>
>pip install pyqt5<br>
>pip install pyqt5-tools<br>

## 2.配置设置
**设置界面**
![](https://github.com/moyy996/AVDC/blob/master/readme/setting.png)

---
#### （1）、普通模式/整理模式
  **1、普通模式**：通过番号刮削数据，包括元数据、封面图、缩略图、背景图。<br>
  **2、整理模式**：仅根据女优把电影命名为番号并分类到女优名称的文件夹下。<br>

---
#### （2）、软链接模式：使用此模式，要以```管理员身份```运行。
  刮削完**不移动视频**，而是在相应目录创建**软链接**（类似于快捷方式），方便PT下载完既想刮削又想继续上传的仓鼠党同志。

---
#### （3）、调试模式
  输出番号的**元数据**，包括封面，导演，演员，简介等。

---
#### （4）、排除目录
  在多层目录刮削时**排除所填目录**。

---
#### （5）、异常字符
  在创建文件夹时，**删除指定的字符**。

---
#### （6）、命名规则
  **1、目录命名**：存放视频数据的目录名，支持**多层目录**，例：actor/studio/number-title ,  目录之间用**斜线/**，两个选项之间用**短横杠-**。<br>
  **2、视频标题**：nfo中的标题命名。例：number-title。可以自定义，两个选项之间需要**短横杠-**。<br>
  **3、可选项**为title（片名）、actor（演员）、studio（公司）、director（导演）、release（发售日）、year（发行年份）、numbe（番号）、runtime（时长）<br>

---
#### （7）、网络设置 
>proxy=127.0.0.1:1081<br>

**proxy**行设置本地代理地址和端口，支持Shadowxxxx/X,V2XXX本地代理端口，代理软件开**全局模式**  ,**建议使用日本代理**。 

**连接超时重试设置**<br>
>timeout=10<br>

10为超时重试时间 单位：秒<br>
**连接重试次数设置**<br>
>retry=3<br>

3即为重试次数<br>

---
### （8）、媒体库选择 
如果是PLEX，请安装插件：```XBMCnfoMoviesImporter```

---
### （9）、排除指定字符和目录
**1、排除字符**:指定字符删除，例如```排除字符： \()```，删除标题中```\()```字符  <br>
**2、排除目录**:指定目录，例如```排除目录： failed,JAV_output```，多目录刮削时跳过failed,JAV_output  <br>

---
### （10）、工具
**1、视频移动**：可将程序目录下除排除目录下的所有视频，移动到程序目录下。<br>
**2、单文件刮削**：偶尔有失败情况时，选择这个视频文件，使用文件名当番号进行刮削。<br>
条件：文件名中间要有下划线或者减号"_","-"，没有多余的内容只有番号为最佳，可以让软件更好获取元数据<br>
对于多影片重命名，可以用[ReNamer](http://www.den4b.com/products/renamer)来批量重命名<br>

---
### （11）、网站选择
**1、All website**: 使用avsox,javbus,fanza,javdb,fc2club进行刮削。<br>
**2、Only javdb**: 仅使用javdb进行刮削。<br>

## 3.多目录影片处理
可以遍历**程序所在目录及子目录**（除指定的**排除目录**），对遍历到的所有视频进行刮削，成功则同**元数据、封面图**一起输出到**JAV_output**目录，失败移入**failed**目录。 

## 4.多集影片处理
可以把多集电影按照集数后缀命名为类似**ssni-xxx-cd1.mp4,ssni-xxx-cd2.mp4，abp-xxx-CD1.mp4**的规则，只要含有```-CDn./-cdn.```类似命名规则，即可使用分集功能

## 5.运行 ```AVDC_Main.py/AVDC.exe```
当文件名包含:<br>
中文，字幕，-c., -C., 处理元数据时会加上**中文字幕**标签
## 5.1 异常处理（重要）
### 请确保软件是完整地！确保ini文件内容是和下载提供ini文件内容的一致的！
---
### 5.1.1、关于软件打开就闪退
可以打开cmd命令提示符，把 ```AVDC_Main.py/AVDC.exe```拖进cmd窗口回车运行，查看错误，出现的错误信息**依据以下条目解决**

---
### 5.1.2、报```Connect Failed! Please check your Proxy or Network!```错误
可以把文件的**proxy=后面的地址和端口删除**，并开启代理软件全局模式，或者重启电脑，代理软件，网卡

---
### 5.1.3、关于 ```Updata_check``` 和 ```JSON``` 相关的错误
跳转 [网络设置](#网络设置)

---
### 5.1.4、关于字幕文件移动功能
字幕文件前缀必须与影片文件前缀一致，才可以使用该功能

---
### 5.1.5、关于```FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'JAV_output''``` 
在软件所在文件夹下新建 JAV_output 文件夹，可能是你没有把软件拉到和电影的同一目录

---
### 5.1.6、关于连接拒绝的错误
请设置好[代理](#针对某些地区的代理设置)<br>

---
### 5.1.7、关于Nonetype,xpath报错
同上<br>

---
### 5.1.8、关于番号提取失败或者异常
**目前可以提取元素的影片:JAVBUS、JAVDB、AVSOX、FANZA、FC2CLUB上有元数据的电影，请确保视频名能在这些网站找到**<br>

---
### 5.1.9、关于PIL/image.py
暂时无解，可能是网络问题或者pillow模块打包问题，你可以用源码运行（要安装好第一步的模块）


## 6.软件会自动把元数据获取成功的电影移动到JAV_output文件夹中，根据演员分类，失败的电影移动到failed文件夹中。
## 7.把JAV_output文件夹导入到EMBY,KODI,PLEX中，等待元数据刷新，完成
## 8.关于群晖NAS
开启SMB在Windows上挂载为网络磁盘即可使用本软件，也适用于其他NAS
## 9.写在后面
怎么样，看着自己的日本电影被这样完美地管理，是不是感觉成就感爆棚呢?<br>



