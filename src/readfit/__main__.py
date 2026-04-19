"""Module entry point for `python -m readfit`."""

from sys import argv

from readfit.cli import main


if __name__ == "__main__":
    raise SystemExit(main(argv[1:]))
