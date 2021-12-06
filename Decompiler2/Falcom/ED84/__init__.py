def _init():
    import Common
    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED84'

_init()

from .InstructionTable import *
from .Parser import *
