def _init():
    import Common
    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED84'

    from .Metadata.chrId_table import chrIdTable

    Common.GlobalConfig.ChrTable.update(chrIdTable)

_init()

from .InstructionTable import *
from .Parser import *
