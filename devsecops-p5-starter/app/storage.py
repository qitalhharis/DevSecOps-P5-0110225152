"""Small JSON persistence layer."""

import json
from pathlib import Path

def save_items(items, path="budget.json"):
    Path(path).write_text(json.dumps(items, indent=2), encoding="utf-8")

def load_items(path="budget.json"):
    file_path = Path(path)
    if not file_path.exists():
        return []
    return json.loads(file_path.read_text(encoding="utf-8"))
