CREATE TABLE StockData
(
    symbol      TEXT NOT NULL,
    date        TEXT NOT NULL,
    open_price  NUMERIC,
    close_price NUMERIC,
    volume      INTEGER,
    PRIMARY KEY (symbol, date)
)
;