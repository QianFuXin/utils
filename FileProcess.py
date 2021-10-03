# 在文本文件的头部插入信息
def insertText2FileTitle(path, insertContent, encoding='utf-8'):
    """
    :param path:文件的路径
    :param insertContent: 插入的内容
    :param encoding: 编码
    :return:
    """
    with open(path, mode='r+', encoding='utf-8') as  file:
        temp = insertContent + "\n" + file.read()
        file.seek(0)
        file.write(temp)
