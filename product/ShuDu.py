# encoding:utf-8
import re

import PySimpleGUI as sg
from utils.SD import *


def getValue():
    # 获得填入的值
    for i in range(1, 10):
        temp = []
        for k in range(1, 10):
            # 如果填入的不是0-9
            if re.match(r"^\d$", values[f'-{i}{k}-']):
                temp.append(int(values[f'-{i}{k}-']))
            else:
                sg.popup("只能输入0-9的数字")
                return False
        recordShudu.append(temp)
    return True


sg.theme('BluePurple')
layout = []
for i in range(1, 10):
    temp = []
    for k in range(1, 10):
        if k % 3 == 0 and not k == 9:
            temp.append(sg.Input(key=f"-{i}{k}-", default_text="0", size=(2, 1)))
            temp.append(sg.Text("   "))
        else:
            temp.append(sg.Input(key=f"-{i}{k}-", default_text="0", size=(2, 1)))
    if i % 3 == 0 and not i == 9:
        layout.append(temp)
        layout.append([sg.Text("")])
    else:
        layout.append(temp)

layout.append(
    [sg.Button("解析数独", key="-parse-"), sg.Text("     "), sg.Button("取消解析", key="-rollback-"), sg.Text("     "),
     sg.Button("全部归零", key="-allToZero-")])

window = sg.Window('解析数独', layout)
zeroShudu = [[0 for i in range(9)] for k in range(9)]
recordShudu = []
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-parse-':
        # 获取且判断值
        if getValue():
            # 解析数独
            parsedShudu = parseSD(recordShudu)
            # 更新值
            for i in range(1, 10):
                for k in range(1, 10):
                    window[f'-{i}{k}-'].update(parsedShudu[i - 1][k - 1])
    # 回滚
    if event == '-rollback-':
        try:
            for i in range(1, 10):
                for k in range(1, 10):
                    window[f'-{i}{k}-'].update(recordShudu[i - 1][k - 1])
        except:
            sg.popup("先点解析，才可以取消解析。")
    # 归零
    if event == "-allToZero-":
        for i in range(1, 10):
            for k in range(1, 10):
                window[f'-{i}{k}-'].update(zeroShudu[i - 1][k - 1])
window.close()
