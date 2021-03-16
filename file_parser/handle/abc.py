from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import PurePath


class ABCFileHandler(ABC):
    @abstractmethod
    def __call__(self, path: PurePath) -> None:
        pass
