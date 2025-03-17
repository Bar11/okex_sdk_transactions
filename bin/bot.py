import os
from config.config import *
from dotenv import load_dotenv
import okx.Account as Account
# import okx. as Order
import okx.Funding as Funding
import okx.Trade as Trade
import okx.MarketData as MarketData


class Robot(object):

    def __init__(self,Logger):
        self.API_KEY = "<KEY>"
        self.API_SECRET = "<KEY>"
        self.PASSPHRASE = "<PASSWORD>"
        self.FLAG = "<FLAGE>"
        self.Logger = Logger
        self.AccountAPI = None
        self.orderAPI = None
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
        print(self.API_KEY)
        print(self.API_SECRET)
        print(self.PASSPHRASE)
        print(self.FLAG)
        self.AccountAPI = Account.AccountAPI(api_key=self.API_KEY, api_secret_key=self.API_SECRET,passphrase=self.PASSPHRASE,flag=self.FLAG)
        self.TradeAPI = Trade.TradeAPI(api_key=self.API_KEY, api_secret_key=self.API_SECRET,passphrase=self.PASSPHRASE,flag=self.FLAG)
        self.FundingAPI = Funding.FundingAPI(api_key=self.API_KEY,api_secret_key=self.API_SECRET,passphrase=self.PASSPHRASE,flag=self.FLAG)
        self.MarketAPI = MarketData.MarketAPI(api_key=self.API_KEY, api_secret_key=self.API_SECRET,passphrase=self.PASSPHRASE,flag=self.FLAG)
        self.Logger.info("init API success!")

    # 直接请求账户信息，作为校验
    def CheckIdentity(self):
        try:
            resp = self.AccountAPI.get_account_balance()
            if resp["code"]=="0":
                self.Logger.info("check identity success!")
                self.proccessing_account_balance(resp)
                return True
            else:
                self.Logger.error(resp['code'] +"  "+ resp['msg']  )
                return False
        except:
            self.Logger.error("check identity failed!！！")
            return False

    # 账户余额数据解析
    def proccessing_account_balance(self,data):
        data = data["data"]
        availBal_list = []
        frozenBal_list = []
        for d in data:
            if d['availBal']>0 and d['Bal']>0:
                availBal_list.append(d)
            elif d['frozenBal']>0:
                frozenBal_list.append(d)
            else:
                pass
        return Account




    def processing_response(self, response):
        pass
