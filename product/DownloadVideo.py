# encoding:utf-8
import os
import re
import subprocess
import PySimpleGUI as sg


# 获得属性并赋值
def initSeting():
    # 配置文件默认和源文件在同一个文件夹
    settingFile = os.path.join(os.path.dirname(__file__), r'settings_file.cfg')

    # 如果配置文件存在
    if os.path.exists(settingFile):
        pass
    # 配置文件不存在，写入默认值
    else:
        sg.popup("已生成配置文件....")
        with open(settingFile, 'w', encoding="utf-8") as f:
            f.write(f"dirName==>{os.path.dirname(__file__)}\n")
            f.write("fileName==>default\n")
            f.write(
                r"cookie==>C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\mn83fomu.default-release\cookies.sqlite")

    # 读文件，赋值配置
    with open(settingFile, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    # 获得属性
    props = [i.split("==>")[1] for i in lines]
    dir = props[0].strip()
    fileName = props[1].strip()
    cookie = props[2].strip()
    return dir, fileName, cookie


# 文本框设置
def TextLabel(text):
    return sg.Text(text, justification='l', size=(10, 1))


# 输入框设置
def Input(key, default_text):
    return sg.Input(key=key, default_text=default_text, size=(100, 1))


# 检查影片可用的清晰度
def checkFormat(url):
    temparg = []
    temparg.append("you-get")
    temparg.append("-i")
    temparg.append(f"{url}")
    process = subprocess.Popen(
        temparg,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        encoding='utf8',
        bufsize=1
    )
    # 错误日志
    log = []
    tempFormat = []
    while subprocess.Popen.poll(process) is None:
        stream = process.stdout.readline()
        stream = stream.replace("\n", "")
        if not stream:
            continue
        if "- format:" in stream:
            format = stream.split()[-1].strip()
            tempFormat.append(format)
        log.append(stream)
    # 如果tempFormat不为null
    if tempFormat:
        window["-availableFormat-"].update(value=tempFormat[0], values=tempFormat)
        return True
    # 输出日志
    else:
        window["-availableFormat-"].update(value="最高清晰度", values=[])
        window['-log-'].update("\n".join(log))
        return False


# 保存设置
def saveSetting():
    settingFile = os.path.join(os.path.dirname(__file__), r'settings_file.cfg')
    with open(settingFile, 'w', encoding="utf-8") as f:
        f.write(f"dirName==>{values['-dirName-']}\n")
        f.write(f"fileName==>{values['-fileName-']}\n")
        f.write(rf"cookie==>{values['-cookie-']}")


# 下载视频
def download(url, dir=None, file=None, cookie=None, format=None, multipart=None):
    temparg = ['you-get']
    if format:
        temparg.append(f"--format={format}")
    if dir:
        temparg.append(f"-o")
        temparg.append(f"{dir}")
    if file:
        temparg.append(f"-O")
        temparg.append(f"{file}")
    if cookie:
        temparg.append(f"-c")
        temparg.append(f"{cookie}")
    if multipart:
        temparg.append(f"-l")
    temparg.append(f"{url}")
    process = subprocess.Popen(
        temparg,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        encoding='utf8',
        bufsize=1
    )
    # 获取实时日志
    log = []
    global downloadStatus
    # 把下载状态修改
    downloadStatus = (True, process)
    while subprocess.Popen.poll(process) is None:
        stream = process.stdout.readline()
        # 去除空白行
        stream = stream.replace("\n", "")
        if not stream:
            continue
        # 添加进度条日志，每次更换进度条
        if "┤[" in stream and ") ├" in stream:
            key = 1
            # 日志包含进度条则替换
            for k, i in enumerate(log):
                # 如果有旧的进度条，则替换
                if re.match(".*┤\[.*", i):
                    log[k] = stream
                    key = 0
                    break
            # 如果日志不包含进度条，则添加
            if key:
                log.append(stream)
        else:
            # 添加非进度条日志
            log.append(stream)
        window['-log-'].update("\n".join(log))
        window.refresh()
    return True


# 下载状态初始化
downloadStatus = (False, None)
# 属性值初始化
dirName, fileName, cookie = initSeting()
layout = [[TextLabel('视频URL'), Input(key='-url-', default_text=""), sg.Button('下载', key="-download-")],
          [sg.Multiline(key="-log-", size=(120, 30))],
          [TextLabel('视频清晰度'), sg.Spin(values=[], key="-availableFormat-", initial_value="最高清晰度"),
           sg.Button('检测该URL可用清晰度', key="-checkFormat-"),
           sg.Checkbox('下载多个视频', default=False, key="-mul-")],
          [TextLabel('保存目录'), Input(key='-dirName-', default_text=dirName),
           sg.FolderBrowse(target='-dirName-')],
          [TextLabel('视频名'), Input(key='-fileName-', default_text=fileName)],
          [TextLabel("cookie位置"), Input(key='-cookie-', default_text=cookie), sg.FileBrowse(target="-cookie-")]]

window = sg.Window('下载视频', layout)

while True:
    event, values = window.read()
    # 退出
    if event == sg.WIN_CLOSED:
        break
    # 检测URL合法性
    if not re.match("^https://.*", values['-url-']):
        sg.popup("无效的URL")
        continue
    # 检查可用清晰度
    if event == '-checkFormat-':
        window['-log-'].update("")
        try:
            window.perform_long_operation(lambda:
                                          checkFormat(values['-url-'].strip()),
                                          '-checkResult-')
        except Exception as e:
            sg.popup(f"出现BUG，详细日志请看控制台")
            window['-log-'].update(e)
    # 如果完成清晰度检测
    if event == '-checkResult-':
        if values['-checkResult-']:
            sg.popup("检测清晰度完成")
        else:
            sg.popup(f"出现BUG，详细日志请看控制台")

    # 下载
    if event == "-download-":
        # 清除日志区
        window['-log-'].update("")
        # 保存最新配置
        saveSetting()
        # 如果已有下载进程，则杀死已有进程
        if downloadStatus[0]:
            downloadStatus[1].kill()
            sg.popup("已停止上个下载任务，开始本次下载任务")
            # 把状态换为无下载任务的状态
            downloadStatus = (False, None)
            window['-log-'].update("")
        # 文件夹
        dirName = values['-dirName-']
        # 文件名
        if "default".__eq__(values["-fileName-"]):
            fileName = None
        else:
            fileName = values["-fileName-"]
        # 下载列表
        if values["-mul-"]:
            multipart = True
        else:
            multipart = False
        # 清晰度
        if "最高清晰度".__eq__(values["-availableFormat-"]):
            format = False
        else:
            format = values["-availableFormat-"]
        try:
            window.perform_long_operation(lambda:
                                          download(values["-url-"].strip(), dirName, fileName, cookie, format,
                                                   multipart),
                                          '-downloadResult-')
        except:
            sg.popup(f"出现BUG，详细日志请看控制台")
            window['-log-'].update(e)
    if event == '-downloadResult-':
        sg.popup("下载成功")
        # 更换状态
        downloadStatus = (False, None)
window.close()
