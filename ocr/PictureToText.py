from PIL import Image
import pytesseract


def getTextFromPicture(path):
    image = Image.open(path)
    # 解析图片
    content = pytesseract.image_to_string(image, lang='chi_sim')
    return content
# 识别代码  注释不用中文
# 识别身份证


print(getTextFromPicture("/Users/apple/Downloads/截图/题库/截屏2021-06-14 15.38.25.png"))