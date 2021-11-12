from Falcom.ED83.Parser.scena_writer import _gScena as scena

def ExitThread():
    # 0x00
    scena.handleOpCode(0x00)

def OP_00():
    # 0x00
    scena.handleOpCode(0x00)

def Return():
    # 0x01
    scena.handleOpCode(0x01)

def OP_01():
    # 0x01
    scena.handleOpCode(0x01)

def Call(type: int, name: str, type2: int):
    # 0x02
    scena.handleOpCode(0x02, type, name, type2)

def OP_02(type: int, name: str, type2: int):
    # 0x02
    scena.handleOpCode(0x02, type, name, type2)

def Goto(label: str):
    # 0x03
    scena.handleOpCode(0x03, label)

def OP_03(label: str):
    # 0x03
    scena.handleOpCode(0x03, label)

def OP_04(arg1: int, arg2: str):
    # 0x04
    scena.handleOpCode(0x04, arg1, arg2)
