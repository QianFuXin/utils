# encoding:utf-8
"""
利用fface_recognitions和deepface实现
"""
import cv2
import face_recognition
import numpy as np
from deepface import DeepFace

from utils.GetPath import *


def analyzeFaces(path):
    """
    找到图片中所有的人脸，然后每一个调用analyse，然后画框
    :return:
    """
    image = cv2.imread(path)
    face_locations = face_recognition.face_locations(face_recognition.load_image_file(path))
    for face in face_locations:
        top, right, bottom, left = face
        cropped = image[top, bottom, left, right]
        print(DeepFace.analyze(img_path=cropped, actions=['age', 'gender', 'race', 'emotion']))



