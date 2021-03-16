from __future__ import annotations
from typing import AnyStr
from unittest import main, TestCase
from unittest.mock import MagicMock, Mock, patch
from pathlib import PurePath
from io import TextIOBase

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from file_parser.output.write import FileAppend


class Container(DeclarativeContainer):
    path = Factory(MagicMock, PurePath)
    write = Factory(FileAppend, path=path)


class Call(TestCase):
    def test_open_called_with_correct_params(self):
        container = Container()
        path = container.path()
        write = container.write(path=path)
        content = MagicMock(AnyStr)

        with patch("file_parser.output.write.open") as open_function:
            write(content=content)

            open_function.assert_called_once_with(path, mode="a")

    def test_correct_content_written(self):
        container = Container()
        write = container.write()
        content = MagicMock(AnyStr)

        with patch("file_parser.output.write.open") as open_function:
            stream = MagicMock(TextIOBase)
            stream.__enter__ = Mock(return_value=stream)
            open_function.return_value = stream
            write(content=content)

            stream.write.assert_called_once_with(content)

if __name__ == "__main__":
    main()
