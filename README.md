# readfit

Python project scaffold using a `src/` package layout and `pytest` for tests.

## Project layout

```text
readfit/
├── pyproject.toml
├── README.md
├── src/
│   └── readfit/
│       ├── __init__.py
│       ├── __main__.py
│       └── cli.py
└── tests/
    ├── conftest.py
    └── test_cli.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m pytest
python -m readfit
```

## Notes

- Put application code in `src/readfit/`.
- Add tests under `tests/`.
- The package currently includes a tiny CLI placeholder you can replace as the project takes shape.
- After the first setup, reactivate the environment with `source .venv/bin/activate`.
