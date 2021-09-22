# encoding:utf-8
"""使用easyOCR去实现OCR
https://www.jaided.ai/easyocr/documentation/ 查看更多参数
"""

import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import easyocr
import cv2
import numpy as np
from utils.GetPath import *


# 获取图片中的文字
def getText(path):
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    # detail=0 只输出内容
    # paragraph=True 按照段落为单位输出
    # rotation_info= [90, 180 ,270] 旋转90，180，270度 找出置信度最高的那个输出
    result = reader.readtext(path, paragraph=True, detail=0)
    return "\n".join(result)


# 把图片中的文字圈出来
def getTextLocation(path):
    reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
    image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
    result = reader.readtext(image)
    # 画框
    for location in result:
        leftTOP = [int(k) for k in location[0][0]]
        rightBottom = [int(k) for k in location[0][2]]
        cv2.rectangle(image, tuple(leftTOP), tuple(rightBottom), (0, 255, 0), 2)
    # 保存文件
    newPath = f"{getFilePrefix(path)}_TextLocation.{getFileSuffix(path)}"
    cv2.imencode("." + getFileSuffix(path), image)[1].tofile(newPath)


"""
实现身份证识别、车牌号识别、银行卡识别
1、图片方向改正（保证图片方向是对的）
2、图片进行缩放到一定尺寸（便于后期切割）
3、然后分割每个身份证区域（对某个区域进行匹配，可以加入allow list（比如身份证允许的字符集只有0-9））
"""
