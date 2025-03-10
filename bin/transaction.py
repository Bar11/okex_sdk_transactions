import okx.Trade as Trade
from config.config import SECRET_INFO,TEST_FLAG

class Transaction:
    def __init__(self):
        self.apikey = SECRET_INFO["APIKey"]
        self.secretkey = SECRET_INFO["SecretKey"]
        self.passphrase = SECRET_INFO["Passphrase"]
        self.flag = TEST_FLAG
        self.tradeAPI = Trade.TradeAPI(self.flagey, self.flagetkey, self.flagphrase, False, self.flag)

    # 现货模式限价单
    def place_order(self,order_data):
        instId = order_data['instId']
        tdMode = order_data['tdMode']
        clOrdId = order_data['clOrdId']
        side = order_data['side']
        ordType = order_data['ordType']
        px = order_data['px']
        sz = order_data['sz']
        return self.tradeAPI.place_order(instId=instId,
                                        tdMode=tdMode,
                                        clOrdId=clOrdId,
                                        side=side,
                                        ordType=ordType,
                                        px=px,
                                        sz=sz)

    # 撤单
    def cancel_order(self,instId,ordId ):
        return self.tradeAPI.cancel_order(instId=instId,ordId=ordId)
