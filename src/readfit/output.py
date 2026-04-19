"""Output formatting for readfit."""

from __future__ import annotations

import numpy as np
from matplotlib import pyplot as plt


def plot_data_and_fit(x_values, y_values, slope: float, intercept: float, axes=None):
    """Plot the input data and its straight-line fit."""
    x_array = np.asarray(x_values, dtype=float)
    y_array = np.asarray(y_values, dtype=float)

    if x_array.ndim != 1 or y_array.ndim != 1:
        raise ValueError("x_values and y_values must be one-dimensional")
    if x_array.size != y_array.size:
        raise ValueError("x_values and y_values must have the same length")
    if x_array.size == 0:
        raise ValueError("at least one data point is required")

    if axes is None:
        figure, axes = plt.subplots()
    else:
        figure = axes.figure

    axes.scatter(x_array, y_array, label="data")

    x_fit = np.array([x_array.min(), x_array.max()], dtype=float)
    y_fit = slope * x_fit + intercept
    axes.plot(x_fit, y_fit, label="best-fit line")

    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.legend()

    return figure, axes
