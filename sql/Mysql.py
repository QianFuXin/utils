from utils.sql.Records import *


# 每个文件原始只有增删查改的功能，后期遇到实际问题，可以添加

def select(user, password, host, database, sql):
    temp = "mysql+pymysql://用户名:密码@主机/数据库" \
        .replace("用户名", user).replace("密码", password). \
        replace("主机", host).replace("数据库", database)
    db = Database(temp)
    rows = db.query(sql)
    li = []
    for i in rows:
        li.append(tuple(i))
    return li


print(select("root", "JingDianCloud2021", "192.168.81.129", "qianfuxin", "select * from person"))
"""
  ``dialect[+driver]://user:password@host/dbname[?key=value..]``, where
    ``dialect`` is a database name such as ``mysql``, ``oracle``,
    ``postgresql``, etc., and ``driver`` the name of a DBAPI, such as
    ``psycopg2``, ``pyodbc``, ``cx_oracle``, etc.  Alternatively,
    the URL can be an instance of :class:`~sqlalchemy.engine.url.URL`.
"""
