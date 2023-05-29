import csv
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from jproperties import Properties
from financial.http_client import StockHttpClient, convert_json_to_stock_price_object
from financial.model import Base, StockPrice
from typing import List
import os

if __name__ == "__main__":
    symbols = ["IBM", "GOOG", "AAPL"]
    # only query to 3 stock data
    enviornment =os.environ.get("environment", "local")
    configs = Properties()
    with open(f"properties/config-{enviornment}.properties", "rb") as f:
        configs.load(f)
    engine = create_engine(configs.get('SQL_CONFIG').data, echo=True)
    Base.metadata.create_all(engine)
    client = StockHttpClient(api_key=configs.get('API_KEY').data)
    stock_data:List[StockPrice] = []
    for symbol in symbols:
        stock_data += convert_json_to_stock_price_object(client.get_recent_daily_data(symbol, outputsize="full"))
    with Session(engine) as session:
        for instance in stock_data:
            session.merge(instance)
            # use merge not add function to upsert the table
        session.commit()
