def createDataBase():
    info = """
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name
[create_option] ...
create_option: [DEFAULT] {
CHARACTER SET [=] charset_name
| COLLATE [=] collation_name
}
# 例子
CREATE DATABASE IF NOT EXISTS 数据库名 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
""".lower()
    return info


def deleteDataBase():
    info = """
drop database IF EXISTS 数据库名        
""".lower()
    return info


def createTable():
    info = """
CREATE TABLE IF NOT EXISTS 表名 (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    FOREIGN KEY (task_id) REFERENCES tasks (task_id)
) ENGINE=INNODB DEFAULT CHARSET=utf8;
""".lower()
    return info


def insertData():
    info = """
insert into 表名(列) value(值)
""".lower()
    return info
