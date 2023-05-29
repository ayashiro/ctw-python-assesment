from sqlalchemy import select, create_engine, func
from sqlalchemy.orm import Session

from financial.aggregate import aggregation
from financial.model import StockPrice, StockPriceModel
from typing import List, Tuple


class Database():
    def __init__(self, engine):
        self.engine = engine

    def select_all(self) -> List[StockPriceModel]:
        with Session(self.engine) as session:
            stmt = select(StockPrice)
            return [test.convert_data_model()
                    for test in session.scalars(stmt)]

    def select_query(self, symbol: str, start_date: str, end_date: str) -> List[StockPriceModel]:
        with Session(self.engine) as session:
            stmt = select(StockPrice).where(StockPrice.symbol == symbol) \
                .where(StockPrice.date >= start_date) \
                .where(StockPrice.date <= end_date)
            return [test.convert_data_model()
                    for test in session.scalars(stmt)]

    def select_paging(self, symbol: str,
                      start_date: str,
                      end_date: str,
                      limit_number: int,
                      page_number: int) -> Tuple[List[StockPriceModel], int, int]:
        if limit_number <= 0:
            from financial.exceptions import PagenationException
            raise PagenationException("Invalid limit number!")
        with Session(self.engine) as session:
            t = session.query(func.count(StockPrice.date)) \
                .filter(StockPrice.symbol == symbol) \
                .filter(StockPrice.date >= start_date) \
                .filter(StockPrice.date <= end_date)
            total_count = t.scalar()
            total_page = (total_count - 1) // limit_number
            if page_number >= total_page or page_number < 0:
                return ([], total_page, total_count)
            offset = limit_number * page_number
            tmp = session.query(StockPrice)\
            .filter(StockPrice.symbol == symbol)\
            .filter(StockPrice.date >= start_date)\
            .filter(StockPrice.date <= end_date).order_by(StockPrice.date)\
                .limit(limit_number)\
                .offset(offset)
            return ([v.convert_data_model() for v in tmp.all()], total_page, total_count)



if __name__ == "__main__":
    engine = create_engine("sqlite:///../data.db")
    database = Database(engine)
    t = database.select_all()
    print(database.select_paging("IBM", "1999-09-01", "2023-06-20", 10, 1))
    print(aggregation(t))
