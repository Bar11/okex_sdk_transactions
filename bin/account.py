
import okx.Account as Account


class MyAccount(object):
    def __init__(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        self.availBalList = []
        self.frozenBalList = []
        self.API = None
        self.initAPI(API_KEY,API_SECRET,PASSPHRASE,FLAG)
        self.config = None

    # API 初始化
    def initAPI(self,API_KEY,API_SECRET,PASSPHRASE,FLAG):
        self.API = Account.AccountAPI(api_key=API_KEY, api_secret_key=API_SECRET, passphrase=PASSPHRASE,
                           flag=FLAG)

    def get_account_config(self):
        resp =  self.API.get_account_config()
        self.config = resp['data']
        return resp

    # 获取账户信息
    def get_account_balance(self, ccy=''):
        return self.API.get_account_balance(ccy=ccy)

    # 账户余额数据解析
    def proccessing_account_balance(self,data):
        data = data["data"]
        for d in data:
            if d['availBal']>0 and d['Bal']>0:
                self.availBalList.append(d)
            elif d['frozenBal']>0:
                self.frozenBalList.append(d)
            else:
                pass

    # SPOT：币币
    def get_instruments_SPOT(self,instId=""):
        return self.API.get_instruments(instType="SPOT",instId=instId)

    # SWAP：永续合约 FUTURES：交割合约 OPTION：期权
    # MARGIN：币币杠杆
    def get_instruments_MARGIN(self,instId=""):
        return self.API.get_instruments(instType="MARGIN",instId=instId)



if __name__ == '__main__':
    pass