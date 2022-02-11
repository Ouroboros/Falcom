from ast import Import

from itsdangerous import exc


def _init():
    import Common

    if Common.log.name:
        return

    Common.GlobalConfig.DefaultEncoding = 'UTF8'
    Common.log.setLevel(Common.logging.DEBUG)
    Common.log.name = 'ED84'

    if not Common.GlobalConfig.ChrTable:
        # try:
        #     from .Metadata.chrId_table_en import chrIdTable as chrIdTable_en
        #     Common.GlobalConfig.ChrTable.update(chrIdTable_en)
        # except ModuleNotFoundError:
        #     pass

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
