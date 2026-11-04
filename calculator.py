"""Pure, independently testable charging-cost calculation.

Educational assumptions: fixed 7.5 kW charger, USD 0.15/kWh.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

CHARGER_POWER_KW = Decimal("7.5")
PRICE_PER_KWH_USD = Decimal("0.15")
MAX_DURATION_HOURS = Decimal("24")


def calculate_charging_cost(hours):
    """Return an estimated USD Decimal rounded to cents.

    Raises ValueError for empty, nonnumeric, non-finite, negative,
    out-of-range, or excessively long inputs.
    """
    raw = str(hours).strip() if hours is not None else ""
    if not raw or len(raw) > 32:
        raise ValueError("Enter a valid number of hours.")
    try:
        duration = Decimal(raw)
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Enter a valid number of hours.") from None
    if not duration.is_finite() or not Decimal("0") <= duration <= MAX_DURATION_HOURS:
        raise ValueError("Charging hours must be between 0 and 24.")
    return (duration * CHARGER_POWER_KW * PRICE_PER_KWH_USD).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
