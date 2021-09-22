# encoding:utf-8
"""
生成随机密码
"""
from utils.MakePassword import *
import PySimpleGUI as sg
import pyperclip

sg.theme('DarkAmber')

layout = [[sg.Spin(values=[i for i in range(1, 10000)], initial_value=1, key="-seed-", size=(2,)),
           sg.Button('生成密码', key="-action-")]]
window = sg.Window('随机生成密码', layout)
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "-action-":
        seed = values['-seed-']
        # 把密码复制到粘贴板
        pyperclip.copy(randomPassword(seed))
        sg.popup('密码已复制到粘贴板')
window.close()


