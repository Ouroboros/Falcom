def _init():
    import Common

    if Common.log.name:
        return

    Common.GlobalConfig.DefaultEncoding = 'GBK'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED6SC'

    if not Common.GlobalConfig.DirTable:
        try:
            from .Metadata.dirTable import dirTable

            Common.GlobalConfig.DirTable.update(dirTable)
            dirTable = Common.GlobalConfig.DirTable

            for index, name in list(dirTable.items()):
                datIndex = int(index, 16)
                name = '.'.join([f.strip() for f in name.rsplit('.', maxsplit = 1)])
                name = f'ED6_DT{datIndex >> 16:02X}/{name}'
                dirTable[name] = datIndex
                dirTable[index] = name

        except ModuleNotFoundError:
            pass

    if not Common.GlobalConfig.ChrTable:
        try:
            from .Metadata.chrId_table import chrIdTable
            Common.GlobalConfig.ChrTable.update(chrIdTable)
        except ModuleNotFoundError:
            pass

    if not Common.GlobalConfig.ItemTable:
        try:
            from .Metadata.itemId_table import itemIdTable
            Common.GlobalConfig.ItemTable.update(itemIdTable)
        except ModuleNotFoundError:
            pass

    if not Common.GlobalConfig.CraftTable:
        try:
            from .Metadata.craftId_table import craftIdTable
            Common.GlobalConfig.CraftTable.update(craftIdTable)
        except ModuleNotFoundError:
            pass

_init()

from .InstructionTable import *
from .Parser import *
