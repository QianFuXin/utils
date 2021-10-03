# 调用百度翻译的接口，实现翻译功能。
# 暂时只实现中英文互转。
import os

import requests
import js2py
import json


# 翻译
def translate(word, fromLa, toLa):
    # 创建上下文对象
    context = js2py.EvalJs()
    # 执行js获得sign
    with open(r'translate/百度翻译的.js', 'r', encoding='utf-8') as f:
        context.execute(f.read())
    sign = context.e(word)

    url = 'https://fanyi.baidu.com/v2transapi'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
        "Cookie": "BAIDUID=C3901397F0ADDA16063801114B3B5C2F:FG=1; BIDUPSID=C3901397F0ADDA16063801114B3B5C2F; PSTM=1537772740; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1547903182; BDUSS=-; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1446_21103_28608_28584_28557_28603_28625; PSINO=5; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1551934850,1551935089,1551935474,1551935483; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1551935483",
        "Referer": "https://fanyi.baidu.com/?aldtype=1604"
    }

    # 请求方式是post 所以准备一下需要提交的参数
    data = {
        'from': fromLa,
        'to': toLa,
        'query': word,
        'sign': sign,
        'token': '80c7de3fa6aa8934219322735de33dc1'
    }
    # 提取回应内容
    response = requests.post(url, headers=headers, data=data)
    result = json.loads(response.content)
    # 返回翻译结果
    return result["trans_result"]['data'][0]['dst']


# 翻译英文到中文
def enToZh(word):
    return translate(word, "en", "zh")


# 翻译中文到英文
def zhToEn(word):
    return translate(word, "zh", "en")
