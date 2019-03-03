# !venv\Scripts python
# -*- coding: utf-8 -*-
# @Author: RZH

"""
Login WeChat
You may need to check the login information on your phone.
"""

from subprocess import Popen


def login():
    Popen('"C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe" --remote-debugging-port=9222', shell=True)


if __name__ == '__main__':
    login()
