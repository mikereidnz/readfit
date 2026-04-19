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
│       ├── cli.py
│       ├── fit.py
│       ├── input.py
│       └── output.py
└── tests/
    ├── conftest.py
    ├── test_cli.py
    ├── test_fit.py
    ├── test_input.py
    └── test_output.py
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
python -m pytest
```

## Run from the command line

Activate the virtual environment, then run the CLI with an input file:

```bash
cd /home/users/mfr24/dev/samples/readfit
source .venv/bin/activate
python -m readfit sample.txt
```

For a simple example:

```bash
printf 'x y\n0 1\n1 3\n2 5\n' > sample.txt
python -m readfit sample.txt
```

This prints the fitted straight-line parameters and opens a plot of the data and best-fit line.

## Run the tests

```bash
cd /home/users/mfr24/dev/samples/readfit
source .venv/bin/activate
python -m pytest
```

## Notes

- Put application code in `src/readfit/`.
- Add tests under `tests/`.
- After the first setup, reactivate the environment with `source .venv/bin/activate`.
