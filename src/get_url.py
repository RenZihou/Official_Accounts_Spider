# -*- coding: utf-8 -*-
# @Author: RZH

import requests
from configparser import ConfigParser
from re import search

config = ConfigParser()
config.read('config.ini')


def get_url():
    global config
    data = requests.get('http://127.0.0.1:9222/json').json()
    url = data[0]['url']  # including `key` and `pass_ticket`
    # title = data[0]['title']
    config['DEFAULT']['key'] = search('key=([^&]*)', url).group(1)  # key
    config['DEFAULT']['pass_ticket'] = search(
        'pass_ticket=([^&]*)', url).group(1).replace('%2B', '+').replace('%2F', '/')  # pass_ticket
    config['DEFAULT']['biz'] = search('__biz=([^&]*)', url).group(1)  # official account's id
    config['DEFAULT']['uin'] = search('uin=([^&]*)', url).group(1)
    with open('config.ini', 'w') as cf:
        config.write(cf)
    return url


if __name__ == '__main__':
    print(get_url())
