import os
from config.config import *
from dotenv import load_dotenv
from .account import MyAccount
from .funding import MyFuding
from .marketdata import MyMarketData
from .transaction import MyTrade


class Robot(object):

    def __init__(self,Logger):
        self.API_KEY = "<KEY>"
        self.API_SECRET = "<KEY>"
        self.PASSPHRASE = "<PASSWORD>"
        self.FLAG = "<FLAGE>"
        self.Logger = Logger
        self.AccountAPI = None
        self.TradeAPI = None
        self.MarketAPI = None
        self.FundingAPI = None

    def load_config(self):
        if TEST_FLAG == "1":
            self.API_KEY = SECRET_INFO["API_KEY"]
            self.API_SECRET = SECRET_INFO["API_SECRET"]
            self.PASSPHRASE = SECRET_INFO["PASSPHRASE"]
            self.FLAG = SECRET_INFO["FLAG"]
            self.Logger.info("load test Robot config success!")
        else:
            load_dotenv()
            self.API_KEY = os.getenv("API_KEY")
            self.API_SECRET = os.getenv("API_SECRET")
            self.PASSPHRASE = os.getenv("PASSPHRASE")
            self.FLAG = os.getenv("FLAG")
            self.Logger.info("load formal Robot config success!")
        self.init_API()



    def init_API(self):
        self.AccountAPI = MyAccount(self.API_KEY, self.API_SECRET,self.PASSPHRASE,self.FLAG)
        self.TradeAPI = MyTrade(self.API_KEY, self.API_SECRET,self.PASSPHRASE,self.FLAG)
        self.FundingAPI = MyFuding(self.API_KEY, self.API_SECRET,self.PASSPHRASE,self.FLAG)
        self.MarketAPI = MyMarketData(self.API_KEY, self.API_SECRET,self.PASSPHRASE,self.FLAG)
        self.Logger.info("init API success!")

    # 直接请求账户信息，作为校验
    def CheckIdentity(self):
        # try:
            resp = self.AccountAPI.get_account_config()
            if resp["code"]=="0":
                self.Logger.info("check identity success!")
                return True
            else:
                self.Logger.error(resp['code'] +"  "+ resp['msg']  )
                return False
        # except:
        #     self.Logger.error("check identity failed!！！")
        #     return False



    def data_init(self):
        # 获取交易产品基础信息
        data = self.AccountAPI.get_instruments_SPOT()
        print(data)

    def processing_response(self, response):
        pass
