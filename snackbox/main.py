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
    git_wrapper = GitWrapper(repo_path=Path(project_path))
    snack_start(git_wrapper=git_wrapper, destination_path=Path(project_path))


@app.command()
def autofix() -> None:
    print("autofix")
    print("ruff check --fix --fix-only --watch")
    print('find . -name "*.py" | entr -d ruff format /_')
    print("pytest-watch -- --testmon")
    print("pytest-watch")
    print("pytest-testmon")


@app.command()
def kitty_shortcuts() -> None:
    print("New window - cmd + ENTER")
    print("Close window - ctrl+shift+w")
    print()
    print("Change layout - ctrl + shft + l")
    print()
    print("Next window - ctrl+shift+]")
    print("Previous window - ctrl+shift+[")


if __name__ == "__main__":
    app()
