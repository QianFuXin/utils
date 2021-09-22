# encoding:utf-8
from utils.webworm.WebProcess import *
import PySimpleGUI as sg


def getLable(url, key):
    url = url.strip()
    key = key.strip()
    if re.match("^https.*|^http.*", url):
        html = getTextByURL(url)
        parsed = parseHtml(html)
        lable = getLocationByText(parsed, key)
    else:
        parsed = parseHtml(url)
        lable = getLocationByText(parsed, key)

    return lable


sg.theme('TealMono')

layout = [[sg.Text('URL或HTML')],
          [sg.Multiline(default_text='', size=(100, 5), key="-info-")],
          [sg.Text('关键字')],
          [sg.InputText(default_text='', size=(100, 1), key="-key-")],
          [sg.Text('结果')],
          [sg.Multiline(default_text='', size=(100, 5), key="-lable-")],
          [sg.Button('抓')]
          ]

window = sg.Window('抓标签', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    lable = getLable(values['-info-'], values['-key-'])
    window['-lable-'].update(lable)
window.close()
