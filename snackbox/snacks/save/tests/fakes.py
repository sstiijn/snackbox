from snackbox.snacks.save.save import BaseGitCommmitter, BaseTestRunner


class FakeTestRunner(BaseTestRunner):
    def __init__(self, passes: bool):
        self.__passes = passes

    def run_tests(self) -> bool:
        """Fake implementation for unit tests"""
        print("running tests")
        return self.__passes


class FakeGitCommitter(BaseGitCommmitter):
    def __init__(self):
        self.committed = False

    def commit(self) -> None:
        """Fake implementation for unit tests"""
        print("Commit")
        self.committed = True
