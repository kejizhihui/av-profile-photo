# AVDC


# 目录
* [1.简介](#1简介)<br>
* [2.反馈](#2反馈)
* [3.常见番号命名规范(必看!!!!!!!!!)](#3常见番号命名规范)
* [4.效果图](#4效果图)
    * [界面截图](#41界面截图)
    * [文件结构](#43文件结构)
    * [媒体库](#44媒体库)
* [5.如何使用](#5如何使用)
    * [下载](#51下载)
    * [简明教程](#52简要教程)
    * [模块安装](#53模块安装)
    * [配置设置](#54配置设置)
* [6.工具](#6工具)
* [7.异常处理（重要）](#7异常处理重要)
* [8.关于群晖NAS](#8关于群晖NAS)
* [9.FAQ](#9FAQ)
* [10.故事](#10故事)
* [11.声明](#11声明)
* [12.写在后面](#12写在后面)


# 1.简介
**[命令行版](https://github.com/yoshiko2/AV_Data_Capture)(原作者)**：<br>
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
![](https://img.shields.io/badge/Python-3.7-yellow.svg?style=flat-square&logo=python)
![](https://img.shields.io/badge/Pyqt-5-blue.svg?style=flat-square)<br>

## 主要功能
* **日本电影元数据 抓取工具 | 刮削器**，配合本地影片管理软件EMBY,KODI，PLEX等管理本地影片，该软件起到分类与元数据抓取作用，利用元数据信息来分类，供本地影片分类整理使用。<br>
* 可**批量抓取**，也可**单个抓取**。可抓取**多集视频**（-cd1/-cd2）,带**字幕**作品（-c., -C.）。<br>
* 可抓取**子目录下视频**：遍历**视频目录及子目录**（除指定的**排除目录**），对遍历到的所有视频进行刮削，成功则同**元数据、封面图**一起输出到**JAV_output**目录，失败移入**failed**目录。
* 目前可抓取网站：**jav321,javbus,javdb,avsox,fc2club,dmm,mgstage**。<br>
* 批量添加Emby演员头像。<br>
* 封面可添加无码、字幕、流出水印。<br>

# 2.反馈
* 欢迎使用体验,有**程序BUG问题（带截图提问）、功能建议**,可进**电报群**反馈    [点击进群](https://t.me/joinchat/J54y1g3-a7nxJ_-WS4-KFQ)<br>

# 3.常见番号命名规范
**刮削前尽量命名规范！！！！**
**不区分大小写**<br>

### 1、标准有码
* **Javdb、Javbus、Jav321**:  SSNI-111
* **Dmm**:  ssni00111
### 2、无码
* **Javdb、Javbus、Avsox**:  111111-1111、111111_111、HEYZO-1111、n1111
* **Ja321**: HEYZO-1111
### 3、素人
* **Jav321、Mgstage**:  259LUXU-1111
* **Jav321、Javdb**:  LUXU-1111
* **Fc2club**:  FC2-111111、FC2-PPV-111111
### 4、欧美
* **Javdb、Javbus**:  sexart.11.11.11(系列.年.月.日)
### 5、自带字幕影片
可以把电影命名为类似**ssni-xxx-c.mp4,ssni-xxx-C.mp4，abp-xxx-CD1-C.mp4**的规则。
### 6、多集影片
可以把多集电影按照集数后缀命名为类似**ssni-xxx-cd1.mp4,ssni-xxx-cd2.mp4，abp-xxx-CD1-C.mp4**的规则，只要含有```-CDn/-cdn```类似命名规则，即可使用分集功能.**不支持-A -B -1 -2,容易跟字幕的-C混淆**.
### 7、多集、字幕顺序
**abp-xxx-CD1-C.mp4**，**分集在前，字幕在后，字幕必须与拓展名靠近，-C.mp4**.
### 8、外挂字幕文件
**字幕文件名**必须与**影片文件名**一致，才可以一起移动到新目录，目前支持**srt ass sub**类型的字幕文件。
### 9、流出影片
**影片文件名**包含**流出**即可。

# 4.效果图
## 4.1.界面截图
**主界面，设置，工具，关于**

<div align="center">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/main_window.png" height="300">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/setting.gif" height="300">
</div>
<div align="center">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/tool.png" height="300">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/about.png" height="300">
</div>

## 4.2.**查看成功番号的信息(GIF演示)**
<div>
<img src="https://github.com/moyy996/AVDC/blob/master/readme/主页面.gif" height="500">
</div>


## 4.3.**文件结构**<br>

<div>
<img src="https://github.com/moyy996/AVDC/blob/master/readme/tree-jav-output.png" height="700">
</div>

## 4.4.媒体库
**以下为刮削、导入后的EMBY**<br>

<div>
<img src="https://github.com/moyy996/AVDC/blob/master/readme/emby.png" height="400">
<img src="https://github.com/moyy996/AVDC/blob/master/readme/emby_each.png" height="400">
</div>

# 5.如何使用
## 5.1.下载
* **Release** 的程序可脱离**python环境**运行，源码包需要 [安装模块](#53模块安装)<br>
* **Release** 下载地址(**仅限Windows**): [点击下载](https://github.com/moyy996/AVDC/releases)<br>
* **源码包** 下载地址(**Windows,Linux,MacOS**): [点击下载](https://github.com/moyy996/AVDC/archive/master.zip)<br>

* Windows Python环境: [点击前往](https://www.python.org/downloads/windows/) 选中executable installer下载
* MacOS Python环境： [点击前往](https://www.python.org/downloads/mac-osx/)
* Linux Python环境：Linux用户懂的吧，不解释下载地址

## 5.2.简要教程:<br>
* **(1).运行AVDC.exe/AVDC_Main.py，配置设置页各项（配置方法请看以下[教程](54配置设置)）**<br>
* **(2).把视频所在目录填在设置->目录设置->视频目录。**<br>
* **(3).在主页面点击开始等待完成(出错请开调试模式后截图)**<br>
* **(4).软件会自动把元数据获取成功的电影移动到```成功输出目录```中，根据演员分类，失败的电影移动到```失败输出目录```中（可选不移动）。**<br>
* **(5).把JAV_output导入至KODI,EMBY,PLEX中。**<br>

## 5.3..模块安装
如果运行**源码**版，运行前请安装**Python环境**和安装以下**模块**<br>  
在终端/cmd/Powershell中输入以下代码来安装模块,两种方法任选其一。<br>
* **5.3.1、批量**从py-require.txt安装<br>
>pip install -r py-require.txt<br>

* **5.3.2、单个**按需安装<br>
>pip install requests<br>
>pip install pyquery<br>
>pip install lxml<br>
>pip install Beautifulsoup4<br>
>pip install pillow<br>
>pip install pyqt5<br>

## 5.4.配置设置
**设置界面**
![](https://github.com/moyy996/AVDC/blob/master/readme/setting.gif)

---
### 普通设置
### 5.4.1.模式
  **1、刮削模式**：通过番号刮削数据，包括元数据、封面图、缩略图、背景图。<br>
  **2、整理模式**：仅根据女优把电影命名为番号并分类到女优名称的文件夹下。<br>

### 5.4.2.软链接模式
  使用此模式，要以```管理员身份```运行。<br>
  刮削完**不移动视频**，而是在相应目录创建**软链接**（类似于快捷方式），方便PT下载完既想刮削又想继续上传的仓鼠党同志。<br>
  但是，只能在媒体库展示，**不能在媒体库播放**。<br>

### 5.4.3.调试模式
  输出番号的**元数据**，包括封面，导演，演员，简介等。

### 5.4.4.检测更新
点击**开始**后，检测是否有新版本。<br>

### 5.4.5.保存日志
开启后日志保存在程序目录的**Log**目录下的**txt文件**内，每次运行会产生一个txt文件，**txt文件可以删除**，不影响程序运行。<br>

### 5.4.6.失败后移动文件
如果刮削不到影片信息，可选择不移动视频，或者自动移动到**失败输出目录**中。<br>

### 5.4.7.网站选择
可以使用**所有网站**，或者指定网站（**jav321,avsox,javbus,dmm,javdb,fc2club，mgstage**）进行刮削。<br>
**仅使用javdb进行刮削**，尽量不要用，刮削30左右会被JAVDB封IP一段时间。<br>

---
### 目录设置
### 5.4.8.命名规则
  **1、目录命名**：存放视频数据的目录名，支持**多层目录**，支持**自定义符号**，例：[actor]/studio/number-【title】。<br>
  **2、视频标题（媒体库中）**：nfo中的标题命名。例：number-[title]。可以自定义符号。<br>
  **3、视频标题（本地文件）**：本地视频、图片的命名。例：number-[title]。可以自定义符号。<br>
  **4、可选项**为title（片名）、actor（演员）、studio（制作商）、director（导演）、release（发售日）、year（发行年份）、number（番号）、runtime（时长）、series（系列）、publisher（发行商）<br>
  
### 5.4.9.目录设置
  **1、视频目录**：要整理的视频的目录，**带盘符的绝对路径**，会遍历此目录下的**所有视频**，包括**子目录**中。<br>
  **2、排除目录**：在多层目录刮削时，**排除所填目录**。<br>
  **3、视频、字幕类型**：程序搜索不到想要的文件类型，可自行按格式添加。<br>
  **4、失败输出目录**：开启失败移动视频后，失败的视频会移动到此目录。<br>
  **5、成功输出目录**：刮削成功的视频，会在此目录创建文件夹，并移动视频、下载图片、写入nfo到此目录。<br>
  
---
### 水印设置
### 5.4.10.水印设置
  **1、封面图、缩略图添加水印**：可选择封面图、缩略图是否添加水印。<br>
  **2、水印类型**：可选择添加无码、字幕、流出三种水印。<br>
  **3、首个水印位置**：可选择添加左上、左下、右上、右下四个位置。<br>
  **4、水印大小**：有五个等级可调节。<br>
  **5、说明**：**多个水印**时，从首个水印开始**顺时针**添加。**水印文件**可**自定义**，要求长宽500x300、背景透明、png格式。  <br>

---
### 其它设置
### 5.4.11.代理设置 
  **1、代理**：设置本地代理地址和端口。代理软件开**全局模式**  ,**使用DMM网站时需要使用日本代理**。<br>
  **2、超时重试设置**：单位：秒，**可选范围3-10**。<br>
  **3、连接重试次数**：**可选范围2-5**。<br>

### 5.4.12.排除设置
**1、排除字符**:指定字符删除，例如```排除字符： \()```，删除创建文件夹时的```\()```字符。<br>
**2、排除字符串**:提取番号时，先删除指定字符串，提高成功率，字符串之间用','隔开。<br>

### 5.4.13.无码封面
**1、封面类型**:可选官方(完整、不清晰)、裁剪(清晰、不完整)<br>
**2、说明**:官方无图，会自动使用缩略图裁剪。<br>

### 5.4.14.无码番号
添加HEYZO、n1111、111111-111、111111_111以外的无码番号**前缀**。例如S2M、SMD、LAF。<br>

---
# 6.工具
**工具界面**
![](https://github.com/moyy996/AVDC/blob/master/readme/tool.png)
**1、视频移动**：可将**视频目录**下除排除目录下的所有视频以及同名字幕，移动到**视频目录**下的**Movie_moved**目录下。<br><br>
**2、单文件刮削**：偶尔有失败情况时，选择这个视频文件，使用文件名当番号进行刮削。<br>
&emsp;&ensp;**建议**的使用流程：到某网站找到这个番号,把番号改成网站上的规范番号,选用对应的网站刮削。<br>
&emsp;&ensp;**条件**：文件名至少与一个网站上的番号相同，没有多余的内容只有番号为最佳，可以让软件更好获取元数据。<br>
对于多影片重命名，可以用[ReNamer](http://www.den4b.com/products/renamer)来批量重命名<br><br>
**3、Emby批量添加头像**：头像文件放在程序所在目录的Actor目录下，填写emby网址、api密钥即可使用。[头像包下载](https://github.com/moyy996/AVDC/releases/tag/%E5%A4%B4%E5%83%8F%E5%8C%85-2)<br>
可查看有头像，无头像女优，可往emby添加头像的女优。<br><br>
**功能更强大、头像更丰富的头像仓库及上传工具 ===>>> [GFriend头像库](https://github.com/xinxin8816/gfriends)**<br><br>
**4、裁剪封面**：针对封面图比例错误，分辨率低的情况，判断人脸位置，裁剪缩略图(thumb)为封面图(poster)。<br><br>

# 7.异常处理（重要）

---
## 7.1.关于软件打不开
* 请确保软件是完整的！，**AVDC.exe，ACDV-ico.png,config.ini**需要在同一目录下，确保ini文件内容是和下载提供ini文件内容的一致的！<br>

---
## 7.2.关于软件闪退
* 尝试**重新运行**<br>
* 还解决不了，查看**log**日志，尝试以下**7.3、7.4**解决<br>

---
## 7.3.网络错误
##### * (1).报```Connect Failed! Please check your Proxy or Network!```错误<br>
##### * (2).报```Updata_check``` 和 ```JSON``` 相关的错误<br>
##### * (3).关于```Nonetype,xpath```报错<br>
##### * (4).关于```KeyError```报错<br>
* 上述错误都可能是**代理问题**，尝试以下办法解决:
    * 使用DMM，如不是日本代理，**请更换日本代理**，确保可以打开[这个网址](https://www.dmm.co.jp/mono/dvd/-/detail/=/cid=ssni518/?dmmref=aMonoDvd_List/)<br>
    * 把代理设置中的**代理：后面的地址和端口删除**<br>
    * 开启代理软件**全局模式**<br>

---
## 7.4.关于番号提取失败或者异常
* 查看命名是否符合[常见番号命名规范](#3常见番号命名规范)。<br>
* 目前可以提取信息的网址:**JAV321、JAVBUS、JAVDB、AVSOX、dmm、FC2CLUB、mgstage**，请确保视频名能在这些网站找到<br>
* 使用**工具页里的单个视频刮削**，选择**刮削网站**，进行刮削。<br>

---
## 7.5.PLEX不显示封面
请安装插件：[**XBMCnfoMoviesImporter**](https://github.com/gboudreau/XBMCnfoMoviesImporter.bundle)


# 8.关于群晖NAS
开启SMB在Windows上映射为本地磁盘(要分配盘符)即可使用本软件，也适用于其他NAS

# 9.FAQ
## 9.1.这软件能下片吗？
* 该软件不提供任何影片下载地址，仅供本地影片分类整理使用。
## 9.2.什么是元数据？
* 元数据包括了影片的：封面，导演，演员，简介，类型......
## 9.3.软件收费吗？
* 软件永久免费。**除了作者钦点以外**
## 9.4.软件运行异常怎么办？
* 认真看 [异常处理（重要）](#7异常处理重要)

# 10.故事
[点击跳转至原作者博客文章](https://yoshiko2.github.io/2019/10/18/AVDC/)

# 11.声明
* 本软件仅供**技术交流，学术交流**使用<br>
* 本软件作者编写出该软件旨在学习Python3，提高编程水平<br>
* 用户在使用该软件前，请用户自觉遵守当地法律法规，如果该软件使用过程中存在违反当地法律法规的行为，请勿使用该软件<br>
* 用户使用该软件时，若产生一切违法行为由用户承担<br>
* 严禁用户使用于商业和个人其他意图<br>
* 本软件作者保留最终决定权和最终解释权<br>
**若用户不同意上述条款任意一条，请勿使用该软件**<br>

# 12.写在后面
怎么样，看着自己的日本电影被这样完美地管理，是不是感觉成就感爆棚呢?<br>



