# encoding:utf-8

from utils.BaiDuFanYi import *
import PySimpleGUI as sg


def e2c(info):
    info = info.strip()
    info = info.replace("\n", "")
    return enToZh(info)


def c2e(info):
    info = info.replace("\n", "")
    return zhToEn(info)


sg.theme('Topanga')

layout = [[sg.Text('原文')],
          [sg.Multiline(default_text='', size=(100, 5), key="-info-")],
          [sg.Text('译文')],
          [sg.Multiline(default_text='', size=(100, 5), key="-translate-")],
          [sg.Text('选择语言')],
          [sg.Radio('英转中', "RADIO1", default=True, size=(10, 1), key="-e2c-"), sg.Radio('中转英', "RADIO1", key="-c2e-")],
          [sg.Button('翻译')]
          ]

window = sg.Window('翻译', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if values['-e2c-'] is True:
        translate = e2c(values['-info-'])
        window['-translate-'].update(translate)
    else:
        translate = c2e(values['-info-'])
        window['-translate-'].update(translate)
window.close()
