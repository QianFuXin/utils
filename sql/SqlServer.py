import pymssql


# 获得cursor
def __getCursor__(user, password, host, database):
    conn = pymssql.connect(host=host, user=user, password=password, database=database, charset="cp936")
    cur = conn.cursor()
    return cur, conn


# 更新操作的接口，包括更新和删除
def __updateAction__(user, password, host, database, sql):
    cur, conn = __getCursor__(user, password, host, database)
    # 如果中间发生异常，回滚,最终提交
    try:
        cur.execute(sql)
        cur.commit()
    except:
        cur.rollback()
        return False
    finally:
        cur.close()
        conn.close()
        return True


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
    # 拼接格式名
    format = len(data[0]) * "%s,"
    format = format[:-1]
    # 替换sql
    sql = "INSERT INTO 表(列)"" VALUES (格式)" \
        .replace("表", table).replace("列", col).replace("格式", format)
    # 如果插入数据发生异常，回滚
    try:
        cur.executemany(sql, data)
        conn.commit()
    except Exception as e:
        cur.rollback()
        return False
    finally:
        cur.close()
        conn.close()
        return True


# condition的类型为str格式为 minTemperature=2 and maxTemperature=200
# 不建议不加条件执行where语句，会删除表中所有数据，所以当你删除表中所有数据时，会报错
def delete(user, password, host, database, table, condition):
    sql = "DELETE FROM 表 where 条件" \
        .replace("表", table).replace("条件", condition)
    return __updateAction__(user, password, host, database, sql)


# columnAndValue是修改的列和值，格式为{"更新列1":更新值1","更新列2":更新值2}
# 不建议不加条件执行where语句，会更新表中列所有数据，所以当你更新表中列所有数据时，会报错
def update(user, password, host, database, table, condition, columnAndValue):
    # 处理set 列=值
    update = ""
    for k, v in columnAndValue.items():
        update = update + str(k) + " = " + str(v) + " ,"
    update = update[:-1]

    sql = "UPDATE 表 SET 赋值 where 条件" \
        .replace("表", table).replace("赋值", update).replace("条件", condition)

    return __updateAction__(user, password, host, database, sql)


# 传进来纯sql，执行sql，建议增删改，不建议查询，因为看不到查询的内容
def runSql(user, password, host, database, sql):
    return __updateAction__(user, password, host, database, sql)
