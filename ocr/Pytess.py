"""
使用pytesseract实现OCR，建议使用easyOCR实现OCR
"""
from PIL import Image
import pytesseract


# 获取图片中的文字
def getText(path):
    image = Image.open(path)
    # 解析图片
    content = pytesseract.image_to_string(image, lang='chi_sim')
    return content
