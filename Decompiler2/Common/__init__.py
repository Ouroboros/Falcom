from ml import *
from typing import List, Callable, Dict, Set, Any, Tuple, TYPE_CHECKING
from enum import IntEnum, IntFlag
import logging

class _Config:
    def __init__(self):
        self.DefaultEncoding    = 'GBK'
        self.DefaultEndian      = 'little'
        self.DefaultIndent      = '    '
        self.DirTable           = {}
        self.ChrTable           = {}
        self.ItemTable          = {}
        self.CraftTable         = {}

        self.load()

    @property
    def StructEndian(self):
        fileio.FileStream.BIG_ENDIAN
        return '<' if self.DefaultEndian == 'little' else '>'

    def load(self):
        pass

GlobalConfig = _Config()

log = logging.Logger('', level = logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] %(message)s', datefmt = '%m-%d %H:%M:%S'))

log.addHandler(handler)

class IntEnum2(IntEnum):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

class IntFlag2(IntFlag):
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
