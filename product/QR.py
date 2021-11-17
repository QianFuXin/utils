# encoding:utf-8
"""
生成二维码
"""
import PySimpleGUI as sg

from utils.QR import makeQR

sg.theme('BluePurple')

layout = [[sg.Multiline(key='-text-',expand_x=True,expand_y=True), sg.Button('制作', key="-Show-")],
          [sg.Image(key='-IMAGE-', source="",expand_x=True,expand_y=True)]]
window = sg.Window('生成二维码', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-Show-':
        # 保存本地
        makeQR(values['-text-']).save("二维码.png")
        window['-IMAGE-'].update(filename="二维码.png")

window.close()
