import os
import re
from easyWriteCode.dir_and_file.GetPath import *


def en(filePath):
    encryptionSet = {0: 17, 1: 228, 2: 247, 3: 30, 4: 170, 5: 40, 6: 249, 7: 63, 8: 116, 9: 42, 10: 251, 11: 115, 12: 1,
                     13: 235, 14: 195, 15: 99, 16: 61, 17: 234, 18: 242, 19: 191, 20: 109, 21: 70, 22: 206, 23: 92,
                     24: 67,
                     25: 14, 26: 159, 27: 20, 28: 244, 29: 32, 30: 7, 31: 143, 32: 82, 33: 23, 34: 53, 35: 9, 36: 141,
                     37: 0,
                     38: 137, 39: 133, 40: 136, 41: 146, 42: 59, 43: 218, 44: 121, 45: 97, 46: 47, 47: 21, 48: 208,
                     49: 29,
                     50: 187, 51: 112, 52: 51, 53: 33, 54: 188, 55: 78, 56: 174, 57: 241, 58: 2, 59: 231, 60: 193,
                     61: 160,
                     62: 26, 63: 12, 64: 200, 65: 152, 66: 52, 67: 155, 68: 202, 69: 164, 70: 150, 71: 103, 72: 212,
                     73: 182,
                     74: 84, 75: 60, 76: 6, 77: 129, 78: 223, 79: 221, 80: 73, 81: 89, 82: 123, 83: 149, 84: 36,
                     85: 183,
                     86: 180, 87: 34, 88: 186, 89: 245, 90: 27, 91: 111, 92: 238, 93: 153, 94: 119, 95: 253, 96: 110,
                     97: 194,
                     98: 25, 99: 203, 100: 16, 101: 205, 102: 106, 103: 91, 104: 181, 105: 69, 106: 177, 107: 19,
                     108: 189,
                     109: 226, 110: 134, 111: 163, 112: 125, 113: 101, 114: 90, 115: 148, 116: 62, 117: 102, 118: 83,
                     119: 209,
                     120: 126, 121: 105, 122: 154, 123: 77, 124: 165, 125: 71, 126: 217, 127: 145, 128: 38, 129: 246,
                     130: 96,
                     131: 10, 132: 3, 133: 178, 134: 57, 135: 225, 136: 41, 137: 140, 138: 80, 139: 132, 140: 196,
                     141: 104,
                     142: 171, 143: 135, 144: 142, 145: 95, 146: 224, 147: 131, 148: 144, 149: 190, 150: 219, 151: 176,
                     152: 198, 153: 227, 154: 130, 155: 107, 156: 248, 157: 255, 158: 161, 159: 68, 160: 157, 161: 56,
                     162: 108, 163: 93, 164: 49, 165: 222, 166: 151, 167: 237, 168: 28, 169: 58, 170: 204, 171: 172,
                     172: 31,
                     173: 39, 174: 243, 175: 213, 176: 147, 177: 72, 178: 124, 179: 207, 180: 8, 181: 50, 182: 215,
                     183: 55,
                     184: 254, 185: 114, 186: 76, 187: 166, 188: 169, 189: 138, 190: 43, 191: 118, 192: 240, 193: 199,
                     194: 113, 195: 98, 196: 173, 197: 216, 198: 252, 199: 233, 200: 197, 201: 64, 202: 24, 203: 48,
                     204: 87,
                     205: 232, 206: 201, 207: 167, 208: 158, 209: 15, 210: 175, 211: 179, 212: 229, 213: 139, 214: 18,
                     215: 162, 216: 22, 217: 184, 218: 100, 219: 66, 220: 5, 221: 13, 222: 168, 223: 74, 224: 239,
                     225: 85,
                     226: 220, 227: 117, 228: 185, 229: 128, 230: 37, 231: 44, 232: 210, 233: 230, 234: 88, 235: 250,
                     236: 122,
                     237: 236, 238: 156, 239: 127, 240: 192, 241: 11, 242: 86, 243: 79, 244: 4, 245: 65, 246: 46,
                     247: 120,
                     248: 211, 249: 214, 250: 81, 251: 45, 252: 54, 253: 75, 254: 94, 255: 35}
    # 操作之前的二进制
    encryptionBeforeBin = b''
    # 操作之后的二进制
    encryptionAfterBin = b''
    # 文本文件或者小文件  字节全转换
    if re.match("(.*\.txt)|(.*\.docx)|(.*\.doc)|(.*\.wps)$", filePath) or os.path.getsize(filePath) < 102400:
        # 读取文件
        with open(filePath, 'rb') as file:
            # 以字节为单位读取
            encryptionBeforeBin = file.read()
            # 循环遍历字节
            for i in encryptionBeforeBin:
                # 转换字节进行加密
                encryptionAfterBin = encryptionAfterBin + bytes([encryptionSet[i]])
        # 重写文件
        with open(filePath, 'wb') as file:
            file.write(encryptionAfterBin)
    # 大文件  前102400个字节全换，后面的字节，第10n个更换
    else:
        with open(filePath, 'rb') as file:
            # 以字节为单位读取
            encryptionBeforeBin = file.read()
            # 循环遍历前102400个字节
            for i in encryptionBeforeBin[:102400]:
                # 转换字节进行加密
                encryptionAfterBin = encryptionAfterBin + bytes([encryptionSet[i]])
            # 相加
            encryptionAfterBin += encryptionBeforeBin[102400:]
            # 重写文件
        with open(filePath, 'wb') as file:
            file.write(encryptionAfterBin)


def de(filePath):
    decodeSet = {17: 0, 228: 1, 247: 2, 30: 3, 170: 4, 40: 5, 249: 6, 63: 7, 116: 8, 42: 9, 251: 10, 115: 11, 1: 12,
                 235: 13, 195: 14, 99: 15, 61: 16, 234: 17, 242: 18, 191: 19, 109: 20, 70: 21, 206: 22, 92: 23, 67: 24,
                 14: 25, 159: 26, 20: 27, 244: 28, 32: 29, 7: 30, 143: 31, 82: 32, 23: 33, 53: 34, 9: 35, 141: 36,
                 0: 37,
                 137: 38, 133: 39, 136: 40, 146: 41, 59: 42, 218: 43, 121: 44, 97: 45, 47: 46, 21: 47, 208: 48, 29: 49,
                 187: 50, 112: 51, 51: 52, 33: 53, 188: 54, 78: 55, 174: 56, 241: 57, 2: 58, 231: 59, 193: 60, 160: 61,
                 26: 62, 12: 63, 200: 64, 152: 65, 52: 66, 155: 67, 202: 68, 164: 69, 150: 70, 103: 71, 212: 72,
                 182: 73,
                 84: 74, 60: 75, 6: 76, 129: 77, 223: 78, 221: 79, 73: 80, 89: 81, 123: 82, 149: 83, 36: 84, 183: 85,
                 180: 86, 34: 87, 186: 88, 245: 89, 27: 90, 111: 91, 238: 92, 153: 93, 119: 94, 253: 95, 110: 96,
                 194: 97,
                 25: 98, 203: 99, 16: 100, 205: 101, 106: 102, 91: 103, 181: 104, 69: 105, 177: 106, 19: 107, 189: 108,
                 226: 109, 134: 110, 163: 111, 125: 112, 101: 113, 90: 114, 148: 115, 62: 116, 102: 117, 83: 118,
                 209: 119,
                 126: 120, 105: 121, 154: 122, 77: 123, 165: 124, 71: 125, 217: 126, 145: 127, 38: 128, 246: 129,
                 96: 130,
                 10: 131, 3: 132, 178: 133, 57: 134, 225: 135, 41: 136, 140: 137, 80: 138, 132: 139, 196: 140, 104: 141,
                 171: 142, 135: 143, 142: 144, 95: 145, 224: 146, 131: 147, 144: 148, 190: 149, 219: 150, 176: 151,
                 198: 152, 227: 153, 130: 154, 107: 155, 248: 156, 255: 157, 161: 158, 68: 159, 157: 160, 56: 161,
                 108: 162, 93: 163, 49: 164, 222: 165, 151: 166, 237: 167, 28: 168, 58: 169, 204: 170, 172: 171,
                 31: 172,
                 39: 173, 243: 174, 213: 175, 147: 176, 72: 177, 124: 178, 207: 179, 8: 180, 50: 181, 215: 182, 55: 183,
                 254: 184, 114: 185, 76: 186, 166: 187, 169: 188, 138: 189, 43: 190, 118: 191, 240: 192, 199: 193,
                 113: 194, 98: 195, 173: 196, 216: 197, 252: 198, 233: 199, 197: 200, 64: 201, 24: 202, 48: 203,
                 87: 204,
                 232: 205, 201: 206, 167: 207, 158: 208, 15: 209, 175: 210, 179: 211, 229: 212, 139: 213, 18: 214,
                 162: 215, 22: 216, 184: 217, 100: 218, 66: 219, 5: 220, 13: 221, 168: 222, 74: 223, 239: 224, 85: 225,
                 220: 226, 117: 227, 185: 228, 128: 229, 37: 230, 44: 231, 210: 232, 230: 233, 88: 234, 250: 235,
                 122: 236,
                 236: 237, 156: 238, 127: 239, 192: 240, 11: 241, 86: 242, 79: 243, 4: 244, 65: 245, 46: 246, 120: 247,
                 211: 248, 214: 249, 81: 250, 45: 251, 54: 252, 75: 253, 94: 254, 35: 255}
    # 操作之前的二进制
    decodeBeforeBin = b''
    # 操作之后的二进制
    decodeAfterBin = b''
    if re.match("(.*\.txt)|(.*\.docx)|(.*\.doc)|(.*\.wps)$", filePath) or os.path.getsize(filePath) < 102400:
        # 以字节为单位读取文件
        with open(filePath, 'rb') as file:
            # 获得文件的二进制文件
            decodeBeforeBin = file.read()
            # 循环遍历字节
            for i in decodeBeforeBin:
                # 转换字节进行解密
                decodeAfterBin = decodeAfterBin + bytes([decodeSet[i]])
        # 重写文件
        with open(filePath, 'wb') as file:
            file.write(decodeAfterBin)
    # 大文件
    else:
        with open(filePath, 'rb') as file:
            # 以字节为单位读取
            decodeBeforeBin = file.read()
            # 循环遍历前102400个字节
            for i in decodeBeforeBin[:102400]:
                # 转换字节进行加密
                decodeAfterBin = decodeAfterBin + bytes([decodeSet[i]])
            #   相加
            decodeAfterBin += decodeBeforeBin[102400:]
        # 重写文件
        with open(filePath, 'wb') as file:
            file.write(decodeAfterBin)


def encryption(path):
    if not os.path.exists(path):
        return False
    else:
        if os.path.isfile(path):
            en(path)
            print("加密" + path + "成功")
        else:
            files = getAllFilesByDir(path)
            for i in files:
                en(i)
                print("加密" + i + "成功")


def decode(path):
    if not os.path.exists(path):
        return False
    else:
        if os.path.isfile(path):
            de(path)
            print("解密" + path + "成功")
        else:
            files = getAllFilesByDir(path)
            for i in files:
                de(i)
                print("解密" + i + "成功")
