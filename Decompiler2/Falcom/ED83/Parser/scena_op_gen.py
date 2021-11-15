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
    assert isinstance(type, int)
    assert isinstance(name, str)
    assert isinstance(type2, int)
    scena.handleOpCode(0x02, type, name, type2)

def OP_02(type: int, name: str, type2: int):
    # 0x02
    assert isinstance(type, int)
    assert isinstance(name, str)
    assert isinstance(type2, int)
    scena.handleOpCode(0x02, type, name, type2)

def Jump(label: str):
    # 0x03
    assert isinstance(label, str)
    scena.handleOpCode(0x03, label)

def OP_03(label: str):
    # 0x03
    assert isinstance(label, str)
    scena.handleOpCode(0x03, label)

def OP_04(arg1: int, arg2: str):
    # 0x04
    assert isinstance(arg1, int)
    assert isinstance(arg2, str)
    scena.handleOpCode(0x04, arg1, arg2)

def Switch():
    raise NotImplementedError

def OP_06():
    raise NotImplementedError

def Battle():
    # 0x2B
    scena.handleOpCode(0x2B)

def OP_2B():
    # 0x2B
    scena.handleOpCode(0x2B)
