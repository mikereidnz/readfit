import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pytest

from readfit.output import plot_data_and_fit


def test_plot_data_and_fit_adds_scatter_and_line() -> None:
    figure, axes = plot_data_and_fit([0.0, 1.0, 2.0], [1.0, 3.0, 5.0], 2.0, 1.0)

    assert figure is axes.figure
    assert len(axes.collections) == 1
    assert len(axes.lines) == 1
    np.testing.assert_allclose(axes.lines[0].get_xdata(), np.array([0.0, 2.0]))
    np.testing.assert_allclose(axes.lines[0].get_ydata(), np.array([1.0, 5.0]))

    plt.close(figure)


def test_plot_data_and_fit_uses_existing_axes() -> None:
    figure, axes = plt.subplots()

    returned_figure, returned_axes = plot_data_and_fit(
        [1.0, 2.0],
        [2.0, 4.0],
        2.0,
        0.0,
        axes=axes,
    )

    assert returned_figure is figure
    assert returned_axes is axes

    plt.close(figure)


def test_plot_data_and_fit_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        plot_data_and_fit([0.0, 1.0], [1.0], 2.0, 1.0)
