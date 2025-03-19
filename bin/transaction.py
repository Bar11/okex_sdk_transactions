import okx.Trade as Trade

class MyTrade(object):

    def __init__(self, API_KEY, API_SECRET, PASSPHRASE, FLAG):
        self.API = None
        self.initAPI(API_KEY, API_SECRET, PASSPHRASE, FLAG)
        self.params = {
            'ordType':"oco",
            'slTriggerPxType':"last",
            'tpTriggerPxType':"last",
            'tdMode':"cash"
        }

    # API 初始化
    def initAPI(self, API_KEY, API_SECRET, PASSPHRASE, FLAG):
        self.API = Trade.TradeAPI(api_key=API_KEY, api_secret_key=API_SECRET, passphrase=PASSPHRASE,
                                        flag=FLAG)

    # 委托数量
    def set_order_base(self,instId,sz,tgtCcy,side):
        self.params['sz'] = sz
        self.params['tgtCcy'] = tgtCcy
        self.params['instId'] = instId
        self.params['side'] = side

    # 设置止盈止损
    def set_TriggerPx_OrdPx(self,TriggerPx,OrdPx):
        self.params['tpTriggerPx'] = TriggerPx
        self.params['slTriggerPx'] = OrdPx
        self.params['tpOrdPx'] = '-1'
        self.params['slOrdPx'] = '-1'

    # 创建交易（策略交易）
    def place_algo_order(self):
        instId = self.params['instId']
        tdMode = self.params['tdMode']
        side = self.params['side']
        ordType = self.params['ordType']
        sz = self.params['sz']
        tgtCcy = self.params['tgtCcy']
        # tpTriggerPx = self.params['tpTriggerPx']
        # tpOrdPx = self.params['tpOrdPx']
        # slTriggerPx = self.params['slTriggerPx']
        # slOrdPx = self.params['slOrdPx']
        return self.API.place_algo_order(instId = instId, tdMode = tdMode, side = side,ordType = ordType, sz=sz,
                                  tgtCcy=tgtCcy, )

    # tpTriggerPx = tpTriggerPx, tpOrdPx = tpOrdPx, slTriggerPx = slTriggerPx, slOrdPx = slOrdPx


if __name__ == '__main__':
    pass
