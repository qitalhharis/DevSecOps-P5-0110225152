import tempfile
import unittest
from pathlib import Path

from app.calculator import calculate_total
from app.planner import summarize
from app.storage import load_items, save_items
from app.validation import validate_item

class PlannerTests(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculate_total([{"cost": 10}, {"cost": 5.5}]), 15.5)

    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):
            calculate_total([{"cost": -1}])

    def test_invalid_item(self):
        self.assertFalse(validate_item({"name": "", "cost": 3}))

    def test_summarize(self):
        result = summarize([{"name": "Book", "cost": 20000}])
        self.assertEqual(result["count"], 1)
        self.assertEqual(result["total"], 20000.0)

    def test_json_storage(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "items.json"
            save_items([{"name": "Book", "cost": 20000}], path)
            self.assertEqual(load_items(path), [{"name": "Book", "cost": 20000}])

if __name__ == "__main__":
    unittest.main()
