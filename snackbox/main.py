import logging

import typer

from snackbox.snacks.save.save import snack_save

logging.basicConfig(level=logging.INFO)

app = typer.Typer()


@app.command()
def save() -> None:
    snack_save()


@app.command()
def pretty() -> None:
    print("Pretty")


if __name__ == "__main__":
    app()
