# 下面两行代码防止pyinstaller打包不成功
from pymssql import _mssql
from pymssql import _pymssql
import pymssql
import pandas as pd


# 获得cursor
def __getCursor__(user, password, host, database, charset="UTF-8"):
    # 如果乱码用cp936
    conn = pymssql.connect(host=host, user=user, password=password, database=database, charset=charset)
    cur = conn.cursor()
    return cur, conn


# 更新操作的接口，包括更新和删除
def __updateAction__(user, password, host, database, sql):
    cur, conn = __getCursor__(user, password, host, database)
    # 如果中间发生异常，回滚,最终提交
    try:
        cur.execute(sql)
        conn.commit()
    except:
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()
        return True


# 获得表的列名，格式为列表
def getTableColumns(user, password, host, database, table):
    cur, conn = __getCursor__(user, password, host, database)
    cur.execute("select top 1 *  from " + table)
    col = cur.description
    li = [i[0] for i in col]
    cur.close()
    conn.close()
    return li


# 返回格式为数组，数组内部单位是元组，第一个元组是列名，一个元组代表一行数据[(),()]
# 第二个参数是DataFrame
def select(user, password, host, database, sql, charset="UTF-8"):
    cur, conn = __getCursor__(user, password, host, database, charset)
    # 查询数据
    cur.execute(sql)
    li = cur.fetchall()
    # 列名
    col = cur.description
    col = [i[0] for i in col]
    li = [tuple(col)] + li
    df = pd.DataFrame(li[1:], columns=li[0])
    cur.close()
    conn.close()
    return li, df


# columns为插入的列名，格式为[c1,c2,c3]
# data为插入的数据，格式为[(1，2，3),(4，5，6)]
# 如果不指定列名(很多列的情况下),把columns=""
def insert(user, password, host, database, table, columns, data):
    if len(data) == 0:
        return "数据为空"
    # 如果不指定列名，默认插入一行
    if "".__eq__(columns):
        columns = getTableColumns(user, password, host, database, table)
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
        return True
    except Exception as e:
        print(e)
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


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
