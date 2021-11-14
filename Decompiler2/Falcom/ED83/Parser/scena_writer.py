from Falcom.Common import *
from Falcom import ED83
from Falcom.ED83.Parser.scena_types import *

class _ScenaWriter:
    def __init__(self, instructionTable: ED83.ED83InstructionTable, scenaName: str) -> None:
        self.functions          = []                    # type: List[ED83.ScenaFunction]
        self.instructionTable   = instructionTable      # type: ED83.ED83InstructionTable
        self.scenaName          = scenaName
        self.fs                 = fileio.FileStream().OpenMemory()

    def functionDecorator(self, name: str, type: ED83.ScenaFunctionType) -> Callable[[], None]:
        def wrapper(f: Callable[[], Any]):
            func = ED83.ScenaFunction(-1, -1, name)
            func.type = type
            func.obj = f
            self.functions.append(func)

            return lambda: None

        return wrapper

    # decorators

    def Function(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.Function)

    def BattleSetting(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.BattleSetting)

    def AnimeClips(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.AnimeClips)

    def ActionTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.ActionTable)

    def WeaponAttTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.WeaponAttTable)

    def BreakTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.BreakTable)

    def AlgoTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.AlgoTable)

    def SummonTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.SummonTable)

    def AddCollision(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.AddCollision)

    def PartTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.PartTable)

    def ReactionTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.ReactionTable)

    def AnimeClipTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.AnimeClipTable)

    def FieldMonsterData(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.FieldMonsterData)

    def FieldFollowData(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.FieldFollowData)

    def ShinigPomBtlset(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.ShinigPomBtlset)

    def FaceAuto(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.FaceAuto)

    def run(self, g):
        hdr = ScenaHeader()
        bss = bytearray()
        for f in self.functions:
            if f.type == ScenaFunctionType.BattleSetting:
                r: ScenaBattleSetting = f.obj()
                # bss.extend(r.serialize())
                # bss.extend(b'\x01\x00\x00\x00')
                # TODO: discard: 01 00 00 00

            elif f.type == ScenaFunctionType.AnimeClips:
                r: ScenaAnimeClips = f.obj()
                bss.extend(r.serialize())
                # bss.extend(b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
                # TODO: discard: 01 00 00 00 and align to 0x10

            elif f.type == ScenaFunctionType.AnimeClipTable:
                r: ScenaAnimeClipTable = f.obj()
                bss.extend(r.serialize())
                # TODO: discard: 00 00 01 00

        # from hexdump import hexdump
        # hexdump(bss)

        open(r'D:\Dev\Source\Falcom\Decompiler2\Falcom\ED83\a0000.dat', 'wb').write(b'\x00' * 0x4E700 + bss)

    def addLabel(self, name):
        pass

    def handleOpCode(self, opcode: int, *args, **kwargs):
        pass

_gScena: _ScenaWriter = None

def createScenaWriter(scriptName: str) -> _ScenaWriter:
    global _gScena

    scena = _ScenaWriter(instructionTable = ED83.ScenaOpTable, scenaName = scriptName)
    _gScena = scena

    return scena

def label(name: str):
    _gScena.addLabel(name)

