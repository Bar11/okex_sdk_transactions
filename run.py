# main.py

from database.data_mysql import DataMySQL
from logs.log_step import LoggingHandler
from bin.bot import Robot

class  Run(object):
    def __init__(self):
        self.Logger = None
        self.Bot = None

    def setup(self):
        self.init_log()
        self.init_DB(self.Logger)
        self.init_Bot(self.Logger)
        self.Bot.load_config()
        self.Bot.CheckIdentity()

    def init_Bot(self,Logger):
        self.Bot = Robot(Logger)

    def init_log(self):
        # 初始化日志
        log_handler = LoggingHandler()
        log_handler.setup_time_rotation()  # 或 setup_size_rotation()
        self.Logger = log_handler.logger
        self.Logger.info("init-log success!")

    def init_DB(self, Logger):
        # 连接并初始化数据库
        self.DB = DataMySQL(Logger)
        self.DB.connect()




if __name__ == '__main__':
    r= Run()
    r.setup()
    bot_ = r.Bot
    bot_.TradeAPI.set_order_base("ETH-USDT","4","quote_ccy","buy")
    resp = bot_.TradeAPI.place_algo_order()
    print(resp)
