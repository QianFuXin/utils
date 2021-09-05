import PyHook3
import pythoncom


def OnMouseEvent(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Position:', event.Position)
    print('Wheel:', event.Wheel)
    print('Injected:', event.Injected)
    print('---')

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


def OnKeyboardEvent(event):
    print('MessageName:', event.MessageName)
    print('Message:', event.Message)
    print('Time:', event.Time)
    print('Window:', event.Window)
    print('WindowName:', event.WindowName)
    print('Ascii:', event.Ascii, chr(event.Ascii))
    print('Key:', event.Key)
    print('KeyID:', event.KeyID)
    print('ScanCode:', event.ScanCode)
    print('Extended:', event.Extended)
    print('Injected:', event.Injected)
    print('Alt', event.Alt)
    print('Transition', event.Transition)
    print('---')

    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True


# create the hook mananger
hm = PyHook3.HookManager()
# register two callbacks
hm.MouseWheel = OnMouseEvent
hm.KeyDown = OnKeyboardEvent

"""
MouseAll
MouseAllButtons
MouseAllButtonsUp
MouseAllButtonsDown
MouseAllButtonsDbl
MouseWheel
MouseMove
MouseLeftUp
MouseLeftDown
MouseLeftDbl
MouseRightUp
MouseRightDown
MouseRightDbl
MouseMiddleUp
MouseMiddleDown
MouseMiddleDbl
键盘事件：
KeyUp
KeyDown
KeyChar
KeyAll
"""
# hook into the mouse and keyboard events
hm.HookMouse()
hm.HookKeyboard()
if __name__ == '__main__':
    pythoncom.PumpMessages()
