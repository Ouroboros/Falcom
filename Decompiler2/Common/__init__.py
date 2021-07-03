from ml import *
from typing import List, Callable, Dict, Any, Tuple, TYPE_CHECKING
from enum import IntEnum, IntFlag

DefaultEncoding = 'GBK'
DefaultIndent   = '    '

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
