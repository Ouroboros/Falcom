from Falcom.ED84.InstructionTable.types import *
from .utils import *

ED85OperandType = ED84OperandType

class ED85OperandFormat(ED84OperandFormat):
    sizeTable = {
        **ED84OperandFormat.sizeTable,
    }

class ED85OperandDescriptor(ED84OperandDescriptor):
    formatTable: Dict[str, 'ED85OperandDescriptor'] = {}

def oprdesc(*args, **kwargs) -> ED85OperandDescriptor:
    return ED85OperandDescriptor(ED85OperandFormat(*args, **kwargs))

ED85OperandDescriptor.formatTable.update({
    **ED84OperandDescriptor.formatTable,
})

class ScriptId(IntEnum2):
    Map                 = 0x00
    System              = 0x0A
    Current             = 0x0B
    BtlSys              = 0x0C
    InfSys              = 0x0E
    Common              = 0x0F
    CurrentCharacter    = 0x10
    BtlMagic            = 0x11
    BtlWin              = 0x12
    BtlCom              = 0x13
    Debug               = 0x14
    Sound               = 0x15
    TalkCommon          = 0x16
    System2             = 0x17
    System3             = 0x18
    System4             = 0x19
    BtlItem             = 0x1A
    Sound2              = 0x1B
    BtlScript           = 0x1C

def _patch():
    from Falcom.ED83.InstructionTable import types
    types.ScriptId = ScriptId

_patch()
