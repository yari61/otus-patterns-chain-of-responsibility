from __future__ import annotations
from pathlib import PurePath

from .abc import ABCFileHandler
from file_parser.output import ABCWrite


class BaseFileHandler(ABCFileHandler):
    __slots__ = ["_write"]

    def __init__(self, write: ABCWrite) -> None:
        self._write = write

    def __call__(self, path: PurePath) -> None:
        with open(path, mode="r") as input_stream:
            content = input_stream.read()
            self._write(content=content)
