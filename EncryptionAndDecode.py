# coding:utf-8
from utils.GetPath import *
import random

# 设置随机种子
seed = 20210903
# 加密的头部大小,前10240个字节全部加密
head = 10240
# 10240之后的字节,第10个替换,可以把10换成5,把间隔缩小,但是会带来性能上的降低
interval = 10
random.seed(seed)
# 生成钥匙和锁
key = [i for i in range(256)]
lock = [i for i in range(256)]
# 打乱
random.shuffle(key)
# {key:lock,key:lock}
encryptionDic = dict(zip(key, lock))
# {lock:key,lock:key}
decodeDic = dict(zip(lock, key))


# 加密解密操作
def __action__(path, dic):
    temp = b''
    # 如果大小大于10240
    if os.path.getsize(path) <= head:
        # 读文件
        with open(path, 'rb') as file:
            # 以字节为单位读取
            for i in file.read():
                temp = temp + bytes([dic[i]])
        # 写文件
        with open(path, 'wb') as file:
            file.write(temp)
    # 10250  10260 10270 开始加密
    else:
        index = 1
        # 读文件
        with open(path, 'rb') as file:
            # 以字节为单位读取
            for i in file.read():
                # 分为加密和不加密
                # 当index小于head时加密
                if index <= head:
                    temp = temp + bytes([dic[i]])
                else:
                    # index%10==0  加密
                    if index % interval == 0:
                        temp = temp + bytes([dic[i]])
                    # 不加密
                    else:
                        temp = temp + bytes([i])
                index = index + 1
        # 写文件
        with open(path, 'wb') as file:
            file.write(temp)


# 对路径进行操作
def __processPath__(path, dic):
    processName = "加密" if dic == encryptionDic else "解密"
    if not os.path.exists(path):
        print("路径" + path + "不存在")
        return False
    else:
        if os.path.isfile(path):
            __action__(path, dic)
            print(processName + path + "成功")
        # 如果路径是文件夹,获得该文件夹下所有文件
        else:
            files = getAllFilesByDir(path)
            for i in files:
                __action__(i, dic)
                print(processName + i + "成功")


# 加密
def en(path):
    path = r"" + path
    __processPath__(path, encryptionDic)


# 解密
def de(path):
    path = r"" + path
    __processPath__(path, decodeDic)
