"""Command-line entry points for the project."""

from __future__ import annotations

import argparse

from matplotlib import pyplot as plt

from readfit.fit import fit_straight_line
from readfit.input import read_input
from readfit.output import plot_data_and_fit


def build_greeting(name: str = "readfit") -> str:
    """Return a simple placeholder message for the CLI."""
    return f"{name} is ready."


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(prog="readfit")
    parser.add_argument(
        "filename",
        nargs="?",
        help="Input data file to read.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the default command-line behavior."""
    if argv is None:
        argv = []

    args = build_parser().parse_args(argv)

    print(build_greeting())
    if args.filename is not None:
        x_values, y_values = read_input(args.filename)
        slope, intercept = fit_straight_line(x_values, y_values)
        print(f"Loaded {len(x_values)} rows from {args.filename}")
        print(f"Best-fit line: y = {slope:.6g} x + {intercept:.6g}")
        plot_data_and_fit(x_values, y_values, slope, intercept)
        plt.show()

    return 0
