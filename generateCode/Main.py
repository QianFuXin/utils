import os
import re

"""
因为人记住的内容有限,只是在脑中保存视图,不会记住所有内容,
所以该程序记录着一些常用且常忘的代码.
warehouse下面放着一些源文件,从源文件的命名你应该就有所了解,函数也同理
"""
# 获取文件夹下的所有py文件
files = os.listdir("warehouse")
files.remove("__init__.py")
files.remove("__pycache__")
for i in files:
    if re.match(".*\.py", i):
        # 导入源文件
        exec("from warehouse import " + i[:-3])

if __name__ == '__main__':
    # 获取所有源文件的文件名，不要.py后缀
    allType = []
    for i in files:
        allType.append(i[:-3])
    allType.sort()
    while True:
        typeId = [str(i) for i in range(1, len(allType) + 1)]
        relationshipType = dict(zip(typeId, allType))
        print("=========================")
        for i in relationshipType:
            print(i + "：" + relationshipType[i] + "代码")
        typeChoose = input("输入序号：")
        if typeChoose not in typeId:
            print("输入错误")
            exit(1)
        functions = []
        exec("functions=dir(" + relationshipType[typeChoose] + ")")
        for i in ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__',
                  '__spec__']:
            functions.remove(i)
        functionId = [str(i) for i in range(1, len(functions) + 1)]
        relationshipFunction = dict(zip(functionId, functions))
        print("=========================")
        for i in relationshipFunction:
            print(str(i) + "：" + relationshipFunction[i] + "")
        functionChoose = input("输入序号：")
        if functionChoose not in functionId:
            print("输入错误")
            exit(1)
        print("=========================")
        exec("print(" + relationshipType[typeChoose] + "." + relationshipFunction[functionChoose] + "()" + ")")
