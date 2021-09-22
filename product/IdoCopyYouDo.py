# encoding:utf-8
"""
1、模仿
需要一个窗体来控制开始和结尾
用勾子获取事件，好像只适用win
分析事件并保存事件，比如，鼠标点击，键盘输入
先写一个勾子获取的接口，然后再写一个自动化的接口
最后该源码中调用两个接口
"""
import PyHook3
import pyautogui

pyautogui.FAILSAFE = False
import pythoncom
import sys

allEvent = {}


def executeEventOrderByTime():
    for k, v in allEvent.items():
        name = v[0]
        # # 鼠标操作
        if "mouse left up".__eq__(name):
            pyautogui.leftClick(v[2][0], v[2][1])
        elif "mouse right up".__eq__(name):
            pyautogui.rightClick(v[2][0], v[2][1], interval=0.5)
        elif "mouse middle up".__eq__(name):
            pyautogui.middleClick(v[2][0], v[2][1])
        elif "key up".__eq__(name):
            print(v[2])
            pyautogui.press(v[2])
        else:
            print("其他")
    exit(1)


def OnMouseEvent(event):
    messageName = event.MessageName
    time = event.Time
    windowName = event.WindowName
    position = event.Position
    # 把事件加入字典
    allEvent[time] = (messageName, windowName, position)
    return True


# 键盘事件
def OnKeyboardEvent(event):
    messageName = event.MessageName
    time = event.Time
    windowName = event.WindowName
    key = event.Key
    # 如果输入右边的control代表退出
    if "Rcontrol".__eq__(key):
        # 如果没有事件,则不进行分析
        if len(allEvent) == 0:
            print("你啥都没做")
        # 分析事件
        else:
            # 取消钩子
            hm.UnhookMouse()
            hm.UnhookKeyboard()
            executeEventOrderByTime()
    # 把事件加入字典
    allEvent[time] = (messageName, windowName, key)
    return True


if __name__ == '__main__':
    # create the hook mananger
    hm = PyHook3.HookManager()
    # register two callbacks
    hm.MouseAllButtonsUp = OnMouseEvent
    hm.KeyUp = OnKeyboardEvent
    # hook into the mouse and keyboard events
    hm.HookMouse()
    hm.HookKeyboard()
    # 持续开启事件
    pythoncom.PumpMessages()
