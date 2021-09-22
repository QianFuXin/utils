# encoding:utf-8
"""
利用face_recognitions实现
"""
import cv2
import face_recognition
import numpy as np
from utils.GetPath import *


# 找人脸的实现函数
def __find__(path):
    # 读取文件为了后期画框
    image = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
    # 获取人脸位置
    face_locations = face_recognition.face_locations(face_recognition.load_image_file(path))
    # 遍历人脸，画框
    for face in face_locations:
        top, right, bottom, left = face
        cv2.rectangle(image, tuple([left, top]), tuple([right, bottom]), (0, 255, 0), 2)
    newPath = f"{getFilePrefix(path)}_{len(face_locations)}face.{getFileSuffix(path)}"
    cv2.imencode("." + getFileSuffix(path), image)[1].tofile(newPath)


# 查找图片中的人脸并画框
def findFaces(path):
    # 如果路径是文件夹，则抽取该文件夹下所有png和jpg和jpeg文件
    if os.path.isdir(path):
        for i in getAllFilesByDir(path, "png") + getAllFilesByDir(path, "jpg") + getAllFilesByDir(path, "jpeg"):
            __find__(i)
    else:
        __find__(path)


"""
查看两张图片是否为同一个人
先对人脸进行编码，然后计算两张脸的欧氏距离（n维空间距离），距离越小，越说明是同一张脸
如果距离小于某个值（0.6），则代表是一个人
"""


def checkFace(pathOne, path_two):
    # 把第一张图片编码
    picture_one = face_recognition.load_image_file(pathOne)
    face_one_encoding = face_recognition.face_encodings(picture_one)[0]
    # 把第二张图片编码
    picture_two = face_recognition.load_image_file(path_two)
    face_two_encoding = face_recognition.face_encodings(picture_two)[0]
    # 比较两张脸
    results = face_recognition.compare_faces([face_one_encoding], face_two_encoding)
    # 返回比较结果
    return results


print(checkFace(r"C:\Users\Administrator\Desktop\图片\d\1.jpg", r"C:\Users\Administrator\Desktop\图片\d\2.jpg"))
