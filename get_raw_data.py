import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from financial.http_client import StockHttpClient, convert_json_to_stock_price_object
from financial.model import Base, StockPrice
from typing import List

if __name__ == "__main__":
    symbols = ["IBM", "GOOG", "AAPL"]
    # The api only accept 5 requests / 5 mins
    engine = create_engine("sqlite:///data.db", echo=True)
    Base.metadata.create_all(engine)
    client = StockHttpClient(api_key="AIHXFDYTFQ6E5NQE")
    stock_data:List[StockPrice] = []
    for symbol in symbols:
        stock_data += convert_json_to_stock_price_object(client.get_recent_daily_data(symbol, outputsize="full"))
    with Session(engine) as session:
        for instance in stock_data:
            session.merge(instance)
            # use merge not add function to upsert the table
        session.commit()
