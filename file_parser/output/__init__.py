from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .write import ABCWrite, FileAppend


class OutputContainer(DeclarativeContainer):
    config = Configuration()
    write = Factory(FileAppend, path=config.path)

__all__ = ["ABCWrite", "OutputContainer"]
