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
