#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/25 15:25
# @Author   : FengYun
# @File     : use_openai.py
# @Software : PyCharm
import openai
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import os

# 秘钥
openai.api_key = None


# 传递的参数，主要是输入
class Param(BaseModel):
    input: str
    # 设置模型
    model: str = "gpt-3.5-turbo"
    # 预设角色
    preset: str = ""
    # 最大token
    tokens: int = 1000


app = FastAPI()


# 写成自己的接口，序列化
@app.post("/apiQA")
async def answerQ(param: Param):
    conversation = []
    system = [{"role": "system", "content": param.preset}]
    prompt = {"role": "user", "content": param.input}
    conversation.append(prompt)
    # 判断是否带有上下文
    # if param.answer != "":
    #     assistant = {"role": "assistant", "content": param.answer}
    #     conversation.append(assistant)
    # 回复
    responses = openai.ChatCompletion.create(
        model=param.model,
        messages=system + conversation,
        max_tokens=param.tokens
    )
    return {"answer": responses['choices'][0]['message']['content']}


'''
后续路径改为绝对路径
'''


@app.post("/apiTalk")
async def Talk(param: Param, start: str):
    # 开始对话
    if start == "1":
        conversation = []
        # 文件不存在就创建文件
        if not os.path.exists("log.txt"):
            open("log.txt", 'w').close()
        # 写入文件时防止重复写入system
        size = os.path.getsize("log.txt")
        if size == 0:
            system = {"role": "system", "content": param.preset}
            conversation.append(system)
        else:
            with open("log.txt", "r", encoding="utf-8") as outfile:
                vars = [wdict for wdict in outfile.read().split("\n")]
                conversation.extend([eval(var) for var in vars[:-1]])
        prompt = {"role": "user", "content": param.input}
        conversation.append(prompt)
        # 回复
        responses = openai.ChatCompletion.create(
            model=param.model,
            messages=conversation,
            max_tokens=param.tokens
        )
        assistant = {"role": "assistant", "content": responses['choices'][0]['message']['content']}
        conversation.append(assistant)
        # 将对话一直追加写入文本文件
        with open(r"log.txt", "w", encoding="utf-8") as infile:
            for i in conversation:
                infile.writelines(str(i) + "\n")
    # 结束对话清空文件
    if start == "0":
        open("log.txt", 'w').close()


if __name__ == '__main__':
    uvicorn.run("use_openai:app", reload=True, port=9999)
