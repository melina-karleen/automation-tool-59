import asyncio
from typing import Dict, List, Tuple


class OrderBookOptimizer:
    def __init__(self, max_depth: int = 100) -> None:
        self.max_depth = max_depth
        self._bids: Dict[float, float] = {}
        self._asks: Dict[float, float] = {}
        self._top_bids_cache: List[Tuple[float, float]] = []
        self._top_asks_cache: List[Tuple[float, float]] = []
        self._dirty: bool = True

    def update_depth(self, bids: List[List[float]], asks: List[List[float]]) -> None:
        for price, qty in bids:
            if qty == 0:
                self._bids.pop(price, None)
            else:
                self._bids[price] = qty

        for price, qty in asks:
            if qty == 0:
                self._asks.pop(price, None)
            else:
                self._asks[price] = qty

        self._dirty = True

    def get_snapshot(self) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        if self._dirty:
            sorted_bids = sorted(self._bids.items(), key=lambda x: x[0], reverse=True)
            sorted_asks = sorted(self._asks.items(), key=lambda x: x[0])
            self._top_bids_cache = sorted_bids[: self.max_depth]
            self._top_asks_cache = sorted_asks[: self.max_depth]
            self._dirty = False

        return self._top_bids_cache, self._top_asks_cache

    def calculate_vwap(self, depth: int = 10) -> Tuple[float, float]:
        bids, asks = self.get_snapshot()

        bid_vol = sum(q for _, q in bids[:depth])
        bid_vwap = sum(p * q for p, q in bids[:depth]) / bid_vol if bid_vol else 0.0

        ask_vol = sum(q for _, q in asks[:depth])
        ask_vwap = sum(p * q for p, q in asks[:depth]) / ask_vol if ask_vol else 0.0

        return bid_vwap, ask_vwap


async def batch_process_ticks(ticks: List[Dict[str, float]], batch_size: int = 500) -> List[float]:
    results = []
    for i in range(0, len(ticks), batch_size):
        batch = ticks[i : i + batch_size]
        vwap = sum(t["price"] * t["volume"] for t in batch) / sum(t["volume"] for t in batch)
        results.append(vwap)
        await asyncio.sleep(0)
    return results
