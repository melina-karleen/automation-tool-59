import asyncio
from typing import Dict, List, Tuple, Callable, Awaitable


class MarketDataEngine:
    __slots__ = ("_bids", "_asks", "_batch_queue", "_batch_size")

    def __init__(self, batch_size: int = 100):
        self._bids: Dict[float, float] = {}
        self._asks: Dict[float, float] = {}
        self._batch_queue: asyncio.Queue = asyncio.Queue()
        self._batch_size = batch_size

    def process_updates(self, updates: List[Tuple[str, float, float]]) -> None:
        for side, price, size in updates:
            target = self._bids if side == "bid" else self._asks
            if size == 0.0:
                target.pop(price, None)
            else:
                target[price] = size

    def get_snapshot(self, depth: int = 10) -> Dict[str, List[Tuple[float, float]]]:
        top_bids = sorted(self._bids.items(), key=lambda x: x[0], reverse=True)[:depth]
        top_asks = sorted(self._asks.items(), key=lambda x: x[0])[:depth]
        return {"bids": top_bids, "asks": top_asks}

    async def flush_batch(self, consumer: Callable[[List[Dict]], Awaitable[None]]) -> None:
        batch = []
        while not self._batch_queue.empty() and len(batch) < self._batch_size:
            batch.append(self._batch_queue.get_nowait())
        if batch:
            await consumer(batch)
