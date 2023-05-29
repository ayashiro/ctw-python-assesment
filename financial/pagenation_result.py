from dataclasses import dataclass, field
from typing import List, Optional

from financial.model import StockPriceModel


@dataclass
class Pagenation:
    count: int
    page: int
    limit: int
    pages: int


@dataclass
class PagenationInfo:
    error: str = ""


@dataclass
class PagenationResult:
    data: List[StockPriceModel] = field(default_factory=list)
    pagenation: Optional[Pagenation] = None
    info: PagenationInfo = PagenationInfo()
