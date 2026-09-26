from decimal import Decimal
from typing import Any, Dict, List, Optional


class OrderProcessor:
    """Processes and validates raw crypto exchange order data."""

    def __init__(self, min_volume: Decimal = Decimal("0.001")) -> None:
        """Initialize processor with volume threshold."""
        self.min_volume = min_volume

    def normalize_ticker(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract and normalize price and volume from raw ticker payload."""
        symbol = str(raw_data.get("symbol", "")).upper()
        price = Decimal(str(raw_data.get("price", "0")))
        volume = Decimal(str(raw_data.get("volume", "0")))
        return {
            "symbol": symbol,
            "price": price,
            "volume": volume,
        }

    def filter_orders(self, orders: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Filter out orders below minimum volume threshold."""
        valid_orders: List[Dict[str, Any]] = []
        for order in orders:
            normalized = self.normalize_ticker(order)
            if normalized["volume"] >= self.min_volume:
                valid_orders.append(normalized)
        return valid_orders

    def calculate_vwap(self, orders: List[Dict[str, Any]]) -> Optional[Decimal]:
        """Calculate Volume-Weighted Average Price for processed orders."""
        if not orders:
            return None

        total_volume = Decimal("0")
        weighted_price_sum = Decimal("0")

        for order in orders:
            price = Decimal(str(order["price"]))
            volume = Decimal(str(order["volume"]))
            total_volume += volume
            weighted_price_sum += price * volume

        if total_volume == Decimal("0"):
            return Decimal("0")

        return (weighted_price_sum / total_volume).quantize(Decimal("0.00000001"))
