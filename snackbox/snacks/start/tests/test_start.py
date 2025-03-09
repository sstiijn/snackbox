from snackbox.snacks.save.tests.fakes import FakeGitWrapper


class TestSnackStart:
    def test_snack_start(self) -> None:
        # Arrange
        gitwrapper = FakeGitWrapper()

        # Act
        gitwrapper.init()

        # Assert
        assert gitwrapper.initialised
