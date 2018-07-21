# 爬虫准备工作

## 参考资料
- 《python网络数据采集》
- 《精通Python爬虫框架Scrapy》

## 前提知识
- url
- http协议
- web前端：html,css,js
- ajax
- re,xpath
- xml

## Python网络包简介
- Python2.x :urllib,urllib2,urllib3,httplib,httplib2,requests
- Python3.x: urllib,urllib3,httplib2,requests

## urllib
- 包含模块
    - urllib.request:打开和读取url
    - urllib.error：包含urllib.request产生的常见错误，使用try捕捉
    - urllib.parse：包含解析url的方法
    - urllib.robotparse: 解析robots.txt文件
    - 案例 v1
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是有可能有误
    - 案例 v2
- urlopen的返回对象
    - 案例 v3
    - geturl:返回请求对象的url
    - info：请求反馈对象的meta信息
    - getcode：返回http code
- request.data 的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict类型，然后用parse编码
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 如果想要使用post信息，需要用到data参数
        - 案例 v4