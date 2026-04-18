from pathlib import Path

import numpy as np

from readfit.input import read_input


def test_read_input_returns_first_two_columns(tmp_path: Path) -> None:
    input_file = tmp_path / "sample.txt"
    input_file.write_text("x y\n1.0 2.0\n3.5 4.5\n", encoding="utf-8")

    x_values, y_values = read_input(input_file)

    np.testing.assert_allclose(x_values, np.array([1.0, 3.5]))
    np.testing.assert_allclose(y_values, np.array([2.0, 4.5]))


def test_read_input_skips_header_row(tmp_path: Path) -> None:
    input_file = tmp_path / "with_header.txt"
    input_file.write_text("time value\n10 20\n30 40\n", encoding="utf-8")

    x_values, y_values = read_input(input_file)

    np.testing.assert_array_equal(x_values, np.array([10.0, 30.0]))
    np.testing.assert_array_equal(y_values, np.array([20.0, 40.0]))
