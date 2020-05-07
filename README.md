# 东南大学疫情填报系统的自动化填报

东南大学新版疫情填报系统自动填报 </br>
__* updated May.7 2020 10:45 GMT +8 *__

### DISCLAIMER:
### 本script仅限学术讨论，请勿用于生产环境
### 如果使用时出现明显身体不适，请一定关闭本程序并如实申报。本script仅提供学术讨论，不承担任何连带责任

### How-to:
 - 修改文件绝对路径，使用前安装selenium 和 chromedriver环境
 > !pip3 install selenium <br>
 > !pip3 install webdriver-manager <br>
 > !apt update && apt upgrade <br>
 > !apt install chromium-chromedriver <br>
 > !cp /usr/lib/chromium-browser/chromedriver /usr/bin <br>
 > import sys <br>
 > sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver') <br>
 - linux 设置crontab事件，定时跑


### Updated V3:
 - 减少report时的激进程度。原先的设计一旦学校系统崩溃/连接失败，会发起多线程不间断同时尝试report。
