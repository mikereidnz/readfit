from readfit import __version__, read_input
from readfit.cli import build_greeting, main


def test_version_is_defined() -> None:
    assert __version__ == "0.1.0"


def test_build_greeting_uses_default_name() -> None:
    assert build_greeting() == "readfit is ready."


def test_read_input_is_exported() -> None:
    assert callable(read_input)


def test_main_prints_placeholder_message(capsys) -> None:
    assert main() == 0
    captured = capsys.readouterr()
    assert captured.out == "readfit is ready.\n"


def test_main_reads_filename_argument(monkeypatch, capsys) -> None:
    read_calls: list[str] = []
    fit_calls: list[tuple[list[float], list[float]]] = []
    plot_calls: list[tuple[list[float], list[float], float, float]] = []
    show_calls: list[str] = []

    def fake_read_input(filename: str):
        read_calls.append(filename)
        return [1.0, 2.0], [3.0, 4.0]

    def fake_fit_straight_line(x_values, y_values):
        fit_calls.append((list(x_values), list(y_values)))
        return 1.5, 0.25

    def fake_plot_data_and_fit(x_values, y_values, slope, intercept):
        plot_calls.append((list(x_values), list(y_values), slope, intercept))
        return object(), object()

    def fake_show():
        show_calls.append("show")

    monkeypatch.setattr("readfit.cli.read_input", fake_read_input)
    monkeypatch.setattr("readfit.cli.fit_straight_line", fake_fit_straight_line)
    monkeypatch.setattr("readfit.cli.plot_data_and_fit", fake_plot_data_and_fit)
    monkeypatch.setattr("readfit.cli.plt.show", fake_show)

    assert main(["sample.txt"]) == 0

    captured = capsys.readouterr()
    assert read_calls == ["sample.txt"]
    assert fit_calls == [([1.0, 2.0], [3.0, 4.0])]
    assert plot_calls == [([1.0, 2.0], [3.0, 4.0], 1.5, 0.25)]
    assert show_calls == ["show"]
    assert captured.out == (
        "readfit is ready.\n"
        "Loaded 2 rows from sample.txt\n"
        "Best-fit line: y = 1.5 x + 0.25\n"
    )
