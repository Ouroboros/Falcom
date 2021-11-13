from Falcom.Common import *
from Falcom import ED83

class _ScenaWriter:
    def __init__(self, instructionTable: ED83.ED83InstructionTable) -> None:
        self.functions          = []                    # type: List[ED83.ScenaFunction]
        self.instructionTable   = instructionTable      # type: ED83.ED83InstructionTable
        self.fs                 = fileio.FileStream().OpenMemory()

    def functionDecorator(self, name: str, type: ED83.ScenaFunctionType) -> Callable[[], None]:
        def wrapper(f: Callable[[], None]):
            func = ED83.ScenaFunction(-1, 0, name)
            func.type = type
            func.func = f
            self.functions.append(func)

            return lambda: None

        return wrapper

    def run(self, g):
        pass

    def addLabel(self, name):
        pass

    def handleOpCode(self, opcode: int, *args, **kwargs):
        pass

    # decorators

    def Function(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.Function)

    def BattleSetting(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.BattleSetting)

    def Effect(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.Effect)

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

_gScena: _ScenaWriter = None

def createScenaWriter(scriptName: str) -> _ScenaWriter:
    global _gScena

    scena = _ScenaWriter(ED83.ScenaOpTable)
    _gScena = scena

    return scena

def label(name: str):
    _gScena.addLabel(name)
