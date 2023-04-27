#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/27 11:24
# @Author   : FengYun
# @File     : test.py
# @Software : PyCharm
import json
import os

import openai

#
# conversation = []
# system = {"role": "system", "content": "预设"}
# conversation.append(system)
# prompt = {"role": "user", "content": "问题"}
# conversation.append(prompt)
# assistant = {"role": "assistant", "content": "回复如下"}
# conversation.append(assistant)
# with open(r"log.txt", "a", encoding="utf-8") as infile:
#     size = os.path.getsize("log.txt")
#     for k, v in enumerate(conversation):
#         if k == 0 and size == 0:
#             infile.writelines(str(v))
#             continue
#         infile.writelines("\n" + str(v))
openai.api_key = "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"
conversation = []
# 文件不存在就创建文件
if not os.path.exists("log.txt"):
    open("log.txt", 'w').close()
# 写入文件时防止重复写入system
size = os.path.getsize("log.txt")
if size == 0:
    system = {"role": "system", "content": ""}
    conversation.append(system)
else:
    with open("log.txt", "r", encoding="utf-8") as outfile:
        vars = [wdict for wdict in outfile.read().split("\n")]
        conversation.extend([eval(var) for var in vars[:-1]])
prompt = {"role": "user", "content": "where are you from?"}
conversation.append(prompt)
# 回复
responses = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
    max_tokens=1000
)
assistant = {"role": "assistant", "content": responses['choices'][0]['message']['content']}
conversation.append(assistant)
# 将对话一直追加写入文本文件
with open(r"log.txt", "w", encoding="utf-8") as infile:
    for i in conversation:
        infile.writelines(str(i) + "\n")