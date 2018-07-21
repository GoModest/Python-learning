"""
request的方法
"""

from urllib import request,parse


if __name__ == '__main__':
    url = 'https://www.baidu.com/s?'

    wd_input = input("Input your keyword:")
    rs = {'wd':wd_input}  # 必须是字典形式
    rs = parse.urlencode(rs)  # 使用parse.urlencode解码
    fullres = url + rs
    print(fullres)
    rsp = request.urlopen(fullres)

    html = rsp.read()
    html = html.decode()
    print(html)
