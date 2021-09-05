from utils.sql.Records import *


# 生成环境
def __getContext__(user, password, host, database):
    connect = "mysql+pymysql://用户名:密码@主机/数据库" \
        .replace("用户名", user).replace("密码", password). \
        replace("主机", host).replace("数据库", database)
    db = Database(connect)
    return db


# 更新操作的接口 包括删除和更新
def __updateAction__(user, password, host, database, sql):
    db = __getContext__(user, password, host, database)
    conn = db.get_connection()
    tx = conn.transaction()
    # 发生异常，数据回滚
    try:
        db.query(sql)
        tx.commit()
    except Exception as e:
        if "ResourceClosedError" in str(repr(e)):
            tx.commit()
            return True
        else:
            print(sql)
            print(repr(e))
            tx.rollback()
        return False
    finally:
        conn.close()
        return True


# 查询
def select(user, password, host, database, sql):
    li = []
    db = __getContext__(user, password, host, database)
    rows = db.query(sql)
    for i in rows:
        li.append(tuple(i))
    db.close()
    return li


# columns为插入的列名，格式为[c1,c2,c3]
# data为插入的数据，格式为[(1，2，3),(4，5，6)]
def insert(user, password, host, database, table, columns, data):
    if len(data) == 0:
        return "数据为空"
    db = __getContext__(user, password, host, database)
    # 拼接列名
    col = ",".join(columns)
    # 拼接格式名
    format = ""
    for i in columns:
        format += ":" + i + ","
    format = format[:-1]
    # 拼接插入的数据格式
    li = []
    for i in data:
        dic = {}
        for k in range(len(i)):
            dic[columns[k]] = i[k]
        li.append(dic)

    # 替换sql
    sql = "INSERT INTO 表(列)"" VALUES (格式)" \
        .replace("表", table).replace("列", col).replace("格式", format)
    conn = db.get_connection()
    tx = conn.transaction()
    # 发生异常，数据回滚
    try:
        db.bulk_query(sql, li)
        tx.commit()
    except Exception as e:
        print(sql)
        print(repr(e))
        tx.rollback()
    finally:
        conn.close()
        return True


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
    __updateAction__(user, password, host, database, sql)
    return True


# condition的类型为str格式为 minTemperature=2 and maxTemperature=200
# 不建议不加条件执行where语句，会删除表中所有数据，所以当你删除表中所有数据时，会报错
def delete(user, password, host, database, table, condition):
    sql = "DELETE FROM 表 where 条件" \
        .replace("表", table).replace("条件", condition)
    return __updateAction__(user, password, host, database, sql)


# 传进来纯sql，执行sql(建议进行增删改，不建议进行查询)，不建议查询，因为看不到查询的内容
def runSql(user, password, host, database, sql):
    return __updateAction__(user, password, host, database, sql)
