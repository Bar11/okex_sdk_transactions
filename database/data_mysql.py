import pymysql,logging
from config.config import MYSQL_INFO,LOGGING_LEVEL

# 数据库
class DataMySQL(object):
    def __init__(self,Logger):
        self.port = MYSQL_INFO['port']
        self.user = MYSQL_INFO['user']
        self.password = MYSQL_INFO['password']
        self.db = MYSQL_INFO['db']
        self.host = MYSQL_INFO['host']
        self.Logger = Logger

    def connect(self):
        """建立数据库连接‌:ml-citation{ref="1,3" data="citationList"}"""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.db,
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