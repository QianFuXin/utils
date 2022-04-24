# encoding:utf-8
from sqlalchemy import create_engine


def createMysqlEngine(user, password, host, database, port=3306):
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")
    return engine


def createSqlServerEngine(user, password, host, database, port=1433):
    engine = create_engine(f"mssql+pymssql://{user}:{password}@{host}:{port}/{database}")
    return engine
