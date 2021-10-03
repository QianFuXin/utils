# encoding:utf-8
def 三种解析器():
    info = """
info = BeautifulSoup(html, "html.parser")
# 需要安装lxml库，可以解析杂乱的HTML页面，但是速度较慢，依赖第三方C语言库
info = BeautifulSoup(html, "lxml")
# 可以解析更加杂乱的HTML页面，速度更慢
info = BeautifulSoup(html, "html5lib")
    """
    return info


def 正则表达式():
    info = """info.find_all("a", id=re.compile('\d+'))"""
    return info


def lambda表达式():
    info = """
# 获取标签属性数量为2的所有标签
info.find_all(lambda tag: len(tag.attrs) == 2)
# 获取标签内容为‘我是文本的’所有标签
info.find_all(lambda tag: tag.get_text() == '我是文本')
    """
    return info
