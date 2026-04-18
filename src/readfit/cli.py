"""Command-line entry points for the project."""


def build_greeting(name: str = "readfit") -> str:
    """Return a simple placeholder message for the CLI."""
    return f"{name} is ready."


def main() -> int:
    """Run the default command-line behavior."""
    print(build_greeting())
    return 0
