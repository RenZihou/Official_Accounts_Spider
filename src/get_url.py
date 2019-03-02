# -*- coding: utf-8 -*-
# @Author: RZH

import requests
from configparser import ConfigParser
from re import search

config = ConfigParser()
config.read('src/config.ini')


def get_url():
    global config
    data = requests.get('http://127.0.0.1:9222/json').json()
    url = data[0]['url']
    title = data[0]['title']  # including `key` and `pass_ticket`
    config['DEFAULT']['key'] = search('key=([^&]*)', title).group(1)  # key
    config['DEFAULT']['pass_ticket'] = search('pass_ticket=([^&]*)', title).group(1)  # pass_ticket
    with open('src/config.ini', 'w') as cf:
        config.write(cf)
    return url


if __name__ == '__main__':
    print(get_url())
