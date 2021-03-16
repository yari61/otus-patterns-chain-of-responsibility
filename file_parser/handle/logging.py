from __future__ import annotations
from logging import Logger
from pathlib import PurePath

from .abc import ABCFileHandler


class LoggingHandler(ABCFileHandler):
    __slots__ = ["_logger", "_next_handler", "_name"]

    def __init__(self, logger: Logger, next_handler: ABCFileHandler, name: str) -> None:
        self._logger = logger
        self._next_handler = next_handler
        self._name = name

    def __call__(self, path: PurePath) -> None:
        self._logger.info(f"{self._name} handler received file {path}")
        return self._next_handler(path=path)
