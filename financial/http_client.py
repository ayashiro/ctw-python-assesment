import requests
import urllib.parse
from typing import Dict, Any, List

from financial.model import StockPrice


class StockHttpClient(object):
    API_HOST = "https://www.alphavantage.co/query?"
    API_FUNCTION = "TIME_SERIES_DAILY_ADJUSTED"

    def __init__(self, api_key: str = "demo", ):
        self.api_key: str = api_key

    def get_recent_daily_data(self, sym: str = ""
                              , outputsize: str = "compact") -> Dict[str, Any]:
        params: Dict[str, str] = {"function": self.API_FUNCTION, "symbol": sym, "apikey": self.api_key,
                                  "outputsize": outputsize}
        url = self.API_HOST + urllib.parse.urlencode(params)
        json = requests.get(url).json()
        return json


def convert_json_to_stock_price_object(json: Dict[str, Any]) -> List[StockPrice]:
    ans = []
    historical_data: Dict[str, Any] = json["Time Series (Daily)"]
    symbol = json["Meta Data"]["2. Symbol"]
    for date in sorted(historical_data.keys(), reverse=True):
        stock_price = historical_data[date]
        symbol = symbol
        date = date
        open_price = stock_price["1. open"]
        close_price = stock_price["4. close"]
        volume = stock_price["6. volume"]
        ans.append(
            StockPrice(
                date=date,
                symbol=symbol,
                open_price=float(open_price),
                close_price=float(close_price),
                volume=float(volume)
            )
        )
    return ans
