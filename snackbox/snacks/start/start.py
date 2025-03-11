import os
import shutil
import subprocess
from pathlib import Path

from snackbox.snacks.helpers import BaseGitWrapper


def snack_start(git_wrapper: BaseGitWrapper, destination_path: Path) -> None:
    git_wrapper.init()

    subprocess.run(["uv", "init", f"{str(destination_path)}"], check=True)
    os.remove(destination_path / Path("main.py"))

    ## copy file gitignore
    gitignore_template_path = Path(
        "snackbox/snacks/start/templates/gitignore_template.txt"
    )
    shutil.copy2(gitignore_template_path, destination_path / Path(".gitignore"))

    os.mkdir(destination_path / destination_path.name)

    open(destination_path / destination_path.name / Path("__init__.py"), "w").close()
