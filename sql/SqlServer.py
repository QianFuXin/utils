import pymssql


def __getCursor__(user, password, host, database):
    conn = pymssql.connect(host=host, user=user, password=password, database=database, charset="cp936")
    cur = conn.cursor()
    return cur, conn


# 返回格式为数组，数组内部单位是元组，一个元组代表一行数据[(),()]
def select(user, password, host, database, sql):
    cur, conn = __getCursor__(user, password, host, database)
    # 查询数据
    cur.execute(sql)
    li = cur.fetchall()

    cur.close()
    conn.close()
    return li


# columns为插入的列名，格式为[c1,c2,c3]
# data为插入的数据，格式为[(1，2，3),(4，5，6)]
def insert(user, password, host, database, table, columns, data):
    if len(data) == 0:
        return "数据为空"
    cur, conn = __getCursor__(user, password, host, database)
    # 拼接列名
    col = ",".join(columns)
    col = " (" + col + ")"
    # 拼接格式名
    tempFormat = "("
    tempFormat = tempFormat + len(data[0]) * "%s,"
    tempFormat = tempFormat[:-1] + ")"

    cur.executemany("INSERT INTO " + table + col + " VALUES " + tempFormat, data)
    conn.commit()

    cur.close()
    conn.close()
    return True


# condition的类型为str格式为 minTemperature=2 and maxTemperature=200
# 不建议不加条件执行where语句，会删除表中所有数据，所以当你删除表中所有数据时，会报错
def delete(user, password, host, database, table, condition):
    cur, conn = __getCursor__(user, password, host, database)
    cur.execute("DELETE FROM " + table + " where " + condition)
    conn.commit()

    cur.close()
    conn.close()
    return True


# columnAndValue是修改的列和值，格式为{"更新列1":更新值1","更新列2":更新值2}
# 不建议不加条件执行where语句，会更新表中列所有数据，所以当你更新表中列所有数据时，会报错
def update(user, password, host, database, table, condition, columnAndValue):
    cur, conn = __getCursor__(user, password, host, database)
    # 处理set 列=值
    tempSet = " SET "
    for k, v in columnAndValue.items():
        tempSet = tempSet + " " + str(k) + " = " + str(v) + " ,"
    tempSet = tempSet[:-1]

    cur.execute("UPDATE " + table + tempSet + " where " + condition)
    conn.commit()

    cur.close()
    conn.close()
    return True
