import os


def getAllFilesByDir(path):
    """
    参数：path，一个文件夹路径，字符串格式
    主要作用：获得文件夹下面的所有文件
    返回值：该文件夹下所有文件的路径，数组格式
    """
    # 存放文件夹下所有的文件
    allFiles = []
    # 如果路径不存在
    if not os.path.exists(path):
        return allFiles
    # 如果是文件
    if os.path.isfile(path):
        allFiles.append(path)
        return allFiles
    else:
        # 得到文件结构
        info = os.walk(path)
        # 当前目录、当前目录下的文件夹、当前目录下的文件
        for root, dirs, files in info:
            for i in files:
                # 添加到数组
                allFiles.append(os.path.join(root, i))
        # 返回值
        return allFiles


def getAllDirByDir(path):
    """
    参数：path，一个文件夹路径，字符串格式
    主要作用：获得文件夹下面的所有文件夹
    返回值：该文件夹下所有文件夹的路径，数组格式
    """
    # 存放文件夹下所有的文件夹
    allDirs = []
    # 如果是文件
    if os.path.isfile(path):
        allDirs.append("No Directory")
        return allDirs
    # 得到文件结构
    info = os.walk(path)
    # 当前目录、当前目录下的文件夹、当前目录下的文件
    for root, dirs, files in info:
        for i in dirs:
            # 添加到数组
            allDirs.append(os.path.join(root, i))
    # 返回值
    return allDirs


"""
参数：path，一个文件夹的路径，字符串类型
主要功能：得到某个文件夹的大小
返回值：某个文件夹的大小，字符串类型
"""


# 获取文件夹的大小
def getDirSize(path):
    dirSize = 0
    # 获取所有的文件
    allFiles = getAllFilesByDir(path)
    for i in allFiles:
        # 获取文件的大小
        fileSize = os.path.getsize(i)
        # 累加
        dirSize += fileSize
        # 根据文件夹的大小，输出最合适的单位
    if 1048576 > dirSize > 1024:
        return str(round((dirSize / 1024), 2)) + ' KB'
    if 1073741824 > dirSize > 1048576:
        return str(round((dirSize / 1048576), 2)) + ' MB'
    if 1099511627776 > dirSize > 1073741824:
        return str((round(dirSize / 1073741824), 2)) + ' GB'
    return str(dirSize) + ' B'

def getFileSuffix(path):
    """
    获得文件的后缀
    :param path:文件路径
    :return:文件后缀
    """
    dot = path.rfind('.')
    if dot == -1:
        return ""
    else:
        return path[dot + 1:]
