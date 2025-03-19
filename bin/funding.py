from config.config import SECRET_INFO,TEST_FLAG
import okx.Funding  as Funding
import json

#资金账户类
class MyFuding(object):
    def __init__(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        # API 初始化
        self.availBalList = []
        self.frozenBalList = []
        self.API = None
        self.initAPI(API_KEY,API_SECRET,PASSPHRASE,FLAG)

    def initAPI(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        self.API = Funding.FundingAPI(api_key=API_KEY, api_secret_key=API_SECRET, passphrase=PASSPHRASE,
                           flag=FLAG)


if __name__ == '__main__':
    pass
