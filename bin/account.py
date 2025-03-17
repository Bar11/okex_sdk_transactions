from config.config import SECRET_INFO,TEST_FLAG
import okx.Account as Account
import json


class MyAccount(object):
    def __init__(self,availBal,frozenBal):
        # API 初始化
        self.availBalList = availBal
        self.frozenBalList = frozenBal




if __name__ == '__main__':
    a = MyAccount()
    balance = a.get_balance()
    for data in balance['data'][0]['details']:
        if data['ccy'] == 'USDT':
            for k,v in data.items():
                print (k,v)
