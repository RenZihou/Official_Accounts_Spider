# -*- coding: utf-8 -*-
# @Author: RZH

from re import search
from src.request import update


def reformat_url(url: str) -> str:
    return url.replace('\\', '').replace(search('(chksm=[^&]*&amp;)', url).group(1), '')

