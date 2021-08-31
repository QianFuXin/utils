import requests
from selenium.webdriver import Chrome, ChromeOptions
from utils.webworm.RandomHeader import *
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def getInfoByURL(URL, encoding="utf-8"):
    # 请求URL
    request = requests.get(URL, headers=getRandomHeader())
    # 设置编码
    request.encoding = encoding
    # 请求到的内容
    html = request.text
    return html


def getInfoByURLWithSelenium(URL, headless=True,chromeDriverPath = '/Users/apple/PycharmProjects/chromedriver90'):
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
        html = browser.page_source
        return html
    finally:
        browser.close()


def downloadBinary(url, path):
    try:
        rsp = requests.get(url, headers=getRandomHeader())
        if rsp.status_code == 200:
            content = rsp.content
            with open(path, "wb") as f:
                f.write(content)
            return True
        else:
            return False
    except Exception:
        return False
