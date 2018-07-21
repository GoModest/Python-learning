"""
urlopen返回对象的函数
"""

from urllib import request

if __name__ == '__main__':
    url = 'https://www.douban.com/'
    rsp = request.urlopen(url)
    html = rsp.read()

    print(rsp.geturl())
    print(rsp.info())
    print(rsp.getcode())



    html = html.decode()