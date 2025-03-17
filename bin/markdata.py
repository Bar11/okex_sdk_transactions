import okx.MarketData as MarketData
from config.config import SECRET_INFO




class MarkData:
    def __init__(self):
        self.flag = SECRET_INFO["Flag"]
        self.marketDataAPI =  MarketData.MarketAPI(flag=SECRET_INFO["Flag"])

    # 获取所有产品行情信息
    def get_tickers(self):
        return self.marketDataAPI.get_tickers(instType="SPOT")

    # 获取产品行情信息
    def get_ticker(self,instId):
        return self.marketDataAPI.get_ticker(instId=instId)

    # 获取产品深度
    def get_orderbook(self,instId):
        return self.marketDataAPI.get_orderbook(instId=instId)

    # 获取K线数据。K线数据按请求的粒度分组返回，K线数据每个粒度最多可获取最近1,440条。
    def get_candlesticks(self,instId):
        return self.marketDataAPI.get_candlesticks(instId=instId)

    # 获取最近几年的历史k线数据(1s k线支持查询最近3个月的数据)
    '''
    after 请求此时间戳之前（更旧的数据）的分页内容，传的值为对应接口的ts
    before 请求此时间戳之后（更新的数据）的分页内容，传的值为对应接口的ts, 单独使用时，会返回最新的数据。
    bar 时间粒度，默认值1m 如 [1s/1m/3m/5m/15m/30m/1H/2H/4H]
                        香港时间开盘价k线：[6H/12H/1D/2D/3D/1W/1M/3M]
                        UTC时间开盘价k线：[6Hutc/12Hutc/1Dutc/2Dutc/3Dutc/1Wutc/1Mutc/3Mutc]
    limit 分页返回的结果集数量，最大为100，不填默认返回100条
    '''
    def get_history_candlesticks(self, instId):
        return self.marketDataAPI.get_history_candlesticks(instId=instId)

    def handle_tickers(self,tickers_data):
        data = tickers_data["data"]
        for inst in data:
            print(inst)


if __name__ == '__main__':
    md = MarkData()
    re = md.get_tickers()
    md.handle_tickers(re)