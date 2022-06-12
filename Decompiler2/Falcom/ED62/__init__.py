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

_init()

from .InstructionTable import *
from .Parser import *
