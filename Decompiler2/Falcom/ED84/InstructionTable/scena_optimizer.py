from Falcom.Common  import *
from Assembler      import *

__all__ = (
    'ED84Optimizer',
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
        0x29,
        ('MenuCreate',                          {0: 0x00}),
        ('MenuAddItem',                         {0: 0x01}),
        ('MenuSetPos',                          {0: 0x02}),
        ('MenuShow',                            {0: 0x04}),
    ),
    opt(
        0x2F,
        ('AnimeClipAddSymbol',                  {0: 0x00}),
        ('AnimeClipRemoveSymbol',               {0: 0x01, 2: ''}),
        ('AnimeClipAddAsset',                   {0: 0x04, 3: ''}),
        ('AnimeClipRemoveAsset',                {0: 0x05, 3: ''}),
        ('AnimeClipLoadByCatalog',              {0: 0x06}),
        ('AnimeClipReleaseByCatalog',           {0: 0x07}),
        ('AnimeClipLoadMultiple',               {0: 0x08}),
        ('AnimeClipChangeSkin',                 {0: 0x0A, 3: ''}),
    ),
    opt(
        0x30,
        ('AttachEquip',                         {0: 0x00}),
        ('DeatchEquip',                         {0: 0x01, 2: ''}),
    ),
    opt(
        0x31,
        ('LoadAsset',                           {0: 0x00}),
        ('ReleaseAsset',                        {0: 0x01}),
        ('IsAssetLoaded',                       {0: 0x02}),
        ('LoadAssetAsync',                      {0: 0x03}),
    ),
    opt(
        0x32,
        ('LoadEffect',                          {0: 0x0A}),
        ('ReleaseEffect',                       {0: 0x0B}),
        ('PlayEffect',                          {0: 0x0C}),
        ('StopEffect',                          {0: 0x0D}),
        ('WaitEffect',                          {0: 0x10}),
        ('EffectSetRGBA',                       {0: 0x14}),
    ),
    opt(
        0x33,
        ('BattleDamage',                        {0: 0x00}),
        ('BattleDamageAnime',                   {0: 0x01}),
        ('BattleTargetsIterReset',              {0: 0x02}),
        ('BattleTargetsIterNext',               {0: 0x03}),
        ('BattleTargetsIterInit',               {0: 0x04}),
        ('BattleInitHit',                       {0: 0x09}),
        ('BattleSetChrFlags',                   {0: 0x0B}),
        ('BattleClearChrFlags',                 {0: 0x0C}),
        ('BattleGetChrFlags',                   {0: 0x0D}),
        ('BattleKillTarget',                    {0: 0x14}),
        ('BattleSetChrAfterImageOn',            {0: 0x15}),
        ('BattleSetChrAfterImageOff',           {0: 0x16}),
        ('BattleCreateChrDummy',                {0: 0x17}),
        ('BattleDeleteChrDummy',                {0: 0x18}),
        ('BattleSetFlags',                      {0: 0x19}),
        ('BattleClearFlags',                    {0: 0x1A}),
        ('BattleCreateTempChar',                {0: 0x1E}),
        ('BattleDeleteTempChar',                {0: 0x1F}),
        ('BattleCreateChrAfterImage',           {0: 0x31}),
        ('BattleSetChrPos',                     {0: 0x37}),
        ('BattleMoveToTarget',                  {0: 0x38}),
        ('BattleSaveChrPosition',               {0: 0x3A}),
        ('BattleSetChrPosAsync',                {0: 0x3E}),
        ('BattleTurnChrDirection',              {0: 0x41}),
        ('BattleShowText',                      {0: 0x64}),
        ('BattleSetChrAbnormalCondition',       {0: 0xB7, 1: 0x00}),
        ('BattleClearChrAbnormalCondition',     {0: 0xB7, 1: 0x01, 4: 0, 5: 0, 6: 0}),
        ('BattleSetChrAbnormalCondition2',      {0: 0xB7, 1: 0x02}),
        ('BattleClearChrAbnormalCondition2',    {0: 0xB7, 1: 0x03, 4: 0, 5: 0, 6: 0}),
        ('BattleGetChrAbnormalCondition',       {0: 0xB7, 1: 0x04, 3: 0, 4: 0, 5: 0, 6: 0}),
        ('BattleGetChrAbnormalCondition2',      {0: 0xB7, 1: 0x05, 3: 0, 4: 0, 5: 0, 6: 0}),
    ),
    opt(
        0x35,
        ('ChrSetPhysicsFlags',                  {0: 0x00}),
        ('ChrClearPhysicsFlags',                {0: 0x01}),
    ),
    opt(
        0x36,
        ('CameraSetPos',                        {0: 0x02}),
        ('CameraRotate',                        {0: 0x04}),
        ('CameraSetDistance',                   {0: 0x05}),
        ('CameraRotateByTarget',                {0: 0x13}),
        ('CameraSetPosByTarget',                {0: 0x14}),
        ('CameraSetHeight',                     {0: 0x16}),
    ),
    opt(
        0x3A,
        ('PlayBGM',                             {0: 0x00}),
        ('StopBGM',                             {0: 0x01}),
        ('ReplaceBGMReset',                     {0: 0x05, 1: 1, 2: 1}),
        ('ReplaceBGM',                          {0: 0x05}),
        ('SetMapBGM',                           {0: 0x06}),
    ),
    opt(
        0x49,
        ('FormationAddMember',                  {0: 0x00}),
        ('FormationReset',                      {0: 0x02}),
        ('FormationSetLeader',                  {0: 0x04}),
    ),
    opt(
        0x54,
        ('ModelSetBattleStyle',                 {0: 0x4A}),
        ('ModelGetBattleStyle',                 {0: 0x4B}),
        ('ModelSetChrId',                       {0: 0x53}),
    ),
    opt(
        0x7A,
        ('IsMapEqualTo',                        {0: 0x00}),
        ('IsBattleModelEqualTo',                {0: 0x01}),
        ('IsAnimeClipEqualTo',                  {0: 0x02}),
    ),
)

class ED84Optimizer(Optimizer):
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
