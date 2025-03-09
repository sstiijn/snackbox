import logging
from pathlib import Path

import typer

from snackbox.snacks.helpers import GitWrapper
from snackbox.snacks.save.save import snack_save
from snackbox.snacks.start.start import snack_start

logging.basicConfig(level=logging.INFO)

app = typer.Typer()


@app.command()
def save() -> None:
    snack_save()


@app.command()
def start(project_path: str) -> None:
    gitwrapper = GitWrapper(Path(project_path))
    snack_start(gitwrapper)


if __name__ == "__main__":
    app()
