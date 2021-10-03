# encoding:utf-8
import re
import PySimpleGUI as sg
import sys, os, subprocess


# 不隐藏
# 初始化属性
def initSeting():
    # 如果存在，则取值赋值
    if os.path.exists(SETTINGS_FILE):
        pass
    # 不存在写入默认值
    else:
        sg.popup("已生成配置文件....")
        with open(SETTINGS_FILE, 'w', encoding="utf-8") as f:
            f.write(f"dir==>{os.path.dirname(__file__)}\n")
            f.write("fileName==>default\n")
            f.write(
                r"cookie==>C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\mn83fomu.default-release\cookies.sqlite")
    # 读文件，赋值配置
    with open(SETTINGS_FILE, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    # 获得属性
    props = [i.split("==>")[1] for i in lines]
    dir = props[0]
    fileName = props[1]
    cookie = props[2]
    return dir.strip(), fileName.strip(), cookie.strip()


# 隐藏和显现
def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key, visible=False))


# 文本框设置
def TextLabel(text):
    return sg.Text(text + ':', justification='l', size=(10, 1))


# 检查影片可用的清晰度
def checkFormat(url):
    multipart = False
    # 获得影片支持的清晰度
    getFormatAndQuality = f"you-get -i {url}"
    # 存放格式和清晰度
    formatAndQuality = {}
    # 获得影片可下载的清晰度
    with os.popen(getFormatAndQuality, "r") as p:
        tempstream = p._stream
        for i in tempstream.buffer.read().decode(encoding='utf-8').split("\n"):
            if "- format:" in i:
                format = i.split()[-1]
            if "quality:" in i:
                quality = i.split()[-1]
                formatAndQuality[quality] = format
    return formatAndQuality





SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'
# 设置文件路径和名称
SETTINGS_FILE =
# 是否折叠
opened = False
# 影片可用的清晰度
formatAndQuality = {}
# 下载状态和线程
downloadStatus = (False, None)
# 折叠的部分
section1 = [
    [TextLabel('可用清晰度'), sg.Spin(values=[], key="-availableFormat-"),
     sg.Checkbox('下载多个视频', default=False, key="-mul-")],
    [TextLabel('存放的目录'), sg.Input(key='-dir-', default_text=""),
     sg.FolderBrowse(target='-dir-')],
    [TextLabel('文件名'), sg.Input(key='-file-', default_text="")],
    [TextLabel("cookie位置"), sg.Input(key='-cookie-', default_text=""), sg.FileBrowse(target="-cookie-")],
    [sg.Button("保存设置", key="-save-")]]
# 布局
layout = [[sg.Input(key='-url-', default_text="视频URL"), sg.Button('下载', key="-download-")],
          [sg.T(SYMBOL_DOWN, enable_events=True, key='-OPEN SEC1-', text_color='yellow', font="any 15"),
           sg.T('设置', enable_events=True, text_color='yellow', key='-OPEN SEC1-TEXT', font="any 15")],
          [collapse(section1, '-SEC1-')]]

window = sg.Window('下载视频', layout)

while True:
    event, values = window.read()
    # 退出
    if event == sg.WIN_CLOSED:
        # 如果有线程，杀死线程
        if downloadStatus[0]:
            downloadStatus[1].kill()
            print("已杀死上一个下载进程")
            # 把状态换回来
            downloadStatus = (False, None)
        break
    # 获得配置信息
    dir, fileName, cookie = initSeting()
    # 进行属性赋值
    window["-dir-"].update(dir)
    window["-file-"].update(fileName)
    window["-cookie-"].update(cookie)
    # 检查url
    if not re.match("^https://www.*", values['-url-']):
        sg.popup("无效的URL")
        continue
    # 打开会检测可用清晰度
    if event.startswith('-OPEN SEC1-') and opened == False:
        # 获得可用清晰度
        try:
            formatAndQuality = checkFormat(values["-url-"])
            availableFormat = list(formatAndQuality.keys())
            window["-availableFormat-"].update(value=availableFormat[0], values=availableFormat)
            opened = not opened
            window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened else SYMBOL_UP)
            window['-SEC1-'].update(visible=opened)
        except:
            sg.popup("网络错误或该URL不可用")
    # 关闭不会检测可用清晰度
    elif event.startswith('-OPEN SEC1-') and opened == True:
        opened = not opened
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened)

    # 保存配置，获取所有配置内容，重写进文件
    if event == "-save-":
        with open(SETTINGS_FILE, 'w', encoding="utf-8") as f:
            f.write(f"dir==>{values['-dir-']}\n")
            f.write(f"fileName==>{values['-file-']}\n")
            f.write(
                rf"cookie==>{values['-cookie-']}")
        sg.popup("保存设置成功")
        # 关闭设置
        opened = not opened
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened)
    # 下载
    if event == "-download-":
        # 如果有线程，杀死线程
        if downloadStatus[0]:
            downloadStatus[1].kill()
            print("已杀死上一个下载进程")
            # 把状态换回来
            downloadStatus = (False, None)
        if "default".__eq__(fileName):
            file = None
        else:
            file = fileName
        if values["-mul-"]:
            multipart = True
        else:
            multipart = False
        # 如果有可用清晰度
        if values["-availableFormat-"]:
            format = formatAndQuality[values["-availableFormat-"]]
        # 没有可用清晰度
        else:
            format = False
        download(values["-url-"], dir, file, cookie, format, multipart)

window.close()
