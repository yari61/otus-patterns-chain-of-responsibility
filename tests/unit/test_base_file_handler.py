from __future__ import annotations
from unittest import main, TestCase
from unittest.mock import MagicMock, Mock, patch
from pathlib import PurePath
from io import TextIOBase

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from file_parser.handle.file import BaseFileHandler
from file_parser.output.write import ABCWrite


class Container(DeclarativeContainer):
    write = Factory(Mock, ABCWrite)
    handler = Factory(BaseFileHandler, write=write)


class Call(TestCase):
    def test_correct_file_opened(self):
        container = Container()
        handler = container.handler()
        path = Mock(PurePath)

        with patch("file_parser.handle.file.open") as open_function:
            handler(path=path)

            open_function.assert_called_once_with(path, mode="r")

    def test_correct_content_written(self):
        container = Container()
        write = container.write()
        handler = container.handler(write=write)
        path = Mock(PurePath)

        with patch("file_parser.handle.file.open") as open_function:
            content = Mock()
            stream = MagicMock(TextIOBase, read=Mock(return_value=content))
            stream.__enter__ = Mock(return_value=stream)
            open_function.return_value = stream
            handler(path=path)

            write.assert_called_once_with(content=content)

if __name__ == "__main__":
    main()
