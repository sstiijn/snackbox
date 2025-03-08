from snackbox.snacks.save.helpers import (
    BaseGitCommmitter,
    BaseTestRunner,
    GitCommitter,
    PytestTestRunner,
)


def snack_save(
    test_runner: BaseTestRunner = PytestTestRunner(),
    git_committer: BaseGitCommmitter = GitCommitter(),
):
    is_success = test_runner.run_tests()
    if is_success:
        git_committer.commit()
