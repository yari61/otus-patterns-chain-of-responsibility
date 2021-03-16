from __future__ import annotations
from sys import stdout
from logging import getLogger, INFO, StreamHandler, Formatter

logger = getLogger("file-parser")
logger.setLevel(level=INFO)

handler = StreamHandler(stream=stdout)
formatter = Formatter("%(asctime)s - %(name)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
