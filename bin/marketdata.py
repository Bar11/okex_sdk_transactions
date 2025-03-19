import okx.MarketData as MarketData
from config.config import SECRET_INFO




class MyMarketData(object):
    def __init__(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        self.API = None
        self.initAPI(API_KEY,API_SECRET,PASSPHRASE,FLAG)

    # API 初始化
    def initAPI(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        self.API = MarketData.MarketAPI(api_key=API_KEY, api_secret_key=API_SECRET, passphrase=PASSPHRASE,
                           flag=FLAG)


if __name__ == '__main__':
    pass
