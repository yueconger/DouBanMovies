# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 14:47
# @Author  : yueconger
# @File    : main.py
# about    : 

import os
import sys
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(['scrapy', 'crawl', 'douban_movies'])