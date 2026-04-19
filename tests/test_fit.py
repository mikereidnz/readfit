import numpy as np
import pytest

from readfit.fit import fit_straight_line


def test_fit_straight_line_returns_slope_and_intercept() -> None:
    slope, intercept = fit_straight_line([0.0, 1.0, 2.0], [1.0, 3.0, 5.0])

    assert slope == pytest.approx(2.0)
    assert intercept == pytest.approx(1.0)


def test_fit_straight_line_handles_inexact_data() -> None:
    x_values = np.array([0.0, 1.0, 2.0, 3.0])
    y_values = np.array([1.1, 2.9, 5.2, 6.8])

    slope, intercept = fit_straight_line(x_values, y_values)

    assert slope == pytest.approx(1.94, rel=1e-2)
    assert intercept == pytest.approx(1.09, rel=1e-2)


def test_fit_straight_line_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        fit_straight_line([0.0, 1.0], [1.0])
