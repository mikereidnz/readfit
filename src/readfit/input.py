"""Input handling for readfit."""

import numpy as np

def read_input(filename):
    """Read input from a file."""
    data = np.loadtxt(filename, skiprows=1)
    return data[:, 0], data[:, 1]
