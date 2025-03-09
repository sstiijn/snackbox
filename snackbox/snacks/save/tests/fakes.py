from snackbox.snacks.save.save import BaseGitWrapper, BaseTestRunner


class FakeTestRunner(BaseTestRunner):
    def __init__(self, passes: bool):
        self.__passes = passes

    def run_tests(self) -> bool:
        """Fake implementation for unit tests"""
        print("running tests")
        return self.__passes


class FakeGitWrapper(BaseGitWrapper):
    def __init__(self):
        self.committed = False
        self.initialised = False

    def commit(self) -> None:
        """Fake implementation for unit tests"""
        print("Commit")
        self.committed = True

    def init(self) -> None:
        """Fake implementation for unit tests"""
        self.initialised = True
