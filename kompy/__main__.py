from genericpath import exists
from pathlib import Path
from typing import Any

from typer import Argument, Typer

kompy = Typer()


def FileArgument(default: Any) -> Path:
    return Argument(
        default,
        file_okay=True,
        dir_okay=False,
        exists=True,
        resolve_path=True,
    )


@kompy.command()
def add(sound: Path = FileArgument(...)) -> None:
    pass


if __name__ == "__main__":
    kompy()
