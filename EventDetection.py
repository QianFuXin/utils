# encoding:utf-8
"""
分析:停留在每个页面上的事件
"""
import PyHook3
import pythoncom
import sys

mouseEvent = {}
keyboardEvent = {}
allEvent = {}


def statistic():
    # 事件和对应的持续事件
    eventAndWasteTime = {}
    # 有一种情况,就是只停留一个窗口,没有切换窗口
    if len(set([i[1] for i in list(allEvent.values())])) == 1:
        temp = list(allEvent.keys())
        eventAndWasteTime[list(allEvent.values())[0][1]] = int(temp[-1].replace(".", "")) - int(
            temp[0].replace(".", ""))
    else:
        # 时间和事件
        timeAndEvent = allEvent.items()
        beginTime = list(timeAndEvent)[0][0]
        beginEvent = list(timeAndEvent)[0][1][1]
        for k, v in timeAndEvent:
            nowTime = k
            nowEvent = v[1]
            # 开始事件和当前事件一致,不用更换
            if nowEvent.__eq__(beginEvent):
                pass
            # 先记录持续事件,再更换新的开始事件
            else:
                # 已有时间+此次持续时间,因为int不会越界,所以此处把时间×100(统一保留两位数字)
                if nowEvent in eventAndWasteTime:
                    eventAndWasteTime[nowEvent] = eventAndWasteTime[nowEvent] + (
                            int(nowTime.replace(".", "")) - int(beginTime.replace(".", "")))
                # 此次持续时间
                else:
                    eventAndWasteTime[nowEvent] = int(nowTime.replace(".", "")) - int(beginTime.replace(".", ""))
                # 更换新时间和新时间
                beginTime = nowTime
                beginEvent = nowEvent
    for k, v in eventAndWasteTime.items():
        print("{} --> {}".format(k, v))


# 测试
# 鼠标事件


def OnMouseEvent(event):
    messageName = event.MessageName
    time = event.Time
    windowName = event.WindowName
    position = event.Position
    # 把事件加入字典
    mouseEvent[time] = (messageName, windowName, position)
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
            print("没发生事件,无法进行分析")
        # 分析事件
        else:
            statistic()
        # 退出
        sys.exit(1)
    # 把事件加入字典
    keyboardEvent[time] = (messageName, windowName, key)
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
