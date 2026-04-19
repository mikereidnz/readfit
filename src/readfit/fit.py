"""Core fitting logic for readfit."""

from __future__ import annotations

import numpy as np


def fit_straight_line(x_values, y_values) -> tuple[float, float]:
    """Fit y = m x + c and return ``(m, c)``."""
    x_array = np.asarray(x_values, dtype=float)
    y_array = np.asarray(y_values, dtype=float)

    if x_array.ndim != 1 or y_array.ndim != 1:
        raise ValueError("x_values and y_values must be one-dimensional")
    if x_array.size != y_array.size:
        raise ValueError("x_values and y_values must have the same length")
    if x_array.size < 2:
        raise ValueError("at least two data points are required")
    if np.allclose(x_array, x_array[0]):
        raise ValueError("x_values must not all be identical")

    design_matrix = np.column_stack((x_array, np.ones_like(x_array)))
    slope, intercept = np.linalg.lstsq(design_matrix, y_array, rcond=None)[0]
    return float(slope), float(intercept)
