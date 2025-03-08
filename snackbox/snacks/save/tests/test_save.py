from snackbox.snacks.save.save import snack_save
from snackbox.snacks.save.tests.fakes import FakeGitCommitter, FakeTestRunner


class TestSave:
    def test_when_tests_pass_commit(self) -> None:
        tests_pass_test_runner = FakeTestRunner(passes=True)
        git_committer = FakeGitCommitter()

        snack_save(test_runner=tests_pass_test_runner, git_committer=git_committer)

        assert git_committer.committed

    def test_when_tests_fail_dont_commit(self) -> None:
        tests_pass_test_runner = FakeTestRunner(passes=False)
        git_committer = FakeGitCommitter()

        snack_save(test_runner=tests_pass_test_runner, git_committer=git_committer)

        assert not git_committer.committed
