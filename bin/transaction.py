import okx.Trade as Trade
from config.config import SECRET_INFO,TEST_FLAG

class Transaction:
    def __init__(self):
        self.apikey = SECRET_INFO["APIKey"]
        self.secretkey = SECRET_INFO["SecretKey"]
        self.passphrase = SECRET_INFO["Passphrase"]
        self.flag = TEST_FLAG

        tradeAPI = Trade.TradeAPI(self.flagey, self.flagetkey, self.flagphrase, False, self.flag)

        # 现货模式限价单
        result = tradeAPI.place_order(
            instId="BTC-USDT",
            tdMode="cash",
            clOrdId="b15",
            side="buy",
            ordType="limit",
            px="2.15",
            sz="2"
        )

        print(result)

