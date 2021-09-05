import time


def stamp2Date(timeStamp, style="%Y_%m_%d_%H_%M_%S"):
    timeArray = time.localtime(timeStamp)
    return time.strftime(style, timeArray)
