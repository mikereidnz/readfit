"""Input handling for readfit."""

from pathlib import Path

import numpy as np


def read_input(filename):
    """Read input from a file."""
    filename = Path(filename)
    print("Input file is: {}".format(filename))
    if not filename.is_file():
        raise SystemExit(f"Input file not found: {filename}")

    data = np.loadtxt(filename, skiprows=1)
    print("Reading from file: {}".format(filename))
    return data[:, 0], data[:, 1]
