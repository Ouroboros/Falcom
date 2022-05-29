from Falcom import ED62
from Falcom.ED6.Parser.scena_writer import *
from Falcom.ED6.Parser.scena_writer import _gScena, _ScenaWriter

def createScenaWriter(scriptName: str) -> _ScenaWriter:
    _gScena.init(instructionTable = ED62.ScenaOpTable, scenaName = scriptName)
    return _gScena
