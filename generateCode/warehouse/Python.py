def 自然数_虚数_布尔的加减乘除():
    info = """
# 1
5 + 2 - 3 * 2

# 2.5
5 / 2

# 2
5 // 2

# 1
5 % 2

# 256
2 ** 8

# 1000000003000000003000000001
1000000001 ** 3

# 33.13784737771648
x = 4.3 ** 2.4

# 9.695e+75
3.5e30 * 2.77e45

# 1.000000003e+27
1000000001.0 ** 3

# 复数
# (0.6817665190890336 - 2.1207457766159625j)
(3 + 2j) ** (2 + 3j)

# (-6 + 35j)
(3 + 2j) * (4 + 9j)

# -6.0 实部
x.real

# 35.0 虚部
x.imag

# 3
round(3.49)

import math
# 4
math.ceil(3.49)

# 布尔
x = False

# True
not x

# 2
y = True * 2
"""
    return info


def 列表():
    info="""
x = ["first", "second", "third", "fourth"]
x[0]
'first'

x[2]
'third'

x[-1]
'fourth'

x[-2]
'third'

x[1:-1]
['second', 'third']

x[0:3]
['first', 'second', 'third']

x[-2:-1]
['third']

x[:3]
['first', 'second', 'third']

x[-2:]
['third', 'fourth']

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x[1] = "two"
x[8:9] = []

x
[1, 'two', 3, 4, 5, 6, 7, 8]

x[5:7] = [6.0, 6.5, 7.0]

x
[1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]

x[5:]
[6.0, 6.5, 7.0, 8]

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

len(x)
9

[-1, 0] + x
[-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

x.reverse()
x
[9, 8, 7, 6, 5, 4, 3, 2, 1]    
"""
    return info
def 元组():
    pass
def 字符串():
    pass
def 集合():
    pass
def 字典():
    pass

def aboutDic():
    info = """
    # 生成字典的快捷方式
    dic = {x: x * x for x in range(100)}
    dic = dict(zip((1, 2, 3), (4, 5, 6)))
    # 遍历字典
    for k, v in dic.items():
        print("{} --> {}".format(k, v))
    """.lower()

    return info


def aboutSet():
    info = """
    a = {1,2,3}
    b = {2, 3}
    #并集 |
    print(a.union(b))
    # 差集 -
    print(a.difference(b))
    # 交集 &
    print(a.intersection(b))
    """.lower()
    return info


def aboutLambda():
    info = """
    list = [(1, 2, 3), (2, 1, 3), (3, 1, 2)]
    # 按照列表元组第二个元素进行排序 传进来item，传出去item[1]
    list.sort(key=lambda item: item[1])
       """.lower()

    return info


def aboutNumpy():
    info = """
import numpy as np
list = [1, 2, 3, 4]
arr = np.array(list)
# 数组中每个元素对应操作
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr / arr)
print(arr % arr)
print(arr ** arr)
# sin值
print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))
print(np.log(arr))
print(np.log2(arr))
print(np.log10(arr))
print(np.exp(arr))

# 生成数组 0 到11 间隔2
print(np.arange(0, 11, 2))
# 开始1，结束9，18个点
print(np.linspace(1, 9, 18))

# 二维数组
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(list))
# 元组转数组
list = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
print(np.array(list))
# 维度等信息
print(list.ndim)
print(list.size)
print(list.shape)
print(list.dtype)

# 10个零
print(np.zeros(10))
print(np.zeros((10, 10)))
# 全是5
print(5 * np.ones((10, 10)))
# 10x10的单位矩阵
print(np.eye(10))
# 随机形状矩阵
print(np.random.randint(low=1, high=10, size=(4, 4)))
# flatten ravel 扁平化
print(np.ravel(np.arange(12).reshape(3, 4)))
# 二项分布
# 抛20枚硬币，正面向上0.6，现在重复八次，求每次20枚硬币正面朝上的数量
print(np.random.binomial(20000, 0.5, 8))
# 正态分布
print(np.random.normal(loc=155, scale=10, size=100))
# 输出随机矩阵
print(np.random.rand(3, 3))
""".lower()

    return info


def aboutPandas():
    info = """
import pandas as pd
import numpy as np
data = [1, 2, 3, 4, 5]
index = ['a', 'b', 'c', 'd', 'e']
dic = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5'}
# 实例化series
print(pd.Series(data=data))
print(pd.Series(data=data, index=index))
print(pd.Series(data=dic))

# 实例化dataframe
matrix_data = np.random.randint(1, 10, 20).reshape(5, 4)
row_lables = ['a', 'b', 'c', 'd', 'e']
columns_lables = ['A', 'B', 'C', 'D']
# 没有所谓的行列，行转就变为列。列名和行名
print(pd.DataFrame(data=matrix_data))
print(pd.DataFrame(data=matrix_data, index=row_lables, columns=columns_lables))
# 字典生成dataFrame
dic = {"a": [1, 2], "b": [3, 4], "c": [5, 6]}
print(pd.DataFrame(data=dic, index=['A', 'B']))
df = pd.DataFrame(data=dic, index=['A', 'B'])
# 输出头和尾
df.head()
df.tail()
# 访问某一列
print(df['a'])
print(df[['a', 'b']])
# 访问列名某一行 第二个参数可选择访问的列
print(df.loc['A'])
print(df.loc[['A', "B"]])
# 通过index访问某一行
print(df.iloc[1])
print(df.iloc[[0, 1]])
# 添加一列
df['d'] = df['a'] + df['b']
print(df)
# 删除某一行  赋值给新的df，当inplace为true，删除原始的数据 axis=1 删除某一列
print(df.drop('A'))
# 计算某列的数量、总和、平均数、中位数（50%,又可以分25%，75%）、最大值、最小值、标准差
# 也可以用describe实现
print(df.describe())
print(df['a'].count())
print(df['a'].sum())
# 平均值
print(df['a'].mean())
# 中位数
print(df['a'].median())
print(np.percentile(df['a'], 25))
print(np.percentile(df['a'], 75))
print(df['a'].max())
print(df['a'].min())
# 标准差
print(df['a'].std())
# 返回去重结果
df['a'].unique()
# 返回去重结果的数量
df['a'].nunique()
# where a >1
df[df'a'] > 1]
#  where where a >0 and b>1
print(df[(df['a'] > 0) & (df['b'] > 1)])
# 如果method='ffill' na的填充值是空值前面的值
# 如果method='bfill' na的填充值是空值后面的值
df['a'].fillna(method='ffill')
# axis=0 删除行 axis=1 删除列 thresh=10 如果该行该列非na的数量大于10，则不删除这一行列
df.dropna(axis=0,thresh=10)
""".lower()

    return info


def aboutMatplotlib():
    info = """
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
plt.rcParams['font.sans-serif'] = ['SimHei']  ###解决中文乱码
plt.rcParams['axes.unicode_minus'] = False
age = np.random.randint(18, 25, 10)
weight = np.random.randint(60, 100, 10)

# 设置图的宽度和高度
plt.figure(figsize=(8, 6))
# 设置标题
plt.title("这是一个标题", fontdict={'fontproperties': font_set})
# 设置x轴标签
plt.xlabel("这是一个X轴标签", fontdict={'fontproperties': font_set})
# # 设置y轴标签
plt.ylabel("这是一个Y轴标签", fontdict={'fontproperties': font_set})
# 配置网格线
plt.grid(True)
# 获取或设置当前轴的 y 范围。
plt.ylim(0, 100)
# 获取或设置 x 轴的当前刻度位置和标签。
plt.xticks([i * 2 for i in range(12)])
# 散点图
plt.scatter(x=age, y=weight, c='orange', s=150, edgecolors='k')
# 向图添加文本
plt.text(x=20, y=70, s="这是一个文本", fontdict={'fontproperties': font_set})
# 在从ymin到ymax 的每个x处绘制垂直线。
plt.vlines(x=20, ymin=0, ymax=80, linestyles="dashed", colors=['blue'])
# 在轴上放置图例。
plt.legend(["这是一个legend"], loc=2, fontsize=15)
plt.show()
""".lower()

    return info
