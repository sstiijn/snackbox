import logging
from abc import ABC, abstractmethod
from pathlib import Path

import pytest
from git import Repo


class BaseTestRunner(ABC):
    @abstractmethod
    def run_tests():
        raise NotImplementedError


class PytestTestRunner(BaseTestRunner):
    def __init__(self, tests_dir: Path = Path()):
        self.__tests_dir = tests_dir

    def run_tests(self) -> bool:
        result = pytest.main([str(self.__tests_dir), "--verbose"])
        return result == 0


class BaseGitWrapper(ABC):
    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def init(self):
        raise NotImplementedError


class GitWrapper(BaseGitWrapper):
    def __init__(self, repo_path: Path = Path(".")):
        self.__repo_path = repo_path

    def commit(self) -> None:
        repo = Repo(self.__repo_path, search_parent_directories=True)
        repo.git.add(all=True)

        if repo.is_dirty():
            logging.info("Committing changes")
            repo.index.commit("Auto commit")
        else:
            logging.info("No changes to commit")

    def init(self) -> None:
        Repo.init(self.__repo_path)
        logging.info("Initialized git repo")
