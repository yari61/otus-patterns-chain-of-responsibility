from __future__ import annotations
from typing import Dict, Hashable
from unittest import main, TestCase
from unittest.mock import MagicMock, Mock

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory

from file_parser.handle.route import SimpleRoutingTable
from file_parser.handle.abc import ABCFileHandler


class Container(DeclarativeContainer):
    key = Factory(MagicMock, Hashable)
    handler = Factory(Mock, ABCFileHandler)
    routing_map = Factory(MagicMock, Dict)
    routing_table = Factory(SimpleRoutingTable, routing_map=routing_map)


class GetHandler(TestCase):
    def test_correct_handler_returned(self):
        container = Container()
        key = container.key()
        handler = container.handler()
        routing_map = container.routing_map()
        routing_map.__getitem__ = Mock(return_value=handler)
        routing_table = container.routing_table(routing_map=routing_map)

        self.assertEqual(routing_table.get_handler(key=key), handler)

if __name__ == "__main__":
    main()
