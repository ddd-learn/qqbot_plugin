#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/22 14:48
# @Author   : FengYun
# @File     : __init__.py
# @Software : PyCharm
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg

# 响应帮助，cd，菜单，help
my_help = on_command("帮助", rule=to_me(), aliases={"cd", "菜单", "help"}, priority=10, block=True)


@my_help.handle()
async def handle_function(args: Message = CommandArg()):
    # 提取参数纯文本，并判断是否有效
    if choice := args.extract_plain_text():
        # 怎么通过选择进入？
        await my_help.finish(f'''选择{choice}\n获取色图方法,xxx是作品集名称\n1.来N张XXX色图\n2.来N张r18色图''')
    else:
        await my_help.finish("当前支持功能\n1.使用/talk的方式访问chatgpt喵\n2.色图时间(使用/help 2查看详细信息)")
