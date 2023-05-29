from dataclasses import dataclass
from typing import List,  Dict, Any

from financial.model import StockPriceModel


@dataclass
class AggregatedResult:
    start_date: str
    end_date: str
    symbol: str
    average_daily_open_price: str
    average_daily_close_price: str
    average_daily_volume: str


def aggregation(result: List[StockPriceModel]) -> List[AggregatedResult]:
    max_date = {}
    min_date = {}
    open_price = {}
    close_price = {}
    volume = {}
    count = {}
    def insert(dic:Dict[str, Any], symbol:str,value:Any, func):
        if symbol not in dic:
            dic[symbol] = value
        else:
            dic[symbol] = func([dic[symbol], value])
    symbols = set()
    for stock in result:
        symbols.add(stock.symbol)
        insert(max_date, stock.symbol, stock.date, max)
        insert(min_date, stock.symbol, stock.date, min)
        insert(open_price, stock.symbol, stock.open_price, sum)
        insert(close_price, stock.symbol, stock.close_price, sum)
        insert(volume, stock.symbol, stock.volume, sum)
        insert(count, stock.symbol, 1, sum)
    result = []
    for symbol in symbols:
        result.append(
            AggregatedResult(
                symbol = symbol,
                start_date=min_date[symbol],
                end_date=max_date[symbol],
                average_daily_open_price=open_price[symbol]/count[symbol],
                average_daily_close_price=close_price[symbol]/count[symbol],
                average_daily_volume=volume[symbol]//count[symbol]
            )
        )
    return result

