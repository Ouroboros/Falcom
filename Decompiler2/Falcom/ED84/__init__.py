def _init():
    import Common

    if Common.log.name:
        return

    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED84'

    if not Common.GlobalConfig.ChrTable:
        from .Metadata.chrId_table import chrIdTable
        from .Metadata.chrId_table_en import chrIdTable as chrIdTable_en
        Common.GlobalConfig.ChrTable.update(chrIdTable_en)
        Common.GlobalConfig.ChrTable.update(chrIdTable)

_init()

from .InstructionTable import *
from .Parser import *
