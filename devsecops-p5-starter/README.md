# Study Budget Planner

A small Python command-line application that validates study-expense items, calculates the total budget, and saves/loads items in JSON format.

## Technology
- Python 3.11
- Python standard library
- `unittest` for unit tests
- Bandit for Static Application Security Testing (SAST)

## Project structure
- `app/calculator.py`: calculates total expenses.
- `app/validation.py`: validates expense items.
- `app/storage.py`: reads and writes JSON data.
- `app/planner.py`: combines validation and summary logic.
- `app/cli.py`: command-line entry point.
- `tests/test_planner.py`: unit tests.

## Run locally
```bash
python -m app.cli
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Run SAST locally
```bash
python -m pip install bandit
bandit -r app -ll -ii
```

## CI/CD pipeline overview
The GitHub Actions workflow at `.github/workflows/devsecops.yml` runs on pushes to `main` and pull requests targeting `main`. The `build` job compiles the Python source and runs unit tests. The `sast-scan` job runs only after `build` succeeds (`needs: build`) and uses Bandit to scan Python code. Bandit's `-ll -ii` options make the job fail when findings meet at least medium severity and medium confidence, serving as a basic Quality Gate. Review findings before suppressing them; document justified false positives.
