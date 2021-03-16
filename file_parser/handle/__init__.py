from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .file import BaseFileHandler
from .logging import LoggingHandler
from .route import RoutingHandler, SimpleRoutingTable


class HandleContainer(DeclarativeContainer):
    config = Configuration()
    base_file_handler = Factory(BaseFileHandler, write=config.write)
    txt_handler = Factory(LoggingHandler, logger=config.logger, next_handler=base_file_handler, name="txt")
    csv_handler = Factory(LoggingHandler, logger=config.logger, next_handler=base_file_handler, name="csv")
    json_handler = Factory(LoggingHandler, logger=config.logger, next_handler=base_file_handler, name="json")
    xml_handler = Factory(LoggingHandler, logger=config.logger, next_handler=base_file_handler, name="xml")
    routing_map = Factory(dict, txt=txt_handler, csv=csv_handler, json=json_handler, xml=xml_handler)
    routing_table = Factory(SimpleRoutingTable, routing_map=routing_map)
    routing_handler = Factory(RoutingHandler, routing_table=routing_table)

__all__ = ["HandleContainer"]
