from __future__ import annotations
from pathlib import Path

from .cli import parser
from .handle import HandleContainer
from .output import OutputContainer
from .logging import logger

if __name__ == "__main__":
    args = parser.parse_args()
    handle_container = HandleContainer()
    output_container = OutputContainer()
    output_container.config.set("path", args.output)
    write = output_container.write()
    handle_container.config.set("write", write)
    handle_container.config.set("logger", logger)
    routing_handler = handle_container.routing_handler()

    with open(args.input, mode="r") as input_stream:
        for line in input_stream.readlines():
            path = Path(line.strip())
            routing_handler(path=path)
