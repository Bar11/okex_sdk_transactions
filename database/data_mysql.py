from logging import Logger

import pymysql,logging,os
from config.config import *
from dotenv import load_dotenv

# 数据库
class DataMySQL(object):
    def __init__(self,Logger):
        self.Logger=Logger
        self.DB = MYSQL_INFO["db"]
        self.DB_Host = MYSQL_INFO["host"]
        self.DB_Port = MYSQL_INFO["port"]
        if TEST_FLAG == "1":
            self.DB_User = MYSQL_INFO["user"]
            self.DB_Password = MYSQL_INFO["password"]
            self.Logger.info("load test config success!")
        else:
            load_dotenv(dotenv_path='.env')
            self.DB_User = os.getenv("DB_USER")
            self.DB_Password = os.getenv("DB_PASSWORD")
            self.Logger.info("load formal config success!")


    def connect(self):
        """建立数据库连接‌:ml-citation{ref="1,3" data="citationList"}"""
        try:
            self.conn = pymysql.connect(
                host=self.DB_Host,
                port=self.DB_Port,
                user=self.DB_User,
                password=self.DB_Password,
                db=self.DB,
                charset='utf8mb4',  # 字符集设置‌:ml-citation{ref="3,5" data="citationList"}
                cursorclass=pymysql.cursors.DictCursor  # 字典类型游标‌:ml-citation{ref="4" data="citationList"}
            )
            self.cursor = self.conn.cursor()
            self.Logger.info("database connecting successfully!")
        except pymysql.Error as e:
            self.Logger.error(e)
            raise


    def disconnect(self):
        """关闭连接和游标‌:ml-citation{ref="1,3" data="citationList"}"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

        self.Logger.info("database disconnecting successfully!")

    def execute(self, sql,params=None):
        """执行SQL语句‌:ml-citation{ref="1,3" data="citationList"}"""
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()  # 自动提交事务‌:ml-citation{ref="4" data="citationList"}
            return self.cursor
        except pymysql.Error as e:
            self.conn.rollback()  # 事务回滚‌:ml-citation{ref="4" data="citationList"}
            self.Logging.log(logging.ERROR, e)
            raise

    def initDB(self):
        """初始化数据库连接‌:ml-citation{ref="3" data="citationList"}"""
        self.connect()
        self.Logger.info("database init successfully!")

        # self.disconnect()

# 使用示例
if __name__ == "__main__":
    db = DataMySQL(logging.getLogger("DEBUG"))
    try:
        db.initDB()
        # result = db.execute("SELECT * FROM your_table LIMIT 5")
        # print(result.fetchall())
    finally:
        db.disconnect()