"""Business logic for the Study Budget Planner."""

from app.calculator import calculate_total
from app.validation import validate_item

def summarize(items):
    invalid = [item for item in items if not validate_item(item)]
    if invalid:
        raise ValueError("One or more items are invalid")
    return {
        "count": len(items),
        "total": calculate_total(items),
        "items": items,
    }
