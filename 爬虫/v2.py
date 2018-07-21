"""
自动检测页面编码
"""

from urllib import request
import chardet

if __name__ == '__main__':
    url = 'https://www.douban.com/'
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)  # 检测html并返回一个结果


    html = html.decode(cs.get('encoding','utf-8'))
    print(html)