import logging
from abc import ABC, abstractmethod
from pathlib import Path

import pytest
from git import Repo


class BaseTestRunner(ABC):

    @abstractmethod
    def run_tests():
        raise NotImplementedError()


class PytestTestRunner(BaseTestRunner):

    def __init__(self, tests_dir: Path = Path(".")):
        self.__tests_dir = tests_dir

    def run_tests(self) -> bool:
        result = pytest.main([str(self.__tests_dir), "--verbose"])
        return result == 0


class BaseGitCommmitter(ABC):
    @abstractmethod
    def commit(self):
        raise NotImplementedError()


class GitCommitter(BaseGitCommmitter):

    def __init__(self, repo_path: Path = Path(".")):
        self.__repo = Repo(repo_path, search_parent_directories=True)

    def commit(self) -> None:
        self.__repo.git.add(all=True)

        if self.__repo.is_dirty():
            logging.info("Committing changes")
            self.__repo.index.commit("Auto commit")
        else:
            logging.info("No changes to commit")
