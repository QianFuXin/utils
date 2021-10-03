import qrcode
import os
import zxing
# 把信息存入二维码、解析二维码的信息

# 存入二维码的内容、保存二维码图片的名称、路径
def makeQR(word, name="qr", path=os.getcwd()):
    qr = qrcode.QRCode(
        # 1、二维码的大小
        # Version 1 是 21 x 21 的矩阵，
        # Version 2 是 25 x 25 的矩阵，
        # Version 3 是 29 的尺寸，
        # 每增加一个 version，就会增加 4 的尺寸，
        # 公式是：(V-1)*4 + 21（V是版本号） 最高 Version 40，(40-1)*4+21 = 177，
        # 所以最高是 177 x 177
        version=3,

        # 2、二维码的纠错等级   默认M
        # 纠错等级是指容错率的大小，按照容错率从小到大如下
        # L(<7%),M(<15%),Q(<25%),H(<30%).容错率也叫纠错率。
        # 纠错码在二维码在被遮挡部分面积后仍能被正常扫描
        # 纠错率指的就是二维码能被正常扫描时允许被遮挡的最大面积占总面积的比率。
        error_correction=qrcode.constants.ERROR_CORRECT_M,

        # 3、二维码每个小格子中包含的像素数量 默认10
        box_size=10,

        # 4、二维码到图片边框的像素数，默认4
        border=4,

        # 5、生成图片的形式，默认PIL图像
        image_factory=None,

        # 6、生成图片的的掩模
        mask_pattern=None)

    # 存入二维码的数据
    qr.add_data(word)

    # 将数据编译成一个二维码数组（fit为True，会自动调整二维码的大小）
    qr.make(fit=True)

    # 创建二维码的图像并返回，默认为PIL图像。默认前者黑后者白，黑色的方块表示1，白色的方块表示0
    # fill_color：二维码的颜色，back_color：背景颜色
    img = qr.make_image(fill_color="black", back_color="white")
    # 保存二维码为图片
    # img.save(os.path.join(path, name + ".png"))
    return img


def parseQR(path):
    # zxing初始化
    reader = zxing.BarCodeReader()
    # 解码二维码中的信息
    parsedInfo = reader.decode(path).parsed
    # 返回解码后的信息
    return parsedInfo


"""
生成二维码的另一种方式，但是不支持中文，支持彩色图片。
from MyQR import myqr

import os

# 存入二维码的信息
info = "hello"
myqr.run(
    # 1、存入二维码的信息
    info,
    # 2、二维码的大小
    # Version 1 是 21 x 21 的矩阵，
    # Version 2 是 25 x 25 的矩阵，
    # Version 3 是 29 的尺寸，
    # 每增加一个 version，就会增加 4 的尺寸，
    # 公式是：(V-1)*4 + 21（V是版本号） 最高 Version 40，(40-1)*4+21 = 177，
    # 所以最高是 177 x 177
    version=3,
    # 3、二维码的纠错等级
    # 纠错等级是指容错率的大小，按照容错率从小到大如下
    # L(<7%),M(<15%),Q(<25%),H(<30%).容错率也叫纠错率。
    # 纠错码在二维码在被遮挡部分面积后仍能被正常扫描
    # 纠错率指的就是二维码能被正常扫描时允许被遮挡的最大面积占总面积的比率。
    level='H',

    # 4、图片路径
    picture="professional.gif",

    # 5、生成的二维码是否为黑白色，黑白(False) 彩色(True)
    colorized=True,

    # 6、对比度
    contrast=1.0,

    # 7、亮度
    brightness=1.0,

    # 8、二维码保存的文件名
    save_name="professionalCode.gif",

    # 9、二维码保存的文件夹
    save_dir=os.getcwd())
"""
