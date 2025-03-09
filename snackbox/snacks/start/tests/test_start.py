from snackbox.snacks.save.tests.fakes import FakeGitWrapper


class TestStartSnack:
    def test_snack_start(self) -> None:
        # Arrange
        gitwrapper = FakeGitWrapper()

        # Act
        gitwrapper.init()

        # Assert
        assert gitwrapper.initialised
