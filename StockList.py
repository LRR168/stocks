#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 12:49:09 2018

@author: liurenrong
"""

import requests
import re

url = "http://www.bestopview.com/stocklist.html"

html = requests.get(url)
html.encoding = "gbk"
content = html.text


pl = "target=\"_blank\">(.*?)</a></li>"
palist = re.compile(pl)
stocklist = palist.findall(content)




