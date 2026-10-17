"""Command-line entry point."""

from app.planner import summarize

SAMPLE_ITEMS = [
    {"name": "Notebook", "cost": 12000},
    {"name": "Pen", "cost": 5000},
    {"name": "Transport", "cost": 10000},
]

def main():
    result = summarize(SAMPLE_ITEMS)
    print("Study Budget Planner")
    print(f"Items: {result['count']}")
    print(f"Estimated total: Rp{result['total']:.2f}")

if __name__ == "__main__":
    main()
