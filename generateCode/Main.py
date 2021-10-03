import os
import re
import PySimpleGUI as sg

"""
因为人记住的内容有限,只是在脑中保存视图,不会记住所有内容,
所以该程序记录着一些常用且常忘的代码.
warehouse下面放着一些源文件,从源文件的命名你应该就有所了解,函数也同理
"""
# 获取文件夹下的所有py文件
files = os.listdir("warehouse")
files.remove("__init__.py")
files.remove("__pycache__")
for i in files:
    if re.match(".*\.py", i):
        # 导入源文件
        exec("from warehouse import " + i[:-3])
# 获取所有源文件的文件名，不要.py后缀
allType = []
for i in files:
    allType.append(i[:-3])
allType.sort()

sg.theme('dark')

layout = [[sg.Listbox(values=allType, enable_events=True, size=(12, 30), key='-file-', font=('Any 15')),
           sg.Listbox(values=[], enable_events=True, size=(24, 30), key='-function-', font=('Any 15')),
           sg.Output(size=(90, 30), key='-code-', font=('Any 13'))]]

window = sg.Window('Pattern 2B', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-file-':
        functions = []
        exec("functions=dir(" + values['-file-'][0] + ")")
        for i in ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
                  '__spec__']:
            functions.remove(i)
        window['-function-'].update(functions)
        window['-code-'].update("")
    if event == "-function-":
        window['-code-'].update("")
        exec("print(" + values['-file-'][0] + "." + values['-function-'][0] + "()" + ")")
window.close()
