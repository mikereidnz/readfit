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
