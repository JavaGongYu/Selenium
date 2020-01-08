# -*- coding=utf-8 -*-

import requests
import itchat
import random

KEY = '04f44290d4cf462aae8ac563ea7aac16'


def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return


@itchat.msg_register(itchat.content.TEXT)
# 文本信息回复
def tuling_reply(msg):
    defaultReplay = 'I received: ' + msg['Text']
    robots = ['I am Jarvis.May I have a message to Tony?', 'Hello,I am Jarvis.']
    reply = get_response(msg['Text']) + random.choice(robots)
    return reply or defaultReplay




@itchat.msg_register([itchat.content.PICTURE, itchat.content.RECORDING, itchat.content.VIDEO])

def other_replay(msg):
    defaultReplay = 'I received: ' + msg['Text']
    robots = ['I am Jarvis.May I have a message to Tony?', 'Hello,I am Jarvis.']
    reply = get_response(msg['Text']) + random.choice(robots)
    return reply or defaultReplay

itchat.auto_login(hotReload=True)
'''不想每次运行程序都扫码，可以设置参数hotReload=True
	如果想在登陆的时候使用命令行显示二维码，可以设置参数enableCmdQR=True
'''
itchat.run()
