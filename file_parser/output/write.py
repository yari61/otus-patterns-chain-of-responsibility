from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import PurePath


class ABCWrite(ABC):
    def __call__(self, content: str) -> None:
        pass


class FileAppend(ABCWrite):
    __slots__ = ["_path"]

    def __init__(self, path: PurePath) -> None:
        self._path = path

    def __call__(self, content: str) -> None:
        with open(self._path, mode="a") as output_stream:
            output_stream.write(content)
