from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Hashable
from pathlib import PurePath

from .abc import ABCFileHandler


class ABCRoutingTable(ABC):
    @abstractmethod
    def get_handler(self, key: Hashable) -> ABCFileHandler:
        pass


class SimpleRoutingTable(ABCRoutingTable):
    __slots__ = ["_routing_map"]

    def __init__(self, routing_map: Dict[Hashable, ABCFileHandler]) -> None:
        self._routing_map = routing_map

    def get_handler(self, key: Hashable) -> ABCFileHandler:
        return self._routing_map[key]


class RoutingHandler(ABCFileHandler):
    __slots__ = ["_routing_table"]

    def __init__(self, routing_table: ABCRoutingTable) -> None:
        self._routing_table = routing_table
    
    def __call__(self, path: PurePath) -> None:
        file_extension = path.suffix[1:]
        next_handler = self._routing_table.get_handler(key=file_extension)
        return next_handler(path=path)
