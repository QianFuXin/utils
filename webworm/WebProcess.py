import re
from lxml import etree
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome, ChromeOptions
from utils.webworm.RandomHeader import *
import ssl
import platform

ssl._create_default_https_context = ssl._create_unverified_context


# 请求页面
def __myRequests__(url):
    response = requests.get(url.strip(), headers=getRandomHeader(), allow_redirects=True)
    #  返回码正常,返回response
    try:
        response.raise_for_status()
        return response
    # 返回码不正常,打印bug信息,返回responseNone
    except Exception as exc:
        print('bugInfo: %s' % (exc))
        return None


# 传进来一个url，返回html解析器
def fastHtmlParse(url, encoding="utf-8"):
    text = getTextByURL(url, encoding)
    if text:
        return parseHtml(text)
    # 如果None,则返回None
    else:
        return None


# 传进来一个URL,返回该URL的文本内容
def getTextByURL(url, encoding="utf-8"):
    # 请求URL
    response = __myRequests__(url)
    # 正常
    if response:
        # 设置编码
        response.encoding = encoding
        # 请求到的内容
        return response.text
    # 如果None,则返回None
    else:
        return None


# 传进来一个URL,返回该URL的二进制内容
def getBinaryByURL(url):
    # 请求URL
    response = __myRequests__(url)
    # 正常
    if response:
        binary = response.content
        return binary
    # 返回None
    else:
        return None


# 下载文件
def downloadFile(url, path):
    binary = getBinaryByURL(url)
    if binary:
        with open(path, "wb") as f:
            f.write(binary)
        print("下载" + path + "成功")
    else:
        print("下载" + path + "失败")


# 返回html解析后的页面  将str转换为bs4
def parseHtml(html, features="html.parser"):
    if features.__eq__("html.parser"):
        parsed = BeautifulSoup(html, features)
        return parsed


def getTagByXPath(url, xpa):
    # 如果参数是字符串，代表只需要解析一个
    if isinstance(xpa, str):
        xpa = [xpa]
    html = getTextByURL(url)
    print(html)
    allParsed = []
    if html:
        # xpath，借用chrome的复制xpath
        parsed = etree.HTML(html)
        for i in xpa:
            result = parsed.xpath(i)
            # 空列表返回None
            if result:
                allParsed.append(result[0])
            else:
                allParsed.append(None)
        # 如果数组只有一个元素，返回数组也没多大意义
        if len(allParsed) == 1:
            return allParsed[0]
        else:
            return allParsed
    else:
        return None


"""
输入网页中的某个唯一文本,返回包含该文本标签的位置  可以理解为自动抓标签
例如
输入 23 ~ 28
输出
parsed.select('html > body > div > div > div > dl > dd >span')[0]
或者 parsed.find_all(name='dd', attrs={'class': ['week']})
"""


def getLocationByText(parsed, text):
    # 通过文本逆抓标签
    temp = parsed.find_all(text=re.compile(text))
    # 如果文本数量不为1,则异常
    if len(temp) == 0:
        print("网页中未找到输入的文本")
        return "网页中未找到输入的文本"
    elif len(temp) == 1:
        # 获得此标签
        tag = temp[0].parent
        # 标签名字
        tagName = tag.name
        # 标签参数
        tagAttri = tag.attrs
        # 利用findall去找,如果只有一个结果,返回,否则用选择器去递归(因为只靠find_all找不到唯一的)
        result = parsed.find_all(name=tagName, attrs=tagAttri)
        if len(result) == 1:
            return "parsed.find_all(name='tagName', attrs=tagAttri)[0].text.strip()".replace("tagName",
                                                                                             tagName).replace(
                "tagAttri",
                str(
                    tagAttri))
        # 当有多个结果,findall无法解决唯一的问题时
        # 则利用更加精细的选择器方法,向上寻找父亲标签
        else:
            relationship = ""
            # 找父亲
            for parent in tag.parents:
                if parent is None:
                    pass
                else:
                    # 不添加[document] 元素
                    if "[document]".__eq__(parent.name):
                        continue
                    # 添加所有的父亲标签
                    relationship = parent.name + " > " + relationship + " "
            # 添加自己的标签
            relationship = relationship.strip() + tagName
            # 如果元素查找长度为1,则说明找到了唯一
            result = parsed.select(relationship)
            if len(result) == 1:
                return "parsed.select('relationship')[0].text.strip()".replace("relationship", relationship)
            # 如果利用选择器后还是有多个结果,则通过text来判断,返回数组下标
            else:
                # 遍历所有内容,然后匹配text,匹配了返回下标(nice),解放双手~
                for i in range(len(result)):
                    if text in result[i].text:
                        return "parsed.select('relationship')[下标].text.strip()".replace("relationship",
                                                                                        relationship).replace("下标",
                                                                                                              str(i))
    else:
        print("输入的文本在网页中不唯一")
        return "网页中未找到输入的文本"


def getInfoByURLWithSelenium(URL, headless=True,
                             chromeDriverPath=r'C:\Users\Administrator\PycharmProjects\QianFuXin\utils\webworm\chromedriver.exe'):
    # 针对windows和linux的差异性，做出代码更改
    if platform.system() == "Linux":
        # linux默认路径
        chromeDriverPath = "/usr/bin/chromedriver"
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("window-size=1024,768")
        chrome_options.add_argument("--no-sandbox")
        browser = Chrome(chrome_options=chrome_options)
    # windows配置
    else:
        option = ChromeOptions()
        # no page pattern
        option.headless = headless
        # ocr Chrome object
        browser = Chrome(chromeDriverPath, options=option)

    try:
        browser.set_page_load_timeout(10)
        browser.get(URL)
        html = browser.page_source
        return html
    except:
        return None
    finally:
        browser.close()
