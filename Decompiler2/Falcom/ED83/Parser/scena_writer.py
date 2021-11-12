from Falcom import ED83
from Falcom.Common import *

class _ScenaWriter:
    def __init__(self, instructionTable: ED83.ED83InstructionTable) -> None:
        self.functions          = []                    # type: List[ED83.ScenaFunction]
        self.instructionTable   = instructionTable      # type: ED83.ED83InstructionTable
        self.fs                 = fileio.FileStream().OpenMemory()

    def functionDecorator(self, name: str, type: ED83.ScenaFunctionType) -> Callable:
        def wrapper(f: Callable[[], None]):
            func = ED83.ScenaFunction(0, name)
            func.type = type
            func.func = f
            self.functions.append(func)

            def nop():
                pass

            return nop

        return wrapper

    def Function(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.Function)

    def AnimeClipTable(self, name: str):
        return self.functionDecorator(name, ED83.ScenaFunctionType.AnimeClipTable)

    def run(self, g):
        pass

    def addLabel(self, name):
        pass

    def opHandler(self, opcode: int, *args, **kwargs):
        pass

_gScena: _ScenaWriter = None

def createScenaWriter(scriptName: str) -> _ScenaWriter:
    global _gScena

    scena = _ScenaWriter(ED83.ScenaOpTable)
    _gScena = scena

    return scena

def label(name: str):
    _gScena.addLabel(name)
