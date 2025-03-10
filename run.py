# main.py
from logs.log_step import LoggingHandler
from database.data_mysql import DataMySQL








if __name__ == '__main__':
    # 初始化日志
    log_handler = LoggingHandler()
    log_handler.setup_time_rotation()  # 或 setup_size_rotation()
    logger = log_handler.logger

    # 业务代码使用
    logger.info("started-application")


    DB = DataMySQL(logger)
    DB.connect()


    # 程序退出前释放资源
    log_handler.close()
    pass