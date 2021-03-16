from __future__ import annotations
from argparse import ArgumentParser
from pathlib import Path

parser = ArgumentParser("file-parser")
parser.add_argument("-i", "--input", type=Path, required=True)
parser.add_argument("-o", "--output", type=Path, required=True)
