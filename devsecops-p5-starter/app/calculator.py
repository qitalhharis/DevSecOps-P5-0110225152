"""Core calculation functions for the Study Budget Planner."""

def calculate_total(items):
    """Return the sum of item costs; reject negative values."""
    total = 0.0
    for item in items:
        cost = float(item.get("cost", 0))
        if cost < 0:
            raise ValueError("Cost cannot be negative")
        total += cost
    return round(total, 2)
