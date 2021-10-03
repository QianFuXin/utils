# encoding:utf-8
import PySimpleGUI as sg
from utils.chinaId.CI import *

"""
1、性别
2、年龄
3、发证地
4、生日
5、生肖
6、星座
7、检验码
# 8、天干地支
"""
sg.theme('BluePurple')

layout = [[sg.Input(key='-ID-', default_text="身份证号"),sg.Button("分析", key="-analyse-")],
          [sg.Text('性别:'), sg.Text(key='-sex-')],
          [sg.Text('年龄:'), sg.Text(key='-age-')],
          [sg.Text('生日:'), sg.Text(key='-birthday-')],
          [sg.Text('发证地:'), sg.Text(key='-area-')],
          [sg.Text('星座:'), sg.Text(key='-zodiac-')],
          [sg.Text('生肖:'), sg.Text(key='-shengxiao-')]]

window = sg.Window('身份证信息抽取', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == '-analyse-':
        result = getInfoByID(values['-ID-'])
        if result:
            window['-area-'].update(result['address'])
            window['-birthday-'].update(result['birthday_code'])
            window['-zodiac-'].update(result['constellation'])
            window['-shengxiao-'].update(result['chinese_zodiac'])
            window['-age-'].update(result['age'])
            window['-sex-'].update("男" if result['sex'].__eq__("1") else "女")
        else:
            window['-area-'].update("")
            window['-birthday-'].update("")
            window['-zodiac-'].update("")
            window['-shengxiao-'].update("")
            window['-age-'].update("")
            window['-sex-'].update("")
            sg.popup("无效的身份证号")

window.close()
