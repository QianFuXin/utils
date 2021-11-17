import os
import zipfile
from utils.GetPath import *

"""
 @Author QFX
 @Data 2021/6/1 上午9:13
 @Describe this function is compress file 
 @Param paths:Files waiting to be compressed
              compressedFileName="compress.zip"
               model=8
 @Return 
"""


def compress(paths, compressedFileName="compressed.zip", model=8):
    """
          ZIP_STORED = 0   不压缩 只归档
          ZIP_DEFLATED = 8      gzip       快  压缩比率小
          ZIP_BZIP2 = 12          bzip2
          ZIP_LZMA = 14           lzma     慢  压缩比率高
    """
    # 构建zipFile对象
    file = zipfile.ZipFile(compressedFileName, mode="w", compression=model)
    # 如果参数是字符串，转换为数组
    if isinstance(paths, str):
        paths = [paths]

    for i in paths:
        # 如果路径是文件夹
        if os.path.isdir(i):
            # 获得文件夹下所有文件
            temp = getAllFilesByDir(i)
            # 压缩
            for k in temp:
                file.write(k, k.replace(os.path.dirname(i), ""))
                print('开始压缩[' + k + ']....')
        # 如果路径是文件
        else:
            print('开始压缩[' + i + ']....')
            file.write(i, os.path.basename(i))


"""
 @Author QFX
 @Data 2021/6/1 上午9:17
 @Describe this function is uncompress file
 @Param compressedFile   xxx.zip
        paths=os.getcwd()  The location of the extracted file
 @Return 
"""


def uncompress(compressedFile, path=os.getcwd(), model=8):
    # 构建zipFile对象
    z = zipfile.ZipFile(compressedFile, mode="r", compression=model)
    # 放到同名文件夹下
    path = os.path.join(path, getFilePrefix(os.path.basename(compressedFile)))
    # 如果没有文件夹
    if not os.path.exists(path):
        os.mkdir(path)
    for i in z.namelist():
        # 解压文件
        print('开始解压[' + i + ']....')
        z.extract(i, path=path)
