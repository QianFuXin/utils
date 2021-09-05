"""
1、参数
grid是数独中所有的数
row是行下标
col是列下标
2、主要功能
寻找空值并返回对应的行列下标
3、返回值
x、y是空值的行列下标
如果数独中没有空值，就返回-1,-1
"""


def getNullIndex(grid, row, col):
    # 从row，col开始遍历
    for x in range(row, 9):
        for y in range(col, 9):
            if grid[x][y] == 0:
                return x, y
    # 从头开始遍历
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    # 没有空值返回-1，-1
    return -1, -1


"""
1、参数：
grid是数独中所有的数，row是行下标、col是列下标、value是填入的值
2、主要功能：
判断填入的值是否符合规则（行、列、九宫格不能重复规则）
3、返回值：
True代表符合规则，False代表不符合规则
"""


def judgeValue(grid, row, col, value):
    # 行结果
    rowValid = all([value != grid[row][x] for x in range(9)])
    # 行合法
    if rowValid:
        # 列结果
        colValid = all([value != grid[x][col] for x in range(9)])
        # 列合法
        if colValid:
            # 最小行、列的下标
            minRow, minCol = 3 * (row // 3), 3 * (col // 3)
            # 遍历所在的九宫格
            for x in range(minRow, minRow + 3):
                for y in range(minCol, minCol + 3):
                    if grid[x][y] == value:
                        return False
            # 九宫格合法
            return True
    # 行不合法
    return False


# 利用深度优先搜索去解决数独问题
"""
1、参数：
grid是数独中所有的数，row是行下标、col是列下标
2、主要功能：
开始填入正确的值
"""


def DFS2SD(grid, row=0, col=0):
    # 得到空值的index
    i, j = getNullIndex(grid, row, col)
    # 数独中没有空值
    if i == -1:
        return True
    # 填入1-10的所有数
    for k in range(1, 10):
        # 如果这个数字符合规则
        if judgeValue(grid, i, j, k):
            # 对空值进行赋值
            grid[i][j] = k
            # 调用自己，递归。
            if DFS2SD(grid, i, j):
                return True
            # 如果递归返回False，把空值复位为0
            grid[i][j] = 0
    return False


def parseSD(matrix):
    """
    # 数独的输入格式，第1行，第二行...第n行，未知数用0代替。
    matrix = [[0, 1, 0, 0, 0, 8, 4, 0, 7],
              [9, 5, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 8, 0, 1, 0, 0, 0, 0],
              [0, 8, 2, 0, 0, 0, 0, 0, 0],
              [7, 0, 0, 4, 0, 6, 0, 0, 8],
              [0, 0, 0, 0, 0, 0, 6, 2, 0],
              [0, 0, 0, 0, 5, 0, 7, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 8, 2],
              [5, 0, 3, 2, 0, 0, 0, 1, 0]]
    """
    DFS2SD(matrix)
    """
    建议如下方输出，更有结构性
    # 输出数独
    for i in matrix:
        print(i)
    """
    return matrix
