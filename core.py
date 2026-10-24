import asyncio
from decimal import Decimal
from typing import Dict, List, Tuple


class FastOrderBook:
    __slots__ = ("_bids", "_asks", "_cache")

    def __init__(self) -> None:
        self._bids: Dict[Decimal, Decimal] = {}
        self._asks: Dict[Decimal, Decimal] = {}
        self._cache: Tuple[Decimal, Decimal] | None = None

    def update_depth(
        self, bids: List[Tuple[str, str]], asks: List[Tuple[str, str]]
    ) -> None:
        self._cache = None
        for price, qty in bids:
            p_dec, q_dec = Decimal(price), Decimal(qty)
            if q_dec == Decimal("0"):
                self._bids.pop(p_dec, None)
            else:
                self._bids[p_dec] = q_dec

        for price, qty in asks:
            p_dec, q_dec = Decimal(price), Decimal(qty)
            if q_dec == Decimal("0"):
                self._asks.pop(p_dec, None)
            else:
                self._asks[p_dec] = q_dec

    def get_best_bid_ask(self) -> Tuple[Decimal, Decimal]:
        if self._cache is None:
            best_bid = max(self._bids.keys()) if self._bids else Decimal("0")
            best_ask = min(self._asks.keys()) if self._asks else Decimal("0")
            self._cache = (best_bid, best_ask)
        return self._cache


class MarketProcessor:
    def __init__(self) -> None:
        self.books: Dict[str, FastOrderBook] = {}

    async def process_ticker_batch(self, updates: Dict[str, dict]) -> None:
        tasks = [
            self._apply_update(symbol, data) for symbol, data in updates.items()
        ]
        await asyncio.gather(*tasks)

    async def _apply_update(self, symbol: str, data: dict) -> None:
        if symbol not in self.books:
            self.books[symbol] = FastOrderBook()
        self.books[symbol].update_depth(
            data.get("bids", []), data.get("asks", [])
        )
