#Exceptions for processing HTTP request.

class StockPriceProcessingException(Exception):
    pass


class PagenationException(StockPriceProcessingException):
    pass
