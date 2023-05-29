from financial.aggregate import AggregatedResult, aggregation
from financial.database import Database

from typing import Optional

from financial.exceptions import PagenationException
from financial.pagenation_result import PagenationResult, Pagenation, PagenationInfo

# Access database and provide dataclass object for handling http request

class DatabaseProxy(object):
    def __init__(self, engine):
        self.engine = engine
        self.database = Database(engine)

    def select_query(self,
                     symbol: str,
                     limit_number: int,
                     page_number: int,
                     date_from: str,
                     date_to: str) -> PagenationResult:
        try:
            listofResult, pages, count = self.database.select_paging(
                symbol=symbol,
                limit_number=limit_number,
                start_date=date_from,
                end_date=date_to,
                page_number=page_number
            )
            return PagenationResult(
                data=listofResult,
                pagenation=Pagenation(
                    count=count,
                    page=page_number + 1,
                    limit=limit_number,
                    pages=pages + 1,
                )
            )
        except PagenationException as e:
            return PagenationResult(
                info=PagenationInfo(error=str(e))
            )

    def aggregate_query(self,
                        symbol: str,
                        date_from: str,
                        date_to: str) -> Optional[AggregatedResult]:

        ans = aggregation(self.database.select_query(symbol=symbol,
                                                     start_date=date_from,
                                                     end_date=date_to))
        if ans:
            return ans[0]
        else:
            return None
