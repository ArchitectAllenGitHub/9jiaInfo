from math import fabs
import os
import sys
import json
import time
import schedule
from dingtalkchatbot.chatbot import DingtalkChatbot
from colorama import *
import Push


def job(citycode, b1):
    try:
        print(Fore.GREEN + "输入的地区代码为: " + citycode)
    except IndexError:
        print(Fore.RED + "usage: python3 9jiainfo.py cd")
    try:
        command = 'curl -H "Host: wxapidg.bendibao.com" -H "content-type: application/json" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79" -H "Referer: https://servicewechat.com/wx2efc0705600eb6db/130/page-frame.html" "https://wxapidg.bendibao.com/smartprogram/zhuanti.php?platform=wx&version=21.12.06&action=jiujia&citycode={}"'.format(
            citycode
        )
    except UnboundLocalError:
        print(Fore.RED + "请输入地区代码，如成都为cd,北京为bj")
    try:
        print(Fore.GREEN + "执行curl命令为:\n" + command)
        a2 = os.popen(command)
        b2 = a2.read()

        if b1 == "":
            b1 = b2

        r = json.loads(b2)
        # json.dumps(r, ensure_ascii=False)
        data = r["data"]
        jiujia = data["website"]
        place = jiujia["place"]
        try:
            global c
            c = ""
            if place is None:
                return b2
            for i in range(0, 5):
                c0 = (
                    "[+]---预约(抢)时间---[+]"
                    + place[i]["yy_time"]
                    + " "
                    + place[i]["name"]
                    + "    "
                    + "[+]---数量---: "
                    + place[i]["minge"]
                    + "   "
                    + place[i]["method"]
                    + "---预约平台---[+]"
                    + place[i]["platform"]
                )
                c += c0 + "\n"
        except IndexError:
            pass
        print(c)
        if b2 not in b1:
            Push.push(citycode + c,at_mobiles=[os.environ.get("webhookPhone")])

        time.sleep(30)  # 是否要在内容比较后，再进行时间等待
        return b2
    except UnboundLocalError:
        sys.exit(2)


def out():
    if int(time.strftime("%H", time.localtime())) < 8:
        print(
            Fore.RED + "[-]---------------休息时间，不进行推送---------------[-]" + time.ctime()
        )
        return False
    elif int(time.strftime("%H", time.localtime())) > 21:
        print(
            Fore.RED + "[-]---------------休息时间，不进行推送---------------[-]" + time.ctime()
        )
        return False
    else:
        return True


global result
result = ""
while True:
    if out() == False:
        time.sleep(60)
        continue
    result = job("zz", result)
    schedule.run_pending()
    time.sleep(1)