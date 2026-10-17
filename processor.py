from decimal import Decimal
from typing import Any, Dict, List, Optional


class TradeProcessor:
    """Process crypto trade signals and validate execution parameters."""

    def __init__(self, min_notional: Decimal = Decimal("10.0")) -> None:
        self.min_notional = min_notional

    def parse_signal(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract and normalize trade signal parameters from payload."""
        symbol = payload.get("symbol")
        side = str(payload.get("side", "")).upper()
        price_raw = payload.get("price")
        amount_raw = payload.get("amount")

        if not all([symbol, side in ("BUY", "SELL"), price_raw, amount_raw]):
            return None

        try:
            price = Decimal(str(price_raw))
            amount = Decimal(str(amount_raw))
            notional = price * amount
        except (ValueError, TypeError):
            return None

        if notional < self.min_notional:
            return None

        return {
            "symbol": str(symbol).upper(),
            "side": side,
            "price": price,
            "amount": amount,
            "notional": notional,
        }

    def process_batch(
        self, signals: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """Filter and process a batch of raw trade signals."""
        processed: List[Dict[str, Any]] = []
        for raw_signal in signals:
            result = self.parse_signal(raw_signal)
            if result:
                processed.append(result)
        return processed
