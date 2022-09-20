def _init():
    import Common

    if Common.log.name:
        return

    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED9'

_init()

from .InstructionTable import *
from .Parser import *
