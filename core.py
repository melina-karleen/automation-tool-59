import asyncio
from decimal import Decimal
from typing import Dict, List, Tuple


class Order:
    __slots__ = ("symbol", "price", "amount", "side")

    def __init__(self, symbol: str, price: Decimal, amount: Decimal, side: str):
        self.symbol = symbol
        self.price = price
        self.amount = amount
        self.side = side


class OptimizedOrderEngine:
    def __init__(self, batch_size: int = 100):
        self.batch_size = batch_size
        self._queue: asyncio.Queue[Order] = asyncio.Queue()
        self._metrics: Dict[str, Decimal] = {}

    async def enqueue_order(
        self, symbol: str, price: str, amount: str, side: str
    ) -> None:
        order = Order(symbol, Decimal(price), Decimal(amount), side)
        await self._queue.put(order)

    async def process_batches(self) -> List[Tuple[str, Decimal, Decimal]]:
        batch: List[Order] = []
        results: List[Tuple[str, Decimal, Decimal]] = []

        while not self._queue.empty() and len(batch) < self.batch_size:
            batch.append(self._queue.get_nowait())

        if not batch:
            return results

        summary: Dict[str, Decimal] = {}
        for order in batch:
            volume = order.price * order.amount
            summary[order.symbol] = summary.get(order.symbol, Decimal("0")) + volume

        for symbol, total_vol in summary.items():
            self._metrics[symbol] = (
                self._metrics.get(symbol, Decimal("0")) + total_vol
            )
            results.append((symbol, total_vol, self._metrics[symbol]))

        return results

    def get_total_volume(self, symbol: str) -> Decimal:
        return self._metrics.get(symbol, Decimal("0"))
