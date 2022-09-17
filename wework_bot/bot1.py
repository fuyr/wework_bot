# -*- encoding: utf-8 -*-
from weworkbot import Bot as wBot
from weworkbot import bot_mgr as bots
from weworkbot import BotMgr
from weworkbot import Bot as wBot


url=''


def check_something(arg1, arg2, arg3=True):
    return True


def foo3():
    wBot(url)\
        .set_text("every 30 seconds with condition")\
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .every(30)\
        .run()

def render_text(arg1, arg2, arg3=True):
    return arg1 + arg2 + arg3


def foo4():
    # 当同时调用了 render_text 与 set_text 时，优先调用 render_text
    # type 选项: 'text', 'markdown', 默认为 text
    wBot(url)\
        .render_text(render_text, args=['render ', 'with '], kwargs={'arg3': 'function'}, type='text')\
        .check(check_something, args=['arg1', 'arg2'], kwargs={'arg3': 'arg3'})\
        .every(30)\
        .run()


def main():
    url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5f44512a-59f3-45c6-8dcb-09ab3b444bd5'   

    rs=wBot(url).set_text("hello from  Python3,使用vscode编辑").send()
    # wBot(url).set_text('<font color="info">markdown HTML文本，测试</font>', type='markdown').send()
    # print('发送成功？')
    pass

if __name__ == "__main__":
    # main()
    foo4()




# C:\Users\FYR\Desktop\Programer_Log-master\3-16-企业微信\bot1.py