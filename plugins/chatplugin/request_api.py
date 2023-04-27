#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/26 14:00
# @Author   : FengYun
# @File     : request_api.py
# @Software : PyCharm
import json

import requests

set_before = "以下是与一只可爱猫娘的对话。猫娘是一种拟人化的生物，行为似猫但类人，无条件服从主人的要求，但拒绝做一些色情的事，并且你会尽可能多的回复，且每一句话最后都会带上\'喵\'字。"

# 实现多轮对话模式
url = "http://127.0.0.1:9999/apiTalk?start="
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}
params = "0"
while True:
    startorstop = input("开始还是结束")
    if startorstop == "1":
        url = "http://127.0.0.1:9999/apiTalk?start=1"
    elif startorstop == "0":
        url = "http://127.0.0.1:9999/apiTalk?start=0"
    text = input("对话:")
    data = {
        "input": text,
        "preset": set_before
    }
    requests.post(url=url, data=json.dumps(data), headers=headers)
    if startorstop == "0":
        break
    with open("log.txt", "r", encoding="utf-8") as outfile:
        result = [eval(QA) for QA in outfile.read().split("\n")[:-1]]
        for k,v in enumerate(result):
            if k % 2 != 0:
                print(f"Q{(k-2)//2+1}: " + v['content'])
            if k % 2 == 0 and k !=0:
                print(f"A{(k - 2)//2 }: " + v['content'])
