from Falcom.ED83.InstructionTable.types import *
from .utils         import *

ED84OperandType = ED83OperandType

class ED84OperandFormat(ED83OperandFormat):
    sizeTable = {
        **ED83OperandFormat.sizeTable,
    }

class ED84OperandDescriptor(ED83OperandDescriptor):
    formatTable: Dict[str, 'ED84OperandDescriptor'] = {}

def oprdesc(*args, **kwargs) -> ED84OperandDescriptor:
    return ED84OperandDescriptor(ED84OperandFormat(*args, **kwargs))

ED84OperandDescriptor.formatTable.update({
    **ED83OperandDescriptor.formatTable,
})
