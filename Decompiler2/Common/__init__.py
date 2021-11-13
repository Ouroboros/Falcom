from ml import *
from typing import List, Callable, Dict, Any, Tuple, TYPE_CHECKING
from enum import IntEnum, IntFlag
import logging

class _Config:
    def __init__(self) -> None:
        self.DefaultEncoding = 'GBK'
        self.DefaultEndian   = 'little'
        self.DefaultIndent   = '    '

        self.load()

    def load(self):
        pass

GlobalConfig = _Config()

log = logging.Logger('ED', level = logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] %(message)s', datefmt = '%y-%m-%d %H:%M:%S'))

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
