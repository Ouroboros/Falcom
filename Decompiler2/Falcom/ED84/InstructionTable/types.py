from Falcom.ED83.InstructionTable.types import *
from .utils import *

ED84OperandType = ED83OperandType

class ED84OperandFormat(ED83OperandFormat):
    sizeTable = {
        **ED83OperandFormat.sizeTable,
    }

class ED84OperandDescriptor(ED83OperandDescriptor):
    formatTable: Dict[str, 'ED84OperandDescriptor'] = {}

    def readValue(self, context: InstructionHandlerContext) -> Any:
        return {
            ED84OperandType.ScriptId        : lambda context: context.disasmContext.fs.ReadByte(),

        }.get(self.format.type, super().readValue)(context)

    def writeValue(self, context: InstructionHandlerContext, value: Any):
        return {
            ED84OperandType.ScriptId    : lambda context, value: context.disasmContext.fs.WriteByte(value),

        }.get(self.format.type, super().writeValue)(context, value)

    def formatValue(self, context: FormatOperandHandlerContext) -> str:
        return {
            ED84OperandType.ScriptId    : lambda context: f'ScriptId.{ScriptId(context.operand.value)}',

        }.get(self.format.type, super().formatValue)(context)

def oprdesc(*args, **kwargs) -> ED84OperandDescriptor:
    return ED84OperandDescriptor(ED84OperandFormat(*args, **kwargs))

ED83OperandDescriptor.formatTable.update({
    's': oprdesc(ED84OperandType.ScriptId),
})

ED84OperandDescriptor.formatTable.update({
    **ED83OperandDescriptor.formatTable,
})

class ScriptId(IntEnum2):
    Map                 = 0x00
    System              = 0x0A
    Current             = 0x0B
    BtlSys              = 0x0C
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
