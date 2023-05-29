class StockPriceProcessingException(Exception):
    pass


class InvalidHttpResponseException(StockPriceProcessingException):
    pass


class AggregationException(StockPriceProcessingException):
    pass


class PagenationException(StockPriceProcessingException):
    pass
