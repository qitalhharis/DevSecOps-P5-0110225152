"""Validation helpers for planner input."""

def validate_item(item):
    if not isinstance(item, dict):
        return False
    if not str(item.get("name", "")).strip():
        return False
    try:
        cost = float(item.get("cost"))
    except (TypeError, ValueError):
        return False
    return cost >= 0
