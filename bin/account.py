from config.config import SECRET_INFO,TEST_FLAG
import okx.Account as Account
import json


class MyAccount(object):
    def __init__(self):
        # API 初始化
        self.apikey = SECRET_INFO["APIKey"]
        self.secretkey = SECRET_INFO["SecretKey"]
        self.passphrase = SECRET_INFO["Passphrase"]
        self.flag = TEST_FLAG
        self.accountAPI = Account.AccountAPI(self.apikey, self.secretkey, self.passphrase, False, self.flag)

    def get_instruments(self):
        return json.loads(self.accountAPI.get_instruments())

    def get_balance(self):
        return self.accountAPI.get_account_balance()

    # 查看账户账单详情 （近七日内）
    def get_account_bills(self):
        return self.accountAPI.get_account_bills()

    # 查看账户账单详情 （近三个月内）
    def get_account_bills_archive(self):
        return self.accountAPI.get_account_bills_archive()

    # 查看账户配置
    def get_config(self):
        return self.accountAPI.get_account_config()

    # 获取最大可买卖/开仓数量
    def get_max_order_size(self,instId):
        return  self.accountAPI.get_max_order_size(instId=instId,tdMode="cash")

    # 获取instId(交易对“BTC-USDT”)币币最大可用数量
    def get_max_avail_size(self,instId):
        return self.accountAPI.get_max_avail_size(instId=instId,tdMode="cash")

    # 获取当前账户交易手续费费率
    def get_fee_rates(self,instType,instId):
        return self.accountAPI.get_fee_rates(instType=instType,instId=instId )


if __name__ == '__main__':
    a = MyAccount()
    balance = a.get_balance()
    for data in balance['data'][0]['details']:
        if data['ccy'] == 'USDT':
            for k,v in data.items():
                print (k,v)
