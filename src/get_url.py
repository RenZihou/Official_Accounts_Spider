# -*- coding: utf-8 -*-
# @Author: RZH

import requests

data = requests.get('http://127.0.0.1:9222/json').json()
url = data[0]['url']
print(url)
