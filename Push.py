from math import fabs
import os
import sys
import json
import time
import schedule
from dingtalkchatbot.chatbot import DingtalkChatbot
from colorama import *

def push(msg,is_at_all=False,at_mobiles=[]):
    # WebHook地址
    webhook = os.environ.get("webhook")
    secret = os.environ.get("webhookSecret")  # 可选：创建机器人勾选“加签”选项时使用
    # 初始化机器人小丁
    # xiaoding = DingtalkChatbot(webhook)  # 方式一：通常初始化方式
    xiaoding = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）
    # xiaoding = DingtalkChatbot(webhook, pc_slide=True)  # 方式三：设置消息链接在PC端侧边栏打开（v1.5以上新功能）
    # Text消息@所有人
    xiaoding.send_text(
        msg=msg, is_at_all=is_at_all, at_mobiles=at_mobiles
    )