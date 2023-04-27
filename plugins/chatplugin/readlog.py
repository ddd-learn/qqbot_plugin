#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 11:24
# @Author   : FengYun
# @File     : readlog.py
# @Software : PyCharm
with open("log.txt","r",encoding="utf-8") as outfile:
    print(outfile.readlines())