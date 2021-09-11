import os
import random
from xpinyin import Pinyin


# 获取汉字的首字母
def firstCharacter(info, description, account):
    pinYinObject = Pinyin()
    transformed = pinYinObject.get_pinyin(info)
    result = ""
    for i in transformed.split("-"):
        result += i[0]
    savePassword(description, account, result)
    return result


# 获取汉字的拼音
def pinYin(description, account, info):
    p = Pinyin()
    transformed = p.get_pinyin(info, tone_marks=True)
    savePassword(description, account, transformed)
    return transformed


def savePassword(description, account, password):
    passwordDir = "/Users/apple/钱甫新的文件/专业知识/密码"
    passwordPath = os.path.join(passwordDir, description + '的账户和密码.txt')
    # 如果文件重复  文件结尾拼接_repeat
    while 1:
        if os.path.exists(passwordPath):
            passwordPath = passwordPath[:-4] + '_repeat.txt'
        else:
            break
    # 把账号密码写入文件，进行备份
    with open(passwordPath, 'w', encoding='utf8') as file:
        file.writelines("账户：" + account + '\n')
        file.writelines('密码：' + password)


# 随机密码，默认数字字母符号组合18位
def randomPassword(description, account, seed):
    # seed 默认九位,seed可以是1,2,3等常数
    seed = 100000000 + seed
    # 字母类型
    englishChar = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z',
                   'x',
                   'c', 'v',
                   'b', 'n', 'm']
    # 数字类型
    numberChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # 符号类型
    symbolChar = ['!', '@', '#', '$']
    passwordCharSet = englishChar.copy() + numberChar.copy() + symbolChar.copy()
    random.seed(seed)
    # 把密码打乱
    random.shuffle(passwordCharSet)

    return "".join(passwordCharSet[:16])
