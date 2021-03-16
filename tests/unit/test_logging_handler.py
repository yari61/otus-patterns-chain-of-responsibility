from __future__ import annotations
from unittest import main, TestCase
from unittest.mock import Mock
from typing import AnyStr
from logging import Logger
from pathlib import PurePath

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from file_parser.handle.logging import LoggingHandler
from file_parser.handle.abc import ABCFileHandler


class Container(DeclarativeContainer):
    logger = Factory(Mock, Logger)
    next_handler = Factory(Mock, ABCFileHandler)
    name = Factory(Mock, AnyStr)
    handler = Factory(LoggingHandler, logger=logger, next_handler=next_handler, name=name)


class Call(TestCase):
    def test_logger_called_with_correct_message(self):
        container = Container()
        logger = container.logger()
        name = container.name()
        handler = container.handler(logger=logger, name=name)
        path = Mock(PurePath)

        handler(path=path)

        logger.info.assert_called_once_with(f"{name} handler received file {path}")

    def test_next_handler_called_with_correct_path(self):
        container = Container()
        next_handler = container.next_handler()
        handler = container.handler(next_handler=next_handler)
        path = Mock(PurePath)

        handler(path=path)

        next_handler.assert_called_once_with(path=path)

if __name__ == "__main__":
    main()
