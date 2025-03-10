from config.config import SECRET_INFO,TEST_FLAG
import okx.Funding  as Funding
import json

#资金账户类
class MyFuding(object):
    def __init__(self):
        # API 初始化
        self.apikey = SECRET_INFO["APIKey"]
        self.secretkey = SECRET_INFO["SecretKey"]
        self.passphrase = SECRET_INFO["Passphrase"]
        self.flag = TEST_FLAG
        self.FundingAPI = Funding.FundingAPI(self.apikey, self.secretkey, self.passphrase, False, self.flag)

    # 获取币种列表
    def get_currencies(self,ccy=''):
        return self.FundingAPI.get_currencies(ccy=ccy)

    # 获取资金账户余额
    def get_balance(self):
        return self.FundingAPI.get_balances()

    # 获取不可交易资产
    def get_non_tradable_assets(self):
        return self.FundingAPI.get_non_tradable_assets()

    # 获取账户资产估值
    def get_asset_valuation(self):
        return self.accountAPI.get_asset_valuation()

    # 资金划转
    def funds_transfer(self):
        pass
    # 获取资金流水
    def get_bills(self):
        pass

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
