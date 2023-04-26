#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/26 13:55
# @Author   : FengYun
# @File     : config.py
# @Software : PyCharm
from pydantic import BaseSettings, Field
from nonebot import get_driver
from nonebot.log import logger
from nonebot.rule import to_me
import requests


# 配置文件
class Config(BaseSettings):
    # 访问的参数
    command_prefix: str = "ai"
    # 预设设人格
    default_preset: str = ""
    # 是否需要@
    need_at: bool = False
    # 每日会话次数限制
    max_chat_per_day: int = 200

    class Config:
        extra = "ignore"


# 请求模块，用于验证
class Request():
    def __init__(self):
        self.url = "http://127.0.0.1:9999/api/",
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json"
        }

    def request_api(self):
        response = requests.post(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return True
        return False


# 作用?
driver = get_driver()
global_config = driver.config
config = Config.parse_obj(global_config)

command_prefix = config.command_prefix
default_preset = config.default_preset
need_at = config.need_at
max_chat_per_day = config.max_chat_per_day

if Request().request_api():
    logger.info("api连接成功")
else:
    logger.info("api连接失败，请检查api")
logger.info(f"加载默认人格: {default_preset}")

# 基本会话
matcher_params = {'cmd': command_prefix}
if need_at:
    matcher_params['rule'] = to_me()

# 其他命令
need_at = {}
if need_at:
    need_at['rule'] = to_me()