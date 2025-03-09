from snackbox.snacks.helpers import (
    BaseGitWrapper,
    BaseTestRunner,
    GitWrapper,
    PytestTestRunner,
)


def snack_save(
    test_runner: BaseTestRunner = PytestTestRunner(),
    git_committer: BaseGitWrapper = GitWrapper(),
):
    is_success = test_runner.run_tests()
    if is_success:
        git_committer.commit()
