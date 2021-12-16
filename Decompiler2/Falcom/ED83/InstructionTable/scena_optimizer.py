from Falcom.Common  import *
from Assembler      import *

__all__ = (
    'ED83Optimizer',
)

class OptimizePattern:
    def __init__(self, index: int, value: Any):
        self.index = index
        self.value = value

    def __str__(self) -> str:
        return f'  [{self.index}] = {self.value}'

    __repr__ = __str__

class OptimizeMatcher:
    def __init__(self, mnemonic: str, *patterns: OptimizePattern):
        self.mnemonic = mnemonic
        self.patterns = patterns

    def match(self, inst: Instruction, operands: List[Any]) -> bool:
        oprCount = len(inst.operands)
        if oprCount < len(self.patterns):
            return False

        for p in self.patterns:
            if p.index >= oprCount:
                return False

            if p.value != inst.operands[p.index].value:
                return False

        return True

    def __str__(self) -> str:
        return '\n'.join([
            f'{self.mnemonic}',
            *[f'  {p}' for p in self.patterns],
        ])

    __repr__ = __str__

class OptimizeData:
    def __init__(self, opcode: int, *matchers: OptimizeMatcher):
        self.opcode = opcode
        self.matchers = matchers

    def __str__(self) -> str:
        return '\n'.join([
            f'0x{self.opcode:02X}',
            *[f'  {m}' for m in self.matchers],
            '',
        ])

    __repr__ = __str__

def buildTable(*opt: OptimizeData):
    return dict([(o.opcode, o) for o in opt])

def opt(opcode: int, *patterns: Tuple[str, Tuple]) -> OptimizeData:
    return OptimizeData(opcode, *[OptimizeMatcher(p[0], *[OptimizePattern(index, value) for index, value in p[1].items()]) for p in patterns])

optimizeTable = buildTable(
    opt(
        0x30,
        ('AttachEquip', {0: 0x00}),
        ('DeatchEquip', {0: 0x01, 2: ''}),
    ),
    opt(
        0x31,
        ('LoadAsset',       {0: 0x00}),
        ('ReleaseAsset',    {0: 0x01}),
        ('IsAssetLoaded',   {0: 0x02}),
        ('LoadAssetAsync',  {0: 0x03}),
    ),
    opt(
        0x32,
        ('LoadEffect',      {0: 0x0A}),
        ('ReleaseEffect',   {0: 0x0B}),
        ('PlayEffect',      {0: 0x0C}),
        ('StopEffect',      {0: 0x0D}),
    ),
    opt(
        0x33,
        ('ChrCreateTempChar',       {0: 0x1E}),
        ('ChrMoveToTarget',         {0: 0x34}),
        ('ChrSetPosByTarget',       {0: 0x33}),
        ('ChrSetPosByTargetAsync',  {0: 0x39}),
        ('ChrTurnDirection',        {0: 0x3C}),
    ),
    opt(
        0x36,
        ('CameraPos',       {0: 0x02, 1: 0x03}),
        ('CameraRotate',    {0: 0x04, 1: 0x03}),
        ('CameraHeight',    {0: 0x05, 1: 0x03}),
    ),
    opt(
        0x49,
        ('FormationAddMember',  {0: 0x00}),
        ('FormationReset',      {0: 0x02}),
        ('FormationSetLeader',  {0: 0x04}),
    ),
    opt(
        0x54,
        ('SetBattleStyle',  {0: 0x4A}),
        ('GetBattleStyle',  {0: 0x4B}),
    ),
    opt(
        0x7A,
        ('IsBattleModelEqualTo',  {0: 0x01}),
    ),
)

class ED83Optimizer(Optimizer):
    def optimize(self, inst: Instruction, operands: List[Any], flags: Flags) -> OptimizeResult:
        opt = optimizeTable.get(inst.opcode)
        if opt is None:
            return None

        for matcher in opt.matchers:
            if not matcher.match(inst, operands):
                continue

            newopr = []
            opr_to_remove = set([p.index for p in matcher.patterns])
            for i, o in enumerate(operands):
                if i in opr_to_remove:
                    continue
                newopr.append(o)

            return OptimizeResult(matcher.mnemonic, newopr, flags)

        return None
