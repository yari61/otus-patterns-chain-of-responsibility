from __future__ import annotations
from typing import AnyStr
from unittest import main, TestCase
from unittest.mock import Mock, MagicMock
from pathlib import PurePath

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from file_parser.handle.abc import ABCFileHandler
from file_parser.handle.route import RoutingHandler, ABCRoutingTable


class Container(DeclarativeContainer):
    routing_table = Factory(Mock, ABCRoutingTable)
    handler = Factory(RoutingHandler, routing_table=routing_table)


class Call(TestCase):
    def test_next_handler_called_with_correct_path(self):
        container = Container()
        routing_table = container.routing_table()
        next_handler = Mock(ABCFileHandler)
        routing_table.get_handler = Mock(return_value=next_handler)
        handler = container.handler(routing_table=routing_table)
        file_extension = ".ext"
        path = Mock(PurePath, suffix=file_extension)

        handler(path=path)

        next_handler.assert_called_once_with(path=path)

    def test_routing_table_called_with_correct_key(self):
        container = Container()
        routing_table = container.routing_table()
        next_handler = Mock(ABCFileHandler)
        routing_table.get_handler = Mock(return_value=next_handler)
        handler = container.handler(routing_table=routing_table)
        file_extension = ".ext"
        path = Mock(PurePath, suffix=file_extension)

        handler(path=path)

        routing_table.get_handler.assert_called_once_with(key=file_extension[1:])

if __name__ == "__main__":
    main()
