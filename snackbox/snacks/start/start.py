from snackbox.snacks.helpers import BaseGitWrapper


def snack_start(gitwrapper: BaseGitWrapper) -> None:
    gitwrapper.init()
