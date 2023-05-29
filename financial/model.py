from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from dataclasses import dataclass

# stock price model for saving stock price data on SQL

@dataclass
class StockPriceModel:
    symbol:str
    date:str
    open_price:float
    close_price:float
    volume: int

class Base(DeclarativeBase):
    pass

class StockPrice(Base):
    __tablename__ = 'financial_data'
    symbol: Mapped[str] = mapped_column(primary_key=True)
    # primary key
    date: Mapped[str] = mapped_column(primary_key=True)
    # primary date
    open_price: Mapped[float] = mapped_column()
    close_price:Mapped[float] = mapped_column()
    volume : Mapped[int] = mapped_column()

    def convert_data_model(self) -> StockPriceModel:
        return StockPriceModel(
            symbol=self.symbol,
            date = self.date,
            open_price=self.open_price,
            close_price=self.close_price,
            volume=self.volume
        )



