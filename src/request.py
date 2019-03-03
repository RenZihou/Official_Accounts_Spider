# -*- coding: utf-8 -*-
# @Author: RZH

import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
s = requests.Session()

# Request headers:
headers = {
    'Accept': '*/*',
    'Accept-Encoding': ', '.join(('gzip', 'deflate', 'br')),
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Host': 'mp.weixin.qq.com',
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/72.0.3626.109 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

cookies = {
        'devicetype': 'Windows10',
        'version': '62060619',
        'lang': 'zh_CN',
        'pass_ticket': config['DEFAULT']['pass_ticket'],
        'wap_sid2': config['DEFAULT']['wap_sid2'],
        'rewardsn': None,
        'wxtokenkey': '777'
    }


# Query String Parameters:
def get_params(offset: int) -> dict:
    params = {
        'action': 'getmsg',
        '__biz': config['DEFAULT']['biz'],
        'f': 'json',
        'offset': str(offset),
        'count': '10',
        'is_ok': '1',
        'scene': '124',
        'uin': '777',
        'key': '777',
        'pass_ticket': None,
        'wxtoken': None,
        'appmsg_token': config['DEFAULT']['appmsg_token'],
        'x5': '0'
    }
    return params


def update(url: str, offset: int):
    global s
    urls = list()
    data = s.get(url, params=get_params(offset), headers=headers, cookies=cookies).json()
    with open('temp3.txt', 'w') as f:
        f.write(str(data))
    for i in range(1, 11):
        urls.append({
            'title': dict(data['general_msg_list'])['list'][i]['app_msg_ext_info']['title'],
            'url': data['general_msg_list']['list'][i]['app_msg_ext_info']['content_url']
        })
    return urls


if __name__ == '__main__':
    print(update('https://mp.weixin.qq.com/mp/profile_ext?', 20))
