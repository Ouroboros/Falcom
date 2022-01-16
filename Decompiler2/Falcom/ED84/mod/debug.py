import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED84.Parser.scena_writer_helper import *
try:
    import debug_hook
except ImportError:
    pass

scena = createScenaWriter('debug.dat')

# id: 0x0000 offset: 0x494
@scena.Code('BeginDebugScript')
def BeginDebugScript():
    OP_13(0x00000002)
    OP_13(0x00000004)

    Return()

# id: 0x0001 offset: 0x4A0
@scena.Code('EndDebugScript')
def EndDebugScript():
    OP_14(0x00000002)
    OP_14(0x00000004)

    Return()

# id: 0x0002 offset: 0x4AC
@scena.Code('SelectArea')
def SelectArea():
    OP_20(0x00, (0xFF, 0x0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.6230000257492065, 0x0), (0xEE, -1.0, 0x0))
    OP_13(0x00000002)

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_4D4(): pass

    label('loc_4D4')

    If(
        (
            (Expr.PushVar, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_103E',
    )

    MenuCreate(0, 30, 24.0, 99)
    MenuAddItem(0, 'a0000～：テストマップ', 0x00000064)
    MenuAddItem(0, '現在マップ再読込み', 0x00000062)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 't0000～：リーヴス', 0x00000000)
    MenuAddItem(0, 't0200～：トールズ第Ⅱ分校・アインヘル小要塞', 0x000186A0)
    MenuAddItem(0, 't1000～：セントアーク', 0x00000002)
    MenuAddItem(0, 't2000～：パルム・ハーメル廃村', 0x00000003)
    MenuAddItem(0, 't3000～：オルディス', 0x00000004)
    MenuAddItem(0, 't4000～：ラクウェル', 0x00000005)
    MenuAddItem(0, 't5000～：エリン', 0x00000006)
    MenuAddItem(0, 't6000～：ミルサンテ', 0x00000007)
    MenuAddItem(0, 't7000～：アルスター', 0x00000008)
    MenuAddItem(0, 't8000～：レグラム', 0x00000009)
    MenuAddItem(0, 't9000～：ルーレ・バリアハート', 0x0000000A)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'c0000～：クロスベル（駅前 中央 東通り 西通り）', 0x0000000B)
    MenuAddItem(0, 'c0800～：クロスベル（港湾区 オルキスタワー）', 0x0000000C)
    MenuAddItem(0, 'c1200～：クロスベル（歓楽街）', 0x0000000D)
    MenuAddItem(0, 'c2000～：帝都（ヴァンクール大通り）', 0x0000000E)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'f0000～：ドレックノール要塞', 0x00000012)
    MenuAddItem(0, 'f1000～：ジュノー海上要塞', 0x00000013)
    MenuAddItem(0, 'f3000～：聖ウルスラ医科大学', 0x00000015)
    MenuAddItem(0, 'f4000～：ミシュラム', 0x00000016)
    MenuAddItem(0, 'f5000～：タイタス門', 0x00000017)
    MenuAddItem(0, 'f6000～：星辰の間', 0x00000018)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'r0000～：街道 セントアーク・パルム周辺', 0x00000019)
    MenuAddItem(0, 'r2000～：街道 クロスベル周辺', 0x0000001A)
    MenuAddItem(0, 'r3000～：街道 オルディス・ラクウェル周辺', 0x0000001B)
    MenuAddItem(0, 'r4000～：街道 リーヴス・ミルサンテ周辺・エイボン丘陵', 0x0000001C)
    MenuAddItem(0, 'r7000～：街道 アルスター周辺・オスギリアス盆地', 0x0000001D)
    MenuAddItem(0, 'r9000～：街道 ノルド北部・アイゼンガルド連峰', 0x0000001E)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'm0000～：ダンジョン アインヘル小要塞', 0x0000001F)
    MenuAddItem(0, 'm0600～：ダンジョン イストミア大森林', 0x00000020)
    MenuAddItem(0, 'm1000～：ダンジョン ジオフロント', 0x00000021)
    MenuAddItem(0, 'm1400～：ダンジョン 星見の塔', 0x00000023)
    MenuAddItem(0, 'm2000～：ダンジョン 神霊窟', 0x00000024)
    MenuAddItem(0, 'm4000～：ダンジョン 黒キ星杯', 0x00000028)
    MenuAddItem(0, 'm5000～：ダンジョン オルキスタワー魔導区画', 0x00000029)
    MenuAddItem(0, 'm5500～：ダンジョン サングラール迷宮', 0x0000002A)
    MenuAddItem(0, 'm6000～：ダンジョン 黒の工房', 0x0000002B)
    MenuAddItem(0, 'm6500～：ダンジョン オルディス地下水路', 0x0000002C)
    MenuAddItem(0, 'm7000～：ダンジョン ドレックノール要塞・内部', 0x0000002D)
    MenuAddItem(0, 'm7400～：ダンジョン パンタグリュエル・内部', 0x0000002E)
    MenuAddItem(0, 'm7600～：ダンジョン ガルガンチュア・内部', 0x00000030)
    MenuAddItem(0, 'm8000～：ダンジョン 忘却の白き杭', 0x00000031)
    MenuAddItem(0, 'm9000～：ダンジョン トゥアハ＝デ＝ダナーン', 0x00000032)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'e0000～：スカイマップ', 0x00000033)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'v0000～：乗り物内部', 0x00000035)
    MenuAddItem(0, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(0, 'bxxxx～：戦闘マップ', 0x00000061)
    MenuAddItem(0, 'title～：システムマップ', 0x00000063)
    MenuSetPos(0, 0x01, 24, 24, 0x01)
    MenuShow(0, 0xF6)

    If(
        (
            (Expr.PushVar, 0xF6),
            (Expr.PushLong, 0x2),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1030',
    )

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushVar, 0xF6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SelectMap')

    Jump('loc_1039')

    def _loc_1030(): pass

    label('loc_1030')

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1039(): pass

    label('loc_1039')

    Jump('loc_4D4')

    def _loc_103E(): pass

    label('loc_103E')

    MenuCmd(0x03, 0)
    OP_14(0x00000002)
    OP_21(0x00)

    Return()

# id: 0x0003 offset: 0x104C
@scena.Code('SelectMap')
def SelectMap():
    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1055(): pass

    label('loc_1055')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DB2C',
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000063, 'loc_123A'),
        (0x00000062, 'loc_12F7'),
        (0x00000060, 'loc_1308'),
        (0x00000061, 'loc_1316'),
        (0x00000064, 'loc_15CF'),
        (0x00000000, 'loc_39F1'),
        (0x000186A0, 'loc_3D84'),
        (0x00000002, 'loc_4376'),
        (0x00000003, 'loc_47C9'),
        (0x00000004, 'loc_4A8F'),
        (0x00000005, 'loc_5192'),
        (0x00000006, 'loc_5457'),
        (0x00000007, 'loc_561D'),
        (0x00000008, 'loc_57A2'),
        (0x00000009, 'loc_59A5'),
        (0x0000000A, 'loc_5A25'),
        (0x0000000B, 'loc_5B63'),
        (0x0000000C, 'loc_6203'),
        (0x0000000D, 'loc_66B2'),
        (0x0000000E, 'loc_689E'),
        (0x0000000F, 'loc_6E0E'),
        (0x00000010, 'loc_758A'),
        (0x00000012, 'loc_7B60'),
        (0x00000013, 'loc_7D1A'),
        (0x00000014, 'loc_7F26'),
        (0x00000015, 'loc_7FAE'),
        (0x00000016, 'loc_80DE'),
        (0x00000017, 'loc_8592'),
        (0x00000018, 'loc_8654'),
        (0x00000019, 'loc_86D4'),
        (0x0000001A, 'loc_8AC6'),
        (0x0000001B, 'loc_8ECE'),
        (0x0000001C, 'loc_93FF'),
        (0x0000001D, 'loc_96B5'),
        (0x0000001E, 'loc_9827'),
        (0x0000001F, 'loc_98F0'),
        (0x00000020, 'loc_9C9F'),
        (0x00000021, 'loc_9DB1'),
        (0x00000022, 'loc_A057'),
        (0x00000023, 'loc_A13D'),
        (0x00000024, 'loc_A3C4'),
        (0x00000025, 'loc_A7EB'),
        (0x00000026, 'loc_ABD8'),
        (0x00000027, 'loc_ACC2'),
        (0x00000028, 'loc_AED3'),
        (0x00000029, 'loc_B100'),
        (0x0000002A, 'loc_B4E0'),
        (0x0000002B, 'loc_B882'),
        (0x0000002C, 'loc_BABB'),
        (0x0000002D, 'loc_BB93'),
        (0x0000002E, 'loc_BCF0'),
        (0x00000030, 'loc_BEC9'),
        (0x00000031, 'loc_C041'),
        (0x00000032, 'loc_C48C'),
        (0x00000033, 'loc_CCF1'),
        (0x00000035, 'loc_D12B'),
        (-1, 'loc_122C'),
    )

    def _loc_122C(): pass

    label('loc_122C')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DB27')

    def _loc_123A(): pass

    label('loc_123A')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'title：タイトル背景用（仮）', 0x00000000)
    MenuAddItem(1, 'プレストーリー用ダミー', 0x00000001)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_12C4'),
        (0x00000001, 'loc_12D4'),
        (-1, 'loc_12E4'),
    )

    def _loc_12C4(): pass

    label('loc_12C4')

    MapJump((0xDD, 'title'), (0xDD, ''), 0x00)

    Jump('loc_12F2')

    def _loc_12D4(): pass

    label('loc_12D4')

    MapJump((0xDD, 'e3500'), (0xDD, ''), 0x00)

    Jump('loc_12F2')

    def _loc_12E4(): pass

    label('loc_12E4')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_12F2')

    def _loc_12F2(): pass

    label('loc_12F2')

    Jump('loc_DB27')

    def _loc_12F7(): pass

    label('loc_12F7')

    MapJump((0xDD, 'reload'), (0xDD, ''), 0x00)

    Jump('loc_DB27')

    def _loc_1308(): pass

    label('loc_1308')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DB27')

    def _loc_1316(): pass

    label('loc_1316')

    MenuCreate(1, 20, 24.0, 99)
    MenuAddItem(1, 'ba0000：大きさサンプル', 0x00000000)
    MenuAddItem(1, 'bt0000：戦闘マップ', 0x00000001)
    MenuAddItem(1, 'be0000：試練の箱・戦闘マップ', 0x00000002)
    MenuAddItem(1, 'be1000：奥義伝承・戦闘マップ', 0x00000003)
    MenuAddItem(1, 'm7010b：ドレックノール要塞・内部', 0x00000004)
    MenuAddItem(1, 'm2010b：陽霊窟祭壇', 0x00000005)
    MenuAddItem(1, 't3510b：公爵家城館・エントランス', 0x00000006)
    MenuAddItem(1, 't0280b：トールズ第Ⅱ分校・倉庫', 0x00000007)
    MenuAddItem(1, 'r2420b：東クロスベル街道③', 0x00000008)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_1515'),
        (0x00000001, 'loc_1526'),
        (0x00000002, 'loc_1537'),
        (0x00000003, 'loc_1548'),
        (0x00000004, 'loc_1559'),
        (0x00000005, 'loc_156A'),
        (0x00000006, 'loc_157B'),
        (0x00000007, 'loc_158C'),
        (0x00000008, 'loc_159D'),
        (0x00000060, 'loc_15AE'),
        (-1, 'loc_15BC'),
    )

    def _loc_1515(): pass

    label('loc_1515')

    MapJump((0xDD, 'ba0000'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_1526(): pass

    label('loc_1526')

    MapJump((0xDD, 'bt0000'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_1537(): pass

    label('loc_1537')

    MapJump((0xDD, 'be0000'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_1548(): pass

    label('loc_1548')

    MapJump((0xDD, 'be1000'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_1559(): pass

    label('loc_1559')

    MapJump((0xDD, 'm7010b'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_156A(): pass

    label('loc_156A')

    MapJump((0xDD, 'm2010b'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_157B(): pass

    label('loc_157B')

    MapJump((0xDD, 't3510b'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_158C(): pass

    label('loc_158C')

    MapJump((0xDD, 't0280b'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_159D(): pass

    label('loc_159D')

    MapJump((0xDD, 'r2420b'), (0xDD, ''), 0x00)

    Jump('loc_15CA')

    def _loc_15AE(): pass

    label('loc_15AE')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_15CA')

    def _loc_15BC(): pass

    label('loc_15BC')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_15CA')

    def _loc_15CA(): pass

    label('loc_15CA')

    Jump('loc_DB27')

    def _loc_15CF(): pass

    label('loc_15CF')

    MenuCreate(1, 20, 24.0, 99)
    MenuAddItem(1, 'a0000：デバッグマップ', 0x00000000)
    MenuAddItem(1, 'a0001：ノードON/OFF部屋', 0x00000001)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a0100：キャラ部屋（プレイヤーキャラ 新旧Ⅶ組）', 0x00000064)
    MenuAddItem(1, 'a0101：キャラ部屋（プレイヤーキャラ 他）', 0x00000065)
    MenuAddItem(1, 'a0103：キャラ部屋（敵キャラ）', 0x00000067)
    MenuAddItem(1, 'a0105：キャラ部屋（サブキャラ）', 0x00000069)
    MenuAddItem(1, 'a0107：キャラ部屋（ネームドNPC男性 c_chr200～）', 0x0000006B)
    MenuAddItem(1, 'a0109：キャラ部屋（ネームドNPC女性 c_chr600～）', 0x0000006D)
    MenuAddItem(1, 'a0111：キャラ部屋（NPC男性1 c_chr250～）', 0x0000006F)
    MenuAddItem(1, 'a0112：キャラ部屋（NPC男性2 c_chr300～）', 0x00000070)
    MenuAddItem(1, 'a0113：キャラ部屋（NPC男性3 c_chr350～）', 0x00000071)
    MenuAddItem(1, 'a0114：キャラ部屋（NPC男性4 c_chr???～）', 0x00000072)
    MenuAddItem(1, 'a0117：キャラ部屋（NPC女性1 c_chr650～）', 0x00000075)
    MenuAddItem(1, 'a0118：キャラ部屋（NPC女性2 c_chr700～）', 0x00000076)
    MenuAddItem(1, 'a0119：キャラ部屋（NPC女性3 c_chr???～）', 0x00000077)
    MenuAddItem(1, 'a0122：キャラ部屋（人外）', 0x0000007A)
    MenuAddItem(1, 'a0130：装備品部屋', 0x00000082)
    MenuAddItem(1, 'a0199：ロボット部屋', 0x000000C7)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a0200：魔獣部屋 (000-019) ザコ1', 0x000000C8)
    MenuAddItem(1, 'a0201：魔獣部屋 (020-039) ザコ2', 0x000000C9)
    MenuAddItem(1, 'a0202：魔獣部屋 (040-059) ザコ3', 0x000000CA)
    MenuAddItem(1, 'a0203：魔獣部屋 (060-079) ザコ4', 0x000000CB)
    MenuAddItem(1, 'a0204：魔獣部屋 (080-099) ザコ5', 0x000000CC)
    MenuAddItem(1, 'a0205：魔獣部屋 (100-119) ザコ6', 0x000000CD)
    MenuAddItem(1, 'a0206：魔獣部屋 (120-139) ザコ7', 0x000000CE)
    MenuAddItem(1, 'a0207：魔獣部屋 (140-159) ザコ8', 0x000000CF)
    MenuAddItem(1, 'a0208：魔獣部屋 (300-304) 手配魔獣1', 0x000000D0)
    MenuAddItem(1, 'a0209：魔獣部屋 (305-309) 手配魔獣2', 0x000000D1)
    MenuAddItem(1, 'a0210：魔獣部屋 (310-349) 手配魔獣3', 0x000000D2)
    MenuAddItem(1, 'a0211：魔獣部屋 (350-399,450-499) 幻獣・ボス', 0x000000D3)
    MenuAddItem(1, 'a0212：魔獣部屋 (400-449) 魔煌兵', 0x000000D4)
    MenuAddItem(1, 'a0213：魔獣部屋 (900-999) 実験', 0x000000D5)
    MenuAddItem(1, 'a0214：ラスボス部屋 (461)', 0x000000D6)
    MenuAddItem(1, 'a0299：街道負荷検証', 0x0000012B)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a0304：マップ部屋（戦闘テスト：エベル街道）', 0x00000130)
    MenuAddItem(1, 'a0306：マップ部屋（戦闘テスト：テスト）', 0x00000132)
    MenuAddItem(1, 'a0308：マップ部屋（戦闘テスト：勝利テスト）', 0x00000134)
    MenuAddItem(1, 'a0320：マップ部屋（ハシゴテスト、マーカー）', 0x00000140)
    MenuAddItem(1, 'a0350：マップ部屋（乗り物①）', 0x0000015E)
    MenuAddItem(1, 'a0351：マップ部屋（乗り物②）', 0x0000015F)
    MenuAddItem(1, 'a0360：マップ部屋（イベントオブジェクト）', 0x00000168)
    MenuAddItem(1, 'a0370：マップ部屋（イス・テーブル）', 0x00000172)
    MenuAddItem(1, 'a0371：マップ部屋（扉）', 0x00000173)
    MenuAddItem(1, 'a0372：マップ部屋（照明）', 0x00000174)
    MenuAddItem(1, 'a0373：マップ部屋（植物）', 0x00000175)
    MenuAddItem(1, 'a0374：マップ部屋（ブレイク）', 0x00000176)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a0414：東地区(一般メッセージテスト)', 0x0000019E)
    MenuAddItem(1, 'a0415：室内(テスト)\x09\x09\x09\x09\x09\x09\x09', 0x0000019F)
    MenuAddItem(1, 'a0417：演習地(一般テスト)\x09\x09\x09\x09\x09\x09', 0x000001A1)
    MenuAddItem(1, 'a0418：ループ撮影用\x09\x09\x09\x09\x09\x09\x09', 0x000001A2)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a0500：マップ室内・箱元データ：教会セット', 0x000001A2)
    MenuAddItem(1, 'a0501：マップ室内・箱元データ：平民セット（庶民系）', 0x000001A3)
    MenuAddItem(1, 'a0502：マップ室内・箱元データ：上流セット（ホテル・デパート・金持ち系）', 0x000001A4)
    MenuAddItem(1, 'a0503：マップ室内・箱元データ：貴族セット（アルゼイド級）', 0x000001A5)
    MenuAddItem(1, 'a0504：マップ室内・箱元データ：城館セット（アルバレア級）', 0x000001A6)
    MenuAddItem(1, 'a0505：マップ室内・箱元データ：超城館セット（バルフレイム級）', 0x000001A7)
    MenuAddItem(1, 'a0506：マップ室内オブジェ：小物：箱・タル・壷系全汎用', 0x000001A8)
    MenuAddItem(1, 'a0507：マップ室内オブジェ：小物：ギルド・機械・工房系', 0x000001A9)
    MenuAddItem(1, 'a0508：マップ室内オブジェ：小物：食品・料理・レジ/机上系小物系', 0x000001AA)
    MenuAddItem(1, 'a0509：マップ室内オブジェ：小物：古董屋・硝子工房・楽器・特殊系', 0x000001AB)
    MenuAddItem(1, 'a0510：マップ室内オブジェ：小物：植物', 0x000001AC)
    MenuAddItem(1, 'a0511：マップ室内オブジェ：小物：インポート・その他', 0x000001AD)
    MenuAddItem(1, 'a0512：マップ室内オブジェ：小物：学院・クロスベル・近代セット', 0x000001AE)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a1000：日置部屋', 0x000003E8)
    MenuAddItem(1, 'a1001：遠藤部屋', 0x000003E9)
    MenuAddItem(1, 'a1002：張部屋', 0x000003EA)
    MenuAddItem(1, 'a1003：前川部屋', 0x000003EB)
    MenuAddItem(1, 'a1004：ロボ戦部屋', 0x000003EC)
    MenuAddItem(1, 'a1005：イベントシステム検証部屋A', 0x000003ED)
    MenuAddItem(1, 'a1006：イベントシステム検証部屋B(重マップ)', 0x000003EE)
    MenuAddItem(1, 'a1008：DAE分割テスト部屋', 0x000003F0)
    MenuAddItem(1, 'a1009：実機負荷検証部屋', 0x000003F1)
    MenuAddItem(1, 'a1010：イベント・一般会話検証部屋', 0x000003F2)
    MenuAddItem(1, 'a1012：宮崎部屋', 0x000003F4)
    MenuAddItem(1, 'a1013：サウンド部屋', 0x000003F5)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'a2000：山田部屋', 0x000007D0)
    MenuAddItem(1, 'a2001：高居部屋', 0x000007D1)
    MenuAddItem(1, 'a2002：一場部屋', 0x000007D2)
    MenuAddItem(1, 'a2003：松川部屋', 0x000007D3)
    MenuAddItem(1, 'a2004：澤村部屋', 0x000007D4)
    MenuAddItem(1, 'a2005：吉田部屋', 0x000007D5)
    MenuAddItem(1, 'a2006：岡田部屋', 0x000007D6)
    MenuAddItem(1, 'a2007：田中部屋', 0x000007D7)
    MenuAddItem(1, 'a2008：矢吹部屋', 0x000007D8)
    MenuAddItem(1, 'a2009：井上（俊）部屋', 0x000007D9)
    MenuAddItem(1, 'a2010：李部屋', 0x000007DA)
    MenuAddItem(1, 'a2011：村上部屋', 0x000007DB)
    MenuAddItem(1, 'a2012：井上（裕）部屋', 0x000007DC)
    MenuAddItem(1, 'a2013：伊藤部屋', 0x000007DD)
    MenuAddItem(1, 'a2014：田中（真）部屋', 0x000007DE)
    MenuAddItem(1, 'a2015：平田部屋', 0x000007DF)
    MenuAddItem(1, 'a2016：松村部屋', 0x000007E0)
    MenuAddItem(1, 'a2017：森下部屋', 0x000007E1)
    MenuAddItem(1, 'a2018：山根部屋', 0x000007E2)
    MenuAddItem(1, 'a2070：外注１部屋', 0x00000816)
    MenuAddItem(1, 'a2080：阿部部屋', 0x00000820)
    MenuAddItem(1, 'a2081：伊藤（さ）部屋', 0x00000821)
    MenuAddItem(1, 'a2082：蝦名部屋', 0x00000822)
    MenuAddItem(1, 'a2090：C&R部屋', 0x0000082A)
    MenuAddItem(1, 'a2091：李モーション部屋', 0x0000082B)
    MenuAddItem(1, 'a2092：村上モーション部屋', 0x0000082C)
    MenuAddItem(1, 'a2093：星出モーション部屋', 0x0000082D)
    MenuAddItem(1, 'a2094：田中（真）モーション部屋', 0x0000082E)
    MenuAddItem(1, 'a2100：DWE Room', 0x00000834)
    MenuAddItem(1, 'a2101：DWE MotionRoom1', 0x00000835)
    MenuAddItem(1, 'a2102：DWE MotionRoom2', 0x00000836)
    MenuAddItem(1, 'a2103：DWE MotionRoom3', 0x00000837)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'am1010：ローエングリン城①', 0x00002B02)
    MenuAddItem(1, 'am1020：ローエングリン城②', 0x00002B0C)
    MenuAddItem(1, 'am1030：ローエングリン城③', 0x00002B16)
    MenuAddItem(1, 'am1040：ローエングリン城④', 0x00002B20)
    MenuAddItem(1, 'am1060：ローエングリン城⑥', 0x00002B34)
    MenuAddItem(1, 'am1070：ローエングリン城⑦', 0x00002B3E)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_3139'),
        (0x00000001, 'loc_3149'),
        (0x00000064, 'loc_3159'),
        (0x00000065, 'loc_3169'),
        (0x00000067, 'loc_3179'),
        (0x00000069, 'loc_3189'),
        (0x0000006B, 'loc_3199'),
        (0x0000006D, 'loc_31A9'),
        (0x0000006F, 'loc_31B9'),
        (0x00000070, 'loc_31C9'),
        (0x00000071, 'loc_31D9'),
        (0x00000072, 'loc_31E9'),
        (0x00000075, 'loc_31F9'),
        (0x00000076, 'loc_3209'),
        (0x00000077, 'loc_3219'),
        (0x0000007A, 'loc_3229'),
        (0x00000082, 'loc_3239'),
        (0x000000C7, 'loc_3249'),
        (0x000000C8, 'loc_3259'),
        (0x000000C9, 'loc_3269'),
        (0x000000CA, 'loc_3279'),
        (0x000000CB, 'loc_3289'),
        (0x000000CC, 'loc_3299'),
        (0x000000CD, 'loc_32A9'),
        (0x000000CE, 'loc_32B9'),
        (0x000000CF, 'loc_32C9'),
        (0x000000D0, 'loc_32D9'),
        (0x000000D1, 'loc_32E9'),
        (0x000000D2, 'loc_32F9'),
        (0x000000D3, 'loc_3309'),
        (0x000000D4, 'loc_3319'),
        (0x000000D5, 'loc_3329'),
        (0x000000D6, 'loc_3339'),
        (0x0000012B, 'loc_3349'),
        (0x0000012C, 'loc_3359'),
        (0x0000012D, 'loc_3369'),
        (0x0000012E, 'loc_3379'),
        (0x0000012F, 'loc_3389'),
        (0x00000130, 'loc_3399'),
        (0x00000131, 'loc_33A9'),
        (0x00000132, 'loc_33B9'),
        (0x00000133, 'loc_33C9'),
        (0x00000134, 'loc_33D9'),
        (0x00000140, 'loc_33E9'),
        (0x00000141, 'loc_33F9'),
        (0x0000015E, 'loc_3409'),
        (0x0000015F, 'loc_3419'),
        (0x00000168, 'loc_3429'),
        (0x00000172, 'loc_3439'),
        (0x00000173, 'loc_3449'),
        (0x00000174, 'loc_3459'),
        (0x00000175, 'loc_3469'),
        (0x00000176, 'loc_3479'),
        (0x00000190, 'loc_3489'),
        (0x00000191, 'loc_3499'),
        (0x00000192, 'loc_34A9'),
        (0x00000193, 'loc_34B9'),
        (0x00000194, 'loc_34C9'),
        (0x00000195, 'loc_34D9'),
        (0x00000196, 'loc_34E9'),
        (0x00000FDD, 'loc_34F9'),
        (0x00000197, 'loc_350A'),
        (0x00000198, 'loc_351A'),
        (0x00000199, 'loc_352A'),
        (0x0000019A, 'loc_353A'),
        (0x0000019B, 'loc_354A'),
        (0x0000019C, 'loc_355A'),
        (0x0000019D, 'loc_356A'),
        (0x0000019E, 'loc_357A'),
        (0x0000019F, 'loc_358A'),
        (0x000001A0, 'loc_359A'),
        (0x000001A1, 'loc_35AA'),
        (0x000001A2, 'loc_35BA'),
        (0x000001A2, 'loc_35CA'),
        (0x000001A3, 'loc_35DA'),
        (0x000001A4, 'loc_35EA'),
        (0x000001A5, 'loc_35FA'),
        (0x000001A6, 'loc_360A'),
        (0x000001A7, 'loc_361A'),
        (0x000001A8, 'loc_362A'),
        (0x000001A9, 'loc_363A'),
        (0x000001AA, 'loc_364A'),
        (0x000001AB, 'loc_365A'),
        (0x000001AC, 'loc_366A'),
        (0x000001AD, 'loc_367A'),
        (0x000001AE, 'loc_368A'),
        (0x000003E8, 'loc_369A'),
        (0x000003E9, 'loc_36AA'),
        (0x000003EA, 'loc_36BA'),
        (0x000003EB, 'loc_36CA'),
        (0x000003EC, 'loc_36DA'),
        (0x000003ED, 'loc_36EA'),
        (0x000003EE, 'loc_36FA'),
        (0x000003F0, 'loc_370A'),
        (0x000003F1, 'loc_371A'),
        (0x000003F2, 'loc_372A'),
        (0x000003F4, 'loc_373A'),
        (0x000003F5, 'loc_374A'),
        (0x000007D0, 'loc_375A'),
        (0x000007D1, 'loc_376A'),
        (0x000007D2, 'loc_377A'),
        (0x000007D3, 'loc_378A'),
        (0x000007D4, 'loc_379A'),
        (0x000007D5, 'loc_37AA'),
        (0x000007D6, 'loc_37BA'),
        (0x000007D7, 'loc_37CA'),
        (0x000007D8, 'loc_37DA'),
        (0x000007D9, 'loc_37EA'),
        (0x000007DA, 'loc_37FA'),
        (0x000007DB, 'loc_380A'),
        (0x000007DC, 'loc_381A'),
        (0x000007DD, 'loc_382A'),
        (0x000007DE, 'loc_383A'),
        (0x000007DF, 'loc_384A'),
        (0x000007E0, 'loc_385A'),
        (0x000007E1, 'loc_386A'),
        (0x000007E2, 'loc_387A'),
        (0x00000816, 'loc_388A'),
        (0x00000820, 'loc_389A'),
        (0x00000821, 'loc_38AA'),
        (0x00000822, 'loc_38BA'),
        (0x0000082A, 'loc_38CA'),
        (0x0000082B, 'loc_38DA'),
        (0x0000082C, 'loc_38EA'),
        (0x0000082D, 'loc_38FA'),
        (0x0000082E, 'loc_390A'),
        (0x00000834, 'loc_391A'),
        (0x00000835, 'loc_392A'),
        (0x00000836, 'loc_393A'),
        (0x00000837, 'loc_394A'),
        (0x0000083E, 'loc_395A'),
        (0x00002B02, 'loc_396A'),
        (0x00002B0C, 'loc_397B'),
        (0x00002B16, 'loc_398C'),
        (0x00002B20, 'loc_399D'),
        (0x00002B34, 'loc_39AE'),
        (0x00002B3E, 'loc_39BF'),
        (0x00000060, 'loc_39D0'),
        (-1, 'loc_39DE'),
    )

    def _loc_3139(): pass

    label('loc_3139')

    MapJump((0xDD, 'a0000'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3149(): pass

    label('loc_3149')

    MapJump((0xDD, 'a0001'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3159(): pass

    label('loc_3159')

    MapJump((0xDD, 'a0100'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3169(): pass

    label('loc_3169')

    MapJump((0xDD, 'a0101'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3179(): pass

    label('loc_3179')

    MapJump((0xDD, 'a0103'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3189(): pass

    label('loc_3189')

    MapJump((0xDD, 'a0105'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3199(): pass

    label('loc_3199')

    MapJump((0xDD, 'a0107'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31A9(): pass

    label('loc_31A9')

    MapJump((0xDD, 'a0109'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31B9(): pass

    label('loc_31B9')

    MapJump((0xDD, 'a0111'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31C9(): pass

    label('loc_31C9')

    MapJump((0xDD, 'a0112'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31D9(): pass

    label('loc_31D9')

    MapJump((0xDD, 'a0113'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31E9(): pass

    label('loc_31E9')

    MapJump((0xDD, 'a0114'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_31F9(): pass

    label('loc_31F9')

    MapJump((0xDD, 'a0117'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3209(): pass

    label('loc_3209')

    MapJump((0xDD, 'a0118'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3219(): pass

    label('loc_3219')

    MapJump((0xDD, 'a0119'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3229(): pass

    label('loc_3229')

    MapJump((0xDD, 'a0122'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3239(): pass

    label('loc_3239')

    MapJump((0xDD, 'a0130'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3249(): pass

    label('loc_3249')

    MapJump((0xDD, 'a0199'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3259(): pass

    label('loc_3259')

    MapJump((0xDD, 'a0200'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3269(): pass

    label('loc_3269')

    MapJump((0xDD, 'a0201'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3279(): pass

    label('loc_3279')

    MapJump((0xDD, 'a0202'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3289(): pass

    label('loc_3289')

    MapJump((0xDD, 'a0203'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3299(): pass

    label('loc_3299')

    MapJump((0xDD, 'a0204'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32A9(): pass

    label('loc_32A9')

    MapJump((0xDD, 'a0205'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32B9(): pass

    label('loc_32B9')

    MapJump((0xDD, 'a0206'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32C9(): pass

    label('loc_32C9')

    MapJump((0xDD, 'a0207'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32D9(): pass

    label('loc_32D9')

    MapJump((0xDD, 'a0208'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32E9(): pass

    label('loc_32E9')

    MapJump((0xDD, 'a0209'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_32F9(): pass

    label('loc_32F9')

    MapJump((0xDD, 'a0210'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3309(): pass

    label('loc_3309')

    MapJump((0xDD, 'a0211'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3319(): pass

    label('loc_3319')

    MapJump((0xDD, 'a0212'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3329(): pass

    label('loc_3329')

    MapJump((0xDD, 'a0213'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3339(): pass

    label('loc_3339')

    MapJump((0xDD, 'a0214'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3349(): pass

    label('loc_3349')

    MapJump((0xDD, 'a0299'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3359(): pass

    label('loc_3359')

    MapJump((0xDD, 'a0300'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3369(): pass

    label('loc_3369')

    MapJump((0xDD, 'a0301'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3379(): pass

    label('loc_3379')

    MapJump((0xDD, 'a0302'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3389(): pass

    label('loc_3389')

    MapJump((0xDD, 'a0303'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3399(): pass

    label('loc_3399')

    MapJump((0xDD, 'a0304'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33A9(): pass

    label('loc_33A9')

    MapJump((0xDD, 'a0305'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33B9(): pass

    label('loc_33B9')

    MapJump((0xDD, 'a0306'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33C9(): pass

    label('loc_33C9')

    MapJump((0xDD, 'a0307'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33D9(): pass

    label('loc_33D9')

    MapJump((0xDD, 'a0308'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33E9(): pass

    label('loc_33E9')

    MapJump((0xDD, 'a0320'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_33F9(): pass

    label('loc_33F9')

    MapJump((0xDD, 'a0321'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3409(): pass

    label('loc_3409')

    MapJump((0xDD, 'a0350'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3419(): pass

    label('loc_3419')

    MapJump((0xDD, 'a0351'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3429(): pass

    label('loc_3429')

    MapJump((0xDD, 'a0360'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3439(): pass

    label('loc_3439')

    MapJump((0xDD, 'a0370'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3449(): pass

    label('loc_3449')

    MapJump((0xDD, 'a0371'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3459(): pass

    label('loc_3459')

    MapJump((0xDD, 'a0372'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3469(): pass

    label('loc_3469')

    MapJump((0xDD, 'a0373'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3479(): pass

    label('loc_3479')

    MapJump((0xDD, 'a0374'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3489(): pass

    label('loc_3489')

    MapJump((0xDD, 'a0400'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_3499(): pass

    label('loc_3499')

    MapJump((0xDD, 'a0401'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34A9(): pass

    label('loc_34A9')

    MapJump((0xDD, 'a0402'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34B9(): pass

    label('loc_34B9')

    MapJump((0xDD, 'a0403'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34C9(): pass

    label('loc_34C9')

    MapJump((0xDD, 'a0404'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34D9(): pass

    label('loc_34D9')

    MapJump((0xDD, 'a0405'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34E9(): pass

    label('loc_34E9')

    MapJump((0xDD, 'a0406'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_34F9(): pass

    label('loc_34F9')

    MapJump((0xDD, 'a0406b'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_350A(): pass

    label('loc_350A')

    MapJump((0xDD, 'a0407'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_351A(): pass

    label('loc_351A')

    MapJump((0xDD, 'a0408'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_352A(): pass

    label('loc_352A')

    MapJump((0xDD, 'a0409'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_353A(): pass

    label('loc_353A')

    MapJump((0xDD, 'a0410'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_354A(): pass

    label('loc_354A')

    MapJump((0xDD, 'a0411'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_355A(): pass

    label('loc_355A')

    MapJump((0xDD, 'a0412'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_356A(): pass

    label('loc_356A')

    MapJump((0xDD, 'a0413'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_357A(): pass

    label('loc_357A')

    MapJump((0xDD, 'a0414'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_358A(): pass

    label('loc_358A')

    MapJump((0xDD, 'a0415'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_359A(): pass

    label('loc_359A')

    MapJump((0xDD, 'a0416'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35AA(): pass

    label('loc_35AA')

    MapJump((0xDD, 'a0417'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35BA(): pass

    label('loc_35BA')

    MapJump((0xDD, 'a0418'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35CA(): pass

    label('loc_35CA')

    MapJump((0xDD, 'a0500'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35DA(): pass

    label('loc_35DA')

    MapJump((0xDD, 'a0501'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35EA(): pass

    label('loc_35EA')

    MapJump((0xDD, 'a0502'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_35FA(): pass

    label('loc_35FA')

    MapJump((0xDD, 'a0503'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_360A(): pass

    label('loc_360A')

    MapJump((0xDD, 'a0504'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_361A(): pass

    label('loc_361A')

    MapJump((0xDD, 'a0505'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_362A(): pass

    label('loc_362A')

    MapJump((0xDD, 'a0506'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_363A(): pass

    label('loc_363A')

    MapJump((0xDD, 'a0507'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_364A(): pass

    label('loc_364A')

    MapJump((0xDD, 'a0508'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_365A(): pass

    label('loc_365A')

    MapJump((0xDD, 'a0509'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_366A(): pass

    label('loc_366A')

    MapJump((0xDD, 'a0510'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_367A(): pass

    label('loc_367A')

    MapJump((0xDD, 'a0511'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_368A(): pass

    label('loc_368A')

    MapJump((0xDD, 'a0512'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_369A(): pass

    label('loc_369A')

    MapJump((0xDD, 'a1000'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36AA(): pass

    label('loc_36AA')

    MapJump((0xDD, 'a1001'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36BA(): pass

    label('loc_36BA')

    MapJump((0xDD, 'a1002'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36CA(): pass

    label('loc_36CA')

    MapJump((0xDD, 'a1003'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36DA(): pass

    label('loc_36DA')

    MapJump((0xDD, 'a1004'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36EA(): pass

    label('loc_36EA')

    MapJump((0xDD, 'a1005'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_36FA(): pass

    label('loc_36FA')

    MapJump((0xDD, 'a1006'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_370A(): pass

    label('loc_370A')

    MapJump((0xDD, 'a1008'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_371A(): pass

    label('loc_371A')

    MapJump((0xDD, 'a1009'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_372A(): pass

    label('loc_372A')

    MapJump((0xDD, 'a1010'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_373A(): pass

    label('loc_373A')

    MapJump((0xDD, 'a1012'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_374A(): pass

    label('loc_374A')

    MapJump((0xDD, 'a1013'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_375A(): pass

    label('loc_375A')

    MapJump((0xDD, 'a2000'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_376A(): pass

    label('loc_376A')

    MapJump((0xDD, 'a2001'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_377A(): pass

    label('loc_377A')

    MapJump((0xDD, 'a2002'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_378A(): pass

    label('loc_378A')

    MapJump((0xDD, 'a2003'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_379A(): pass

    label('loc_379A')

    MapJump((0xDD, 'a2004'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37AA(): pass

    label('loc_37AA')

    MapJump((0xDD, 'a2005'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37BA(): pass

    label('loc_37BA')

    MapJump((0xDD, 'a2006'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37CA(): pass

    label('loc_37CA')

    MapJump((0xDD, 'a2007'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37DA(): pass

    label('loc_37DA')

    MapJump((0xDD, 'a2008'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37EA(): pass

    label('loc_37EA')

    MapJump((0xDD, 'a2009'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_37FA(): pass

    label('loc_37FA')

    MapJump((0xDD, 'a2010'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_380A(): pass

    label('loc_380A')

    MapJump((0xDD, 'a2011'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_381A(): pass

    label('loc_381A')

    MapJump((0xDD, 'a2012'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_382A(): pass

    label('loc_382A')

    MapJump((0xDD, 'a2013'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_383A(): pass

    label('loc_383A')

    MapJump((0xDD, 'a2014'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_384A(): pass

    label('loc_384A')

    MapJump((0xDD, 'a2015'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_385A(): pass

    label('loc_385A')

    MapJump((0xDD, 'a2016'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_386A(): pass

    label('loc_386A')

    MapJump((0xDD, 'a2017'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_387A(): pass

    label('loc_387A')

    MapJump((0xDD, 'a2018'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_388A(): pass

    label('loc_388A')

    MapJump((0xDD, 'a2070'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_389A(): pass

    label('loc_389A')

    MapJump((0xDD, 'a2080'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38AA(): pass

    label('loc_38AA')

    MapJump((0xDD, 'a2081'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38BA(): pass

    label('loc_38BA')

    MapJump((0xDD, 'a2082'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38CA(): pass

    label('loc_38CA')

    MapJump((0xDD, 'a2090'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38DA(): pass

    label('loc_38DA')

    MapJump((0xDD, 'a2091'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38EA(): pass

    label('loc_38EA')

    MapJump((0xDD, 'a2092'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_38FA(): pass

    label('loc_38FA')

    MapJump((0xDD, 'a2093'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_390A(): pass

    label('loc_390A')

    MapJump((0xDD, 'a2094'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_391A(): pass

    label('loc_391A')

    MapJump((0xDD, 'a2100'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_392A(): pass

    label('loc_392A')

    MapJump((0xDD, 'a2101'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_393A(): pass

    label('loc_393A')

    MapJump((0xDD, 'a2102'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_394A(): pass

    label('loc_394A')

    MapJump((0xDD, 'a2103'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_395A(): pass

    label('loc_395A')

    MapJump((0xDD, 'a2110'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_396A(): pass

    label('loc_396A')

    MapJump((0xDD, 'am1010'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_397B(): pass

    label('loc_397B')

    MapJump((0xDD, 'am1020'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_398C(): pass

    label('loc_398C')

    MapJump((0xDD, 'am1030'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_399D(): pass

    label('loc_399D')

    MapJump((0xDD, 'am1040'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_39AE(): pass

    label('loc_39AE')

    MapJump((0xDD, 'am1060'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_39BF(): pass

    label('loc_39BF')

    MapJump((0xDD, 'am1070'), (0xDD, ''), 0x00)

    Jump('loc_39EC')

    def _loc_39D0(): pass

    label('loc_39D0')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_39EC')

    def _loc_39DE(): pass

    label('loc_39DE')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_39EC')

    def _loc_39EC(): pass

    label('loc_39EC')

    Jump('loc_DB27')

    def _loc_39F1(): pass

    label('loc_39F1')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't0000：[リーヴス]', 0x00030D40)
    MenuAddItem(1, 't0010：第Ⅱ分校宿舎', 0x00030DA4)
    MenuAddItem(1, 't0030：七耀教会・リーヴス礼拝堂', 0x00030E6C)
    MenuAddItem(1, 't0040：宿酒場《バーニーズ》', 0x00030ED0)
    MenuAddItem(1, 't0050：食材・雑貨《如水庵》', 0x00030F34)
    MenuAddItem(1, 't0060：ブティック《ラパン》', 0x00030F98)
    MenuAddItem(1, 't0070：本・遊具《カーネギー書房》', 0x00030FFC)
    MenuAddItem(1, 't0080：ラジオ局《トリスタ放送》', 0x00031060)
    MenuAddItem(1, 't0090：武器・交換屋《ナインヴァリ》', 0x000310C4)
    MenuAddItem(1, 't0100：ベーカリーカフェ《ルセット》', 0x00031128)
    MenuAddItem(1, 't0110：民家①', 0x0003118C)
    MenuAddItem(1, 't0120：民家②', 0x000311F0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00030D40, 'loc_3C93'),
        (0x00030DA4, 'loc_3CA3'),
        (0x00030E08, 'loc_3CB3'),
        (0x00030E6C, 'loc_3CC3'),
        (0x00030ED0, 'loc_3CD3'),
        (0x00030F34, 'loc_3CE3'),
        (0x00030F98, 'loc_3CF3'),
        (0x00030FFC, 'loc_3D03'),
        (0x00031060, 'loc_3D13'),
        (0x000310C4, 'loc_3D23'),
        (0x00031128, 'loc_3D33'),
        (0x0003118C, 'loc_3D43'),
        (0x000311F0, 'loc_3D53'),
        (0x00000060, 'loc_3D63'),
        (-1, 'loc_3D71'),
    )

    def _loc_3C93(): pass

    label('loc_3C93')

    MapJump((0xDD, 't0000'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CA3(): pass

    label('loc_3CA3')

    MapJump((0xDD, 't0010'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CB3(): pass

    label('loc_3CB3')

    MapJump((0xDD, 't0020'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CC3(): pass

    label('loc_3CC3')

    MapJump((0xDD, 't0030'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CD3(): pass

    label('loc_3CD3')

    MapJump((0xDD, 't0040'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CE3(): pass

    label('loc_3CE3')

    MapJump((0xDD, 't0050'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3CF3(): pass

    label('loc_3CF3')

    MapJump((0xDD, 't0060'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D03(): pass

    label('loc_3D03')

    MapJump((0xDD, 't0070'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D13(): pass

    label('loc_3D13')

    MapJump((0xDD, 't0080'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D23(): pass

    label('loc_3D23')

    MapJump((0xDD, 't0090'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D33(): pass

    label('loc_3D33')

    MapJump((0xDD, 't0100'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D43(): pass

    label('loc_3D43')

    MapJump((0xDD, 't0110'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D53(): pass

    label('loc_3D53')

    MapJump((0xDD, 't0120'), (0xDD, ''), 0x00)

    Jump('loc_3D7F')

    def _loc_3D63(): pass

    label('loc_3D63')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3D7F')

    def _loc_3D71(): pass

    label('loc_3D71')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_3D7F')

    def _loc_3D7F(): pass

    label('loc_3D7F')

    Jump('loc_DB27')

    def _loc_3D84(): pass

    label('loc_3D84')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't0200：[トールズ第Ⅱ分校]', 0x00031510)
    MenuAddItem(1, 't0210：校舎１Ｆ・２Ｆ', 0x00031574)
    MenuAddItem(1, 't0230：食堂', 0x0003163C)
    MenuAddItem(1, 't0240：学生会館', 0x000316A0)
    MenuAddItem(1, 't0250：ギムナジウム・プール', 0x00031704)
    MenuAddItem(1, 't0260：格納庫・研究棟', 0x00031768)
    MenuAddItem(1, 't0270：ホーム', 0x000317CC)
    MenuAddItem(1, 't0280：倉庫', 0x00031830)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't0400：[アインヘル小要塞]', 0x00031CE0)
    MenuAddItem(1, 't0410：１階フロア', 0x00031D44)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm0500：アインヘル小要塞・Ｘ層①', 0x00062E08)
    MenuAddItem(1, 'm0510：アインヘル小要塞・Ｘ層②', 0x00062E6C)
    MenuAddItem(1, 'm0590：アインヘル小要塞・Ｘ層ボスマップ', 0x0006318C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00031510, 'loc_4125'),
        (0x00031574, 'loc_4135'),
        (0x0003163C, 'loc_4145'),
        (0x000316A0, 'loc_4155'),
        (0x00031704, 'loc_4165'),
        (0x00031768, 'loc_4175'),
        (0x000317CC, 'loc_4185'),
        (0x00031830, 'loc_4195'),
        (0x00031CE0, 'loc_41A5'),
        (0x00031D44, 'loc_41B5'),
        (0x00061A80, 'loc_41C5'),
        (0x00061A8A, 'loc_41D5'),
        (0x00061E04, 'loc_41E5'),
        (0x00061E0E, 'loc_41F5'),
        (0x00061E68, 'loc_4205'),
        (0x000621EC, 'loc_4215'),
        (0x00062250, 'loc_4225'),
        (0x000625D4, 'loc_4235'),
        (0x00062638, 'loc_4245'),
        (0x0006269C, 'loc_4255'),
        (0x000629BC, 'loc_4265'),
        (0x00062A20, 'loc_4275'),
        (0x00062A84, 'loc_4285'),
        (0x00062DA4, 'loc_4295'),
        (0x00062188, 'loc_42A5'),
        (0x000621F6, 'loc_42B5'),
        (0x00062570, 'loc_42C5'),
        (0x000625DE, 'loc_42D5'),
        (0x00062958, 'loc_42E5'),
        (0x000629C6, 'loc_42F5'),
        (0x00062D40, 'loc_4305'),
        (0x00062DAE, 'loc_4315'),
        (0x00062E08, 'loc_4325'),
        (0x00062E6C, 'loc_4335'),
        (0x0006318C, 'loc_4345'),
        (0x00000060, 'loc_4355'),
        (-1, 'loc_4363'),
    )

    def _loc_4125(): pass

    label('loc_4125')

    MapJump((0xDD, 't0200'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4135(): pass

    label('loc_4135')

    MapJump((0xDD, 't0210'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4145(): pass

    label('loc_4145')

    MapJump((0xDD, 't0230'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4155(): pass

    label('loc_4155')

    MapJump((0xDD, 't0240'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4165(): pass

    label('loc_4165')

    MapJump((0xDD, 't0250'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4175(): pass

    label('loc_4175')

    MapJump((0xDD, 't0260'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4185(): pass

    label('loc_4185')

    MapJump((0xDD, 't0270'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4195(): pass

    label('loc_4195')

    MapJump((0xDD, 't0280'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41A5(): pass

    label('loc_41A5')

    MapJump((0xDD, 't0400'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41B5(): pass

    label('loc_41B5')

    MapJump((0xDD, 't0410'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41C5(): pass

    label('loc_41C5')

    MapJump((0xDD, 'm0000'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41D5(): pass

    label('loc_41D5')

    MapJump((0xDD, 'm0001'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41E5(): pass

    label('loc_41E5')

    MapJump((0xDD, 'm0090'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_41F5(): pass

    label('loc_41F5')

    MapJump((0xDD, 'm0091'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4205(): pass

    label('loc_4205')

    MapJump((0xDD, 'm0100'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4215(): pass

    label('loc_4215')

    MapJump((0xDD, 'm0190'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4225(): pass

    label('loc_4225')

    MapJump((0xDD, 'm0200'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4235(): pass

    label('loc_4235')

    MapJump((0xDD, 'm0290'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4245(): pass

    label('loc_4245')

    MapJump((0xDD, 'm0300'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4255(): pass

    label('loc_4255')

    MapJump((0xDD, 'm0310'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4265(): pass

    label('loc_4265')

    MapJump((0xDD, 'm0390'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4275(): pass

    label('loc_4275')

    MapJump((0xDD, 'm0400'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4285(): pass

    label('loc_4285')

    MapJump((0xDD, 'm0410'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4295(): pass

    label('loc_4295')

    MapJump((0xDD, 'm0490'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42A5(): pass

    label('loc_42A5')

    MapJump((0xDD, 'm0180'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42B5(): pass

    label('loc_42B5')

    MapJump((0xDD, 'm0191'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42C5(): pass

    label('loc_42C5')

    MapJump((0xDD, 'm0280'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42D5(): pass

    label('loc_42D5')

    MapJump((0xDD, 'm0291'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42E5(): pass

    label('loc_42E5')

    MapJump((0xDD, 'm0380'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_42F5(): pass

    label('loc_42F5')

    MapJump((0xDD, 'm0391'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4305(): pass

    label('loc_4305')

    MapJump((0xDD, 'm0480'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4315(): pass

    label('loc_4315')

    MapJump((0xDD, 'm0491'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4325(): pass

    label('loc_4325')

    MapJump((0xDD, 'm0500'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4335(): pass

    label('loc_4335')

    MapJump((0xDD, 'm0510'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4345(): pass

    label('loc_4345')

    MapJump((0xDD, 'm0590'), (0xDD, ''), 0x00)

    Jump('loc_4371')

    def _loc_4355(): pass

    label('loc_4355')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4371')

    def _loc_4363(): pass

    label('loc_4363')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4371')

    def _loc_4371(): pass

    label('loc_4371')

    Jump('loc_DB27')

    def _loc_4376(): pass

    label('loc_4376')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't1000：[セントアーク・大聖堂前]', 0x00033450)
    MenuAddItem(1, 't1020：セントアーク大聖堂', 0x00033518)
    MenuAddItem(1, 't1030：《ホテル・オーガスタ》', 0x0003357C)
    MenuAddItem(1, 't1040：百貨店《アルビオンガーデン》', 0x000335E0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't1200：[セントアーク・住宅街]', 0x00033C20)
    MenuAddItem(1, 't1210：カフェ・宿泊《エイプリル》', 0x00033C84)
    MenuAddItem(1, 't1220：《チェンバーズ工房》', 0x00033CE8)
    MenuAddItem(1, 't1230：交換・古董品《デメテル》', 0x00033D4C)
    MenuAddItem(1, 't1240：アパルトメント《ルナクレスト》', 0x00033DB0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't1400：[セントアーク・貴族街]', 0x000343F0)
    MenuAddItem(1, 't1410：城館', 0x00034454)
    MenuAddItem(1, 't1420：貴族邸①', 0x000344B8)
    MenuAddItem(1, 't1430：貴族邸②', 0x0003451C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00033450, 'loc_46C8'),
        (0x000334B4, 'loc_46D8'),
        (0x00033518, 'loc_46E8'),
        (0x0003357C, 'loc_46F8'),
        (0x000335E0, 'loc_4708'),
        (0x00033C20, 'loc_4718'),
        (0x00033C84, 'loc_4728'),
        (0x00033CE8, 'loc_4738'),
        (0x00033D4C, 'loc_4748'),
        (0x00033DB0, 'loc_4758'),
        (0x000343F0, 'loc_4768'),
        (0x00034454, 'loc_4778'),
        (0x000344B8, 'loc_4788'),
        (0x0003451C, 'loc_4798'),
        (0x00000060, 'loc_47A8'),
        (-1, 'loc_47B6'),
    )

    def _loc_46C8(): pass

    label('loc_46C8')

    MapJump((0xDD, 't1000'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_46D8(): pass

    label('loc_46D8')

    MapJump((0xDD, 't1010'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_46E8(): pass

    label('loc_46E8')

    MapJump((0xDD, 't1020'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_46F8(): pass

    label('loc_46F8')

    MapJump((0xDD, 't1030'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4708(): pass

    label('loc_4708')

    MapJump((0xDD, 't1040'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4718(): pass

    label('loc_4718')

    MapJump((0xDD, 't1200'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4728(): pass

    label('loc_4728')

    MapJump((0xDD, 't1210'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4738(): pass

    label('loc_4738')

    MapJump((0xDD, 't1220'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4748(): pass

    label('loc_4748')

    MapJump((0xDD, 't1230'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4758(): pass

    label('loc_4758')

    MapJump((0xDD, 't1240'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4768(): pass

    label('loc_4768')

    MapJump((0xDD, 't1400'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4778(): pass

    label('loc_4778')

    MapJump((0xDD, 't1410'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4788(): pass

    label('loc_4788')

    MapJump((0xDD, 't1420'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_4798(): pass

    label('loc_4798')

    MapJump((0xDD, 't1430'), (0xDD, ''), 0x00)

    Jump('loc_47C4')

    def _loc_47A8(): pass

    label('loc_47A8')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_47C4')

    def _loc_47B6(): pass

    label('loc_47B6')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_47C4')

    def _loc_47C4(): pass

    label('loc_47C4')

    Jump('loc_DB27')

    def _loc_47C9(): pass

    label('loc_47C9')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't2000：[パルム]', 0x00035B60)
    MenuAddItem(1, 't2010：七耀教会・パルム礼拝堂', 0x00035BC4)
    MenuAddItem(1, 't2020：宿酒場《白の小道亭》', 0x00035C28)
    MenuAddItem(1, 't2030：武具・工房《ドワイト商会》', 0x00035C8C)
    MenuAddItem(1, 't2040：雑貨・仕立て屋《ジェローム》', 0x00035CF0)
    MenuAddItem(1, 't2050：ヴァンダール流・練武場', 0x00035D54)
    MenuAddItem(1, 't2060：民家', 0x00035DB8)
    MenuAddItem(1, 't2070：町長宅', 0x00035E1C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't2200：ハーメル廃村', 0x00036330)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00035B60, 'loc_49DE'),
        (0x00035BC4, 'loc_49EE'),
        (0x00035C28, 'loc_49FE'),
        (0x00035C8C, 'loc_4A0E'),
        (0x00035CF0, 'loc_4A1E'),
        (0x00035D54, 'loc_4A2E'),
        (0x00035DB8, 'loc_4A3E'),
        (0x00035E1C, 'loc_4A4E'),
        (0x00036330, 'loc_4A5E'),
        (0x00000060, 'loc_4A6E'),
        (-1, 'loc_4A7C'),
    )

    def _loc_49DE(): pass

    label('loc_49DE')

    MapJump((0xDD, 't2000'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_49EE(): pass

    label('loc_49EE')

    MapJump((0xDD, 't2010'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_49FE(): pass

    label('loc_49FE')

    MapJump((0xDD, 't2020'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A0E(): pass

    label('loc_4A0E')

    MapJump((0xDD, 't2030'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A1E(): pass

    label('loc_4A1E')

    MapJump((0xDD, 't2040'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A2E(): pass

    label('loc_4A2E')

    MapJump((0xDD, 't2050'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A3E(): pass

    label('loc_4A3E')

    MapJump((0xDD, 't2060'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A4E(): pass

    label('loc_4A4E')

    MapJump((0xDD, 't2070'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A5E(): pass

    label('loc_4A5E')

    MapJump((0xDD, 't2200'), (0xDD, ''), 0x00)

    Jump('loc_4A8A')

    def _loc_4A6E(): pass

    label('loc_4A6E')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4A8A')

    def _loc_4A7C(): pass

    label('loc_4A7C')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_4A8A')

    def _loc_4A8A(): pass

    label('loc_4A8A')

    Jump('loc_DB27')

    def _loc_4A8F(): pass

    label('loc_4A8F')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't3000：[オルディス・商業エリア]', 0x00038270)
    MenuAddItem(1, 't3010：《ホテル・オルテンシア》', 0x000382D4)
    MenuAddItem(1, 't3021：《リヴィエラコート》', 0x00038342)
    MenuAddItem(1, 't3030：《クライストモール》', 0x0003839C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't3200：[オルディス・庶民街]', 0x00038A40)
    MenuAddItem(1, 't3210：宿酒場《海風亭》', 0x00038AA4)
    MenuAddItem(1, 't3220：《シュトラウス工房》', 0x00038B08)
    MenuAddItem(1, 't3230：イーグレット伯爵邸', 0x00038B6C)
    MenuAddItem(1, 't3240：民家', 0x00038BD0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't3400：[オルディス・貴族街]', 0x00039210)
    MenuAddItem(1, 't3410：七耀教会・オルディス大聖堂', 0x00039274)
    MenuAddItem(1, 't3420：貴族邸①', 0x000392D8)
    MenuAddItem(1, 't3430：貴族邸②', 0x0003933C)
    MenuAddItem(1, 't3510：公爵家城館・エントランス', 0x0003965C)
    MenuAddItem(1, 't3520：公爵家城館・食事スペース', 0x000396C0)
    MenuAddItem(1, 't3530：公爵家城館・会議スペース', 0x00039724)
    MenuAddItem(1, 't3540：[公爵家城館・テラス]', 0x00039788)
    MenuAddItem(1, 't3550：公爵家城館・廊下', 0x000397EC)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't3600：[オルディス・港湾エリア]', 0x000399E0)
    MenuAddItem(1, 't3610：船員酒場《ミランダ》', 0x00039A44)
    MenuAddItem(1, 't3620：《リヴィエラコート》移転', 0x00039AA8)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 't3800：[オルディス沖合い]', 0x0003A1B0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00038270, 'loc_5011'),
        (0x000382D4, 'loc_5021'),
        (0x00038342, 'loc_5031'),
        (0x0003839C, 'loc_5041'),
        (0x00038A40, 'loc_5051'),
        (0x00038AA4, 'loc_5061'),
        (0x00038B08, 'loc_5071'),
        (0x00038B6C, 'loc_5081'),
        (0x00038BD0, 'loc_5091'),
        (0x00039210, 'loc_50A1'),
        (0x00039274, 'loc_50B1'),
        (0x000392D8, 'loc_50C1'),
        (0x0003933C, 'loc_50D1'),
        (0x0003965C, 'loc_50E1'),
        (0x000396C0, 'loc_50F1'),
        (0x00039724, 'loc_5101'),
        (0x00039788, 'loc_5111'),
        (0x000397EC, 'loc_5121'),
        (0x000399E0, 'loc_5131'),
        (0x00039A44, 'loc_5141'),
        (0x00039AA8, 'loc_5151'),
        (0x0003A1B0, 'loc_5161'),
        (0x00000060, 'loc_5171'),
        (-1, 'loc_517F'),
    )

    def _loc_5011(): pass

    label('loc_5011')

    MapJump((0xDD, 't3000'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5021(): pass

    label('loc_5021')

    MapJump((0xDD, 't3010'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5031(): pass

    label('loc_5031')

    MapJump((0xDD, 't3021'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5041(): pass

    label('loc_5041')

    MapJump((0xDD, 't3030'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5051(): pass

    label('loc_5051')

    MapJump((0xDD, 't3200'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5061(): pass

    label('loc_5061')

    MapJump((0xDD, 't3210'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5071(): pass

    label('loc_5071')

    MapJump((0xDD, 't3220'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5081(): pass

    label('loc_5081')

    MapJump((0xDD, 't3230'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5091(): pass

    label('loc_5091')

    MapJump((0xDD, 't3240'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50A1(): pass

    label('loc_50A1')

    MapJump((0xDD, 't3400'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50B1(): pass

    label('loc_50B1')

    MapJump((0xDD, 't3410'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50C1(): pass

    label('loc_50C1')

    MapJump((0xDD, 't3420'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50D1(): pass

    label('loc_50D1')

    MapJump((0xDD, 't3430'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50E1(): pass

    label('loc_50E1')

    MapJump((0xDD, 't3510'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_50F1(): pass

    label('loc_50F1')

    MapJump((0xDD, 't3520'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5101(): pass

    label('loc_5101')

    MapJump((0xDD, 't3530'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5111(): pass

    label('loc_5111')

    MapJump((0xDD, 't3540'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5121(): pass

    label('loc_5121')

    MapJump((0xDD, 't3550'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5131(): pass

    label('loc_5131')

    MapJump((0xDD, 't3600'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5141(): pass

    label('loc_5141')

    MapJump((0xDD, 't3610'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5151(): pass

    label('loc_5151')

    MapJump((0xDD, 't3620'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5161(): pass

    label('loc_5161')

    MapJump((0xDD, 't3800'), (0xDD, ''), 0x00)

    Jump('loc_518D')

    def _loc_5171(): pass

    label('loc_5171')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_518D')

    def _loc_517F(): pass

    label('loc_517F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_518D')

    def _loc_518D(): pass

    label('loc_518D')

    Jump('loc_DB27')

    def _loc_5192(): pass

    label('loc_5192')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't4000：[ラクウェル]', 0x0003A980)
    MenuAddItem(1, 't4010：七耀教会・ラクウェル礼拝堂', 0x0003A9E4)
    MenuAddItem(1, 't4020：パブ・宿泊《ハーミット》', 0x0003AA48)
    MenuAddItem(1, 't4030：大衆食堂《デッケン》', 0x0003AAAC)
    MenuAddItem(1, 't4040：《イカロス・マート》', 0x0003AB10)
    MenuAddItem(1, 't4050：質屋《マッケンロー》', 0x0003AB74)
    MenuAddItem(1, 't4060：カジノ《アリーシャ》\x09', 0x0003ABD8)
    MenuAddItem(1, 't4070：《リバティーハイツ》', 0x0003AC3C)
    MenuAddItem(1, 't4080：《メゾン・エカイユ》', 0x0003ACA0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0003A980, 'loc_53A6'),
        (0x0003A9E4, 'loc_53B6'),
        (0x0003AA48, 'loc_53C6'),
        (0x0003AAAC, 'loc_53D6'),
        (0x0003AB10, 'loc_53E6'),
        (0x0003AB74, 'loc_53F6'),
        (0x0003ABD8, 'loc_5406'),
        (0x0003AC3C, 'loc_5416'),
        (0x0003ACA0, 'loc_5426'),
        (0x00000060, 'loc_5436'),
        (-1, 'loc_5444'),
    )

    def _loc_53A6(): pass

    label('loc_53A6')

    MapJump((0xDD, 't4000'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_53B6(): pass

    label('loc_53B6')

    MapJump((0xDD, 't4010'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_53C6(): pass

    label('loc_53C6')

    MapJump((0xDD, 't4020'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_53D6(): pass

    label('loc_53D6')

    MapJump((0xDD, 't4030'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_53E6(): pass

    label('loc_53E6')

    MapJump((0xDD, 't4040'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_53F6(): pass

    label('loc_53F6')

    MapJump((0xDD, 't4050'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_5406(): pass

    label('loc_5406')

    MapJump((0xDD, 't4060'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_5416(): pass

    label('loc_5416')

    MapJump((0xDD, 't4070'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_5426(): pass

    label('loc_5426')

    MapJump((0xDD, 't4080'), (0xDD, ''), 0x00)

    Jump('loc_5452')

    def _loc_5436(): pass

    label('loc_5436')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5452')

    def _loc_5444(): pass

    label('loc_5444')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5452')

    def _loc_5452(): pass

    label('loc_5452')

    Jump('loc_DB27')

    def _loc_5457(): pass

    label('loc_5457')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't5000：[エリン]', 0x0003D090)
    MenuAddItem(1, 't5010：ロゼのアトリエ', 0x0003D0F4)
    MenuAddItem(1, 't5020：宿酒場', 0x0003D158)
    MenuAddItem(1, 't5030：雑貨食材屋', 0x0003D1BC)
    MenuAddItem(1, 't5040：武器防具屋', 0x0003D220)
    MenuAddItem(1, 't5050：薬師', 0x0003D284)
    MenuAddItem(1, 't5060：民家（占い師）', 0x0003D2E8)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0003D090, 'loc_558C'),
        (0x0003D0F4, 'loc_559C'),
        (0x0003D158, 'loc_55AC'),
        (0x0003D1BC, 'loc_55BC'),
        (0x0003D220, 'loc_55CC'),
        (0x0003D284, 'loc_55DC'),
        (0x0003D2E8, 'loc_55EC'),
        (0x00000060, 'loc_55FC'),
        (-1, 'loc_560A'),
    )

    def _loc_558C(): pass

    label('loc_558C')

    MapJump((0xDD, 't5000'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_559C(): pass

    label('loc_559C')

    MapJump((0xDD, 't5010'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55AC(): pass

    label('loc_55AC')

    MapJump((0xDD, 't5020'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55BC(): pass

    label('loc_55BC')

    MapJump((0xDD, 't5030'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55CC(): pass

    label('loc_55CC')

    MapJump((0xDD, 't5040'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55DC(): pass

    label('loc_55DC')

    MapJump((0xDD, 't5050'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55EC(): pass

    label('loc_55EC')

    MapJump((0xDD, 't5060'), (0xDD, ''), 0x00)

    Jump('loc_5618')

    def _loc_55FC(): pass

    label('loc_55FC')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5618')

    def _loc_560A(): pass

    label('loc_560A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5618')

    def _loc_5618(): pass

    label('loc_5618')

    Jump('loc_DB27')

    def _loc_561D(): pass

    label('loc_561D')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't6000：[ミルサンテ]', 0x0003F7A0)
    MenuAddItem(1, 't6010：教会', 0x0003F804)
    MenuAddItem(1, 't6020：宿酒場', 0x0003F868)
    MenuAddItem(1, 't6030：武具工房・雑貨食材', 0x0003F8CC)
    MenuAddItem(1, 't6040：民家', 0x0003F930)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0003F7A0, 'loc_5711'),
        (0x000007D1, 'loc_5721'),
        (0x0003F804, 'loc_5731'),
        (0x0003F868, 'loc_5741'),
        (0x0003F8CC, 'loc_5751'),
        (0x0003F930, 'loc_5761'),
        (0x0003F994, 'loc_5771'),
        (0x00000060, 'loc_5781'),
        (-1, 'loc_578F'),
    )

    def _loc_5711(): pass

    label('loc_5711')

    MapJump((0xDD, 't6000'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5721(): pass

    label('loc_5721')

    MapJump((0xDD, 'a2001'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5731(): pass

    label('loc_5731')

    MapJump((0xDD, 't6010'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5741(): pass

    label('loc_5741')

    MapJump((0xDD, 't6020'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5751(): pass

    label('loc_5751')

    MapJump((0xDD, 't6030'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5761(): pass

    label('loc_5761')

    MapJump((0xDD, 't6040'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5771(): pass

    label('loc_5771')

    MapJump((0xDD, 't6050'), (0xDD, ''), 0x00)

    Jump('loc_579D')

    def _loc_5781(): pass

    label('loc_5781')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_579D')

    def _loc_578F(): pass

    label('loc_578F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_579D')

    def _loc_579D(): pass

    label('loc_579D')

    Jump('loc_DB27')

    def _loc_57A2(): pass

    label('loc_57A2')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't7000：[アルスター]', 0x00041EB0)
    MenuAddItem(1, 't7010：教会', 0x00041F14)
    MenuAddItem(1, 't7020：宿酒場', 0x00041F78)
    MenuAddItem(1, 't7030：武具工房・雑貨', 0x00041FDC)
    MenuAddItem(1, 't7040：ウイスキー蒸留所', 0x00042040)
    MenuAddItem(1, 't7050：カイ・ティーリア宅', 0x000420A4)
    MenuAddItem(1, 't7060：民家', 0x00042108)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00041EB0, 'loc_58F3'),
        (0x00004E2B, 'loc_5903'),
        (0x00041F14, 'loc_5914'),
        (0x00041F78, 'loc_5924'),
        (0x00041FDC, 'loc_5934'),
        (0x00042040, 'loc_5944'),
        (0x000420A4, 'loc_5954'),
        (0x00042108, 'loc_5964'),
        (0x0004216C, 'loc_5974'),
        (0x00000060, 'loc_5984'),
        (-1, 'loc_5992'),
    )

    def _loc_58F3(): pass

    label('loc_58F3')

    MapJump((0xDD, 't7000'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5903(): pass

    label('loc_5903')

    MapJump((0xDD, 'a2001b'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5914(): pass

    label('loc_5914')

    MapJump((0xDD, 't7010'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5924(): pass

    label('loc_5924')

    MapJump((0xDD, 't7020'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5934(): pass

    label('loc_5934')

    MapJump((0xDD, 't7030'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5944(): pass

    label('loc_5944')

    MapJump((0xDD, 't7040'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5954(): pass

    label('loc_5954')

    MapJump((0xDD, 't7050'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5964(): pass

    label('loc_5964')

    MapJump((0xDD, 't7060'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5974(): pass

    label('loc_5974')

    MapJump((0xDD, 't7070'), (0xDD, ''), 0x00)

    Jump('loc_59A0')

    def _loc_5984(): pass

    label('loc_5984')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_59A0')

    def _loc_5992(): pass

    label('loc_5992')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_59A0')

    def _loc_59A0(): pass

    label('loc_59A0')

    Jump('loc_DB27')

    def _loc_59A5(): pass

    label('loc_59A5')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't8000：レグラム', 0x000445C0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000445C0, 'loc_59F4'),
        (0x00000060, 'loc_5A04'),
        (-1, 'loc_5A12'),
    )

    def _loc_59F4(): pass

    label('loc_59F4')

    MapJump((0xDD, 't8000'), (0xDD, ''), 0x00)

    Jump('loc_5A20')

    def _loc_5A04(): pass

    label('loc_5A04')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5A20')

    def _loc_5A12(): pass

    label('loc_5A12')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5A20')

    def _loc_5A20(): pass

    label('loc_5A20')

    Jump('loc_DB27')

    def _loc_5A25(): pass

    label('loc_5A25')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't9000：ＲＦ本社ビル', 0x00000000)
    MenuAddItem(1, 't9010：[ルーレ]', 0x00000001)
    MenuAddItem(1, 't9200：アルバレア公爵邸', 0x00000002)
    MenuAddItem(1, 't9210：[バリアハート貴族街]', 0x00000003)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_5B02'),
        (0x00000001, 'loc_5B12'),
        (0x00000002, 'loc_5B22'),
        (0x00000003, 'loc_5B32'),
        (0x00000060, 'loc_5B42'),
        (-1, 'loc_5B50'),
    )

    def _loc_5B02(): pass

    label('loc_5B02')

    MapJump((0xDD, 't9000'), (0xDD, ''), 0x00)

    Jump('loc_5B5E')

    def _loc_5B12(): pass

    label('loc_5B12')

    MapJump((0xDD, 't9010'), (0xDD, ''), 0x00)

    Jump('loc_5B5E')

    def _loc_5B22(): pass

    label('loc_5B22')

    MapJump((0xDD, 't9200'), (0xDD, ''), 0x00)

    Jump('loc_5B5E')

    def _loc_5B32(): pass

    label('loc_5B32')

    MapJump((0xDD, 't9210'), (0xDD, ''), 0x00)

    Jump('loc_5B5E')

    def _loc_5B42(): pass

    label('loc_5B42')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5B5E')

    def _loc_5B50(): pass

    label('loc_5B50')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_5B5E')

    def _loc_5B5E(): pass

    label('loc_5B5E')

    Jump('loc_DB27')

    def _loc_5B63(): pass

    label('loc_5B63')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c0000：[駅前]', 0x000186A0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c0200：[中央広場]', 0x00018E70)
    MenuAddItem(1, 'c0210：百貨店《タイムズ》', 0x00018ED4)
    MenuAddItem(1, 'c0220：オーバルストア《ゲンテン》', 0x00018F38)
    MenuAddItem(1, 'c0230：《ジロンド武器商会》', 0x00018F9C)
    MenuAddItem(1, 'c0240：カフェレストラン《ヴァンセット》', 0x00019000)
    MenuAddItem(1, 'c0250：旧特務支援科', 0x00019064)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c0400：[東通り]', 0x00019640)
    MenuAddItem(1, 'c0410：宿酒場《龍老飯店》', 0x000196A4)
    MenuAddItem(1, 'c0420：釣公師団・クロスベル支部', 0x00019708)
    MenuAddItem(1, 'c0430：クロスベル商工組合', 0x0001976C)
    MenuAddItem(1, 'c0440：交換屋《ナインヴァリ》', 0x000197D0)
    MenuAddItem(1, 'c0450：アパルトメント《アカシア荘》', 0x00019834)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c0600：[西通り]', 0x00019E10)
    MenuAddItem(1, 'c0610：ベーカリー《モルジュ》', 0x00019E74)
    MenuAddItem(1, 'c0620：食品・雑貨《タリーズ商店》', 0x00019ED8)
    MenuAddItem(1, 'c0631：クロスベル通信社（元法律事務所）', 0x00019F46)
    MenuAddItem(1, 'c0640：アパルトメント《ベルハイム》', 0x00019FA0)
    MenuAddItem(1, 'c0650：アパルトメント《ヴィラ・レザン》', 0x0001A004)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000186A0, 'loc_6062'),
        (0x00018E70, 'loc_6072'),
        (0x00018ED4, 'loc_6082'),
        (0x00018F38, 'loc_6092'),
        (0x00018F9C, 'loc_60A2'),
        (0x00019000, 'loc_60B2'),
        (0x00019064, 'loc_60C2'),
        (0x00019640, 'loc_60D2'),
        (0x000196A4, 'loc_60E2'),
        (0x00019708, 'loc_60F2'),
        (0x0001976C, 'loc_6102'),
        (0x000197D0, 'loc_6112'),
        (0x00019834, 'loc_6122'),
        (0x00019E10, 'loc_6132'),
        (0x00019E74, 'loc_6142'),
        (0x00019ED8, 'loc_6152'),
        (0x00019F46, 'loc_6162'),
        (0x00019FA0, 'loc_6172'),
        (0x0001A004, 'loc_6182'),
        (0x0001A5E0, 'loc_6192'),
        (0x0001A644, 'loc_61A2'),
        (0x0001A6A8, 'loc_61B2'),
        (0x0001A70C, 'loc_61C2'),
        (0x0001ADB0, 'loc_61D2'),
        (0x00000060, 'loc_61E2'),
        (-1, 'loc_61F0'),
    )

    def _loc_6062(): pass

    label('loc_6062')

    MapJump((0xDD, 'c0000'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6072(): pass

    label('loc_6072')

    MapJump((0xDD, 'c0200'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6082(): pass

    label('loc_6082')

    MapJump((0xDD, 'c0210'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6092(): pass

    label('loc_6092')

    MapJump((0xDD, 'c0220'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60A2(): pass

    label('loc_60A2')

    MapJump((0xDD, 'c0230'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60B2(): pass

    label('loc_60B2')

    MapJump((0xDD, 'c0240'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60C2(): pass

    label('loc_60C2')

    MapJump((0xDD, 'c0250'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60D2(): pass

    label('loc_60D2')

    MapJump((0xDD, 'c0400'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60E2(): pass

    label('loc_60E2')

    MapJump((0xDD, 'c0410'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_60F2(): pass

    label('loc_60F2')

    MapJump((0xDD, 'c0420'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6102(): pass

    label('loc_6102')

    MapJump((0xDD, 'c0430'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6112(): pass

    label('loc_6112')

    MapJump((0xDD, 'c0440'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6122(): pass

    label('loc_6122')

    MapJump((0xDD, 'c0450'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6132(): pass

    label('loc_6132')

    MapJump((0xDD, 'c0600'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6142(): pass

    label('loc_6142')

    MapJump((0xDD, 'c0610'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6152(): pass

    label('loc_6152')

    MapJump((0xDD, 'c0620'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6162(): pass

    label('loc_6162')

    MapJump((0xDD, 'c0631'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6172(): pass

    label('loc_6172')

    MapJump((0xDD, 'c0640'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6182(): pass

    label('loc_6182')

    MapJump((0xDD, 'c0650'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_6192(): pass

    label('loc_6192')

    MapJump((0xDD, 'c0800'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_61A2(): pass

    label('loc_61A2')

    MapJump((0xDD, 'c0810'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_61B2(): pass

    label('loc_61B2')

    MapJump((0xDD, 'c0820'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_61C2(): pass

    label('loc_61C2')

    MapJump((0xDD, 'c0830'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_61D2(): pass

    label('loc_61D2')

    MapJump((0xDD, 'c1000'), (0xDD, ''), 0x00)

    Jump('loc_61FE')

    def _loc_61E2(): pass

    label('loc_61E2')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_61FE')

    def _loc_61F0(): pass

    label('loc_61F0')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_61FE')

    def _loc_61FE(): pass

    label('loc_61FE')

    Jump('loc_DB27')

    def _loc_6203(): pass

    label('loc_6203')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c0800：[港湾区]', 0x0001A5E0)
    MenuAddItem(1, 'c0820：ＲＦグループ・クロスベル支社', 0x0001A6A8)
    MenuAddItem(1, 'c0830：黒月貿易公司', 0x0001A70C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c1000：[オルキスタワー]', 0x0001ADB0)
    MenuAddItem(1, 'c1020：高速エレベーター', 0x0001AE78)
    MenuAddItem(1, 'c1030：２０Ｆ執務室', 0x0001AEDC)
    MenuAddItem(1, 'c1080：屋上', 0x0001B0D0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000186A0, 'loc_6471'),
        (0x00018E70, 'loc_6481'),
        (0x00018ED4, 'loc_6491'),
        (0x00018F38, 'loc_64A1'),
        (0x00018F9C, 'loc_64B1'),
        (0x00019000, 'loc_64C1'),
        (0x00019640, 'loc_64D1'),
        (0x000196A4, 'loc_64E1'),
        (0x00019708, 'loc_64F1'),
        (0x0001976C, 'loc_6501'),
        (0x000197D0, 'loc_6511'),
        (0x00019834, 'loc_6521'),
        (0x00019E10, 'loc_6531'),
        (0x00019E74, 'loc_6541'),
        (0x00019ED8, 'loc_6551'),
        (0x00019F3C, 'loc_6561'),
        (0x00019FA0, 'loc_6571'),
        (0x0001A004, 'loc_6581'),
        (0x0001A5E0, 'loc_6591'),
        (0x0001A644, 'loc_65A1'),
        (0x0001A6A8, 'loc_65B1'),
        (0x0001A70C, 'loc_65C1'),
        (0x0001ADB0, 'loc_65D1'),
        (0x0001AE14, 'loc_65E1'),
        (0x0001AE78, 'loc_65F1'),
        (0x0001AEDC, 'loc_6601'),
        (0x0001AF40, 'loc_6611'),
        (0x0001AFA4, 'loc_6621'),
        (0x0001B008, 'loc_6631'),
        (0x0001B06C, 'loc_6641'),
        (0x0001B076, 'loc_6651'),
        (0x0001B0D0, 'loc_6661'),
        (0x0001B580, 'loc_6671'),
        (0x0001BD50, 'loc_6681'),
        (0x00000060, 'loc_6691'),
        (-1, 'loc_669F'),
    )

    def _loc_6471(): pass

    label('loc_6471')

    MapJump((0xDD, 'c0000'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6481(): pass

    label('loc_6481')

    MapJump((0xDD, 'c0200'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6491(): pass

    label('loc_6491')

    MapJump((0xDD, 'c0210'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64A1(): pass

    label('loc_64A1')

    MapJump((0xDD, 'c0220'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64B1(): pass

    label('loc_64B1')

    MapJump((0xDD, 'c0230'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64C1(): pass

    label('loc_64C1')

    MapJump((0xDD, 'c0240'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64D1(): pass

    label('loc_64D1')

    MapJump((0xDD, 'c0400'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64E1(): pass

    label('loc_64E1')

    MapJump((0xDD, 'c0410'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_64F1(): pass

    label('loc_64F1')

    MapJump((0xDD, 'c0420'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6501(): pass

    label('loc_6501')

    MapJump((0xDD, 'c0430'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6511(): pass

    label('loc_6511')

    MapJump((0xDD, 'c0440'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6521(): pass

    label('loc_6521')

    MapJump((0xDD, 'c0450'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6531(): pass

    label('loc_6531')

    MapJump((0xDD, 'c0600'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6541(): pass

    label('loc_6541')

    MapJump((0xDD, 'c0610'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6551(): pass

    label('loc_6551')

    MapJump((0xDD, 'c0620'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6561(): pass

    label('loc_6561')

    MapJump((0xDD, 'c0630'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6571(): pass

    label('loc_6571')

    MapJump((0xDD, 'c0640'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6581(): pass

    label('loc_6581')

    MapJump((0xDD, 'c0650'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6591(): pass

    label('loc_6591')

    MapJump((0xDD, 'c0800'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65A1(): pass

    label('loc_65A1')

    MapJump((0xDD, 'c0810'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65B1(): pass

    label('loc_65B1')

    MapJump((0xDD, 'c0820'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65C1(): pass

    label('loc_65C1')

    MapJump((0xDD, 'c0830'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65D1(): pass

    label('loc_65D1')

    MapJump((0xDD, 'c1000'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65E1(): pass

    label('loc_65E1')

    MapJump((0xDD, 'c1010'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_65F1(): pass

    label('loc_65F1')

    MapJump((0xDD, 'c1020'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6601(): pass

    label('loc_6601')

    MapJump((0xDD, 'c1030'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6611(): pass

    label('loc_6611')

    MapJump((0xDD, 'c1040'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6621(): pass

    label('loc_6621')

    MapJump((0xDD, 'c1050'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6631(): pass

    label('loc_6631')

    MapJump((0xDD, 'c1060'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6641(): pass

    label('loc_6641')

    MapJump((0xDD, 'c1070'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6651(): pass

    label('loc_6651')

    MapJump((0xDD, 'c1071'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6661(): pass

    label('loc_6661')

    MapJump((0xDD, 'c1080'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6671(): pass

    label('loc_6671')

    MapJump((0xDD, 'c1200'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6681(): pass

    label('loc_6681')

    MapJump((0xDD, 'c1400'), (0xDD, ''), 0x00)

    Jump('loc_66AD')

    def _loc_6691(): pass

    label('loc_6691')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_66AD')

    def _loc_669F(): pass

    label('loc_669F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_66AD')

    def _loc_66AD(): pass

    label('loc_66AD')

    Jump('loc_DB27')

    def _loc_66B2(): pass

    label('loc_66B2')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c1200：[歓楽街／裏通り]', 0x0001B580)
    MenuAddItem(1, 'c1210：ホテル', 0x0001B5E4)
    MenuAddItem(1, 'c1220：カジノ', 0x0001B648)
    MenuAddItem(1, 'c1230：イメルダ', 0x0001B6AC)
    MenuAddItem(1, 'c1240：バー', 0x0001B710)
    MenuAddItem(1, 'c1250：アルカンシェル', 0x0001B774)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0001B580, 'loc_67DD'),
        (0x0001B5E4, 'loc_67ED'),
        (0x0001B648, 'loc_67FD'),
        (0x0001B6AC, 'loc_680D'),
        (0x0001B710, 'loc_681D'),
        (0x0001B774, 'loc_682D'),
        (0x0001BD50, 'loc_683D'),
        (0x0001BDB4, 'loc_684D'),
        (0x0001BE18, 'loc_685D'),
        (0x0001BD50, 'loc_686D'),
        (0x00000060, 'loc_687D'),
        (-1, 'loc_688B'),
    )

    def _loc_67DD(): pass

    label('loc_67DD')

    MapJump((0xDD, 'c1200'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_67ED(): pass

    label('loc_67ED')

    MapJump((0xDD, 'c1210'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_67FD(): pass

    label('loc_67FD')

    MapJump((0xDD, 'c1220'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_680D(): pass

    label('loc_680D')

    MapJump((0xDD, 'c1230'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_681D(): pass

    label('loc_681D')

    MapJump((0xDD, 'c1240'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_682D(): pass

    label('loc_682D')

    MapJump((0xDD, 'c1250'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_683D(): pass

    label('loc_683D')

    MapJump((0xDD, 'c1400'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_684D(): pass

    label('loc_684D')

    MapJump((0xDD, 'c1410'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_685D(): pass

    label('loc_685D')

    MapJump((0xDD, 'c1400'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_686D(): pass

    label('loc_686D')

    MapJump((0xDD, 'c1400'), (0xDD, ''), 0x00)

    Jump('loc_6899')

    def _loc_687D(): pass

    label('loc_687D')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6899')

    def _loc_688B(): pass

    label('loc_688B')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6899')

    def _loc_6899(): pass

    label('loc_6899')

    Jump('loc_DB27')

    def _loc_689E(): pass

    label('loc_689E')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c2200：[ヴァンクール大通り]', 0x0001DC90)
    MenuAddItem(1, 'c2400：[ドライケルス広場]', 0x0001E460)
    MenuAddItem(1, 'c2410：バルフレイム宮･執務室', 0x0001E4C4)
    MenuAddItem(1, 'c2430：バルフレイム宮･翡翠庭園', 0x0001E58C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c3610：カレル離宮・大伽藍', 0x000213A4)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0001D4C0, 'loc_6B3D'),
        (0x0001D524, 'loc_6B4D'),
        (0x0001D588, 'loc_6B5D'),
        (0x0001DC90, 'loc_6B6D'),
        (0x0001DC9A, 'loc_6B7D'),
        (0x0001DCF4, 'loc_6B8D'),
        (0x0001DD58, 'loc_6B9D'),
        (0x0001DDBC, 'loc_6BAD'),
        (0x0001DE20, 'loc_6BBD'),
        (0x0001DE84, 'loc_6BCD'),
        (0x0001E460, 'loc_6BDD'),
        (0x0001E4C4, 'loc_6BED'),
        (0x0001E528, 'loc_6BFD'),
        (0x0001E58C, 'loc_6C0D'),
        (0x00000BB8, 'loc_6C1D'),
        (0x0001E5F0, 'loc_6C2D'),
        (0x0001EC30, 'loc_6C3D'),
        (0x0001EC94, 'loc_6C4D'),
        (0x0001ECF8, 'loc_6C5D'),
        (0x0001ED5C, 'loc_6C6D'),
        (0x0001EDC0, 'loc_6C7D'),
        (0x0001EE24, 'loc_6C8D'),
        (0x0001EE88, 'loc_6C9D'),
        (0x0001F400, 'loc_6CAD'),
        (0x0001F464, 'loc_6CBD'),
        (0x0001F4C8, 'loc_6CCD'),
        (0x0001F52C, 'loc_6CDD'),
        (0x0001F590, 'loc_6CED'),
        (0x0001F5F4, 'loc_6CFD'),
        (0x0001F658, 'loc_6D0D'),
        (0x0001FBD0, 'loc_6D1D'),
        (0x0001FC34, 'loc_6D2D'),
        (0x0001FC98, 'loc_6D3D'),
        (0x0001FCFC, 'loc_6D4D'),
        (0x000203A0, 'loc_6D5D'),
        (0x00020404, 'loc_6D6D'),
        (0x00020468, 'loc_6D7D'),
        (0x000204CC, 'loc_6D8D'),
        (0x00020BD4, 'loc_6D9D'),
        (0x00020C38, 'loc_6DAD'),
        (0x00021340, 'loc_6DBD'),
        (0x000213A4, 'loc_6DCD'),
        (0x00021408, 'loc_6DDD'),
        (0x00000060, 'loc_6DED'),
        (-1, 'loc_6DFB'),
    )

    def _loc_6B3D(): pass

    label('loc_6B3D')

    MapJump((0xDD, 'c2000'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B4D(): pass

    label('loc_6B4D')

    MapJump((0xDD, 'c2010'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B5D(): pass

    label('loc_6B5D')

    MapJump((0xDD, 'c2020'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B6D(): pass

    label('loc_6B6D')

    MapJump((0xDD, 'c2200'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B7D(): pass

    label('loc_6B7D')

    MapJump((0xDD, 'c2201'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B8D(): pass

    label('loc_6B8D')

    MapJump((0xDD, 'c2210'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6B9D(): pass

    label('loc_6B9D')

    MapJump((0xDD, 'c2220'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BAD(): pass

    label('loc_6BAD')

    MapJump((0xDD, 'c2230'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BBD(): pass

    label('loc_6BBD')

    MapJump((0xDD, 'c2240'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BCD(): pass

    label('loc_6BCD')

    MapJump((0xDD, 'c2250'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BDD(): pass

    label('loc_6BDD')

    MapJump((0xDD, 'c2400'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BED(): pass

    label('loc_6BED')

    MapJump((0xDD, 'c2410'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6BFD(): pass

    label('loc_6BFD')

    MapJump((0xDD, 'c2420'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C0D(): pass

    label('loc_6C0D')

    MapJump((0xDD, 'c2430'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C1D(): pass

    label('loc_6C1D')

    MapJump((0xDD, 'a3000'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C2D(): pass

    label('loc_6C2D')

    MapJump((0xDD, 'c2440'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C3D(): pass

    label('loc_6C3D')

    MapJump((0xDD, 'c2600'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C4D(): pass

    label('loc_6C4D')

    MapJump((0xDD, 'c2610'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C5D(): pass

    label('loc_6C5D')

    MapJump((0xDD, 'c2620'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C6D(): pass

    label('loc_6C6D')

    MapJump((0xDD, 'c2630'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C7D(): pass

    label('loc_6C7D')

    MapJump((0xDD, 'c2640'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C8D(): pass

    label('loc_6C8D')

    MapJump((0xDD, 'c2650'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6C9D(): pass

    label('loc_6C9D')

    MapJump((0xDD, 'c2660'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CAD(): pass

    label('loc_6CAD')

    MapJump((0xDD, 'c2800'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CBD(): pass

    label('loc_6CBD')

    MapJump((0xDD, 'c2810'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CCD(): pass

    label('loc_6CCD')

    MapJump((0xDD, 'c2820'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CDD(): pass

    label('loc_6CDD')

    MapJump((0xDD, 'c2830'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CED(): pass

    label('loc_6CED')

    MapJump((0xDD, 'c2840'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6CFD(): pass

    label('loc_6CFD')

    MapJump((0xDD, 'c2850'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D0D(): pass

    label('loc_6D0D')

    MapJump((0xDD, 'c2860'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D1D(): pass

    label('loc_6D1D')

    MapJump((0xDD, 'c3000'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D2D(): pass

    label('loc_6D2D')

    MapJump((0xDD, 'c3010'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D3D(): pass

    label('loc_6D3D')

    MapJump((0xDD, 'c3020'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D4D(): pass

    label('loc_6D4D')

    MapJump((0xDD, 'c3030'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D5D(): pass

    label('loc_6D5D')

    MapJump((0xDD, 'c3200'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D6D(): pass

    label('loc_6D6D')

    MapJump((0xDD, 'c3210'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D7D(): pass

    label('loc_6D7D')

    MapJump((0xDD, 'c3220'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D8D(): pass

    label('loc_6D8D')

    MapJump((0xDD, 'c3230'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6D9D(): pass

    label('loc_6D9D')

    MapJump((0xDD, 'c3410'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6DAD(): pass

    label('loc_6DAD')

    MapJump((0xDD, 'c3420'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6DBD(): pass

    label('loc_6DBD')

    MapJump((0xDD, 'c3600'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6DCD(): pass

    label('loc_6DCD')

    MapJump((0xDD, 'c3610'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6DDD(): pass

    label('loc_6DDD')

    MapJump((0xDD, 'c3620'), (0xDD, ''), 0x00)

    Jump('loc_6E09')

    def _loc_6DED(): pass

    label('loc_6DED')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6E09')

    def _loc_6DFB(): pass

    label('loc_6DFB')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_6E09')

    def _loc_6E09(): pass

    label('loc_6E09')

    Jump('loc_DB27')

    def _loc_6E0E(): pass

    label('loc_6E0E')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c2600：[ヴェスタ通り]', 0x0001EC30)
    MenuAddItem(1, 'c2610：宿酒場《フォレスタ》', 0x0001EC94)
    MenuAddItem(1, 'c2620：ベーカリー《ラフィット》', 0x0001ECF8)
    MenuAddItem(1, 'c2630：《ハーシェル雑貨店》', 0x0001ED5C)
    MenuAddItem(1, 'c2640：遊撃士協会・帝都西支部', 0x0001EDC0)
    MenuAddItem(1, 'c2650：アパルトメント《ホリーフラット》', 0x0001EE24)
    MenuAddItem(1, 'c2660：民家', 0x0001EE88)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c2800：[ライカ地区]', 0x0001F400)
    MenuAddItem(1, 'c2810：美術喫茶《ルシアン》', 0x0001F464)
    MenuAddItem(1, 'c2820：《レイクロード社》', 0x0001F4C8)
    MenuAddItem(1, 'c2830：《リーヴェルト社》', 0x0001F52C)
    MenuAddItem(1, 'c2840：ヴァンダール流練武場', 0x0001F590)
    MenuAddItem(1, 'c2850：帝國博物館', 0x0001F5F4)
    MenuAddItem(1, 'c2860：民家', 0x0001F658)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c3000：[サンクト地区]', 0x0001FBD0)
    MenuAddItem(1, 'c3010：ヘイムダル大聖堂', 0x0001FC34)
    MenuAddItem(1, 'c3020：《ホテル・ヴァラール》', 0x0001FC98)
    MenuAddItem(1, 'c3030：聖アストライア女学院', 0x0001FCFC)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0001D4C0, 'loc_72D9'),
        (0x0001D524, 'loc_72E9'),
        (0x0001D588, 'loc_72F9'),
        (0x0001DC90, 'loc_7309'),
        (0x0001DCF4, 'loc_7319'),
        (0x0001DD58, 'loc_7329'),
        (0x0001DDBC, 'loc_7339'),
        (0x0001DE20, 'loc_7349'),
        (0x0001DE84, 'loc_7359'),
        (0x0001E460, 'loc_7369'),
        (0x0001E4C4, 'loc_7379'),
        (0x0001E528, 'loc_7389'),
        (0x0001E58C, 'loc_7399'),
        (0x0001E5F0, 'loc_73A9'),
        (0x0001EC30, 'loc_73B9'),
        (0x0001EC94, 'loc_73C9'),
        (0x0001ECF8, 'loc_73D9'),
        (0x0001ED5C, 'loc_73E9'),
        (0x0001EDC0, 'loc_73F9'),
        (0x0001EE24, 'loc_7409'),
        (0x0001EE88, 'loc_7419'),
        (0x0001F400, 'loc_7429'),
        (0x0001F464, 'loc_7439'),
        (0x0001F4C8, 'loc_7449'),
        (0x0001F52C, 'loc_7459'),
        (0x0001F590, 'loc_7469'),
        (0x0001F5F4, 'loc_7479'),
        (0x0001F658, 'loc_7489'),
        (0x0001FBD0, 'loc_7499'),
        (0x0001FC34, 'loc_74A9'),
        (0x0001FC98, 'loc_74B9'),
        (0x0001FCFC, 'loc_74C9'),
        (0x000203A0, 'loc_74D9'),
        (0x00020404, 'loc_74E9'),
        (0x00020468, 'loc_74F9'),
        (0x000204CC, 'loc_7509'),
        (0x00020BD4, 'loc_7519'),
        (0x00020C38, 'loc_7529'),
        (0x00021340, 'loc_7539'),
        (0x000213A4, 'loc_7549'),
        (0x00021408, 'loc_7559'),
        (0x00000060, 'loc_7569'),
        (-1, 'loc_7577'),
    )

    def _loc_72D9(): pass

    label('loc_72D9')

    MapJump((0xDD, 'c2000'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_72E9(): pass

    label('loc_72E9')

    MapJump((0xDD, 'c2010'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_72F9(): pass

    label('loc_72F9')

    MapJump((0xDD, 'c2020'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7309(): pass

    label('loc_7309')

    MapJump((0xDD, 'c2200'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7319(): pass

    label('loc_7319')

    MapJump((0xDD, 'c2210'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7329(): pass

    label('loc_7329')

    MapJump((0xDD, 'c2220'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7339(): pass

    label('loc_7339')

    MapJump((0xDD, 'c2230'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7349(): pass

    label('loc_7349')

    MapJump((0xDD, 'c2240'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7359(): pass

    label('loc_7359')

    MapJump((0xDD, 'c2250'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7369(): pass

    label('loc_7369')

    MapJump((0xDD, 'c2400'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7379(): pass

    label('loc_7379')

    MapJump((0xDD, 'c2410'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7389(): pass

    label('loc_7389')

    MapJump((0xDD, 'c2420'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7399(): pass

    label('loc_7399')

    MapJump((0xDD, 'c2430'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73A9(): pass

    label('loc_73A9')

    MapJump((0xDD, 'c2440'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73B9(): pass

    label('loc_73B9')

    MapJump((0xDD, 'c2600'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73C9(): pass

    label('loc_73C9')

    MapJump((0xDD, 'c2610'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73D9(): pass

    label('loc_73D9')

    MapJump((0xDD, 'c2620'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73E9(): pass

    label('loc_73E9')

    MapJump((0xDD, 'c2630'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_73F9(): pass

    label('loc_73F9')

    MapJump((0xDD, 'c2640'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7409(): pass

    label('loc_7409')

    MapJump((0xDD, 'c2650'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7419(): pass

    label('loc_7419')

    MapJump((0xDD, 'c2660'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7429(): pass

    label('loc_7429')

    MapJump((0xDD, 'c2800'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7439(): pass

    label('loc_7439')

    MapJump((0xDD, 'c2810'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7449(): pass

    label('loc_7449')

    MapJump((0xDD, 'c2820'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7459(): pass

    label('loc_7459')

    MapJump((0xDD, 'c2830'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7469(): pass

    label('loc_7469')

    MapJump((0xDD, 'c2840'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7479(): pass

    label('loc_7479')

    MapJump((0xDD, 'c2850'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7489(): pass

    label('loc_7489')

    MapJump((0xDD, 'c2860'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7499(): pass

    label('loc_7499')

    MapJump((0xDD, 'c3000'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74A9(): pass

    label('loc_74A9')

    MapJump((0xDD, 'c3010'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74B9(): pass

    label('loc_74B9')

    MapJump((0xDD, 'c3020'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74C9(): pass

    label('loc_74C9')

    MapJump((0xDD, 'c3030'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74D9(): pass

    label('loc_74D9')

    MapJump((0xDD, 'c3200'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74E9(): pass

    label('loc_74E9')

    MapJump((0xDD, 'c3210'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_74F9(): pass

    label('loc_74F9')

    MapJump((0xDD, 'c3220'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7509(): pass

    label('loc_7509')

    MapJump((0xDD, 'c3230'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7519(): pass

    label('loc_7519')

    MapJump((0xDD, 'c3410'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7529(): pass

    label('loc_7529')

    MapJump((0xDD, 'c3420'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7539(): pass

    label('loc_7539')

    MapJump((0xDD, 'c3600'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7549(): pass

    label('loc_7549')

    MapJump((0xDD, 'c3610'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7559(): pass

    label('loc_7559')

    MapJump((0xDD, 'c3620'), (0xDD, ''), 0x00)

    Jump('loc_7585')

    def _loc_7569(): pass

    label('loc_7569')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7585')

    def _loc_7577(): pass

    label('loc_7577')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7585')

    def _loc_7585(): pass

    label('loc_7585')

    Jump('loc_DB27')

    def _loc_758A(): pass

    label('loc_758A')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'c3200：[帝都競馬場]', 0x000203A0)
    MenuAddItem(1, 'c3210：帝都競馬場・構内', 0x00020404)
    MenuAddItem(1, 'c3220：帝都競馬場・廊下', 0x00020468)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c3410：ヘイムダル空港ターミナル', 0x00020BD4)
    MenuAddItem(1, 'c3420：[ヘイムダル空港デッキ]', 0x00020C38)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'c3600：[カレル離宮]', 0x00021340)
    MenuAddItem(1, 'c3610：[カレル離宮・大伽藍]', 0x000213A4)
    MenuAddItem(1, 'c3620：カレル離宮内部', 0x00021408)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0001D4C0, 'loc_78AF'),
        (0x0001D524, 'loc_78BF'),
        (0x0001D588, 'loc_78CF'),
        (0x0001DC90, 'loc_78DF'),
        (0x0001DCF4, 'loc_78EF'),
        (0x0001DD58, 'loc_78FF'),
        (0x0001DDBC, 'loc_790F'),
        (0x0001DE20, 'loc_791F'),
        (0x0001DE84, 'loc_792F'),
        (0x0001E460, 'loc_793F'),
        (0x0001E4C4, 'loc_794F'),
        (0x0001E528, 'loc_795F'),
        (0x0001E58C, 'loc_796F'),
        (0x0001E5F0, 'loc_797F'),
        (0x0001EC30, 'loc_798F'),
        (0x0001EC94, 'loc_799F'),
        (0x0001ECF8, 'loc_79AF'),
        (0x0001ED5C, 'loc_79BF'),
        (0x0001EDC0, 'loc_79CF'),
        (0x0001EE24, 'loc_79DF'),
        (0x0001EE88, 'loc_79EF'),
        (0x0001F400, 'loc_79FF'),
        (0x0001F464, 'loc_7A0F'),
        (0x0001F4C8, 'loc_7A1F'),
        (0x0001F52C, 'loc_7A2F'),
        (0x0001F590, 'loc_7A3F'),
        (0x0001F5F4, 'loc_7A4F'),
        (0x0001F658, 'loc_7A5F'),
        (0x0001FBD0, 'loc_7A6F'),
        (0x0001FC34, 'loc_7A7F'),
        (0x0001FC98, 'loc_7A8F'),
        (0x0001FCFC, 'loc_7A9F'),
        (0x000203A0, 'loc_7AAF'),
        (0x00020404, 'loc_7ABF'),
        (0x00020468, 'loc_7ACF'),
        (0x000204CC, 'loc_7ADF'),
        (0x00020BD4, 'loc_7AEF'),
        (0x00020C38, 'loc_7AFF'),
        (0x00021340, 'loc_7B0F'),
        (0x000213A4, 'loc_7B1F'),
        (0x00021408, 'loc_7B2F'),
        (0x00000060, 'loc_7B3F'),
        (-1, 'loc_7B4D'),
    )

    def _loc_78AF(): pass

    label('loc_78AF')

    MapJump((0xDD, 'c2000'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_78BF(): pass

    label('loc_78BF')

    MapJump((0xDD, 'c2010'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_78CF(): pass

    label('loc_78CF')

    MapJump((0xDD, 'c2020'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_78DF(): pass

    label('loc_78DF')

    MapJump((0xDD, 'c2200'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_78EF(): pass

    label('loc_78EF')

    MapJump((0xDD, 'c2210'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_78FF(): pass

    label('loc_78FF')

    MapJump((0xDD, 'c2220'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_790F(): pass

    label('loc_790F')

    MapJump((0xDD, 'c2230'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_791F(): pass

    label('loc_791F')

    MapJump((0xDD, 'c2240'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_792F(): pass

    label('loc_792F')

    MapJump((0xDD, 'c2250'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_793F(): pass

    label('loc_793F')

    MapJump((0xDD, 'c2400'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_794F(): pass

    label('loc_794F')

    MapJump((0xDD, 'c2410'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_795F(): pass

    label('loc_795F')

    MapJump((0xDD, 'c2420'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_796F(): pass

    label('loc_796F')

    MapJump((0xDD, 'c2430'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_797F(): pass

    label('loc_797F')

    MapJump((0xDD, 'c2440'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_798F(): pass

    label('loc_798F')

    MapJump((0xDD, 'c2600'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_799F(): pass

    label('loc_799F')

    MapJump((0xDD, 'c2610'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79AF(): pass

    label('loc_79AF')

    MapJump((0xDD, 'c2620'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79BF(): pass

    label('loc_79BF')

    MapJump((0xDD, 'c2630'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79CF(): pass

    label('loc_79CF')

    MapJump((0xDD, 'c2640'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79DF(): pass

    label('loc_79DF')

    MapJump((0xDD, 'c2650'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79EF(): pass

    label('loc_79EF')

    MapJump((0xDD, 'c2660'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_79FF(): pass

    label('loc_79FF')

    MapJump((0xDD, 'c2800'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A0F(): pass

    label('loc_7A0F')

    MapJump((0xDD, 'c2810'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A1F(): pass

    label('loc_7A1F')

    MapJump((0xDD, 'c2820'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A2F(): pass

    label('loc_7A2F')

    MapJump((0xDD, 'c2830'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A3F(): pass

    label('loc_7A3F')

    MapJump((0xDD, 'c2840'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A4F(): pass

    label('loc_7A4F')

    MapJump((0xDD, 'c2850'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A5F(): pass

    label('loc_7A5F')

    MapJump((0xDD, 'c2860'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A6F(): pass

    label('loc_7A6F')

    MapJump((0xDD, 'c3000'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A7F(): pass

    label('loc_7A7F')

    MapJump((0xDD, 'c3010'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A8F(): pass

    label('loc_7A8F')

    MapJump((0xDD, 'c3020'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7A9F(): pass

    label('loc_7A9F')

    MapJump((0xDD, 'c3030'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7AAF(): pass

    label('loc_7AAF')

    MapJump((0xDD, 'c3200'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7ABF(): pass

    label('loc_7ABF')

    MapJump((0xDD, 'c3210'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7ACF(): pass

    label('loc_7ACF')

    MapJump((0xDD, 'c3220'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7ADF(): pass

    label('loc_7ADF')

    MapJump((0xDD, 'c3230'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7AEF(): pass

    label('loc_7AEF')

    MapJump((0xDD, 'c3410'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7AFF(): pass

    label('loc_7AFF')

    MapJump((0xDD, 'c3420'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7B0F(): pass

    label('loc_7B0F')

    MapJump((0xDD, 'c3600'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7B1F(): pass

    label('loc_7B1F')

    MapJump((0xDD, 'c3610'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7B2F(): pass

    label('loc_7B2F')

    MapJump((0xDD, 'c3620'), (0xDD, ''), 0x00)

    Jump('loc_7B5B')

    def _loc_7B3F(): pass

    label('loc_7B3F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7B5B')

    def _loc_7B4D(): pass

    label('loc_7B4D')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7B5B')

    def _loc_7B5B(): pass

    label('loc_7B5B')

    Jump('loc_DB27')

    def _loc_7B60(): pass

    label('loc_7B60')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f0000：[ドレックノール要塞]', 0x000927C0)
    MenuAddItem(1, 'm7000：ドレックノール要塞・内部①（1F・2F）', 0x00072BF0)
    MenuAddItem(1, 'm7010：ドレックノール要塞・内部②（3F）', 0x00072C54)
    MenuAddItem(1, 'm7020：ドレックノール要塞・内部③（司令室）', 0x00072CB8)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000927C0, 'loc_7CA9'),
        (0x00092824, 'loc_7CB9'),
        (0x00072BF0, 'loc_7CC9'),
        (0x00072C54, 'loc_7CD9'),
        (0x00072CB8, 'loc_7CE9'),
        (0x00000060, 'loc_7CF9'),
        (-1, 'loc_7D07'),
    )

    def _loc_7CA9(): pass

    label('loc_7CA9')

    MapJump((0xDD, 'f0000'), (0xDD, ''), 0x00)

    Jump('loc_7D15')

    def _loc_7CB9(): pass

    label('loc_7CB9')

    MapJump((0xDD, 'f0010'), (0xDD, ''), 0x00)

    Jump('loc_7D15')

    def _loc_7CC9(): pass

    label('loc_7CC9')

    MapJump((0xDD, 'm7000'), (0xDD, ''), 0x00)

    Jump('loc_7D15')

    def _loc_7CD9(): pass

    label('loc_7CD9')

    MapJump((0xDD, 'm7010'), (0xDD, ''), 0x00)

    Jump('loc_7D15')

    def _loc_7CE9(): pass

    label('loc_7CE9')

    MapJump((0xDD, 'm7020'), (0xDD, ''), 0x00)

    Jump('loc_7D15')

    def _loc_7CF9(): pass

    label('loc_7CF9')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7D15')

    def _loc_7D07(): pass

    label('loc_7D07')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7D15')

    def _loc_7D15(): pass

    label('loc_7D15')

    Jump('loc_DB27')

    def _loc_7D1A(): pass

    label('loc_7D1A')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f1000：[ジュノー海上要塞]', 0x00094ED0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00094ED0, 'loc_7DCF'),
        (0x00094F34, 'loc_7DDF'),
        (0x00068FB0, 'loc_7DF7'),
        (0x00069014, 'loc_7E12'),
        (0x00069078, 'loc_7E2D'),
        (0x000690DC, 'loc_7E48'),
        (0x00069140, 'loc_7E63'),
        (0x000691A4, 'loc_7E7E'),
        (0x00069208, 'loc_7E99'),
        (0x0006926C, 'loc_7EB4'),
        (0x000692D0, 'loc_7ECF'),
        (0x00069334, 'loc_7EEA'),
        (0x00000060, 'loc_7F05'),
        (-1, 'loc_7F13'),
    )

    def _loc_7DCF(): pass

    label('loc_7DCF')

    MapJump((0xDD, 'f1000'), (0xDD, ''), 0x00)

    Jump('loc_7F21')

    def _loc_7DDF(): pass

    label('loc_7DDF')

    MapJump((0xDD, 'f1010'), (0xDD, 'go_f1000'), 0x00)

    Jump('loc_7F21')

    def _loc_7DF7(): pass

    label('loc_7DF7')

    MapJump((0xDD, 'm3000'), (0xDD, 'go_f1000_a0'), 0x00)

    Jump('loc_7F21')

    def _loc_7E12(): pass

    label('loc_7E12')

    MapJump((0xDD, 'm3010'), (0xDD, 'go_m3000_a1'), 0x00)

    Jump('loc_7F21')

    def _loc_7E2D(): pass

    label('loc_7E2D')

    MapJump((0xDD, 'm3040'), (0xDD, 'go_m3010_a2'), 0x00)

    Jump('loc_7F21')

    def _loc_7E48(): pass

    label('loc_7E48')

    MapJump((0xDD, 'm3020'), (0xDD, 'go_m3040_a3'), 0x00)

    Jump('loc_7F21')

    def _loc_7E63(): pass

    label('loc_7E63')

    MapJump((0xDD, 'm3050'), (0xDD, 'go_m3020_a2'), 0x00)

    Jump('loc_7F21')

    def _loc_7E7E(): pass

    label('loc_7E7E')

    MapJump((0xDD, 'm3000'), (0xDD, 'go_f1000_b0'), 0x00)

    Jump('loc_7F21')

    def _loc_7E99(): pass

    label('loc_7E99')

    MapJump((0xDD, 'm3010'), (0xDD, 'go_m3000_b1'), 0x00)

    Jump('loc_7F21')

    def _loc_7EB4(): pass

    label('loc_7EB4')

    MapJump((0xDD, 'm3040'), (0xDD, 'go_m3010_b2'), 0x00)

    Jump('loc_7F21')

    def _loc_7ECF(): pass

    label('loc_7ECF')

    MapJump((0xDD, 'm3030'), (0xDD, 'go_m3040_b3'), 0x00)

    Jump('loc_7F21')

    def _loc_7EEA(): pass

    label('loc_7EEA')

    MapJump((0xDD, 'm3050'), (0xDD, 'go_m3030_b0'), 0x00)

    Jump('loc_7F21')

    def _loc_7F05(): pass

    label('loc_7F05')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7F21')

    def _loc_7F13(): pass

    label('loc_7F13')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7F21')

    def _loc_7F21(): pass

    label('loc_7F21')

    Jump('loc_DB27')

    def _loc_7F26(): pass

    label('loc_7F26')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f2000：[ヒンメル霊園]', 0x000975E0)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000975E0, 'loc_7F7D'),
        (0x00000060, 'loc_7F8D'),
        (-1, 'loc_7F9B'),
    )

    def _loc_7F7D(): pass

    label('loc_7F7D')

    MapJump((0xDD, 'f2000'), (0xDD, ''), 0x00)

    Jump('loc_7FA9')

    def _loc_7F8D(): pass

    label('loc_7F8D')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7FA9')

    def _loc_7F9B(): pass

    label('loc_7F9B')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_7FA9')

    def _loc_7FA9(): pass

    label('loc_7FA9')

    Jump('loc_DB27')

    def _loc_7FAE(): pass

    label('loc_7FAE')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f3000：[聖ウルスラ医科大学]', 0x00099CF0)
    MenuAddItem(1, 'f3010：ロビー＋病室', 0x00099D54)
    MenuAddItem(1, 'f3020：宿舎', 0x00099DB8)
    MenuAddItem(1, 'f3030：皇帝の病室', 0x00099E1C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00099CF0, 'loc_807D'),
        (0x00099D54, 'loc_808D'),
        (0x00099DB8, 'loc_809D'),
        (0x00099E1C, 'loc_80AD'),
        (0x00000060, 'loc_80BD'),
        (-1, 'loc_80CB'),
    )

    def _loc_807D(): pass

    label('loc_807D')

    MapJump((0xDD, 'f3000'), (0xDD, ''), 0x00)

    Jump('loc_80D9')

    def _loc_808D(): pass

    label('loc_808D')

    MapJump((0xDD, 'f3010'), (0xDD, ''), 0x00)

    Jump('loc_80D9')

    def _loc_809D(): pass

    label('loc_809D')

    MapJump((0xDD, 'f3020'), (0xDD, ''), 0x00)

    Jump('loc_80D9')

    def _loc_80AD(): pass

    label('loc_80AD')

    MapJump((0xDD, 'f3030'), (0xDD, ''), 0x00)

    Jump('loc_80D9')

    def _loc_80BD(): pass

    label('loc_80BD')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_80D9')

    def _loc_80CB(): pass

    label('loc_80CB')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_80D9')

    def _loc_80D9(): pass

    label('loc_80D9')

    Jump('loc_DB27')

    def _loc_80DE(): pass

    label('loc_80DE')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f4000：[ミシュラム・波止場]', 0x0009C400)
    MenuAddItem(1, 'f4010：アーケード１階', 0x0009C464)
    MenuAddItem(1, 'f4020：アーケード２階', 0x0009C4C8)
    MenuAddItem(1, 'f4030：土産・宝飾《サンドリヨン》', 0x0009C52C)
    MenuAddItem(1, 'f4040：ブティック《コルセリカ》', 0x0009C590)
    MenuAddItem(1, 'f4050：レストラン《フォルトゥナ》', 0x0009C5F4)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'f4200：[ミシュラム・ビーチ＋街道接続]', 0x0009CBD0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'f4400：[ミシュラム・中央広場]', 0x0009D3A0)
    MenuAddItem(1, 'f4420：占い館・エントランス', 0x0009D468)
    MenuAddItem(1, 'f4430：占い館・廊下', 0x0009D4CC)
    MenuAddItem(1, 'f4440：占い館・占い所', 0x0009D530)
    MenuAddItem(1, 'f4460：コースター・ルート', 0x0009D5F8)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'f4600：[ミシュラム・観覧車前＋休憩所]', 0x0009DB70)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0009C400, 'loc_8481'),
        (0x0009C464, 'loc_8491'),
        (0x0009C4C8, 'loc_84A1'),
        (0x0009C52C, 'loc_84B1'),
        (0x0009C590, 'loc_84C1'),
        (0x0009C5F4, 'loc_84D1'),
        (0x0009CBD0, 'loc_84E1'),
        (0x0009D3A0, 'loc_84F1'),
        (0x0009D404, 'loc_8501'),
        (0x0009D468, 'loc_8511'),
        (0x0009D4CC, 'loc_8521'),
        (0x0009D530, 'loc_8531'),
        (0x0009D594, 'loc_8541'),
        (0x0009D5F8, 'loc_8551'),
        (0x0009DB70, 'loc_8561'),
        (0x00000060, 'loc_8571'),
        (-1, 'loc_857F'),
    )

    def _loc_8481(): pass

    label('loc_8481')

    MapJump((0xDD, 'f4000'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8491(): pass

    label('loc_8491')

    MapJump((0xDD, 'f4010'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84A1(): pass

    label('loc_84A1')

    MapJump((0xDD, 'f4020'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84B1(): pass

    label('loc_84B1')

    MapJump((0xDD, 'f4030'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84C1(): pass

    label('loc_84C1')

    MapJump((0xDD, 'f4040'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84D1(): pass

    label('loc_84D1')

    MapJump((0xDD, 'f4050'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84E1(): pass

    label('loc_84E1')

    MapJump((0xDD, 'f4200'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_84F1(): pass

    label('loc_84F1')

    MapJump((0xDD, 'f4400'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8501(): pass

    label('loc_8501')

    MapJump((0xDD, 'f4410'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8511(): pass

    label('loc_8511')

    MapJump((0xDD, 'f4420'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8521(): pass

    label('loc_8521')

    MapJump((0xDD, 'f4430'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8531(): pass

    label('loc_8531')

    MapJump((0xDD, 'f4440'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8541(): pass

    label('loc_8541')

    MapJump((0xDD, 'f4450'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8551(): pass

    label('loc_8551')

    MapJump((0xDD, 'f4460'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8561(): pass

    label('loc_8561')

    MapJump((0xDD, 'f4600'), (0xDD, ''), 0x00)

    Jump('loc_858D')

    def _loc_8571(): pass

    label('loc_8571')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_858D')

    def _loc_857F(): pass

    label('loc_857F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_858D')

    def _loc_858D(): pass

    label('loc_858D')

    Jump('loc_DB27')

    def _loc_8592(): pass

    label('loc_8592')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f5000：[タイタス門]', 0x0009EB10)
    MenuAddItem(1, 'f5010：タイタス門内部', 0x0009EB74)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0009EB10, 'loc_8613'),
        (0x0009EB74, 'loc_8623'),
        (0x00000060, 'loc_8633'),
        (-1, 'loc_8641'),
    )

    def _loc_8613(): pass

    label('loc_8613')

    MapJump((0xDD, 'f5000'), (0xDD, ''), 0x00)

    Jump('loc_864F')

    def _loc_8623(): pass

    label('loc_8623')

    MapJump((0xDD, 'f5010'), (0xDD, ''), 0x00)

    Jump('loc_864F')

    def _loc_8633(): pass

    label('loc_8633')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_864F')

    def _loc_8641(): pass

    label('loc_8641')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_864F')

    def _loc_864F(): pass

    label('loc_864F')

    Jump('loc_DB27')

    def _loc_8654(): pass

    label('loc_8654')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'f6000：星辰の間', 0x000A1220)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000A1220, 'loc_86A3'),
        (0x00000060, 'loc_86B3'),
        (-1, 'loc_86C1'),
    )

    def _loc_86A3(): pass

    label('loc_86A3')

    MapJump((0xDD, 'f6000'), (0xDD, ''), 0x00)

    Jump('loc_86CF')

    def _loc_86B3(): pass

    label('loc_86B3')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_86CF')

    def _loc_86C1(): pass

    label('loc_86C1')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_86CF')

    def _loc_86CF(): pass

    label('loc_86CF')

    Jump('loc_DB27')

    def _loc_86D4(): pass

    label('loc_86D4')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r0000：南サザーラント街道①', 0x000493E0)
    MenuAddItem(1, 'r0010：南サザーラント街道②', 0x00049444)
    MenuAddItem(1, 'r0090：南サザーラント街道・演習地', 0x00049764)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r0200：北サザーラント街道①', 0x00049BB0)
    MenuAddItem(1, 'r0210：北サザーラント街道②', 0x00049C14)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r0400：西サザーラント街道', 0x0004A380)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r1000：アグリア旧道', 0x0004BAF0)
    MenuAddItem(1, 'r1200：パルム間道①', 0x0004C2C0)
    MenuAddItem(1, 'r1210：パルム間道②', 0x0004C324)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r1400：ハーメル廃道①', 0x0004CA90)
    MenuAddItem(1, 'r1410：ハーメル廃道②', 0x0004CAF4)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000493E0, 'loc_89F5'),
        (0x00049444, 'loc_8A05'),
        (0x00049764, 'loc_8A15'),
        (0x00049BB0, 'loc_8A25'),
        (0x00049C14, 'loc_8A35'),
        (0x0004A380, 'loc_8A45'),
        (0x0004BAF0, 'loc_8A55'),
        (0x0004C2C0, 'loc_8A65'),
        (0x0004C324, 'loc_8A75'),
        (0x0004CA90, 'loc_8A85'),
        (0x0004CAF4, 'loc_8A95'),
        (0x00000060, 'loc_8AA5'),
        (-1, 'loc_8AB3'),
    )

    def _loc_89F5(): pass

    label('loc_89F5')

    MapJump((0xDD, 'r0000'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A05(): pass

    label('loc_8A05')

    MapJump((0xDD, 'r0010'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A15(): pass

    label('loc_8A15')

    MapJump((0xDD, 'r0090'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A25(): pass

    label('loc_8A25')

    MapJump((0xDD, 'r0200'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A35(): pass

    label('loc_8A35')

    MapJump((0xDD, 'r0210'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A45(): pass

    label('loc_8A45')

    MapJump((0xDD, 'r0400'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A55(): pass

    label('loc_8A55')

    MapJump((0xDD, 'r1000'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A65(): pass

    label('loc_8A65')

    MapJump((0xDD, 'r1200'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A75(): pass

    label('loc_8A75')

    MapJump((0xDD, 'r1210'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A85(): pass

    label('loc_8A85')

    MapJump((0xDD, 'r1400'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8A95(): pass

    label('loc_8A95')

    MapJump((0xDD, 'r1410'), (0xDD, ''), 0x00)

    Jump('loc_8AC1')

    def _loc_8AA5(): pass

    label('loc_8AA5')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8AC1')

    def _loc_8AB3(): pass

    label('loc_8AB3')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8AC1')

    def _loc_8AC1(): pass

    label('loc_8AC1')

    Jump('loc_DB27')

    def _loc_8AC6(): pass

    label('loc_8AC6')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r2200：ウルスラ間道①', 0x0004E9D0)
    MenuAddItem(1, 'r2210：ウルスラ間道②', 0x0004EA34)
    MenuAddItem(1, 'r2220：ウルスラ間道③', 0x0004EA98)
    MenuAddItem(1, 'r2290：ウルスラ間道・演習地', 0x0004ED54)
    MenuAddItem(1, 'f3000：[聖ウルスラ医科大学]', 0x00099CF0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r2400：東クロスベル街道①', 0x0004F1A0)
    MenuAddItem(1, 'r2410：東クロスベル街道②', 0x0004F204)
    MenuAddItem(1, 'r2420：東クロスベル街道③', 0x0004F268)
    MenuAddItem(1, 'r2430：ボート小屋内部', 0x0004F2CC)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r2600：エルム湖湿地帯①', 0x0004F970)
    MenuAddItem(1, 'r2610：エルム湖湿地帯②', 0x0004F9D4)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r2800：タングラム丘陵', 0x00050140)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0004E200, 'loc_8DDD'),
        (0x0004E9D0, 'loc_8DED'),
        (0x0004EA34, 'loc_8DFD'),
        (0x0004EA98, 'loc_8E0D'),
        (0x0004ED54, 'loc_8E1D'),
        (0x00099CF0, 'loc_8E2D'),
        (0x0004F1A0, 'loc_8E3D'),
        (0x0004F204, 'loc_8E4D'),
        (0x0004F268, 'loc_8E5D'),
        (0x0004F2CC, 'loc_8E6D'),
        (0x0004F970, 'loc_8E7D'),
        (0x0004F9D4, 'loc_8E8D'),
        (0x00050140, 'loc_8E9D'),
        (0x00000060, 'loc_8EAD'),
        (-1, 'loc_8EBB'),
    )

    def _loc_8DDD(): pass

    label('loc_8DDD')

    MapJump((0xDD, 'r2000'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8DED(): pass

    label('loc_8DED')

    MapJump((0xDD, 'r2200'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8DFD(): pass

    label('loc_8DFD')

    MapJump((0xDD, 'r2210'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E0D(): pass

    label('loc_8E0D')

    MapJump((0xDD, 'r2220'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E1D(): pass

    label('loc_8E1D')

    MapJump((0xDD, 'r2290'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E2D(): pass

    label('loc_8E2D')

    MapJump((0xDD, 'f3000'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E3D(): pass

    label('loc_8E3D')

    MapJump((0xDD, 'r2400'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E4D(): pass

    label('loc_8E4D')

    MapJump((0xDD, 'r2410'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E5D(): pass

    label('loc_8E5D')

    MapJump((0xDD, 'r2420'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E6D(): pass

    label('loc_8E6D')

    MapJump((0xDD, 'r2430'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E7D(): pass

    label('loc_8E7D')

    MapJump((0xDD, 'r2600'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E8D(): pass

    label('loc_8E8D')

    MapJump((0xDD, 'r2610'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8E9D(): pass

    label('loc_8E9D')

    MapJump((0xDD, 'r2800'), (0xDD, ''), 0x00)

    Jump('loc_8EC9')

    def _loc_8EAD(): pass

    label('loc_8EAD')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8EC9')

    def _loc_8EBB(): pass

    label('loc_8EBB')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_8EC9')

    def _loc_8EC9(): pass

    label('loc_8EC9')

    Jump('loc_DB27')

    def _loc_8ECE(): pass

    label('loc_8ECE')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r3000：西ラマール街道①', 0x00050910)
    MenuAddItem(1, 'r3010：西ラマール街道②', 0x00050974)
    MenuAddItem(1, 'r3090：西ラマール街道・演習地', 0x00050C94)
    MenuAddItem(1, 'f1000：[ジュノー海上要塞]', 0x00094ED0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r3200：アウロス海岸道', 0x000510E0)
    MenuAddItem(1, 'r3210：アウロス海岸道②', 0x00051144)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r3400：西ラングドック峡谷道', 0x000518B0)
    MenuAddItem(1, 'r3410：ロック＝パティオ', 0x00051914)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r3420：北ラングドック峡谷道①', 0x00051978)
    MenuAddItem(1, 'r3450：北ラングドック峡谷道②', 0x00051AA4)
    MenuAddItem(1, 'r3430：ラングドック峡谷・北部', 0x000519DC)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r3500：ミルサンテ間道②（ラクウェルの東）', 0x00051C98)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r3600：ブリオニア島', 0x00052080)
    MenuAddItem(1, 'r3690：ブリオニア島・管理室', 0x00052404)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00050910, 'loc_92EE'),
        (0x00050974, 'loc_92FE'),
        (0x00050C94, 'loc_930E'),
        (0x000510E0, 'loc_931E'),
        (0x00051144, 'loc_932E'),
        (0x000518B0, 'loc_933E'),
        (0x00051914, 'loc_934E'),
        (0x00051978, 'loc_935E'),
        (0x00051AA4, 'loc_936E'),
        (0x000519DC, 'loc_937E'),
        (0x00051A40, 'loc_938E'),
        (0x00051C98, 'loc_939E'),
        (0x00052080, 'loc_93AE'),
        (0x00052404, 'loc_93BE'),
        (0x00094ED0, 'loc_93CE'),
        (0x00000060, 'loc_93DE'),
        (-1, 'loc_93EC'),
    )

    def _loc_92EE(): pass

    label('loc_92EE')

    MapJump((0xDD, 'r3000'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_92FE(): pass

    label('loc_92FE')

    MapJump((0xDD, 'r3010'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_930E(): pass

    label('loc_930E')

    MapJump((0xDD, 'r3090'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_931E(): pass

    label('loc_931E')

    MapJump((0xDD, 'r3200'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_932E(): pass

    label('loc_932E')

    MapJump((0xDD, 'r3210'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_933E(): pass

    label('loc_933E')

    MapJump((0xDD, 'r3400'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_934E(): pass

    label('loc_934E')

    MapJump((0xDD, 'r3410'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_935E(): pass

    label('loc_935E')

    MapJump((0xDD, 'r3420'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_936E(): pass

    label('loc_936E')

    MapJump((0xDD, 'r3450'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_937E(): pass

    label('loc_937E')

    MapJump((0xDD, 'r3430'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_938E(): pass

    label('loc_938E')

    MapJump((0xDD, 'r3440'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_939E(): pass

    label('loc_939E')

    MapJump((0xDD, 'r3500'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_93AE(): pass

    label('loc_93AE')

    MapJump((0xDD, 'r3600'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_93BE(): pass

    label('loc_93BE')

    MapJump((0xDD, 'r3690'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_93CE(): pass

    label('loc_93CE')

    MapJump((0xDD, 'f1000'), (0xDD, ''), 0x00)

    Jump('loc_93FA')

    def _loc_93DE(): pass

    label('loc_93DE')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_93FA')

    def _loc_93EC(): pass

    label('loc_93EC')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_93FA')

    def _loc_93FA(): pass

    label('loc_93FA')

    Jump('loc_DB27')

    def _loc_93FF(): pass

    label('loc_93FF')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r4290：南オスティア街道・演習地', 0x00053B74)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r4600：脇道～リーヴス', 0x00054790)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r5000：ミルサンテ間道①', 0x00055730)
    MenuAddItem(1, 'r3500：ミルサンテ間道②', 0x00051C98)
    MenuAddItem(1, 'r5200：ガラ湖周遊～脇道', 0x00055F00)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r6000：エイボン丘陵', 0x00057E40)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00053020, 'loc_9604'),
        (0x000537F0, 'loc_9614'),
        (0x00053B74, 'loc_9624'),
        (0x00053FC0, 'loc_9634'),
        (0x00054790, 'loc_9644'),
        (0x00055730, 'loc_9654'),
        (0x00051C98, 'loc_9664'),
        (0x00055F00, 'loc_9674'),
        (0x00057E40, 'loc_9684'),
        (0x00000060, 'loc_9694'),
        (-1, 'loc_96A2'),
    )

    def _loc_9604(): pass

    label('loc_9604')

    MapJump((0xDD, 'r4000'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9614(): pass

    label('loc_9614')

    MapJump((0xDD, 'r4200'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9624(): pass

    label('loc_9624')

    MapJump((0xDD, 'r4290'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9634(): pass

    label('loc_9634')

    MapJump((0xDD, 'r4400'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9644(): pass

    label('loc_9644')

    MapJump((0xDD, 'r4600'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9654(): pass

    label('loc_9654')

    MapJump((0xDD, 'r5000'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9664(): pass

    label('loc_9664')

    MapJump((0xDD, 'r3500'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9674(): pass

    label('loc_9674')

    MapJump((0xDD, 'r5200'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9684(): pass

    label('loc_9684')

    MapJump((0xDD, 'r6000'), (0xDD, ''), 0x00)

    Jump('loc_96B0')

    def _loc_9694(): pass

    label('loc_9694')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_96B0')

    def _loc_96A2(): pass

    label('loc_96A2')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_96B0')

    def _loc_96B0(): pass

    label('loc_96B0')

    Jump('loc_DB27')

    def _loc_96B5(): pass

    label('loc_96B5')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r7000：ラマール旧道①', 0x0005A550)
    MenuAddItem(1, 'r7010：ラマール旧道②', 0x0005A5B4)
    MenuAddItem(1, 'r7020：休憩ロッジ', 0x0005A618)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'r8000：オスギリアス盆地', 0x0005CC60)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0005A550, 'loc_97C6'),
        (0x0005A5B4, 'loc_97D6'),
        (0x0005A618, 'loc_97E6'),
        (0x0005CC60, 'loc_97F6'),
        (0x00000060, 'loc_9806'),
        (-1, 'loc_9814'),
    )

    def _loc_97C6(): pass

    label('loc_97C6')

    MapJump((0xDD, 'r7000'), (0xDD, ''), 0x00)

    Jump('loc_9822')

    def _loc_97D6(): pass

    label('loc_97D6')

    MapJump((0xDD, 'r7010'), (0xDD, ''), 0x00)

    Jump('loc_9822')

    def _loc_97E6(): pass

    label('loc_97E6')

    MapJump((0xDD, 'r7020'), (0xDD, ''), 0x00)

    Jump('loc_9822')

    def _loc_97F6(): pass

    label('loc_97F6')

    MapJump((0xDD, 'r8000'), (0xDD, ''), 0x00)

    Jump('loc_9822')

    def _loc_9806(): pass

    label('loc_9806')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_9822')

    def _loc_9814(): pass

    label('loc_9814')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_9822')

    def _loc_9822(): pass

    label('loc_9822')

    Jump('loc_DB27')

    def _loc_9827(): pass

    label('loc_9827')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'r9000：ノルド北部', 0x0005F370)
    MenuAddItem(1, 'r9200：アイゼンガルド連峰③', 0x0005FB40)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0005F370, 'loc_98AF'),
        (0x0005FB40, 'loc_98BF'),
        (0x00000060, 'loc_98CF'),
        (-1, 'loc_98DD'),
    )

    def _loc_98AF(): pass

    label('loc_98AF')

    MapJump((0xDD, 'r9000'), (0xDD, ''), 0x00)

    Jump('loc_98EB')

    def _loc_98BF(): pass

    label('loc_98BF')

    MapJump((0xDD, 'r9200'), (0xDD, ''), 0x00)

    Jump('loc_98EB')

    def _loc_98CF(): pass

    label('loc_98CF')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_98EB')

    def _loc_98DD(): pass

    label('loc_98DD')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_98EB')

    def _loc_98EB(): pass

    label('loc_98EB')

    Jump('loc_DB27')

    def _loc_98F0(): pass

    label('loc_98F0')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 't0400：[アインヘル小要塞]', 0x00031CE0)
    MenuAddItem(1, 't0410：１階フロア', 0x00031D44)
    MenuAddItem(1, 'm0500：アインヘル小要塞・Ｘ層①', 0x00062E08)
    MenuAddItem(1, 'm0510：アインヘル小要塞・Ｘ層②', 0x00062E6C)
    MenuAddItem(1, 'm0590：アインヘル小要塞・Ｘ層ボスマップ', 0x0006318C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00031CE0, 'loc_9ADC'),
        (0x00031D44, 'loc_9AEC'),
        (0x00061A80, 'loc_9AFC'),
        (0x00061A8A, 'loc_9B0C'),
        (0x00061E04, 'loc_9B1C'),
        (0x00061E0E, 'loc_9B2C'),
        (0x00061E68, 'loc_9B3C'),
        (0x000621EC, 'loc_9B4C'),
        (0x00062250, 'loc_9B5C'),
        (0x000625D4, 'loc_9B6C'),
        (0x00062638, 'loc_9B7C'),
        (0x0006269C, 'loc_9B8C'),
        (0x000629BC, 'loc_9B9C'),
        (0x00062A20, 'loc_9BAC'),
        (0x00062A84, 'loc_9BBC'),
        (0x00062DA4, 'loc_9BCC'),
        (0x00062188, 'loc_9BDC'),
        (0x000621F6, 'loc_9BEC'),
        (0x00062570, 'loc_9BFC'),
        (0x000625DE, 'loc_9C0C'),
        (0x00062958, 'loc_9C1C'),
        (0x000629C6, 'loc_9C2C'),
        (0x00062D40, 'loc_9C3C'),
        (0x00062DAE, 'loc_9C4C'),
        (0x00062E08, 'loc_9C5C'),
        (0x00062E6C, 'loc_9C6C'),
        (0x0006318C, 'loc_9C7C'),
        (-1, 'loc_9C8C'),
    )

    def _loc_9ADC(): pass

    label('loc_9ADC')

    MapJump((0xDD, 't0400'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9AEC(): pass

    label('loc_9AEC')

    MapJump((0xDD, 't0410'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9AFC(): pass

    label('loc_9AFC')

    MapJump((0xDD, 'm0000'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B0C(): pass

    label('loc_9B0C')

    MapJump((0xDD, 'm0001'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B1C(): pass

    label('loc_9B1C')

    MapJump((0xDD, 'm0090'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B2C(): pass

    label('loc_9B2C')

    MapJump((0xDD, 'm0091'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B3C(): pass

    label('loc_9B3C')

    MapJump((0xDD, 'm0100'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B4C(): pass

    label('loc_9B4C')

    MapJump((0xDD, 'm0190'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B5C(): pass

    label('loc_9B5C')

    MapJump((0xDD, 'm0200'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B6C(): pass

    label('loc_9B6C')

    MapJump((0xDD, 'm0290'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B7C(): pass

    label('loc_9B7C')

    MapJump((0xDD, 'm0300'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B8C(): pass

    label('loc_9B8C')

    MapJump((0xDD, 'm0310'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9B9C(): pass

    label('loc_9B9C')

    MapJump((0xDD, 'm0390'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BAC(): pass

    label('loc_9BAC')

    MapJump((0xDD, 'm0400'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BBC(): pass

    label('loc_9BBC')

    MapJump((0xDD, 'm0410'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BCC(): pass

    label('loc_9BCC')

    MapJump((0xDD, 'm0490'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BDC(): pass

    label('loc_9BDC')

    MapJump((0xDD, 'm0180'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BEC(): pass

    label('loc_9BEC')

    MapJump((0xDD, 'm0191'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9BFC(): pass

    label('loc_9BFC')

    MapJump((0xDD, 'm0280'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C0C(): pass

    label('loc_9C0C')

    MapJump((0xDD, 'm0291'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C1C(): pass

    label('loc_9C1C')

    MapJump((0xDD, 'm0380'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C2C(): pass

    label('loc_9C2C')

    MapJump((0xDD, 'm0391'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C3C(): pass

    label('loc_9C3C')

    MapJump((0xDD, 'm0480'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C4C(): pass

    label('loc_9C4C')

    MapJump((0xDD, 'm0491'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C5C(): pass

    label('loc_9C5C')

    MapJump((0xDD, 'm0500'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C6C(): pass

    label('loc_9C6C')

    MapJump((0xDD, 'm0510'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C7C(): pass

    label('loc_9C7C')

    MapJump((0xDD, 'm0590'), (0xDD, ''), 0x00)

    Jump('loc_9C9A')

    def _loc_9C8C(): pass

    label('loc_9C8C')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_9C9A')

    def _loc_9C9A(): pass

    label('loc_9C9A')

    Jump('loc_DB27')

    def _loc_9C9F(): pass

    label('loc_9C9F')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm0600：イストミア大森林', 0x000631F0)
    MenuAddItem(1, 'm0610：魔の森Ａ', 0x00063254)
    MenuAddItem(1, 'm0620：魔の森Ｂ', 0x000632B8)
    MenuAddItem(1, 'm0630：魔の森Ｃ', 0x0006331C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000631F0, 'loc_9D5E'),
        (0x00063254, 'loc_9D6E'),
        (0x000632B8, 'loc_9D7E'),
        (0x0006331C, 'loc_9D8E'),
        (-1, 'loc_9D9E'),
    )

    def _loc_9D5E(): pass

    label('loc_9D5E')

    MapJump((0xDD, 'm0600'), (0xDD, ''), 0x00)

    Jump('loc_9DAC')

    def _loc_9D6E(): pass

    label('loc_9D6E')

    MapJump((0xDD, 'm0610'), (0xDD, ''), 0x00)

    Jump('loc_9DAC')

    def _loc_9D7E(): pass

    label('loc_9D7E')

    MapJump((0xDD, 'm0620'), (0xDD, ''), 0x00)

    Jump('loc_9DAC')

    def _loc_9D8E(): pass

    label('loc_9D8E')

    MapJump((0xDD, 'm0630'), (0xDD, ''), 0x00)

    Jump('loc_9DAC')

    def _loc_9D9E(): pass

    label('loc_9D9E')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_9DAC')

    def _loc_9DAC(): pass

    label('loc_9DAC')

    Jump('loc_DB27')

    def _loc_9DB1(): pass

    label('loc_9DB1')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm1090：ジオフロントＡＦジャンクション', 0x00064514)
    MenuAddItem(1, 'm1000：ジオフロントＦ区画①', 0x00064190)
    MenuAddItem(1, 'm1010：ジオフロントＦ区画②', 0x000641F4)
    MenuAddItem(1, 'm1020：ジオフロントＦ区画③', 0x00064258)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm1300：ジオフロントＸ区画①', 0x00064D48)
    MenuAddItem(1, 'm1310：ジオフロントＸ区画②', 0x00064DAC)
    MenuAddItem(1, 'm1320：ジオフロントＸ区画・ループマップ', 0x00064E10)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00064190, 'loc_9FB4'),
        (0x000641F4, 'loc_9FC4'),
        (0x00064258, 'loc_9FD4'),
        (0x00064514, 'loc_9FE4'),
        (0x00064960, 'loc_9FF4'),
        (0x000649C4, 'loc_A004'),
        (0x00064D48, 'loc_A014'),
        (0x00064DAC, 'loc_A024'),
        (0x00064E10, 'loc_A034'),
        (-1, 'loc_A044'),
    )

    def _loc_9FB4(): pass

    label('loc_9FB4')

    MapJump((0xDD, 'm1000'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_9FC4(): pass

    label('loc_9FC4')

    MapJump((0xDD, 'm1010'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_9FD4(): pass

    label('loc_9FD4')

    MapJump((0xDD, 'm1020'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_9FE4(): pass

    label('loc_9FE4')

    MapJump((0xDD, 'm1090'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_9FF4(): pass

    label('loc_9FF4')

    MapJump((0xDD, 'm1200'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_A004(): pass

    label('loc_A004')

    MapJump((0xDD, 'm1210'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_A014(): pass

    label('loc_A014')

    MapJump((0xDD, 'm1300'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_A024(): pass

    label('loc_A024')

    MapJump((0xDD, 'm1310'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_A034(): pass

    label('loc_A034')

    MapJump((0xDD, 'm1320'), (0xDD, ''), 0x00)

    Jump('loc_A052')

    def _loc_A044(): pass

    label('loc_A044')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A052')

    def _loc_A052(): pass

    label('loc_A052')

    Jump('loc_DB27')

    def _loc_A057(): pass

    label('loc_A057')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm1200：ジオフロントＢ区画／ＳⅡエリア①', 0x00064960)
    MenuAddItem(1, 'm1210：ジオフロントＢ区画／ＳⅡエリア②', 0x000649C4)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00064960, 'loc_A10A'),
        (0x000649C4, 'loc_A11A'),
        (-1, 'loc_A12A'),
    )

    def _loc_A10A(): pass

    label('loc_A10A')

    MapJump((0xDD, 'm1200'), (0xDD, ''), 0x00)

    Jump('loc_A138')

    def _loc_A11A(): pass

    label('loc_A11A')

    MapJump((0xDD, 'm1210'), (0xDD, ''), 0x00)

    Jump('loc_A138')

    def _loc_A12A(): pass

    label('loc_A12A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A138')

    def _loc_A138(): pass

    label('loc_A138')

    Jump('loc_DB27')

    def _loc_A13D(): pass

    label('loc_A13D')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm1490：星見の塔・外観', 0x000654B4)
    MenuAddItem(1, 'm1400：星見の塔①・入口', 0x00065130)
    MenuAddItem(1, 'm1410：星見の塔②・攻略①', 0x00065194)
    MenuAddItem(1, 'm1420：星見の塔③・外周', 0x000651F8)
    MenuAddItem(1, 'm1430：星見の塔④・攻略②前半', 0x0006525C)
    MenuAddItem(1, 'm1420：星見の塔③・外周', 0x000651F9)
    MenuAddItem(1, 'm1430：星見の塔④・攻略②後半', 0x0006525D)
    MenuAddItem(1, 'm1420：星見の塔③・ボスエリア', 0x000651FA)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00065130, 'loc_A303'),
        (0x00065194, 'loc_A313'),
        (0x000651F8, 'loc_A323'),
        (0x0006525C, 'loc_A333'),
        (0x000651F9, 'loc_A343'),
        (0x0006525D, 'loc_A35D'),
        (0x000651FA, 'loc_A377'),
        (0x000652C0, 'loc_A391'),
        (0x000654B4, 'loc_A3A1'),
        (-1, 'loc_A3B1'),
    )

    def _loc_A303(): pass

    label('loc_A303')

    MapJump((0xDD, 'm1400'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A313(): pass

    label('loc_A313')

    MapJump((0xDD, 'm1410'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A323(): pass

    label('loc_A323')

    MapJump((0xDD, 'm1420'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A333(): pass

    label('loc_A333')

    MapJump((0xDD, 'm1430'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A343(): pass

    label('loc_A343')

    MapJump((0xDD, 'm1420'), (0xDD, 'go_m1430_2'), 0x00)

    Jump('loc_A3BF')

    def _loc_A35D(): pass

    label('loc_A35D')

    MapJump((0xDD, 'm1430'), (0xDD, 'go_m1420_3'), 0x00)

    Jump('loc_A3BF')

    def _loc_A377(): pass

    label('loc_A377')

    MapJump((0xDD, 'm1420'), (0xDD, 'go_m1430_4'), 0x00)

    Jump('loc_A3BF')

    def _loc_A391(): pass

    label('loc_A391')

    MapJump((0xDD, 'm1440'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A3A1(): pass

    label('loc_A3A1')

    MapJump((0xDD, 'm1490'), (0xDD, ''), 0x00)

    Jump('loc_A3BF')

    def _loc_A3B1(): pass

    label('loc_A3B1')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A3BF')

    def _loc_A3BF(): pass

    label('loc_A3BF')

    Jump('loc_DB27')

    def _loc_A3C4(): pass

    label('loc_A3C4')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm2010：陽霊窟・祭壇', 0x00066904)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm2200：龍霊窟', 0x00067070)
    MenuAddItem(1, 'm2210：龍霊窟・祭壇', 0x000670D4)
    MenuAddItem(1, 'm2250：龍の霊場', 0x00067264)
    MenuAddItem(1, 'm2260：龍の霊場・祭壇', 0x000672C8)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm2410：月霊窟・祭壇', 0x000678A4)
    MenuAddItem(1, 'm2450：月の霊場', 0x00067A34)
    MenuAddItem(1, 'm2460：月の霊場・祭壇', 0x00067A98)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm2600：星霊窟', 0x00068010)
    MenuAddItem(1, 'm2610：星霊窟・祭壇', 0x00068074)
    MenuAddItem(1, 'm2650：星の霊場', 0x00068204)
    MenuAddItem(1, 'm2660：星の霊場・祭壇', 0x00068268)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm2810：聖霊窟・祭壇', 0x00068844)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000668A0, 'loc_A6DA'),
        (0x00066904, 'loc_A6EA'),
        (0x00067070, 'loc_A6FA'),
        (0x000670D4, 'loc_A70A'),
        (0x00067264, 'loc_A71A'),
        (0x000672C8, 'loc_A72A'),
        (0x00067840, 'loc_A73A'),
        (0x000678A4, 'loc_A74A'),
        (0x00067A34, 'loc_A75A'),
        (0x00067A98, 'loc_A76A'),
        (0x00068010, 'loc_A77A'),
        (0x00068074, 'loc_A78A'),
        (0x00068204, 'loc_A79A'),
        (0x00068268, 'loc_A7AA'),
        (0x00068844, 'loc_A7BA'),
        (0x00000060, 'loc_A7CA'),
        (-1, 'loc_A7D8'),
    )

    def _loc_A6DA(): pass

    label('loc_A6DA')

    MapJump((0xDD, 'm2000'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A6EA(): pass

    label('loc_A6EA')

    MapJump((0xDD, 'm2010'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A6FA(): pass

    label('loc_A6FA')

    MapJump((0xDD, 'm2200'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A70A(): pass

    label('loc_A70A')

    MapJump((0xDD, 'm2210'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A71A(): pass

    label('loc_A71A')

    MapJump((0xDD, 'm2250'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A72A(): pass

    label('loc_A72A')

    MapJump((0xDD, 'm2260'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A73A(): pass

    label('loc_A73A')

    MapJump((0xDD, 'm2400'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A74A(): pass

    label('loc_A74A')

    MapJump((0xDD, 'm2410'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A75A(): pass

    label('loc_A75A')

    MapJump((0xDD, 'm2450'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A76A(): pass

    label('loc_A76A')

    MapJump((0xDD, 'm2460'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A77A(): pass

    label('loc_A77A')

    MapJump((0xDD, 'm2600'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A78A(): pass

    label('loc_A78A')

    MapJump((0xDD, 'm2610'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A79A(): pass

    label('loc_A79A')

    MapJump((0xDD, 'm2650'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A7AA(): pass

    label('loc_A7AA')

    MapJump((0xDD, 'm2660'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A7BA(): pass

    label('loc_A7BA')

    MapJump((0xDD, 'm2810'), (0xDD, ''), 0x00)

    Jump('loc_A7E6')

    def _loc_A7CA(): pass

    label('loc_A7CA')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7E6')

    def _loc_A7D8(): pass

    label('loc_A7D8')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_A7E6')

    def _loc_A7E6(): pass

    label('loc_A7E6')

    Jump('loc_DB27')

    def _loc_A7EB(): pass

    label('loc_A7EB')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm3000：海上要塞・主ルート①', 0x00068FB0)
    MenuAddItem(1, 'm3010：海上要塞・主ルート②', 0x00069014)
    MenuAddItem(1, 'm3040：海上要塞・主ルートジャンクション', 0x00069078)
    MenuAddItem(1, 'm3020：海上要塞・主ルート①Ｂ', 0x000690DC)
    MenuAddItem(1, 'm3050：海上要塞・主ルート天守閣屋上', 0x00069140)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm3000：海上要塞・副ルート①', 0x000691A4)
    MenuAddItem(1, 'm3030：海上要塞・副ルート②', 0x00069208)
    MenuAddItem(1, 'm3040：海上要塞・副ルートジャンクション', 0x0006926C)
    MenuAddItem(1, 'm3030：海上要塞・副ルート②Ｂ', 0x000692D0)
    MenuAddItem(1, 'm3050：海上要塞・副ルート天守閣屋上', 0x00069334)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00068FB0, 'loc_AAA9'),
        (0x00069014, 'loc_AAC4'),
        (0x00069078, 'loc_AADF'),
        (0x000690DC, 'loc_AAFA'),
        (0x00069140, 'loc_AB15'),
        (0x000691A4, 'loc_AB30'),
        (0x00069208, 'loc_AB4B'),
        (0x0006926C, 'loc_AB66'),
        (0x000692D0, 'loc_AB81'),
        (0x00069334, 'loc_AB9C'),
        (0x00000060, 'loc_ABB7'),
        (-1, 'loc_ABC5'),
    )

    def _loc_AAA9(): pass

    label('loc_AAA9')

    MapJump((0xDD, 'm3000'), (0xDD, 'go_f1000_a0'), 0x00)

    Jump('loc_ABD3')

    def _loc_AAC4(): pass

    label('loc_AAC4')

    MapJump((0xDD, 'm3010'), (0xDD, 'go_m3000_a1'), 0x00)

    Jump('loc_ABD3')

    def _loc_AADF(): pass

    label('loc_AADF')

    MapJump((0xDD, 'm3040'), (0xDD, 'go_m3010_a2'), 0x00)

    Jump('loc_ABD3')

    def _loc_AAFA(): pass

    label('loc_AAFA')

    MapJump((0xDD, 'm3020'), (0xDD, 'go_m3040_a3'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB15(): pass

    label('loc_AB15')

    MapJump((0xDD, 'm3050'), (0xDD, 'go_m3020_a2'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB30(): pass

    label('loc_AB30')

    MapJump((0xDD, 'm3000'), (0xDD, 'go_f1000_b0'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB4B(): pass

    label('loc_AB4B')

    MapJump((0xDD, 'm3010'), (0xDD, 'go_m3000_b1'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB66(): pass

    label('loc_AB66')

    MapJump((0xDD, 'm3040'), (0xDD, 'go_m3010_b2'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB81(): pass

    label('loc_AB81')

    MapJump((0xDD, 'm3030'), (0xDD, 'go_m3040_b3'), 0x00)

    Jump('loc_ABD3')

    def _loc_AB9C(): pass

    label('loc_AB9C')

    MapJump((0xDD, 'm3050'), (0xDD, 'go_m3030_b0'), 0x00)

    Jump('loc_ABD3')

    def _loc_ABB7(): pass

    label('loc_ABB7')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_ABD3')

    def _loc_ABC5(): pass

    label('loc_ABC5')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_ABD3')

    def _loc_ABD3(): pass

    label('loc_ABD3')

    Jump('loc_DB27')

    def _loc_ABD8(): pass

    label('loc_ABD8')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm3200：帝都地下道①', 0x00069780)
    MenuAddItem(1, 'm3210：帝都地下道②', 0x000697E4)
    MenuAddItem(1, 'm3220：帝都地下・最深部', 0x00069848)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00069780, 'loc_AC7F'),
        (0x000697E4, 'loc_AC8F'),
        (0x00069848, 'loc_AC9F'),
        (-1, 'loc_ACAF'),
    )

    def _loc_AC7F(): pass

    label('loc_AC7F')

    MapJump((0xDD, 'm3200'), (0xDD, ''), 0x00)

    Jump('loc_ACBD')

    def _loc_AC8F(): pass

    label('loc_AC8F')

    MapJump((0xDD, 'm3210'), (0xDD, ''), 0x00)

    Jump('loc_ACBD')

    def _loc_AC9F(): pass

    label('loc_AC9F')

    MapJump((0xDD, 'm3220'), (0xDD, ''), 0x00)

    Jump('loc_ACBD')

    def _loc_ACAF(): pass

    label('loc_ACAF')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_ACBD')

    def _loc_ACBD(): pass

    label('loc_ACBD')

    Jump('loc_DB27')

    def _loc_ACC2(): pass

    label('loc_ACC2')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm3400：帝都地下墓所・変化', 0x00069F50)
    MenuAddItem(1, 'm3410：帝都地下墓所・通常', 0x00069FB4)
    MenuAddItem(1, 'm3420：暗黒竜の寝所・入口', 0x0006A018)
    MenuAddItem(1, 'm3430：暗黒竜の寝所①', 0x0006A07C)
    MenuAddItem(1, 'm3440：暗黒竜の寝所②', 0x0006A0E0)
    MenuAddItem(1, 'm3450：暗黒竜の寝所③', 0x0006A144)
    MenuAddItem(1, 'm3490：暗黒竜の寝所・最奥', 0x0006A2D4)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00069F50, 'loc_AE40'),
        (0x00069FB4, 'loc_AE50'),
        (0x0006A018, 'loc_AE60'),
        (0x0006A07C, 'loc_AE70'),
        (0x0006A0E0, 'loc_AE80'),
        (0x0006A144, 'loc_AE90'),
        (0x0006A1A8, 'loc_AEA0'),
        (0x0006A2D4, 'loc_AEB0'),
        (-1, 'loc_AEC0'),
    )

    def _loc_AE40(): pass

    label('loc_AE40')

    MapJump((0xDD, 'm3400'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AE50(): pass

    label('loc_AE50')

    MapJump((0xDD, 'm3410'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AE60(): pass

    label('loc_AE60')

    MapJump((0xDD, 'm3420'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AE70(): pass

    label('loc_AE70')

    MapJump((0xDD, 'm3430'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AE80(): pass

    label('loc_AE80')

    MapJump((0xDD, 'm3440'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AE90(): pass

    label('loc_AE90')

    MapJump((0xDD, 'm3450'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AEA0(): pass

    label('loc_AEA0')

    MapJump((0xDD, 'm3460'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AEB0(): pass

    label('loc_AEB0')

    MapJump((0xDD, 'm3490'), (0xDD, ''), 0x00)

    Jump('loc_AECE')

    def _loc_AEC0(): pass

    label('loc_AEC0')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_AECE')

    def _loc_AECE(): pass

    label('loc_AECE')

    Jump('loc_DB27')

    def _loc_AED3(): pass

    label('loc_AED3')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm4004：黒キ星杯・始まりの地(ラスボスマップのみ)', 0x0006B6E8)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0006B6C0, 'loc_AFC1'),
        (0x0006B6CA, 'loc_AFD1'),
        (0x0006B6D4, 'loc_AFEC'),
        (0x0006B6DE, 'loc_B007'),
        (0x0006B6E8, 'loc_B022'),
        (0x0006B6F2, 'loc_B03D'),
        (0x0006B724, 'loc_B04D'),
        (0x0006B72E, 'loc_B05D'),
        (0x0006B788, 'loc_B06D'),
        (0x0006B792, 'loc_B07D'),
        (0x0006B79C, 'loc_B08D'),
        (0x0006B7EC, 'loc_B09D'),
        (0x0006B7F6, 'loc_B0AD'),
        (0x0006B800, 'loc_B0BD'),
        (0x0006B850, 'loc_B0CD'),
        (0x0006B85A, 'loc_B0DD'),
        (-1, 'loc_B0ED'),
    )

    def _loc_AFC1(): pass

    label('loc_AFC1')

    MapJump((0xDD, 'm4000'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_AFD1(): pass

    label('loc_AFD1')

    MapJump((0xDD, 'm4001'), (0xDD, 'go_m4011_01'), 0x00)

    Jump('loc_B0FB')

    def _loc_AFEC(): pass

    label('loc_AFEC')

    MapJump((0xDD, 'm4002'), (0xDD, 'go_m4022_01'), 0x00)

    Jump('loc_B0FB')

    def _loc_B007(): pass

    label('loc_B007')

    MapJump((0xDD, 'm4003'), (0xDD, 'go_m4032_01'), 0x00)

    Jump('loc_B0FB')

    def _loc_B022(): pass

    label('loc_B022')

    MapJump((0xDD, 'm4004'), (0xDD, 'go_m4041_01'), 0x00)

    Jump('loc_B0FB')

    def _loc_B03D(): pass

    label('loc_B03D')

    MapJump((0xDD, 'm4005'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B04D(): pass

    label('loc_B04D')

    MapJump((0xDD, 'm4010'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B05D(): pass

    label('loc_B05D')

    MapJump((0xDD, 'm4011'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B06D(): pass

    label('loc_B06D')

    MapJump((0xDD, 'm4020'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B07D(): pass

    label('loc_B07D')

    MapJump((0xDD, 'm4021'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B08D(): pass

    label('loc_B08D')

    MapJump((0xDD, 'm4022'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B09D(): pass

    label('loc_B09D')

    MapJump((0xDD, 'm4030'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B0AD(): pass

    label('loc_B0AD')

    MapJump((0xDD, 'm4031'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B0BD(): pass

    label('loc_B0BD')

    MapJump((0xDD, 'm4032'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B0CD(): pass

    label('loc_B0CD')

    MapJump((0xDD, 'm4040'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B0DD(): pass

    label('loc_B0DD')

    MapJump((0xDD, 'm4041'), (0xDD, ''), 0x00)

    Jump('loc_B0FB')

    def _loc_B0ED(): pass

    label('loc_B0ED')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B0FB')

    def _loc_B0FB(): pass

    label('loc_B0FB')

    Jump('loc_DB27')

    def _loc_B100(): pass

    label('loc_B100')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm5000：オルキス魔導区：エレベータ内', 0x0006DDD0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm5011：オルキス魔導区：下層・外郭／序章', 0x0006DE3E)
    MenuAddItem(1, 'm5051：オルキス魔導区：下層・中枢／序章', 0x0006DFCE)
    MenuAddItem(1, 'm5071：オルキス魔導区：上層・中枢／序章', 0x0006E096)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm5010：オルキス魔導区：下層・外郭／Ⅲ部', 0x0006DE34)
    MenuAddItem(1, 'm5050：オルキス魔導区：下層・中枢／Ⅲ部', 0x0006DFC4)
    MenuAddItem(1, 'm5020：オルキス魔導区：中層・外郭／Ⅲ部', 0x0006DE98)
    MenuAddItem(1, 'm5060：オルキス魔導区：中層・中枢／Ⅲ部', 0x0006E028)
    MenuAddItem(1, 'm5070：オルキス魔導区：上層・中枢／Ⅲ部', 0x0006E08C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0006DDD0, 'loc_B41F'),
        (0x0006DE3E, 'loc_B42F'),
        (0x0006DFCE, 'loc_B43F'),
        (0x0006E096, 'loc_B44F'),
        (0x0006DE34, 'loc_B45F'),
        (0x0006DE98, 'loc_B46F'),
        (0x0006DEFC, 'loc_B47F'),
        (0x0006DFC4, 'loc_B48F'),
        (0x0006E028, 'loc_B49F'),
        (0x0006E08C, 'loc_B4AF'),
        (0x00000060, 'loc_B4BF'),
        (-1, 'loc_B4CD'),
    )

    def _loc_B41F(): pass

    label('loc_B41F')

    MapJump((0xDD, 'm5000'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B42F(): pass

    label('loc_B42F')

    MapJump((0xDD, 'm5011'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B43F(): pass

    label('loc_B43F')

    MapJump((0xDD, 'm5051'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B44F(): pass

    label('loc_B44F')

    MapJump((0xDD, 'm5071'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B45F(): pass

    label('loc_B45F')

    MapJump((0xDD, 'm5010'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B46F(): pass

    label('loc_B46F')

    MapJump((0xDD, 'm5020'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B47F(): pass

    label('loc_B47F')

    MapJump((0xDD, 'm5030'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B48F(): pass

    label('loc_B48F')

    MapJump((0xDD, 'm5050'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B49F(): pass

    label('loc_B49F')

    MapJump((0xDD, 'm5060'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B4AF(): pass

    label('loc_B4AF')

    MapJump((0xDD, 'm5070'), (0xDD, ''), 0x00)

    Jump('loc_B4DB')

    def _loc_B4BF(): pass

    label('loc_B4BF')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B4DB')

    def _loc_B4CD(): pass

    label('loc_B4CD')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B4DB')

    def _loc_B4DB(): pass

    label('loc_B4DB')

    Jump('loc_DB27')

    def _loc_B4E0(): pass

    label('loc_B4E0')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm5500：サングラール迷宮・入口', 0x0006F158)
    MenuAddItem(1, 'm5510：サングラール迷宮・第一相', 0x0006F1BC)
    MenuAddItem(1, 'm5520：サングラール迷宮・第一相最奥', 0x0006F220)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm5540：サングラール迷宮・第二相', 0x0006F2E8)
    MenuAddItem(1, 'm5550：サングラール迷宮・第二相最奥', 0x0006F34C)
    MenuAddItem(1, 'm5560：サングラール迷宮・第三相', 0x0006F3B0)
    MenuAddItem(1, 'm5570：サングラール迷宮・第三相最奥', 0x0006F414)
    MenuAddItem(1, 'm5580：サングラール迷宮・第四相', 0x0006F478)
    MenuAddItem(1, 'm5590：サングラール迷宮・第四相最奥', 0x0006F4DC)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0006F158, 'loc_B791'),
        (0x0006F1BC, 'loc_B7A1'),
        (0x0006F220, 'loc_B7B1'),
        (0x0006F2E8, 'loc_B7C1'),
        (0x0006F34C, 'loc_B7D1'),
        (0x0006F3B0, 'loc_B7E1'),
        (0x0006F414, 'loc_B7F1'),
        (0x0006F478, 'loc_B801'),
        (0x0006F479, 'loc_B811'),
        (0x0006F47A, 'loc_B821'),
        (0x0006F47B, 'loc_B831'),
        (0x0006F47C, 'loc_B841'),
        (0x0006F4DC, 'loc_B851'),
        (0x00000060, 'loc_B861'),
        (-1, 'loc_B86F'),
    )

    def _loc_B791(): pass

    label('loc_B791')

    MapJump((0xDD, 'm5500'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7A1(): pass

    label('loc_B7A1')

    MapJump((0xDD, 'm5510'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7B1(): pass

    label('loc_B7B1')

    MapJump((0xDD, 'm5520'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7C1(): pass

    label('loc_B7C1')

    MapJump((0xDD, 'm5540'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7D1(): pass

    label('loc_B7D1')

    MapJump((0xDD, 'm5550'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7E1(): pass

    label('loc_B7E1')

    MapJump((0xDD, 'm5560'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B7F1(): pass

    label('loc_B7F1')

    MapJump((0xDD, 'm5570'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B801(): pass

    label('loc_B801')

    MapJump((0xDD, 'm5580'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B811(): pass

    label('loc_B811')

    MapJump((0xDD, 'm5581'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B821(): pass

    label('loc_B821')

    MapJump((0xDD, 'm5582'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B831(): pass

    label('loc_B831')

    MapJump((0xDD, 'm5583'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B841(): pass

    label('loc_B841')

    MapJump((0xDD, 'm5584'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B851(): pass

    label('loc_B851')

    MapJump((0xDD, 'm5590'), (0xDD, ''), 0x00)

    Jump('loc_B87D')

    def _loc_B861(): pass

    label('loc_B861')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B87D')

    def _loc_B86F(): pass

    label('loc_B86F')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_B87D')

    def _loc_B87D(): pass

    label('loc_B87D')

    Jump('loc_DB27')

    def _loc_B882(): pass

    label('loc_B882')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm6000：黒の工房・Aルート前半', 0x000704E0)
    MenuAddItem(1, 'm6010：黒の工房・Aルート後半', 0x00070544)
    MenuAddItem(1, 'm6020：黒の工房・Bルート前半', 0x000705A8)
    MenuAddItem(1, 'm6030：黒の工房・Bルート後半', 0x0007060C)
    MenuAddItem(1, 'm6040：黒の工房・Cルート前半', 0x00070670)
    MenuAddItem(1, 'm6050：黒の工房・Cルート後半', 0x000706D4)
    MenuAddItem(1, 'm6090：黒の工房・聯絡回廊', 0x00070864)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000704E0, 'loc_BA2A'),
        (0x00070544, 'loc_BA3A'),
        (0x000705A8, 'loc_BA4A'),
        (0x0007060C, 'loc_BA5A'),
        (0x00070670, 'loc_BA6A'),
        (0x000706D4, 'loc_BA7A'),
        (0x00070864, 'loc_BA8A'),
        (0x00000060, 'loc_BA9A'),
        (-1, 'loc_BAA8'),
    )

    def _loc_BA2A(): pass

    label('loc_BA2A')

    MapJump((0xDD, 'm6000'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA3A(): pass

    label('loc_BA3A')

    MapJump((0xDD, 'm6010'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA4A(): pass

    label('loc_BA4A')

    MapJump((0xDD, 'm6020'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA5A(): pass

    label('loc_BA5A')

    MapJump((0xDD, 'm6030'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA6A(): pass

    label('loc_BA6A')

    MapJump((0xDD, 'm6040'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA7A(): pass

    label('loc_BA7A')

    MapJump((0xDD, 'm6050'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA8A(): pass

    label('loc_BA8A')

    MapJump((0xDD, 'm6090'), (0xDD, ''), 0x00)

    Jump('loc_BAB6')

    def _loc_BA9A(): pass

    label('loc_BA9A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BAB6')

    def _loc_BAA8(): pass

    label('loc_BAA8')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BAB6')

    def _loc_BAB6(): pass

    label('loc_BAB6')

    Jump('loc_DB27')

    def _loc_BABB(): pass

    label('loc_BABB')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm6500：オルディス地下水路①', 0x00071868)
    MenuAddItem(1, 'm6510：オルディス地下水路②', 0x000718CC)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00071868, 'loc_BB52'),
        (0x000718CC, 'loc_BB62'),
        (0x00000060, 'loc_BB72'),
        (-1, 'loc_BB80'),
    )

    def _loc_BB52(): pass

    label('loc_BB52')

    MapJump((0xDD, 'm6500'), (0xDD, ''), 0x00)

    Jump('loc_BB8E')

    def _loc_BB62(): pass

    label('loc_BB62')

    MapJump((0xDD, 'm6510'), (0xDD, ''), 0x00)

    Jump('loc_BB8E')

    def _loc_BB72(): pass

    label('loc_BB72')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BB8E')

    def _loc_BB80(): pass

    label('loc_BB80')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BB8E')

    def _loc_BB8E(): pass

    label('loc_BB8E')

    Jump('loc_DB27')

    def _loc_BB93(): pass

    label('loc_BB93')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm7000：ドレックノール要塞・内部①（1F・2F）', 0x00072BF0)
    MenuAddItem(1, 'm7010：ドレックノール要塞・内部②（3F）', 0x00072C54)
    MenuAddItem(1, 'm7020：ドレックノール要塞・内部③（司令室）', 0x00072CB8)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00072BF0, 'loc_BC9F'),
        (0x00072C54, 'loc_BCAF'),
        (0x00072CB8, 'loc_BCBF'),
        (0x00000060, 'loc_BCCF'),
        (-1, 'loc_BCDD'),
    )

    def _loc_BC9F(): pass

    label('loc_BC9F')

    MapJump((0xDD, 'm7000'), (0xDD, ''), 0x00)

    Jump('loc_BCEB')

    def _loc_BCAF(): pass

    label('loc_BCAF')

    MapJump((0xDD, 'm7010'), (0xDD, ''), 0x00)

    Jump('loc_BCEB')

    def _loc_BCBF(): pass

    label('loc_BCBF')

    MapJump((0xDD, 'm7020'), (0xDD, ''), 0x00)

    Jump('loc_BCEB')

    def _loc_BCCF(): pass

    label('loc_BCCF')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BCEB')

    def _loc_BCDD(): pass

    label('loc_BCDD')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BCEB')

    def _loc_BCEB(): pass

    label('loc_BCEB')

    Jump('loc_DB27')

    def _loc_BCF0(): pass

    label('loc_BCF0')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm7400：パンタグリュエル・内部①（貴賓室）', 0x00073B90)
    MenuAddItem(1, 'm7410：パンタグリュエル・内部②（攻略パート①）', 0x00073BF4)
    MenuAddItem(1, 'm7420：パンタグリュエル・内部③（攻略パート②）', 0x00073C58)
    MenuAddItem(1, 'm7430：パンタグリュエル・内部④（攻略パート・甲板）', 0x00073CBC)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00073B90, 'loc_BE68'),
        (0x00073BF4, 'loc_BE78'),
        (0x00073C58, 'loc_BE88'),
        (0x00073CBC, 'loc_BE98'),
        (0x00000060, 'loc_BEA8'),
        (-1, 'loc_BEB6'),
    )

    def _loc_BE68(): pass

    label('loc_BE68')

    MapJump((0xDD, 'm7400'), (0xDD, ''), 0x00)

    Jump('loc_BEC4')

    def _loc_BE78(): pass

    label('loc_BE78')

    MapJump((0xDD, 'm7410'), (0xDD, ''), 0x00)

    Jump('loc_BEC4')

    def _loc_BE88(): pass

    label('loc_BE88')

    MapJump((0xDD, 'm7420'), (0xDD, ''), 0x00)

    Jump('loc_BEC4')

    def _loc_BE98(): pass

    label('loc_BE98')

    MapJump((0xDD, 'm7430'), (0xDD, ''), 0x00)

    Jump('loc_BEC4')

    def _loc_BEA8(): pass

    label('loc_BEA8')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BEC4')

    def _loc_BEB6(): pass

    label('loc_BEB6')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_BEC4')

    def _loc_BEC4(): pass

    label('loc_BEC4')

    Jump('loc_DB27')

    def _loc_BEC9(): pass

    label('loc_BEC9')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm7600：ガルガンチュア級飛行要塞・内部①（船倉）', 0x00074360)
    MenuAddItem(1, 'm7610：ガルガンチュア級飛行要塞・内部②（通路）', 0x000743C4)
    MenuAddItem(1, 'm7620：ガルガンチュア級飛行要塞・内部③（中枢）', 0x00074428)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00074360, 'loc_BFF0'),
        (0x000743C4, 'loc_C000'),
        (0x00074428, 'loc_C010'),
        (0x00000060, 'loc_C020'),
        (-1, 'loc_C02E'),
    )

    def _loc_BFF0(): pass

    label('loc_BFF0')

    MapJump((0xDD, 'm7600'), (0xDD, ''), 0x00)

    Jump('loc_C03C')

    def _loc_C000(): pass

    label('loc_C000')

    MapJump((0xDD, 'm7610'), (0xDD, ''), 0x00)

    Jump('loc_C03C')

    def _loc_C010(): pass

    label('loc_C010')

    MapJump((0xDD, 'm7620'), (0xDD, ''), 0x00)

    Jump('loc_C03C')

    def _loc_C020(): pass

    label('loc_C020')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C03C')

    def _loc_C02E(): pass

    label('loc_C02E')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C03C')

    def _loc_C03C(): pass

    label('loc_C03C')

    Jump('loc_DB27')

    def _loc_C041(): pass

    label('loc_C041')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm8000：忘却の白き杭Ａ（エステルチーム用）', 0x00075300)
    MenuAddItem(1, 'm8010：忘却の白き杭Ａ・最奥', 0x00075364)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm8100：忘却の白き杭Ｂ（ロイドチーム用）', 0x000756E8)
    MenuAddItem(1, 'm8110：忘却の白き杭Ｂ・最奥', 0x0007574C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm8200：忘却の白き杭Ｃ（アンゼリカチーム用）', 0x00075AD0)
    MenuAddItem(1, 'm8210：忘却の白き杭Ｃ・最奥', 0x00075B34)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm8300：忘却の白き杭Ｄ（デュバリィチーム用）', 0x00075EB8)
    MenuAddItem(1, 'm8310：忘却の白き杭Ｄ・最奥', 0x00075F1C)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm8400：忘却の白き杭Ｅ（オーレリアチーム用）', 0x000762A0)
    MenuAddItem(1, 'm8410：忘却の白き杭Ｅ・最奥', 0x00076304)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00075300, 'loc_C3CB'),
        (0x00075364, 'loc_C3DB'),
        (0x000756E8, 'loc_C3EB'),
        (0x0007574C, 'loc_C3FB'),
        (0x00075AD0, 'loc_C40B'),
        (0x00075B34, 'loc_C41B'),
        (0x00075EB8, 'loc_C42B'),
        (0x00075F1C, 'loc_C43B'),
        (0x000762A0, 'loc_C44B'),
        (0x00076304, 'loc_C45B'),
        (0x00000060, 'loc_C46B'),
        (-1, 'loc_C479'),
    )

    def _loc_C3CB(): pass

    label('loc_C3CB')

    MapJump((0xDD, 'm8000'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C3DB(): pass

    label('loc_C3DB')

    MapJump((0xDD, 'm8010'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C3EB(): pass

    label('loc_C3EB')

    MapJump((0xDD, 'm8100'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C3FB(): pass

    label('loc_C3FB')

    MapJump((0xDD, 'm8110'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C40B(): pass

    label('loc_C40B')

    MapJump((0xDD, 'm8200'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C41B(): pass

    label('loc_C41B')

    MapJump((0xDD, 'm8210'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C42B(): pass

    label('loc_C42B')

    MapJump((0xDD, 'm8300'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C43B(): pass

    label('loc_C43B')

    MapJump((0xDD, 'm8310'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C44B(): pass

    label('loc_C44B')

    MapJump((0xDD, 'm8400'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C45B(): pass

    label('loc_C45B')

    MapJump((0xDD, 'm8410'), (0xDD, ''), 0x00)

    Jump('loc_C487')

    def _loc_C46B(): pass

    label('loc_C46B')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C487')

    def _loc_C479(): pass

    label('loc_C479')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_C487')

    def _loc_C487(): pass

    label('loc_C487')

    Jump('loc_DB27')

    def _loc_C48C(): pass

    label('loc_C48C')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'm9000：トゥアハ＝デ＝ダナーン・外観・入り口\x09\x09\x09', 0x00077A10)
    MenuAddItem(1, 'm9001：トゥアハ＝デ＝ダナーン・小庭園までの道\x09\x09\x09', 0x00077A1A)
    MenuAddItem(1, 'm9002：トゥアハ＝デ＝ダナーン・小庭園【非戦闘エリア】\x09', 0x00077A24)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9010：トゥアハ＝デ＝ダナーン・攻略A\x09\x09\x09\x09\x09', 0x00077A74)
    MenuAddItem(1, 'm9011：トゥアハ＝デ＝ダナーン・ボスA\x09\x09\x09\x09\x09', 0x00077A7E)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9020：トゥアハ＝デ＝ダナーン・攻略B\x09\x09\x09\x09\x09', 0x00077AD8)
    MenuAddItem(1, 'm9021：トゥアハ＝デ＝ダナーン・ボスB\x09\x09\x09\x09\x09', 0x00077AE2)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9030：トゥアハ＝デ＝ダナーン・攻略C①\x09\x09\x09\x09', 0x00077B3C)
    MenuAddItem(1, 'm9031：トゥアハ＝デ＝ダナーン・ボスC①\x09\x09\x09\x09', 0x00077B46)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9040：トゥアハ＝デ＝ダナーン・攻略C②\x09\x09\x09\x09', 0x00077BA0)
    MenuAddItem(1, 'm9041：トゥアハ＝デ＝ダナーン・ボスC②\x09\x09\x09\x09', 0x00077BAA)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9050：トゥアハ＝デ＝ダナーン・中枢区画①\x09\x09\x09\x09', 0x00077C04)
    MenuAddItem(1, 'm9051：トゥアハ＝デ＝ダナーン・中枢区画ボス①\x09\x09\x09', 0x00077C0E)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9060：トゥアハ＝デ＝ダナーン・中枢区画②\x09\x09\x09\x09', 0x00077C68)
    MenuAddItem(1, 'm9061：トゥアハ＝デ＝ダナーン・最下層ラスボス戦\x09\x09', 0x00077C72)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'm9100：トゥアハ＝デ＝ダナーン・因果律の奔流\x09\x09\x09', 0x00077DF8)
    MenuAddItem(1, 'm9101：トゥアハ＝デ＝ダナーン・真ラスボス戦\x09\x09\x09', 0x00077E02)
    MenuAddItem(1, 'm9102：トゥアハ＝デ＝ダナーン・白い闇・内部\x09\x09\x09', 0x00077E0C)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00077A10, 'loc_CBB0'),
        (0x00077A1A, 'loc_CBC0'),
        (0x00077A24, 'loc_CBD0'),
        (0x00077A74, 'loc_CBE0'),
        (0x00077A7E, 'loc_CBF0'),
        (0x00077AD8, 'loc_CC00'),
        (0x00077AE2, 'loc_CC10'),
        (0x00077B3C, 'loc_CC20'),
        (0x00077B46, 'loc_CC30'),
        (0x00077BA0, 'loc_CC40'),
        (0x00077BAA, 'loc_CC50'),
        (0x00077C04, 'loc_CC60'),
        (0x00077C0E, 'loc_CC70'),
        (0x00077C68, 'loc_CC80'),
        (0x00077C72, 'loc_CC90'),
        (0x00077DF8, 'loc_CCA0'),
        (0x00077E02, 'loc_CCB0'),
        (0x00077E0C, 'loc_CCC0'),
        (0x00000060, 'loc_CCD0'),
        (-1, 'loc_CCDE'),
    )

    def _loc_CBB0(): pass

    label('loc_CBB0')

    MapJump((0xDD, 'm9000'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CBC0(): pass

    label('loc_CBC0')

    MapJump((0xDD, 'm9001'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CBD0(): pass

    label('loc_CBD0')

    MapJump((0xDD, 'm9002'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CBE0(): pass

    label('loc_CBE0')

    MapJump((0xDD, 'm9010'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CBF0(): pass

    label('loc_CBF0')

    MapJump((0xDD, 'm9011'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC00(): pass

    label('loc_CC00')

    MapJump((0xDD, 'm9020'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC10(): pass

    label('loc_CC10')

    MapJump((0xDD, 'm9021'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC20(): pass

    label('loc_CC20')

    MapJump((0xDD, 'm9030'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC30(): pass

    label('loc_CC30')

    MapJump((0xDD, 'm9031'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC40(): pass

    label('loc_CC40')

    MapJump((0xDD, 'm9040'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC50(): pass

    label('loc_CC50')

    MapJump((0xDD, 'm9041'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC60(): pass

    label('loc_CC60')

    MapJump((0xDD, 'm9050'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC70(): pass

    label('loc_CC70')

    MapJump((0xDD, 'm9051'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC80(): pass

    label('loc_CC80')

    MapJump((0xDD, 'm9060'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CC90(): pass

    label('loc_CC90')

    MapJump((0xDD, 'm9061'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CCA0(): pass

    label('loc_CCA0')

    MapJump((0xDD, 'm9100'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CCB0(): pass

    label('loc_CCB0')

    MapJump((0xDD, 'm9101'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CCC0(): pass

    label('loc_CCC0')

    MapJump((0xDD, 'm9102'), (0xDD, ''), 0x00)

    Jump('loc_CCEC')

    def _loc_CCD0(): pass

    label('loc_CCD0')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CCEC')

    def _loc_CCDE(): pass

    label('loc_CCDE')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_CCEC')

    def _loc_CCEC(): pass

    label('loc_CCEC')

    Jump('loc_DB27')

    def _loc_CCF1(): pass

    label('loc_CCF1')

    MenuCreate(1, 0, 24.0, 99)
    MenuAddItem(1, 'e2000：アイゼンガルド連峰西上空', 0x0007EF40)
    MenuAddItem(1, 'e2100：汎用スカイマップ（雲＋地表）', 0x0007F328)
    MenuAddItem(1, 'e2200：汎用スカイマップ（雲）', 0x0007F710)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v3090：カレイジャスⅡ・甲板', 0x000ABA72)
    MenuAddItem(1, 'v5090：メルカバ・甲板', 0x000AC242)
    MenuAddItem(1, 'v6090：山猫号Ⅱ・甲板', 0x000AC62A)
    MenuAddItem(1, 'v7090：ガルガンチュア級・甲板', 0x000ACA12)
    MenuAddItem(1, 'v8090：パンタグリュエル・甲板', 0x000ACDFA)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0007A120, 'loc_CF8A'),
        (0x0007A184, 'loc_CF9A'),
        (0x0007A56C, 'loc_CFAA'),
        (0x0007A8F0, 'loc_CFBA'),
        (0x0007ACD8, 'loc_CFCA'),
        (0x0007B0C0, 'loc_CFDA'),
        (0x0007B4A8, 'loc_CFEA'),
        (0x0007B890, 'loc_CFFA'),
        (0x0007B8F4, 'loc_D00A'),
        (0x0007BC78, 'loc_D01A'),
        (0x0007C060, 'loc_D02A'),
        (0x0007C448, 'loc_D03A'),
        (0x0007C830, 'loc_D04A'),
        (0x0007CC18, 'loc_D05A'),
        (0x0007D000, 'loc_D06A'),
        (0x0007D3E8, 'loc_D07A'),
        (0x0007EF40, 'loc_D08A'),
        (0x0007F328, 'loc_D09A'),
        (0x0007F710, 'loc_D0AA'),
        (0x000ABA72, 'loc_D0BA'),
        (0x000AC242, 'loc_D0CA'),
        (0x000AC62A, 'loc_D0DA'),
        (0x000ACA12, 'loc_D0EA'),
        (0x000ACDFA, 'loc_D0FA'),
        (0x00000060, 'loc_D10A'),
        (-1, 'loc_D118'),
    )

    def _loc_CF8A(): pass

    label('loc_CF8A')

    MapJump((0xDD, 'e0000'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CF9A(): pass

    label('loc_CF9A')

    MapJump((0xDD, 'e0010'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFAA(): pass

    label('loc_CFAA')

    MapJump((0xDD, 'e0110'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFBA(): pass

    label('loc_CFBA')

    MapJump((0xDD, 'e0200'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFCA(): pass

    label('loc_CFCA')

    MapJump((0xDD, 'e0300'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFDA(): pass

    label('loc_CFDA')

    MapJump((0xDD, 'e0400'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFEA(): pass

    label('loc_CFEA')

    MapJump((0xDD, 'e0500'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_CFFA(): pass

    label('loc_CFFA')

    MapJump((0xDD, 'e0600'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D00A(): pass

    label('loc_D00A')

    MapJump((0xDD, 'e0610'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D01A(): pass

    label('loc_D01A')

    MapJump((0xDD, 'e0700'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D02A(): pass

    label('loc_D02A')

    MapJump((0xDD, 'e0800'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D03A(): pass

    label('loc_D03A')

    MapJump((0xDD, 'e0900'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D04A(): pass

    label('loc_D04A')

    MapJump((0xDD, 'e1000'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D05A(): pass

    label('loc_D05A')

    MapJump((0xDD, 'e1100'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D06A(): pass

    label('loc_D06A')

    MapJump((0xDD, 'e1200'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D07A(): pass

    label('loc_D07A')

    MapJump((0xDD, 'e1300'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D08A(): pass

    label('loc_D08A')

    MapJump((0xDD, 'e2000'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D09A(): pass

    label('loc_D09A')

    MapJump((0xDD, 'e2100'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0AA(): pass

    label('loc_D0AA')

    MapJump((0xDD, 'e2200'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0BA(): pass

    label('loc_D0BA')

    MapJump((0xDD, 'v3090'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0CA(): pass

    label('loc_D0CA')

    MapJump((0xDD, 'v5090'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0DA(): pass

    label('loc_D0DA')

    MapJump((0xDD, 'v6090'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0EA(): pass

    label('loc_D0EA')

    MapJump((0xDD, 'v7090'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D0FA(): pass

    label('loc_D0FA')

    MapJump((0xDD, 'v8090'), (0xDD, ''), 0x00)

    Jump('loc_D126')

    def _loc_D10A(): pass

    label('loc_D10A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D126')

    def _loc_D118(): pass

    label('loc_D118')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_D126')

    def _loc_D126(): pass

    label('loc_D126')

    Jump('loc_DB27')

    def _loc_D12B(): pass

    label('loc_D12B')

    MenuCreate(1, 20, 24.0, 99)
    MenuAddItem(1, 'v0000：デアフリンガー号１号車', 0x000AAE60)
    MenuAddItem(1, 'v0010：デアフリンガー号２号車', 0x000AAE6A)
    MenuAddItem(1, 'v0020：デアフリンガー号３号車', 0x000AAE74)
    MenuAddItem(1, 'v0030：デアフリンガー号４号車', 0x000AAE7E)
    MenuAddItem(1, 'v0040：デアフリンガー号５号車', 0x000AAE88)
    MenuAddItem(1, 'v0050：デアフリンガー号６号車', 0x000AAE92)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v2000：カレイジャス・ブリッジ', 0x000AB630)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v3090：カレイジャスⅡ・甲板', 0x000ABA72)
    MenuAddItem(1, 'v3000：カレイジャスⅡ・４Ｆ ブリッジ', 0x000ABA18)
    MenuAddItem(1, 'v3010：カレイジャスⅡ・３Ｆ 会議／貴賓／訓練', 0x000ABA22)
    MenuAddItem(1, 'v3020：カレイジャスⅡ・２Ｆ 食堂／購買／端末', 0x000ABA2C)
    MenuAddItem(1, 'v3030：カレイジャスⅡ・１Ｆ 工房／倉庫／格納庫', 0x000ABA36)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v4000：騎神コクピット', 0x000ABE00)
    MenuAddItem(1, 'v4200：機甲兵コクピット', 0x000ABEC8)
    MenuAddItem(1, 'v4210：魔煌機兵コクピット', 0x000ABED2)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v5090：メルカバ・甲板', 0x000AC242)
    MenuAddItem(1, 'v5000：メルカバ・内部', 0x000AC1E8)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v6090：山猫号Ⅱ・甲板', 0x000AC62A)
    MenuAddItem(1, 'v6000：山猫号Ⅱ・内部', 0x000AC5D0)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v7090：ガルガンチュア級・甲板', 0x000ACA12)
    MenuAddItem(1, 'v7000：ガルガンチュア級・内部', 0x000AC9B8)
    MenuAddItem(1, '━━━━━━━━━━━━━━━', 0x00000060)
    MenuAddItem(1, 'v8090：パンタグリュエル・甲板', 0x000ACDFA)
    MenuAddItem(1, 'v8000：パンタグリュエル・ブリッジ', 0x000ACDA0)
    MenuAddItem(1, 'm7400：パンタグリュエル・貴賓室(ダンジョン扱い)', 0x00073B90)
    MenuAddItem(1, 'v8010：パンタグリュエル・船倉', 0x000ACDAA)
    MenuAddItem(1, 'v8020：パンタグリュエル・饗応の間', 0x000ACDB4)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000AAE60, 'loc_D8F2'),
        (0x000AAE6A, 'loc_D902'),
        (0x000AAE74, 'loc_D912'),
        (0x000AAE7E, 'loc_D922'),
        (0x000AAE88, 'loc_D932'),
        (0x000AAE92, 'loc_D942'),
        (0x000AAF28, 'loc_D952'),
        (0x000AAFF0, 'loc_D962'),
        (0x000AB630, 'loc_D972'),
        (0x000AB63A, 'loc_D982'),
        (0x000ABA18, 'loc_D992'),
        (0x000ABA22, 'loc_D9A2'),
        (0x000ABA2C, 'loc_D9B2'),
        (0x000ABA36, 'loc_D9C2'),
        (0x000ABA18, 'loc_D9D2'),
        (0x000ABA22, 'loc_D9E3'),
        (0x000ABA2C, 'loc_D9F4'),
        (0x000ABA36, 'loc_DA05'),
        (0x000ABA72, 'loc_DA16'),
        (0x000ABE00, 'loc_DA26'),
        (0x000ABEC8, 'loc_DA36'),
        (0x000ABED2, 'loc_DA46'),
        (0x000AC1E8, 'loc_DA56'),
        (0x000AC242, 'loc_DA66'),
        (0x000AC5D0, 'loc_DA76'),
        (0x000AC62A, 'loc_DA86'),
        (0x000AC9B8, 'loc_DA96'),
        (0x00073B90, 'loc_DAA6'),
        (0x000ACA12, 'loc_DAB6'),
        (0x000ACDA0, 'loc_DAC6'),
        (0x000ACDAA, 'loc_DAD6'),
        (0x000ACDB4, 'loc_DAE6'),
        (0x000ACDFA, 'loc_DAF6'),
        (0x00000060, 'loc_DB06'),
        (-1, 'loc_DB14'),
    )

    def _loc_D8F2(): pass

    label('loc_D8F2')

    MapJump((0xDD, 'v0000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D902(): pass

    label('loc_D902')

    MapJump((0xDD, 'v0010'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D912(): pass

    label('loc_D912')

    MapJump((0xDD, 'v0020'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D922(): pass

    label('loc_D922')

    MapJump((0xDD, 'v0030'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D932(): pass

    label('loc_D932')

    MapJump((0xDD, 'v0040'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D942(): pass

    label('loc_D942')

    MapJump((0xDD, 'v0050'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D952(): pass

    label('loc_D952')

    MapJump((0xDD, 'v0200'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D962(): pass

    label('loc_D962')

    MapJump((0xDD, 'v0400'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D972(): pass

    label('loc_D972')

    MapJump((0xDD, 'v2000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D982(): pass

    label('loc_D982')

    MapJump((0xDD, 'v2010'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D992(): pass

    label('loc_D992')

    MapJump((0xDD, 'v3000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9A2(): pass

    label('loc_D9A2')

    MapJump((0xDD, 'v3010'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9B2(): pass

    label('loc_D9B2')

    MapJump((0xDD, 'v3020'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9C2(): pass

    label('loc_D9C2')

    MapJump((0xDD, 'v3030'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9D2(): pass

    label('loc_D9D2')

    MapJump((0xDD, 'a2001b'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9E3(): pass

    label('loc_D9E3')

    MapJump((0xDD, 'a2001c'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_D9F4(): pass

    label('loc_D9F4')

    MapJump((0xDD, 'a2001d'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA05(): pass

    label('loc_DA05')

    MapJump((0xDD, 'a2001e'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA16(): pass

    label('loc_DA16')

    MapJump((0xDD, 'v3090'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA26(): pass

    label('loc_DA26')

    MapJump((0xDD, 'v4000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA36(): pass

    label('loc_DA36')

    MapJump((0xDD, 'v4200'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA46(): pass

    label('loc_DA46')

    MapJump((0xDD, 'v4210'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA56(): pass

    label('loc_DA56')

    MapJump((0xDD, 'v5000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA66(): pass

    label('loc_DA66')

    MapJump((0xDD, 'v5090'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA76(): pass

    label('loc_DA76')

    MapJump((0xDD, 'v6000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA86(): pass

    label('loc_DA86')

    MapJump((0xDD, 'v6090'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DA96(): pass

    label('loc_DA96')

    MapJump((0xDD, 'v7000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAA6(): pass

    label('loc_DAA6')

    MapJump((0xDD, 'm7400'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAB6(): pass

    label('loc_DAB6')

    MapJump((0xDD, 'v7090'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAC6(): pass

    label('loc_DAC6')

    MapJump((0xDD, 'v8000'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAD6(): pass

    label('loc_DAD6')

    MapJump((0xDD, 'v8010'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAE6(): pass

    label('loc_DAE6')

    MapJump((0xDD, 'v8020'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DAF6(): pass

    label('loc_DAF6')

    MapJump((0xDD, 'v8090'), (0xDD, ''), 0x00)

    Jump('loc_DB22')

    def _loc_DB06(): pass

    label('loc_DB06')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DB22')

    def _loc_DB14(): pass

    label('loc_DB14')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_DB22')

    def _loc_DB22(): pass

    label('loc_DB22')

    Jump('loc_DB27')

    def _loc_DB27(): pass

    label('loc_DB27')

    Jump('loc_1055')

    def _loc_DB2C(): pass

    label('loc_DB2C')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x03, 1)

    Return()

# id: 0x0004 offset: 0xDB3C
@scena.Code('FC_BattleTestParty')
def FC_BattleTestParty():
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationSetLeader(ChrTable['黎恩'])
    FormationCtrl(0x08, ChrTable['黎恩'], 0.0, 0.0, 0x01)
    FormationCtrl(0x08, ChrTable['尤娜'], 2.0, 0.0, 0x01)
    FormationCtrl(0x08, ChrTable['庫爾特'], -2.0, 0.0, 0x01)
    FormationCtrl(0x08, ChrTable['亞爾緹娜'], 0.0, 2.0, 0x01)
    ModelCtrl(0x37, 0x0000, 0x00, 0x00, 0x00)
    ModelCtrl(0x37, 0x000C, 0x00, 0x01, 0x00)
    ModelCtrl(0x37, 0x000B, 0x01, 0x00, 0x00)
    ModelCtrl(0x37, 0x000E, 0x01, 0x00, 0x00)
    ModelCtrl(0x37, 0x000A, 0x01, 0x01, 0x00)
    ModelCtrl(0x37, 0x000D, 0x01, 0x01, 0x00)
    ModelCtrl(0x37, 0x0000, 0x00, 0x00, 0x01)
    ModelCtrl(0x37, 0x000C, 0x00, 0x02, 0x01)
    ModelCtrl(0x37, 0x000A, 0x01, 0x00, 0x01)
    ModelCtrl(0x37, 0x000B, 0x01, 0x01, 0x01)
    ModelCtrl(0x37, 0x000D, 0x00, 0x01, 0x01)
    ModelCtrl(0x37, 0x000E, 0x01, 0x01, 0x01)
    AddItem(0x00, 0x04B0, 1)
    AddItem(0x00, 0x04BF, 1)
    AddItem(0x00, 0x04D8, 1)
    AddItem(0x00, 0x04F1, 1)
    AddItem(0x00, 0x050A, 1)
    AddItem(0x00, 0x051E, 1)
    AddItem(0x00, 0x01F9, 3)
    AddItem(0x00, 0x01FA, 3)
    AddItem(0x00, 0x022B, 3)
    AddItem(0x00, 0x022C, 3)
    AddItem(0x00, 0x025B, 1)
    AddItem(0x00, 0x0267, 1)
    AddItem(0x00, 0x0270, 1)
    AddItem(0x00, 0x0276, 1)
    OP_70(0x00, 0x0000, 0x04B0, 0xFF, 0x00)
    OP_70(0x00, 0x0000, 0x01F9, 0xFF, 0x00)
    OP_70(0x00, 0x0000, 0x022B, 0xFF, 0x00)
    OP_70(0x00, 0x000A, 0x04BF, 0xFF, 0x00)
    OP_70(0x00, 0x000A, 0x01FA, 0xFF, 0x00)
    OP_70(0x00, 0x000A, 0x022C, 0xFF, 0x00)
    OP_70(0x00, 0x000B, 0x04D8, 0xFF, 0x00)
    OP_70(0x00, 0x000B, 0x01F9, 0xFF, 0x00)
    OP_70(0x00, 0x000B, 0x022B, 0xFF, 0x00)
    OP_70(0x00, 0x000C, 0x04F1, 0xFF, 0x00)
    OP_70(0x00, 0x000C, 0x01FA, 0xFF, 0x00)
    OP_70(0x00, 0x000C, 0x022C, 0xFF, 0x00)
    OP_70(0x00, 0x000D, 0x050A, 0xFF, 0x00)
    OP_70(0x00, 0x000D, 0x01FA, 0xFF, 0x00)
    OP_70(0x00, 0x000D, 0x022C, 0xFF, 0x00)
    OP_70(0x00, 0x000E, 0x051E, 0xFF, 0x00)
    OP_70(0x00, 0x000E, 0x01F9, 0xFF, 0x00)
    OP_70(0x00, 0x000E, 0x022B, 0xFF, 0x00)
    OP_70(0x00, 0x0000, 0x025B, 0xFF, 0x00)
    OP_70(0x00, 0x000A, 0x0267, 0xFF, 0x00)
    OP_70(0x00, 0x000B, 0x0270, 0xFF, 0x00)
    OP_70(0x00, 0x000C, 0x0276, 0xFF, 0x00)
    OP_48(0x00, 0x0000, 0x0001, 0x0014)
    OP_48(0x00, 0x000A, 0x0001, 0x0014)
    OP_48(0x00, 0x000B, 0x0001, 0x0014)
    OP_48(0x00, 0x000C, 0x0001, 0x0014)
    OP_48(0x00, 0x000D, 0x0001, 0x0014)
    OP_48(0x00, 0x000E, 0x0001, 0x0014)
    OP_70(0x06, 0xFFFF, 0x00, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x01, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x02, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x03, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x04, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x05, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x06, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x07, 0x03, 0x00, 0x01)
    OP_70(0x06, 0xFFFF, 0x08, 0x03, 0x00, 0x01)
    SetScenaFlags(ScenaFlag(0x0080, 0, 0x400))
    SetScenaFlags(ScenaFlag(0x0080, 1, 0x401))
    SetScenaFlags(ScenaFlag(0x0080, 2, 0x402))
    OP_69(0x04, 0x0007)
    OP_69(0x02, 0x0000, 0xFFFF, 0x0002)
    OP_69(0x02, 0x000A, 0xFFFF, 0x0002)
    OP_69(0x02, 0x000B, 0xFFFF, 0x0002)
    OP_69(0x02, 0x000C, 0xFFFF, 0x0002)
    OP_69(0x02, 0x000D, 0xFFFF, 0x0002)
    OP_69(0x02, 0x000E, 0xFFFF, 0x0002)
    OP_69(0x00, 0x0000, 0x000C, 0xFF, 0x00, 0x00)
    OP_69(0x00, 0x000A, 0x000B, 0xFF, 0x00, 0x00)
    OP_69(0x15, 0x0003)
    CraftCtrl(0x07, 0xFFFF)
    CraftCtrl(0x0B, ChrTable['黎恩'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['尤娜'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['庫爾特'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['亞爾緹娜'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['繆潔'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['亞修'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['亞莉莎'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['艾略特'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['勞拉'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['馬奇亞斯'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['艾瑪'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['尤西斯'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['菲'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['蓋烏斯'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['米莉亞姆'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['莎拉'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['奧蕾莉亞將軍'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['阿加特'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['安潔莉卡'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['奧利維特皇子'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['提妲'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['緹歐'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['雪倫'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['克蕾雅少校'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['雷克特少校'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['托娃'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['派崔克'], 0x00000000)
    AddItem(0x00, 0x0001, 15)
    AddItem(0x00, 0x0006, 15)
    AddItem(0x00, 0x000A, 15)
    AddItem(0x00, 0x0026, 15)
    AddItem(0x00, 0x0025, 15)
    OP_48(0x00, 0xFFFF, 0x002D, 0x0000)
    OP_48(0x00, 0xFFFF, 0x001E, 0x0000)
    OP_48(0x00, 0xFFFF, 0x0020, 0x0064)

    Return()

# id: 0x0005 offset: 0xDEEC
@scena.Code('TK_ExpressionTest')
def TK_ExpressionTest():
    OP_8C(0x03, 0x00)
    SetChrFace(0x03, 0xFFFE, '#100s', '#100s', '#100s', '#b', '0')
    OP_23(0x01, 200, 800, 0x00, 0x0A)

    Switch(
        (
            (Expr.PushVar, 0xF6),
            Expr.Return,
        ),
        (0x00000000, 'loc_DFFB'),
        (0x00000001, 'loc_E068'),
        (0x00000002, 'loc_E0D6'),
        (0x00000003, 'loc_E143'),
        (0x00000004, 'loc_E1B1'),
        (0x00000005, 'loc_E21E'),
        (0x00000006, 'loc_E28C'),
        (0x00000007, 'loc_E2F9'),
        (0x00000008, 'loc_E367'),
        (0x00000009, 'loc_E3D4'),
        (0x0000000A, 'loc_E442'),
        (0x0000000B, 'loc_E4B0'),
        (0x0000000C, 'loc_E51D'),
        (0x0000000D, 'loc_E59D'),
        (0x0000000E, 'loc_E60B'),
        (0x0000000F, 'loc_E67A'),
        (0x00000010, 'loc_E6E7'),
        (0x00000011, 'loc_E755'),
        (0x00000012, 'loc_E7C3'),
        (0x00000013, 'loc_E831'),
        (0x00000014, 'loc_E89F'),
        (0x00000015, 'loc_E90D'),
        (0x00000016, 'loc_E981'),
        (0x00000064, 'loc_E9F5'),
        (0x00000065, 'loc_EA42'),
        (0x00000066, 'loc_EA8C'),
        (0x00000067, 'loc_EAE8'),
        (0x00000384, 'loc_EB3B'),
        (-1, 'loc_EB6E'),
    )

    def _loc_DFFB(): pass

    label('loc_DFFB')

    SetChrFace(0x04, 0xFFFE, '#E_0#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E068(): pass

    label('loc_E068')

    SetChrFace(0x04, 0xFFFE, '#E[1]#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E0D6(): pass

    label('loc_E0D6')

    SetChrFace(0x04, 0xFFFE, '#E_2#M_2')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E143(): pass

    label('loc_E143')

    SetChrFace(0x04, 0xFFFE, '#E[3]#M_2')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E1B1(): pass

    label('loc_E1B1')

    SetChrFace(0x04, 0xFFFE, '#E_4#M_4')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E21E(): pass

    label('loc_E21E')

    SetChrFace(0x04, 0xFFFE, '#E[5]#M_4')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E28C(): pass

    label('loc_E28C')

    SetChrFace(0x04, 0xFFFE, '#E_6#M_2')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E2F9(): pass

    label('loc_E2F9')

    SetChrFace(0x04, 0xFFFE, '#E[7]#M_2')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E367(): pass

    label('loc_E367')

    SetChrFace(0x04, 0xFFFE, '#E_8#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E3D4(): pass

    label('loc_E3D4')

    SetChrFace(0x04, 0xFFFE, '#E[9]#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E442(): pass

    label('loc_E442')

    SetChrFace(0x04, 0xFFFE, '#E[A]#M_0')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E4B0(): pass

    label('loc_E4B0')

    SetChrFace(0x04, 0xFFFE, '#E_6#M_6')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E51D(): pass

    label('loc_E51D')

    SetChrFace(0x04, 0xFFFE, '#E[C]#M_8#B[A]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    SetChrFace(0x03, 0xFFFE, '', '', '0', '#b', '0')

    Jump('loc_EB6E')

    def _loc_E59D(): pass

    label('loc_E59D')

    SetChrFace(0x04, 0xFFFE, '#E[D]#M_C')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E60B(): pass

    label('loc_E60B')

    SetChrFace(0x04, 0xFFFE, '#E[9]#M[H]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E67A(): pass

    label('loc_E67A')

    SetChrFace(0x04, 0xFFFE, '#E_0#M_A')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E6E7(): pass

    label('loc_E6E7')

    SetChrFace(0x04, 0xFFFE, '#E_0#B[0]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E755(): pass

    label('loc_E755')

    SetChrFace(0x04, 0xFFFE, '#E_0#B[7]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E7C3(): pass

    label('loc_E7C3')

    SetChrFace(0x04, 0xFFFE, '#E_0#B[3]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E831(): pass

    label('loc_E831')

    SetChrFace(0x04, 0xFFFE, '#E_0#B[1]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E89F(): pass

    label('loc_E89F')

    SetChrFace(0x04, 0xFFFE, '#E_0#B[5]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E90D(): pass

    label('loc_E90D')

    SetChrFace(0x04, 0xFFFE, '#E[1]#e[0]#B[0]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E981(): pass

    label('loc_E981')

    SetChrFace(0x04, 0xFFFE, '#E[0]#e[1]#B[0]')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kふふ、なんだかラクロス部を\n',
            '思い出して楽しかったです。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_E9F5(): pass

    label('loc_E9F5')

    SetChrFace(0x03, 0xFFFE, '3', '13#200w0', '', '#b', '0')
    SetChrFace(0x04, 0xFFFE, '')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#K間にwaitを入れるテスト。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_EA42(): pass

    label('loc_EA42')

    SetChrFace(0x03, 0xFFFE, '0', '', '#100s1234567812345678', '#b', '0')
    SetChrFace(0x04, 0xFFFE, '')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#K通常スピード',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_EA8C(): pass

    label('loc_EA8C')

    SetChrFace(0x03, 0xFFFE, '0', '', '#200s1234567812345678', '#b', '0')
    SetChrFace(0x04, 0xFFFE, '')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#Kアニメスピードを速くする',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_EAE8(): pass

    label('loc_EAE8')

    SetChrFace(0x03, 0xFFFE, '0,1,2,3,4,0', '0,1,2,3,4,0', '0,2,3,4,5,6,7,8', '#b', '0')
    SetChrFace(0x04, 0xFFFE, '')

    ChrTalk(
        0xFFFE,
        0x00000000,
        (
            '#K補完なし',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    Jump('loc_EB6E')

    def _loc_EB3B(): pass

    label('loc_EB3B')

    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')
    DebugLog(0x02, (0xDD, 'tst'))

    Jump('loc_EB6E')

    def _loc_EB6E(): pass

    label('loc_EB6E')

    OP_63(0xFFFE, 0x00)
    OP_63(0xFFFF, 0x01)
    OP_23(0x01, 65535, 65535, 0x00, 0x0A)
    OP_8C(0x03, 0x01)

    Return()

# id: 0x0006 offset: 0xEB84
@scena.Code('SelectFlag_System')
def SelectFlag_System():
    Call(ScriptId.Current, 'BeginDebugScript')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_EBA1(): pass

    label('loc_EBA1')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F924',
    )

    MenuCreate(0, 32, 24.0, 99)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 0, 0x300)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'ゲーム開始', 0x00000000, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0060, 3, 0x303)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '２周目', 0x00000001, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0002)"),
            Expr.Return,
        ),
        'loc_EC40',
    )

    MenuAddItem(0, '■ノーマルエンド見た', 0x0000004D)

    Jump('loc_EC66')

    def _loc_EC40(): pass

    label('loc_EC40')

    MenuAddItem(0, '□ノーマルエンド見た', 0x0000004D)

    def _loc_EC66(): pass

    label('loc_EC66')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0003)"),
            Expr.Return,
        ),
        'loc_EC9C',
    )

    MenuAddItem(0, '■トゥルーエンド見た', 0x0000004E)

    Jump('loc_ECC2')

    def _loc_EC9C(): pass

    label('loc_EC9C')

    MenuAddItem(0, '□トゥルーエンド見た', 0x0000004E)

    def _loc_ECC2(): pass

    label('loc_ECC2')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0061, 6, 0x30E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'サイドカー入手', 0x00000019, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '馬乗れる', 0x0000001A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 1, 0x311)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'バイク乗れる', 0x0000001B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuAddItem(0, '追従セリーヌ', 0x0000001C)
    MenuAddItem(0, '追従キャラテスト', 0x0000001D)
    MenuAddItem(0, 'マップジャンプ ON', 0x00000045)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.Expr24, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '街（武器振り禁止）', 0x0000001E, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.Expr24, 0x80000000),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'モノクロ', 0x0000001F, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.Expr24, 0x80),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'フォローカメラ無効', 0x00000020, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.Expr24, 0x40),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '戦闘BGM切り替えOFF', 0x00000029, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 0, 0x400)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'リンク許可', 0x00000006, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 1, 0x401)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'リンクラッシュ許可', 0x00000007, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 2, 0x402)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'リンクバースト許可', 0x00000008, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 2, 0x42A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '騎神バースト許可 最大５', 0x00000009, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0073, 4, 0x39C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'カレンダー非表示', 0x0000000B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuAddItem(0, 'パーティ回復 ＞', 0x0000000C)
    MenuAddItem(0, 'オーブメントスロットLV2', 0x00000011)
    MenuAddItem(0, 'オーブメントスロットLV0', 0x00000012)
    MenuAddItem(0, 'クラフト全破棄', 0x00000013)
    MenuAddItem(0, 'クラフト現レベルで入手', 0x00000014)
    MenuAddItem(0, 'クラフト全入手', 0x00000015)
    MenuAddItem(0, '全キャラＬＶＭＡＸ', 0x00000016)
    MenuAddItem(0, '全キャラリンクＬＶＭＡＸ', 0x00000017)
    MenuAddItem(0, 'モードチェンジ禁止 ＞', 0x00000018)
    MenuAddItem(0, 'キャンプパーティ入手 ＞', 0x00000032)
    MenuAddItem(0, '待機メンバー経験値入手 ＞', 0x00000033)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0080, 7, 0x407)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, '待機メンバー経験値入手無効', 0x00000034, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuAddItem(0, 'ファンクション引数テスト', 0x00000034)
    MenuAddItem(0, 'Ｓクラフト入手・アルティナ', 0x00000046)
    MenuAddItem(0, '絆行動ポイント＋１', 0x00000047)
    MenuAddItem(0, 'Ｌ２のアークス許可', 0x00000048)
    MenuAddItem(0, 'コスチュームメニュー登録', 0x00000049)
    MenuAddItem(0, '装備関連いろいろ／ＭＱレベル', 0x0000004A)
    MenuAddItem(0, '全アクティブボイスフラグクリア', 0x0000004B)
    MenuAddItem(0, 'パーティ関連編集・人数など', 0x0000004C)
    MenuAddItem(0, 'システムセーブフラグ管理', 0x0000004F)
    MenuSetPos(0, 0x01, 24, 24, 0x01)
    MenuShow(0, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_F43B'),
        (0x00000001, 'loc_F443'),
        (0x0000004D, 'loc_F44B'),
        (0x0000004E, 'loc_F468'),
        (0x00000006, 'loc_F485'),
        (0x00000007, 'loc_F48D'),
        (0x00000008, 'loc_F495'),
        (0x00000009, 'loc_F49D'),
        (0x0000000B, 'loc_F4A5'),
        (0x0000000C, 'loc_F4AD'),
        (0x00000011, 'loc_F4C5'),
        (0x00000012, 'loc_F4D2'),
        (0x00000013, 'loc_F4DF'),
        (0x00000014, 'loc_F4E8'),
        (0x00000015, 'loc_F4F3'),
        (0x00000016, 'loc_F5F0'),
        (0x00000017, 'loc_F5FD'),
        (0x00000018, 'loc_F722'),
        (0x00000019, 'loc_F740'),
        (0x0000001A, 'loc_F748'),
        (0x0000001B, 'loc_F759'),
        (0x0000001C, 'loc_F761'),
        (0x0000001D, 'loc_F779'),
        (0x00000045, 'loc_F7D4'),
        (0x0000001E, 'loc_F7EC'),
        (0x0000001F, 'loc_F7F6'),
        (0x00000020, 'loc_F800'),
        (0x00000029, 'loc_F80A'),
        (0x00000032, 'loc_F814'),
        (0x00000033, 'loc_F831'),
        (0x00000034, 'loc_F857'),
        (0x00000034, 'loc_F85F'),
        (0x00000046, 'loc_F874'),
        (0x00000047, 'loc_F885'),
        (0x00000048, 'loc_F88D'),
        (0x00000049, 'loc_F895'),
        (0x0000004A, 'loc_F8AB'),
        (0x0000004B, 'loc_F8BF'),
        (0x0000004C, 'loc_F8DD'),
        (0x0000004F, 'loc_F8F8'),
        (-1, 'loc_F916'),
    )

    def _loc_F43B(): pass

    label('loc_F43B')

    XorScenaFlags(ScenaFlag(0x0060, 0, 0x300))

    Jump('loc_F91F')

    def _loc_F443(): pass

    label('loc_F443')

    XorScenaFlags(ScenaFlag(0x0060, 3, 0x303))

    Jump('loc_F91F')

    def _loc_F44B(): pass

    label('loc_F44B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0002)"),
            Expr.Return,
        ),
        'loc_F45F',
    )

    OP_19(0x01, 0x0002)

    Jump('loc_F463')

    def _loc_F45F(): pass

    label('loc_F45F')

    OP_19(0x00, 0x0002)

    def _loc_F463(): pass

    label('loc_F463')

    Jump('loc_F91F')

    def _loc_F468(): pass

    label('loc_F468')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0003)"),
            Expr.Return,
        ),
        'loc_F47C',
    )

    OP_19(0x01, 0x0003)

    Jump('loc_F480')

    def _loc_F47C(): pass

    label('loc_F47C')

    OP_19(0x00, 0x0003)

    def _loc_F480(): pass

    label('loc_F480')

    Jump('loc_F91F')

    def _loc_F485(): pass

    label('loc_F485')

    XorScenaFlags(ScenaFlag(0x0080, 0, 0x400))

    Jump('loc_F91F')

    def _loc_F48D(): pass

    label('loc_F48D')

    XorScenaFlags(ScenaFlag(0x0080, 1, 0x401))

    Jump('loc_F91F')

    def _loc_F495(): pass

    label('loc_F495')

    XorScenaFlags(ScenaFlag(0x0080, 2, 0x402))

    Jump('loc_F91F')

    def _loc_F49D(): pass

    label('loc_F49D')

    XorScenaFlags(ScenaFlag(0x0085, 2, 0x42A))

    Jump('loc_F91F')

    def _loc_F4A5(): pass

    label('loc_F4A5')

    XorScenaFlags(ScenaFlag(0x0073, 4, 0x39C))

    Jump('loc_F91F')

    def _loc_F4AD(): pass

    label('loc_F4AD')

    Call(ScriptId.Current, 'FC_SetHealParty')

    Jump('loc_F91F')

    def _loc_F4C5(): pass

    label('loc_F4C5')

    OP_70(0x06, 0xFFFF, 0xFF, 0x03, 0x01, 0x01)

    Jump('loc_F91F')

    def _loc_F4D2(): pass

    label('loc_F4D2')

    OP_70(0x06, 0xFFFF, 0xFF, 0x01, 0x01, 0x01)

    Jump('loc_F91F')

    def _loc_F4DF(): pass

    label('loc_F4DF')

    CraftCtrl(0x03, 0xFFFF)

    Jump('loc_F91F')

    def _loc_F4E8(): pass

    label('loc_F4E8')

    CraftCtrl(0x00, 0xFFFF, 0x0000)

    Jump('loc_F91F')

    def _loc_F4F3(): pass

    label('loc_F4F3')

    CraftCtrl(0x02, ChrTable['黎恩'], 0x00000000)
    CraftCtrl(0x02, ChrTable['亞莉莎'], 0x00000000)
    CraftCtrl(0x02, ChrTable['艾略特'], 0x00000000)
    CraftCtrl(0x02, ChrTable['勞拉'], 0x00000000)
    CraftCtrl(0x02, ChrTable['馬奇亞斯'], 0x00000000)
    CraftCtrl(0x02, ChrTable['艾瑪'], 0x00000000)
    CraftCtrl(0x02, ChrTable['尤西斯'], 0x00000000)
    CraftCtrl(0x02, ChrTable['菲'], 0x00000000)
    CraftCtrl(0x02, ChrTable['蓋烏斯'], 0x00000000)
    CraftCtrl(0x02, ChrTable['尤娜'], 0x00000000)
    CraftCtrl(0x02, ChrTable['庫爾特'], 0x00000000)
    CraftCtrl(0x02, ChrTable['亞爾緹娜'], 0x00000000)
    CraftCtrl(0x02, ChrTable['繆潔'], 0x00000000)
    CraftCtrl(0x02, ChrTable['亞修'], 0x00000000)
    CraftCtrl(0x02, ChrTable['莎拉'], 0x00000000)
    CraftCtrl(0x02, ChrTable['奧蕾莉亞將軍'], 0x00000000)
    CraftCtrl(0x02, ChrTable['阿加特'], 0x00000000)
    CraftCtrl(0x02, ChrTable['安潔莉卡'], 0x00000000)
    CraftCtrl(0x02, ChrTable['奧利維特皇子'], 0x00000000)
    CraftCtrl(0x02, ChrTable['提妲'], 0x00000000)
    CraftCtrl(0x02, ChrTable['緹歐'], 0x00000000)
    CraftCtrl(0x02, ChrTable['雪倫'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['黎恩'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['亞莉莎'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['艾略特'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['勞拉'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['馬奇亞斯'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['艾瑪'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['尤西斯'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['菲'], 0x00000000)
    CraftCtrl(0x0B, ChrTable['蓋烏斯'], 0x00000000)

    Jump('loc_F91F')

    def _loc_F5F0(): pass

    label('loc_F5F0')

    OP_48(0x00, 0xFFFF, 0x0001, 0x00C8)

    Jump('loc_F91F')

    def _loc_F5FD(): pass

    label('loc_F5FD')

    OP_69(0x02, 0x0000, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0001, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0002, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0003, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0004, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0005, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0006, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0007, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0008, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000A, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000B, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000C, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000D, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000E, 0xFFFF, 0x0007)
    OP_69(0x02, 0x000F, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0010, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0011, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0012, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0014, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0015, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0016, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0017, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0023, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0020, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0018, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001A, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001B, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001C, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001D, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001E, 0xFFFF, 0x0007)
    OP_69(0x02, 0x001F, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0019, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0022, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0026, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0027, 0xFFFF, 0x0007)
    OP_69(0x02, 0x0021, 0xFFFF, 0x0007)

    Jump('loc_F91F')

    def _loc_F722(): pass

    label('loc_F722')

    Call(ScriptId.Current, 'SelectFlag_ModeChange')

    Jump('loc_F91F')

    def _loc_F740(): pass

    label('loc_F740')

    XorScenaFlags(ScenaFlag(0x0061, 6, 0x30E))

    Jump('loc_F91F')

    def _loc_F748(): pass

    label('loc_F748')

    XorScenaFlags(ScenaFlag(0x0062, 0, 0x310))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0062, 0, 0x310)),
            Expr.Return,
        ),
        'loc_F754',
    )

    def _loc_F754(): pass

    label('loc_F754')

    Jump('loc_F91F')

    def _loc_F759(): pass

    label('loc_F759')

    XorScenaFlags(ScenaFlag(0x0062, 1, 0x311))

    Jump('loc_F91F')

    def _loc_F761(): pass

    label('loc_F761')

    ModelCtrl(0x31, 0x00, 0x0002, 0x005F, 0.5, 0.2, 0x03, 0x01, 0x0000)

    Jump('loc_F91F')

    def _loc_F779(): pass

    label('loc_F779')

    ModelCtrl(0x23, 0x0000, 0xFFFF, 0x0000, -1.0)
    ModelCtrl(0x23, 0x0001, 0xFFFF, 0x0000, -1.0)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x0A, 0xF001)"),
            Expr.Return,
        ),
        'loc_F7B0',
    )

    ModelCtrl(0x23, 0x0000, 0xF001, 0x0001, 0.25)
    ChrClearPhysicsFlags(0xF001, 0x00000001)

    def _loc_F7B0(): pass

    label('loc_F7B0')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x0A, 0xF002)"),
            Expr.Return,
        ),
        'loc_F7CF',
    )

    ModelCtrl(0x23, 0x0001, 0xF002, 0x0001, 0.25)
    ChrClearPhysicsFlags(0xF002, 0x00000001)

    def _loc_F7CF(): pass

    label('loc_F7CF')

    Jump('loc_F91F')

    def _loc_F7D4(): pass

    label('loc_F7D4')

    Call(ScriptId.Current, 'FC_mapjump_open')

    Jump('loc_F91F')

    def _loc_F7EC(): pass

    label('loc_F7EC')

    OP_15(0x00000008)

    Jump('loc_F91F')

    def _loc_F7F6(): pass

    label('loc_F7F6')

    OP_15(0x80000000)

    Jump('loc_F91F')

    def _loc_F800(): pass

    label('loc_F800')

    OP_15(0x00000080)

    Jump('loc_F91F')

    def _loc_F80A(): pass

    label('loc_F80A')

    OP_15(0x00000040)

    Jump('loc_F91F')

    def _loc_F814(): pass

    label('loc_F814')

    Call(ScriptId.Current, 'SelectFlag_CampParty')

    Jump('loc_F91F')

    def _loc_F831(): pass

    label('loc_F831')

    Call(ScriptId.Current, 'SelectFlag_GetExpReserveParty')

    Jump('loc_F91F')

    def _loc_F857(): pass

    label('loc_F857')

    XorScenaFlags(ScenaFlag(0x0080, 7, 0x407))

    Jump('loc_F91F')

    def _loc_F85F(): pass

    label('loc_F85F')

    Call(ScriptId.Current, 'ArgumentTest')

    Jump('loc_F91F')

    def _loc_F874(): pass

    label('loc_F874')

    CraftCtrl(0x00, ChrTable['亞爾緹娜'], 0x0A3C)
    CraftCtrl(0x04, ChrTable['亞爾緹娜'], 0x0A3C)

    Jump('loc_F91F')

    def _loc_F885(): pass

    label('loc_F885')

    OP_89(0x0001)

    Jump('loc_F91F')

    def _loc_F88D(): pass

    label('loc_F88D')

    SetScenaFlags(ScenaFlag(0x0073, 2, 0x39A))

    Jump('loc_F91F')

    def _loc_F895(): pass

    label('loc_F895')

    Call(ScriptId.Current, 'FC_SetCostume')

    Jump('loc_F91F')

    def _loc_F8AB(): pass

    label('loc_F8AB')

    Call(ScriptId.Current, 'FC_SetEquip')

    Jump('loc_F91F')

    def _loc_F8BF(): pass

    label('loc_F8BF')

    Call(ScriptId.Current, 'FC_AVoiceFlagAllClear')

    Jump('loc_F91F')

    def _loc_F8DD(): pass

    label('loc_F8DD')

    Call(ScriptId.Current, 'FC_PartyMemberEdit')

    Jump('loc_F91F')

    def _loc_F8F8(): pass

    label('loc_F8F8')

    Call(ScriptId.Current, 'FC_SystemSaveFlagEdit')

    Jump('loc_F91F')

    def _loc_F916(): pass

    label('loc_F916')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F91F(): pass

    label('loc_F91F')

    Jump('loc_EBA1')

    def _loc_F924(): pass

    label('loc_F924')

    MenuCmd(0x03, 0)

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EndDebugScript')

    Return()

# id: 0x0007 offset: 0xF944
@scena.Code('ResetTempFlag')
def ResetTempFlag():
    ClearScenaFlags(ScenaFlag(0x0005, 1, 0x29))
    ClearScenaFlags(ScenaFlag(0x0005, 2, 0x2A))
    ClearScenaFlags(ScenaFlag(0x0005, 3, 0x2B))
    ClearScenaFlags(ScenaFlag(0x0005, 4, 0x2C))
    ClearScenaFlags(ScenaFlag(0x0005, 5, 0x2D))
    ClearScenaFlags(ScenaFlag(0x0005, 6, 0x2E))
    ClearScenaFlags(ScenaFlag(0x0005, 7, 0x2F))
    ClearScenaFlags(ScenaFlag(0x0006, 0, 0x30))
    ClearScenaFlags(ScenaFlag(0x0006, 1, 0x31))
    ClearScenaFlags(ScenaFlag(0x0006, 2, 0x32))
    ClearScenaFlags(ScenaFlag(0x0006, 3, 0x33))
    ClearScenaFlags(ScenaFlag(0x0006, 4, 0x34))
    ClearScenaFlags(ScenaFlag(0x0006, 5, 0x35))
    ClearScenaFlags(ScenaFlag(0x0006, 6, 0x36))
    ClearScenaFlags(ScenaFlag(0x0006, 7, 0x37))
    ClearScenaFlags(ScenaFlag(0x0007, 0, 0x38))
    ClearScenaFlags(ScenaFlag(0x0007, 1, 0x39))
    ClearScenaFlags(ScenaFlag(0x0007, 2, 0x3A))
    ClearScenaFlags(ScenaFlag(0x0007, 3, 0x3B))
    ClearScenaFlags(ScenaFlag(0x0007, 4, 0x3C))
    ClearScenaFlags(ScenaFlag(0x0007, 5, 0x3D))
    ClearScenaFlags(ScenaFlag(0x0007, 6, 0x3E))
    ClearScenaFlags(ScenaFlag(0x0007, 7, 0x3F))
    ClearScenaFlags(ScenaFlag(0x0008, 0, 0x40))
    ClearScenaFlags(ScenaFlag(0x0008, 1, 0x41))
    ClearScenaFlags(ScenaFlag(0x0008, 2, 0x42))
    ClearScenaFlags(ScenaFlag(0x0008, 3, 0x43))
    ClearScenaFlags(ScenaFlag(0x0008, 4, 0x44))
    ClearScenaFlags(ScenaFlag(0x0008, 5, 0x45))
    ClearScenaFlags(ScenaFlag(0x0008, 6, 0x46))
    ClearScenaFlags(ScenaFlag(0x0008, 7, 0x47))
    ClearScenaFlags(ScenaFlag(0x0009, 0, 0x48))
    ClearScenaFlags(ScenaFlag(0x0009, 1, 0x49))
    ClearScenaFlags(ScenaFlag(0x0009, 2, 0x4A))
    ClearScenaFlags(ScenaFlag(0x0009, 3, 0x4B))
    ClearScenaFlags(ScenaFlag(0x0009, 4, 0x4C))
    ClearScenaFlags(ScenaFlag(0x0009, 5, 0x4D))
    ClearScenaFlags(ScenaFlag(0x0009, 6, 0x4E))
    ClearScenaFlags(ScenaFlag(0x0009, 7, 0x4F))
    ClearScenaFlags(ScenaFlag(0x000A, 0, 0x50))

    Return()

# id: 0x0008 offset: 0xF9C0
@scena.Code('SelectFlag_ModeChange')
def SelectFlag_ModeChange():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_F9C9(): pass

    label('loc_F9C9')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FAAF',
    )

    Call(ScriptId.Current, 'ResetTempFlag')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['尤娜'], 0x40000000)"),
            Expr.Return,
        ),
        'loc_F9FA',
    )

    SetScenaFlags(ScenaFlag(0x0005, 2, 0x2A))

    def _loc_F9FA(): pass

    label('loc_F9FA')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['克洛'], 0x40000000)"),
            Expr.Return,
        ),
        'loc_FA0C',
    )

    SetScenaFlags(ScenaFlag(0x0005, 2, 0x2A))

    def _loc_FA0C(): pass

    label('loc_FA0C')

    MenuCreate(1, 24, 24.0, 99)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 2, 0x2A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ユウナ', 0x00000000, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 1, 0x29)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'クロウ', 0x00000001, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuSetPos(1, 0x01, 224, 24, 0x01)
    MenuShow(1, 0xF8)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x00000000, 'loc_FA87'),
        (0x00000001, 'loc_FA94'),
        (-1, 'loc_FAA1'),
    )

    def _loc_FA87(): pass

    label('loc_FA87')

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x40000000)

    Jump('loc_FAAA')

    def _loc_FA94(): pass

    label('loc_FA94')

    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x40000000)

    Jump('loc_FAAA')

    def _loc_FAA1(): pass

    label('loc_FAA1')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FAAA(): pass

    label('loc_FAAA')

    Jump('loc_F9C9')

    def _loc_FAAF(): pass

    label('loc_FAAF')

    MenuCmd(0x03, 1)

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0009 offset: 0xFABC
@scena.Code('SelectFlag_CampParty')
def SelectFlag_CampParty():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_FAC5(): pass

    label('loc_FAC5')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1051D',
    )

    Call(ScriptId.Current, 'ResetTempFlag')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['黎恩'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FAF6',
    )

    SetScenaFlags(ScenaFlag(0x0005, 1, 0x29))

    def _loc_FAF6(): pass

    label('loc_FAF6')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['尤娜'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB08',
    )

    SetScenaFlags(ScenaFlag(0x0005, 2, 0x2A))

    def _loc_FB08(): pass

    label('loc_FB08')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['庫爾特'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB1A',
    )

    SetScenaFlags(ScenaFlag(0x0005, 3, 0x2B))

    def _loc_FB1A(): pass

    label('loc_FB1A')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞爾緹娜'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB2C',
    )

    SetScenaFlags(ScenaFlag(0x0005, 4, 0x2C))

    def _loc_FB2C(): pass

    label('loc_FB2C')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞修'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB3E',
    )

    SetScenaFlags(ScenaFlag(0x0005, 5, 0x2D))

    def _loc_FB3E(): pass

    label('loc_FB3E')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['繆潔'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB50',
    )

    SetScenaFlags(ScenaFlag(0x0005, 6, 0x2E))

    def _loc_FB50(): pass

    label('loc_FB50')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞莉莎'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB62',
    )

    SetScenaFlags(ScenaFlag(0x0005, 7, 0x2F))

    def _loc_FB62(): pass

    label('loc_FB62')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾略特'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB74',
    )

    SetScenaFlags(ScenaFlag(0x0006, 0, 0x30))

    def _loc_FB74(): pass

    label('loc_FB74')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['勞拉'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB86',
    )

    SetScenaFlags(ScenaFlag(0x0006, 1, 0x31))

    def _loc_FB86(): pass

    label('loc_FB86')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['馬奇亞斯'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FB98',
    )

    SetScenaFlags(ScenaFlag(0x0006, 2, 0x32))

    def _loc_FB98(): pass

    label('loc_FB98')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾瑪'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FBAA',
    )

    SetScenaFlags(ScenaFlag(0x0006, 3, 0x33))

    def _loc_FBAA(): pass

    label('loc_FBAA')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['尤西斯'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FBBC',
    )

    SetScenaFlags(ScenaFlag(0x0006, 4, 0x34))

    def _loc_FBBC(): pass

    label('loc_FBBC')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['菲'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FBCE',
    )

    SetScenaFlags(ScenaFlag(0x0006, 5, 0x35))

    def _loc_FBCE(): pass

    label('loc_FBCE')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['蓋烏斯'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FBE0',
    )

    SetScenaFlags(ScenaFlag(0x0006, 6, 0x36))

    def _loc_FBE0(): pass

    label('loc_FBE0')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['莎拉'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FBF2',
    )

    SetScenaFlags(ScenaFlag(0x0007, 0, 0x38))

    def _loc_FBF2(): pass

    label('loc_FBF2')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['奧蕾莉亞將軍'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC04',
    )

    SetScenaFlags(ScenaFlag(0x0007, 1, 0x39))

    def _loc_FC04(): pass

    label('loc_FC04')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['阿加特'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC16',
    )

    SetScenaFlags(ScenaFlag(0x0007, 2, 0x3A))

    def _loc_FC16(): pass

    label('loc_FC16')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['安潔莉卡'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC28',
    )

    SetScenaFlags(ScenaFlag(0x0007, 3, 0x3B))

    def _loc_FC28(): pass

    label('loc_FC28')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['喬治'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC3A',
    )

    SetScenaFlags(ScenaFlag(0x0007, 4, 0x3C))

    def _loc_FC3A(): pass

    label('loc_FC3A')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['提妲'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC4C',
    )

    SetScenaFlags(ScenaFlag(0x0007, 5, 0x3D))

    def _loc_FC4C(): pass

    label('loc_FC4C')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['緹歐'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC5E',
    )

    SetScenaFlags(ScenaFlag(0x0007, 6, 0x3E))

    def _loc_FC5E(): pass

    label('loc_FC5E')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['雪倫'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC70',
    )

    SetScenaFlags(ScenaFlag(0x0007, 7, 0x3F))

    def _loc_FC70(): pass

    label('loc_FC70')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['克洛'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC82',
    )

    SetScenaFlags(ScenaFlag(0x0008, 0, 0x40))

    def _loc_FC82(): pass

    label('loc_FC82')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['杜巴莉'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FC94',
    )

    SetScenaFlags(ScenaFlag(0x0008, 1, 0x41))

    def _loc_FC94(): pass

    label('loc_FC94')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['剛毅艾奈絲'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FCA6',
    )

    SetScenaFlags(ScenaFlag(0x0008, 2, 0x42))

    def _loc_FCA6(): pass

    label('loc_FCA6')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['魔弓恩奈雅'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FCB8',
    )

    SetScenaFlags(ScenaFlag(0x0008, 3, 0x43))

    def _loc_FCB8(): pass

    label('loc_FCB8')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['陷阱師傑諾'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FCCA',
    )

    SetScenaFlags(ScenaFlag(0x0008, 4, 0x44))

    def _loc_FCCA(): pass

    label('loc_FCCA')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['破壞獸雷歐尼達斯'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FCDC',
    )

    SetScenaFlags(ScenaFlag(0x0008, 5, 0x45))

    def _loc_FCDC(): pass

    label('loc_FCDC')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['瑟蕾奴'], 0x00000001)"),
            Expr.Return,
        ),
        'loc_FCEE',
    )

    SetScenaFlags(ScenaFlag(0x0008, 6, 0x46))

    def _loc_FCEE(): pass

    label('loc_FCEE')

    MenuCreate(1, 24, 24.0, 99)
    MenuAddItem(1, '全員取得', 0x00000064)
    MenuAddItem(1, '全員未取得', 0x00000065)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 1, 0x29)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'リィン', 0x00000000, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 2, 0x2A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ユウナ', 0x00000001, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 3, 0x2B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'クルト', 0x00000002, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 4, 0x2C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アルティナ', 0x00000003, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 5, 0x2D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アッシュ', 0x00000004, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 6, 0x2E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ミュゼ', 0x00000005, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 7, 0x2F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アリサ', 0x00000006, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 0, 0x30)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'エリオット', 0x00000007, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 1, 0x31)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ラウラ', 0x00000008, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 2, 0x32)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'マキアス', 0x00000009, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 3, 0x33)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'エマ', 0x0000000A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 4, 0x34)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ユーシス', 0x0000000B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 5, 0x35)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'フィー', 0x0000000C, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 6, 0x36)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ガイウス', 0x0000000D, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 0, 0x38)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'サラ', 0x0000000F, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 1, 0x39)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'オーレリア', 0x00000010, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 2, 0x3A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アガット', 0x00000011, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 3, 0x3B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アンゼリカ', 0x00000012, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 4, 0x3C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ジョルジュ', 0x00000013, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 5, 0x3D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ティータ', 0x00000014, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 6, 0x3E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ティオ', 0x00000015, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 7, 0x3F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'シャロン', 0x00000016, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 0, 0x40)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'クロウ', 0x00000017, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 1, 0x41)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'デュバリィ', 0x00000018, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 2, 0x42)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アイネス', 0x00000019, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 3, 0x43)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'エンネア', 0x0000001A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 4, 0x44)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ゼノ', 0x0000001B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 5, 0x45)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'レオニダス', 0x0000001C, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 6, 0x46)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'セリーヌ', 0x0000001D, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuSetPos(1, 0x01, 224, 24, 0x01)
    MenuShow(1, 0xF8)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x00000064, 'loc_1028F'),
        (0x00000065, 'loc_1037C'),
        (0x00000000, 'loc_10389'),
        (0x00000001, 'loc_10396'),
        (0x00000002, 'loc_103A3'),
        (0x00000003, 'loc_103B0'),
        (0x00000004, 'loc_103BD'),
        (0x00000005, 'loc_103CA'),
        (0x00000006, 'loc_103D7'),
        (0x00000007, 'loc_103E4'),
        (0x00000008, 'loc_103F1'),
        (0x00000009, 'loc_103FE'),
        (0x0000000A, 'loc_1040B'),
        (0x0000000B, 'loc_10418'),
        (0x0000000C, 'loc_10425'),
        (0x0000000D, 'loc_10432'),
        (0x0000000E, 'loc_1043F'),
        (0x0000000F, 'loc_1044C'),
        (0x00000010, 'loc_10459'),
        (0x00000011, 'loc_10466'),
        (0x00000012, 'loc_10473'),
        (0x00000013, 'loc_10480'),
        (0x00000014, 'loc_1048D'),
        (0x00000015, 'loc_1049A'),
        (0x00000016, 'loc_104A7'),
        (0x00000017, 'loc_104B4'),
        (0x00000018, 'loc_104C1'),
        (0x00000019, 'loc_104CE'),
        (0x0000001A, 'loc_104DB'),
        (0x0000001B, 'loc_104E8'),
        (0x0000001C, 'loc_104F5'),
        (0x0000001D, 'loc_10502'),
        (-1, 'loc_1050F'),
    )

    def _loc_1028F(): pass

    label('loc_1028F')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['奧蕾莉亞將軍'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['喬治'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['剛毅艾奈絲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['魔弓恩奈雅'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['陷阱師傑諾'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['破壞獸雷歐尼達斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000001)

    Jump('loc_10518')

    def _loc_1037C(): pass

    label('loc_1037C')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x00000001)

    Jump('loc_10518')

    def _loc_10389(): pass

    label('loc_10389')

    MenuChrFlagCmd(0x02, ChrTable['黎恩'], 0x00000001)

    Jump('loc_10518')

    def _loc_10396(): pass

    label('loc_10396')

    MenuChrFlagCmd(0x02, ChrTable['尤娜'], 0x00000001)

    Jump('loc_10518')

    def _loc_103A3(): pass

    label('loc_103A3')

    MenuChrFlagCmd(0x02, ChrTable['庫爾特'], 0x00000001)

    Jump('loc_10518')

    def _loc_103B0(): pass

    label('loc_103B0')

    MenuChrFlagCmd(0x02, ChrTable['亞爾緹娜'], 0x00000001)

    Jump('loc_10518')

    def _loc_103BD(): pass

    label('loc_103BD')

    MenuChrFlagCmd(0x02, ChrTable['亞修'], 0x00000001)

    Jump('loc_10518')

    def _loc_103CA(): pass

    label('loc_103CA')

    MenuChrFlagCmd(0x02, ChrTable['繆潔'], 0x00000001)

    Jump('loc_10518')

    def _loc_103D7(): pass

    label('loc_103D7')

    MenuChrFlagCmd(0x02, ChrTable['亞莉莎'], 0x00000001)

    Jump('loc_10518')

    def _loc_103E4(): pass

    label('loc_103E4')

    MenuChrFlagCmd(0x02, ChrTable['艾略特'], 0x00000001)

    Jump('loc_10518')

    def _loc_103F1(): pass

    label('loc_103F1')

    MenuChrFlagCmd(0x02, ChrTable['勞拉'], 0x00000001)

    Jump('loc_10518')

    def _loc_103FE(): pass

    label('loc_103FE')

    MenuChrFlagCmd(0x02, ChrTable['馬奇亞斯'], 0x00000001)

    Jump('loc_10518')

    def _loc_1040B(): pass

    label('loc_1040B')

    MenuChrFlagCmd(0x02, ChrTable['艾瑪'], 0x00000001)

    Jump('loc_10518')

    def _loc_10418(): pass

    label('loc_10418')

    MenuChrFlagCmd(0x02, ChrTable['尤西斯'], 0x00000001)

    Jump('loc_10518')

    def _loc_10425(): pass

    label('loc_10425')

    MenuChrFlagCmd(0x02, ChrTable['菲'], 0x00000001)

    Jump('loc_10518')

    def _loc_10432(): pass

    label('loc_10432')

    MenuChrFlagCmd(0x02, ChrTable['蓋烏斯'], 0x00000001)

    Jump('loc_10518')

    def _loc_1043F(): pass

    label('loc_1043F')

    MenuChrFlagCmd(0x02, ChrTable['米莉亞姆'], 0x00000001)

    Jump('loc_10518')

    def _loc_1044C(): pass

    label('loc_1044C')

    MenuChrFlagCmd(0x02, ChrTable['莎拉'], 0x00000001)

    Jump('loc_10518')

    def _loc_10459(): pass

    label('loc_10459')

    MenuChrFlagCmd(0x02, ChrTable['奧蕾莉亞將軍'], 0x00000001)

    Jump('loc_10518')

    def _loc_10466(): pass

    label('loc_10466')

    MenuChrFlagCmd(0x02, ChrTable['阿加特'], 0x00000001)

    Jump('loc_10518')

    def _loc_10473(): pass

    label('loc_10473')

    MenuChrFlagCmd(0x02, ChrTable['安潔莉卡'], 0x00000001)

    Jump('loc_10518')

    def _loc_10480(): pass

    label('loc_10480')

    MenuChrFlagCmd(0x02, ChrTable['喬治'], 0x00000001)

    Jump('loc_10518')

    def _loc_1048D(): pass

    label('loc_1048D')

    MenuChrFlagCmd(0x02, ChrTable['提妲'], 0x00000001)

    Jump('loc_10518')

    def _loc_1049A(): pass

    label('loc_1049A')

    MenuChrFlagCmd(0x02, ChrTable['緹歐'], 0x00000001)

    Jump('loc_10518')

    def _loc_104A7(): pass

    label('loc_104A7')

    MenuChrFlagCmd(0x02, ChrTable['雪倫'], 0x00000001)

    Jump('loc_10518')

    def _loc_104B4(): pass

    label('loc_104B4')

    MenuChrFlagCmd(0x02, ChrTable['克洛'], 0x00000001)

    Jump('loc_10518')

    def _loc_104C1(): pass

    label('loc_104C1')

    MenuChrFlagCmd(0x02, ChrTable['杜巴莉'], 0x00000001)

    Jump('loc_10518')

    def _loc_104CE(): pass

    label('loc_104CE')

    MenuChrFlagCmd(0x02, ChrTable['剛毅艾奈絲'], 0x00000001)

    Jump('loc_10518')

    def _loc_104DB(): pass

    label('loc_104DB')

    MenuChrFlagCmd(0x02, ChrTable['魔弓恩奈雅'], 0x00000001)

    Jump('loc_10518')

    def _loc_104E8(): pass

    label('loc_104E8')

    MenuChrFlagCmd(0x02, ChrTable['陷阱師傑諾'], 0x00000001)

    Jump('loc_10518')

    def _loc_104F5(): pass

    label('loc_104F5')

    MenuChrFlagCmd(0x02, ChrTable['破壞獸雷歐尼達斯'], 0x00000001)

    Jump('loc_10518')

    def _loc_10502(): pass

    label('loc_10502')

    MenuChrFlagCmd(0x02, ChrTable['瑟蕾奴'], 0x00000001)

    Jump('loc_10518')

    def _loc_1050F(): pass

    label('loc_1050F')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10518(): pass

    label('loc_10518')

    Jump('loc_FAC5')

    def _loc_1051D(): pass

    label('loc_1051D')

    MenuCmd(0x03, 1)

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000A offset: 0x1052C
@scena.Code('SelectFlag_GetExpReserveParty')
def SelectFlag_GetExpReserveParty():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10535(): pass

    label('loc_10535')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10E48',
    )

    Call(ScriptId.Current, 'ResetTempFlag')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['黎恩'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10566',
    )

    SetScenaFlags(ScenaFlag(0x0005, 1, 0x29))

    def _loc_10566(): pass

    label('loc_10566')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['尤娜'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10578',
    )

    SetScenaFlags(ScenaFlag(0x0005, 2, 0x2A))

    def _loc_10578(): pass

    label('loc_10578')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['庫爾特'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1058A',
    )

    SetScenaFlags(ScenaFlag(0x0005, 3, 0x2B))

    def _loc_1058A(): pass

    label('loc_1058A')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞爾緹娜'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1059C',
    )

    SetScenaFlags(ScenaFlag(0x0005, 4, 0x2C))

    def _loc_1059C(): pass

    label('loc_1059C')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞修'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_105AE',
    )

    SetScenaFlags(ScenaFlag(0x0005, 5, 0x2D))

    def _loc_105AE(): pass

    label('loc_105AE')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['繆潔'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_105C0',
    )

    SetScenaFlags(ScenaFlag(0x0005, 6, 0x2E))

    def _loc_105C0(): pass

    label('loc_105C0')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['亞莉莎'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_105D2',
    )

    SetScenaFlags(ScenaFlag(0x0005, 7, 0x2F))

    def _loc_105D2(): pass

    label('loc_105D2')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾略特'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_105E4',
    )

    SetScenaFlags(ScenaFlag(0x0006, 0, 0x30))

    def _loc_105E4(): pass

    label('loc_105E4')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['勞拉'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_105F6',
    )

    SetScenaFlags(ScenaFlag(0x0006, 1, 0x31))

    def _loc_105F6(): pass

    label('loc_105F6')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['馬奇亞斯'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10608',
    )

    SetScenaFlags(ScenaFlag(0x0006, 2, 0x32))

    def _loc_10608(): pass

    label('loc_10608')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾瑪'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1061A',
    )

    SetScenaFlags(ScenaFlag(0x0006, 3, 0x33))

    def _loc_1061A(): pass

    label('loc_1061A')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['尤西斯'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1062C',
    )

    SetScenaFlags(ScenaFlag(0x0006, 4, 0x34))

    def _loc_1062C(): pass

    label('loc_1062C')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['菲'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1063E',
    )

    SetScenaFlags(ScenaFlag(0x0006, 5, 0x35))

    def _loc_1063E(): pass

    label('loc_1063E')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['蓋烏斯'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10650',
    )

    SetScenaFlags(ScenaFlag(0x0006, 6, 0x36))

    def _loc_10650(): pass

    label('loc_10650')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['莎拉'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10662',
    )

    SetScenaFlags(ScenaFlag(0x0007, 0, 0x38))

    def _loc_10662(): pass

    label('loc_10662')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['奧蕾莉亞將軍'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10674',
    )

    SetScenaFlags(ScenaFlag(0x0007, 1, 0x39))

    def _loc_10674(): pass

    label('loc_10674')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['阿加特'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10686',
    )

    SetScenaFlags(ScenaFlag(0x0007, 2, 0x3A))

    def _loc_10686(): pass

    label('loc_10686')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['安潔莉卡'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10698',
    )

    SetScenaFlags(ScenaFlag(0x0007, 3, 0x3B))

    def _loc_10698(): pass

    label('loc_10698')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['喬治'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_106AA',
    )

    SetScenaFlags(ScenaFlag(0x0007, 4, 0x3C))

    def _loc_106AA(): pass

    label('loc_106AA')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['提妲'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_106BC',
    )

    SetScenaFlags(ScenaFlag(0x0007, 5, 0x3D))

    def _loc_106BC(): pass

    label('loc_106BC')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['緹歐'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_106CE',
    )

    SetScenaFlags(ScenaFlag(0x0007, 6, 0x3E))

    def _loc_106CE(): pass

    label('loc_106CE')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['雪倫'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_106E0',
    )

    SetScenaFlags(ScenaFlag(0x0007, 7, 0x3F))

    def _loc_106E0(): pass

    label('loc_106E0')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['克洛'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_106F2',
    )

    SetScenaFlags(ScenaFlag(0x0008, 0, 0x40))

    def _loc_106F2(): pass

    label('loc_106F2')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['克洛提德'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10704',
    )

    SetScenaFlags(ScenaFlag(0x0008, 1, 0x41))

    def _loc_10704(): pass

    label('loc_10704')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['遊擊士托瓦爾'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10716',
    )

    SetScenaFlags(ScenaFlag(0x0008, 2, 0x42))

    def _loc_10716(): pass

    label('loc_10716')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾絲蒂爾'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10728',
    )

    SetScenaFlags(ScenaFlag(0x0008, 3, 0x43))

    def _loc_10728(): pass

    label('loc_10728')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['約修亞'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1073A',
    )

    SetScenaFlags(ScenaFlag(0x0008, 4, 0x44))

    def _loc_1073A(): pass

    label('loc_1073A')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['玲'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1074C',
    )

    SetScenaFlags(ScenaFlag(0x0008, 5, 0x45))

    def _loc_1074C(): pass

    label('loc_1074C')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['羅伊德'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_1075E',
    )

    SetScenaFlags(ScenaFlag(0x0008, 6, 0x46))

    def _loc_1075E(): pass

    label('loc_1075E')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['艾莉'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10770',
    )

    SetScenaFlags(ScenaFlag(0x0008, 7, 0x47))

    def _loc_10770(): pass

    label('loc_10770')

    If(
        (
            (Expr.Eval, "MenuChrFlagCmd(0x03, ChrTable['蘭迪'], 0x10000000)"),
            Expr.Return,
        ),
        'loc_10782',
    )

    SetScenaFlags(ScenaFlag(0x0009, 0, 0x48))

    def _loc_10782(): pass

    label('loc_10782')

    MenuCreate(1, 40, 24.0, 99)
    MenuAddItem(1, '全員取得', 0x00000064)
    MenuAddItem(1, '全員未取得', 0x00000065)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 1, 0x29)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'リィン', 0x00000000, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 2, 0x2A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ユウナ', 0x00000001, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 3, 0x2B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'クルト', 0x00000002, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 4, 0x2C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アルティナ', 0x00000003, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 5, 0x2D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アッシュ', 0x00000004, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 6, 0x2E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ミュゼ', 0x00000005, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0005, 7, 0x2F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アリサ', 0x00000006, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 0, 0x30)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'エリオット', 0x00000007, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 1, 0x31)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ラウラ', 0x00000008, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 2, 0x32)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'マキアス', 0x00000009, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 3, 0x33)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'エマ', 0x0000000A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 4, 0x34)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ユーシス', 0x0000000B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 5, 0x35)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'フィー', 0x0000000C, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0006, 6, 0x36)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ガイウス', 0x0000000D, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 0, 0x38)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'サラ', 0x0000000F, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 1, 0x39)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'オーレリア', 0x00000010, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 2, 0x3A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アガット', 0x00000011, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 3, 0x3B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'アンゼリカ', 0x00000012, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 4, 0x3C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ジョルジュ', 0x00000013, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 5, 0x3D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ティータ', 0x00000014, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 6, 0x3E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'ティオ', 0x00000015, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0007, 7, 0x3F)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'シャロン', 0x00000016, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 0, 0x40)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'クロウ', 0x00000017, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0008, 2, 0x42)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, 'トヴァル', 0x00000019, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuSetPos(1, 0x01, 224, 24, 0x01)
    MenuShow(1, 0xF8)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x00000064, 'loc_10C30'),
        (0x00000065, 'loc_10CF5'),
        (0x00000000, 'loc_10D02'),
        (0x00000001, 'loc_10D0F'),
        (0x00000002, 'loc_10D1C'),
        (0x00000003, 'loc_10D29'),
        (0x00000004, 'loc_10D36'),
        (0x00000005, 'loc_10D43'),
        (0x00000006, 'loc_10D50'),
        (0x00000007, 'loc_10D5D'),
        (0x00000008, 'loc_10D6A'),
        (0x00000009, 'loc_10D77'),
        (0x0000000A, 'loc_10D84'),
        (0x0000000B, 'loc_10D91'),
        (0x0000000C, 'loc_10D9E'),
        (0x0000000D, 'loc_10DAB'),
        (0x0000000F, 'loc_10DB8'),
        (0x00000010, 'loc_10DC5'),
        (0x00000011, 'loc_10DD2'),
        (0x00000012, 'loc_10DDF'),
        (0x00000013, 'loc_10DEC'),
        (0x00000014, 'loc_10DF9'),
        (0x00000015, 'loc_10E06'),
        (0x00000016, 'loc_10E13'),
        (0x00000017, 'loc_10E20'),
        (0x00000019, 'loc_10E2D'),
        (-1, 'loc_10E3A'),
    )

    def _loc_10C30(): pass

    label('loc_10C30')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['奧蕾莉亞將軍'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['喬治'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x10000000)
    MenuChrFlagCmd(0x00, ChrTable['遊擊士托瓦爾'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10CF5(): pass

    label('loc_10CF5')

    MenuChrFlagCmd(0x01, 0xFFFF, 0x10000000)

    Jump('loc_10E43')

    def _loc_10D02(): pass

    label('loc_10D02')

    MenuChrFlagCmd(0x02, ChrTable['黎恩'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D0F(): pass

    label('loc_10D0F')

    MenuChrFlagCmd(0x02, ChrTable['尤娜'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D1C(): pass

    label('loc_10D1C')

    MenuChrFlagCmd(0x02, ChrTable['庫爾特'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D29(): pass

    label('loc_10D29')

    MenuChrFlagCmd(0x02, ChrTable['亞爾緹娜'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D36(): pass

    label('loc_10D36')

    MenuChrFlagCmd(0x02, ChrTable['亞修'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D43(): pass

    label('loc_10D43')

    MenuChrFlagCmd(0x02, ChrTable['繆潔'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D50(): pass

    label('loc_10D50')

    MenuChrFlagCmd(0x02, ChrTable['亞莉莎'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D5D(): pass

    label('loc_10D5D')

    MenuChrFlagCmd(0x02, ChrTable['艾略特'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D6A(): pass

    label('loc_10D6A')

    MenuChrFlagCmd(0x02, ChrTable['勞拉'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D77(): pass

    label('loc_10D77')

    MenuChrFlagCmd(0x02, ChrTable['馬奇亞斯'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D84(): pass

    label('loc_10D84')

    MenuChrFlagCmd(0x02, ChrTable['艾瑪'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D91(): pass

    label('loc_10D91')

    MenuChrFlagCmd(0x02, ChrTable['尤西斯'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10D9E(): pass

    label('loc_10D9E')

    MenuChrFlagCmd(0x02, ChrTable['菲'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DAB(): pass

    label('loc_10DAB')

    MenuChrFlagCmd(0x02, ChrTable['蓋烏斯'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DB8(): pass

    label('loc_10DB8')

    MenuChrFlagCmd(0x02, ChrTable['莎拉'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DC5(): pass

    label('loc_10DC5')

    MenuChrFlagCmd(0x02, ChrTable['奧蕾莉亞將軍'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DD2(): pass

    label('loc_10DD2')

    MenuChrFlagCmd(0x02, ChrTable['阿加特'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DDF(): pass

    label('loc_10DDF')

    MenuChrFlagCmd(0x02, ChrTable['安潔莉卡'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DEC(): pass

    label('loc_10DEC')

    MenuChrFlagCmd(0x02, ChrTable['喬治'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10DF9(): pass

    label('loc_10DF9')

    MenuChrFlagCmd(0x02, ChrTable['提妲'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10E06(): pass

    label('loc_10E06')

    MenuChrFlagCmd(0x02, ChrTable['緹歐'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10E13(): pass

    label('loc_10E13')

    MenuChrFlagCmd(0x02, ChrTable['雪倫'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10E20(): pass

    label('loc_10E20')

    MenuChrFlagCmd(0x02, ChrTable['克洛'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10E2D(): pass

    label('loc_10E2D')

    MenuChrFlagCmd(0x02, ChrTable['遊擊士托瓦爾'], 0x10000000)

    Jump('loc_10E43')

    def _loc_10E3A(): pass

    label('loc_10E3A')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10E43(): pass

    label('loc_10E43')

    Jump('loc_10535')

    def _loc_10E48(): pass

    label('loc_10E48')

    MenuCmd(0x03, 1)

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0x10E58
@scena.Code('SelectFlag')
def SelectFlag():
    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushValueByIndex, 0xC),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_13(0x00000002)
    OP_13(0x00000004)

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_10E71(): pass

    label('loc_10E71')

    If(
        (
            (Expr.PushVar, 0xF6),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11178',
    )

    MenuCreate(0, 30, 24.0, 99)
    MenuAddItem(0, '一般・序　　～第Ⅰ部（パーティ＆フラグ設定）', 0x00000069)
    MenuAddItem(0, '一般・断章　～第Ⅱ部（パーティ＆フラグ設定）', 0x0000006A)
    MenuAddItem(0, '一般・第Ⅲ部～最終幕（パーティ＆フラグ設定）', 0x0000006B)
    MenuAddItem(0, '一般・序　　～第Ⅰ部（フラグのみ設定）', 0x00000064)
    MenuAddItem(0, '一般・断章　～第Ⅱ部（フラグのみ設定）', 0x00000065)
    MenuAddItem(0, '一般・第Ⅲ部～最終幕（フラグのみ設定）', 0x00000066)
    MenuAddItem(0, '絆フラグ系', 0x0000006C)
    MenuAddItem(0, '一人操作モードを解除しパーティを更新する', 0x00000068)
    MenuAddItem(0, 'NPC非作成モードを解除しマップを読み直す', 0x0000006D)
    MenuSetPos(0, 0x01, 24, 24, 0x00)
    MenuShow(0, 0xF6)

    Switch(
        (
            (Expr.PushVar, 0xF6),
            Expr.Return,
        ),
        (0x00000064, 'loc_1112F'),
        (0x00000065, 'loc_1112F'),
        (0x00000066, 'loc_1112F'),
        (0x00000069, 'loc_1112F'),
        (0x0000006A, 'loc_1112F'),
        (0x0000006B, 'loc_1112F'),
        (0x00000067, 'loc_1112F'),
        (0x0000006C, 'loc_1112F'),
        (0x00000068, 'loc_1114E'),
        (0x0000006D, 'loc_11156'),
        (-1, 'loc_1116A'),
    )

    def _loc_1112F(): pass

    label('loc_1112F')

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushVar, 0xF6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'SelectFlag_Ippan')

    Jump('loc_11173')

    def _loc_1114E(): pass

    label('loc_1114E')

    FormationCtrl(0x1C, 0x01)

    Jump('loc_11173')

    def _loc_11156(): pass

    label('loc_11156')

    ClearScenaFlags(ScenaFlag(0x0061, 0, 0x308))
    MapJump((0xDD, 'reload'), (0xDD, ''), 0x00)

    Jump('loc_11173')

    def _loc_1116A(): pass

    label('loc_1116A')

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11173(): pass

    label('loc_11173')

    Jump('loc_10E71')

    def _loc_11178(): pass

    label('loc_11178')

    MenuCmd(0x03, 0)

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_08(
        0x0C,
        (
            (Expr.PushReg, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000C offset: 0x1118C
@scena.Code('SelectFlag_Ippan')
def SelectFlag_Ippan():
    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11198(): pass

    label('loc_11198')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1383B',
    )

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_111EF'),
        (0x00000069, 'loc_111EF'),
        (0x00000065, 'loc_11852'),
        (0x0000006A, 'loc_11852'),
        (0x00000066, 'loc_11E7A'),
        (0x0000006B, 'loc_11E7A'),
        (0x0000006C, 'loc_12462'),
        (0x00000067, 'loc_13766'),
        (-1, 'loc_13836'),
    )

    def _loc_111EF(): pass

    label('loc_111EF')

    MenuCreate(1, 0, 24.0, 0)
    MenuAddItem(1, '▼序①オルキスタワー攻略', 0x00000019)
    MenuAddItem(1, '▼序②分校宿舎をさまよう（夜・ユウナの夢）', 0x00000028)
    MenuAddItem(1, '▼序③隠れ里エリンを回る', 0x00000039)
    MenuAddItem(1, '▼第Ⅰ部00サングラール迷宮で訓練する', 0x00001004)
    MenuAddItem(1, '▼第Ⅰ部01サザ面①セントアーク潜入', 0x00001012)
    MenuAddItem(1, '▼第Ⅰ部01サザ面②カイリと再会しパルムへ', 0x00001020)
    MenuAddItem(1, '▼第Ⅰ部01サザ面③パブロと再会しタイタス門へ', 0x0000102A)
    MenuAddItem(1, '▼第Ⅰ部01サザ面④ハーメル廃村へ向かう', 0x00001031)
    MenuAddItem(1, '▼第Ⅰ部01★休息日１（クルト）', 0x00001052)
    MenuAddItem(1, '▼第Ⅰ部02ラマ面①ミルサンテ潜入', 0x00001056)
    MenuAddItem(1, '▼第Ⅰ部02ラマ面②ラクウェルで情報収集', 0x00001061)
    MenuAddItem(1, '▼第Ⅰ部02ラマ面③北部峡谷道を調べる', 0x00001065)
    MenuAddItem(1, '▼第Ⅰ部02ラマ面④エーデルと再会しアルスターを回る', 0x0000106C)
    MenuAddItem(1, '▽第Ⅰ部02ラマ面⑤オスギリアス盆地へ向かう', 0x00001071)
    MenuAddItem(1, '▼第Ⅰ部02★休息日２（ユウナ）', 0x00001082)
    MenuAddItem(1, '▼第Ⅰ部03クロ面①山猫号Ⅱ探索', 0x00001086)
    MenuAddItem(1, '▼第Ⅰ部03クロ面②クロスベル市へ向かう', 0x00001091)
    MenuAddItem(1, '▼第Ⅰ部03クロ面③クロスベル市潜入', 0x0000109A)
    MenuAddItem(1, '▼第Ⅰ部03クロ面④ウルスラ医科大学へ向かう', 0x000010AB)
    MenuAddItem(1, '▼第Ⅰ部03クロ面⑤皇帝と謁見しミシュラムを目指す', 0x000010B8)
    MenuAddItem(1, '▼第Ⅰ部03クロ面⑥ミシュラムで情報収集', 0x000010BF)
    MenuAddItem(1, '▽第Ⅰ部03クロ面⑦湿地帯へ向かう', 0x000010C7)
    MenuAddItem(1, '　★序＆第Ⅰ部リセット', 0x00000000)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)
    MenuCmd(0x03, 1)

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_117A1',
    )

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1184D')

    def _loc_117A1(): pass

    label('loc_117A1')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_117C9',
    )

    Call(ScriptId.Current, 'Reset_FLG_ippan_1')

    Jump('loc_1184D')

    def _loc_117C9(): pass

    label('loc_117C9')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x1000),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_117EF',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_00')

    Jump('loc_11810')

    def _loc_117EF(): pass

    label('loc_117EF')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x2000),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11810',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_01')

    def _loc_11810(): pass

    label('loc_11810')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x69),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11844',
    )

    Call(ScriptId.Current, 'EV_Party_Set', (0xFF, 0x0, 0x0))
    OP_43(0x64, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)

    def _loc_11844(): pass

    label('loc_11844')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1184D(): pass

    label('loc_1184D')

    Jump('loc_13836')

    def _loc_11852(): pass

    label('loc_11852')

    MenuCreate(1, 0, 24.0, 0)
    MenuAddItem(1, '▼断章01★休息日３（アルティナ）', 0x00002008)
    MenuAddItem(1, '▼断章02①黒の工房攻略', 0x00002019)
    MenuAddItem(1, '▽断章02②クロウ・デュバリィが合流した', 0x00002021)
    MenuAddItem(1, '▼第Ⅱ部00出立の準備', 0x00003006)
    MenuAddItem(1, '▼第Ⅱ部01ブリ編①メルカバ捌号機探索', 0x0000300C)
    MenuAddItem(1, '▼第Ⅱ部01ブリ編②陽霊窟攻略', 0x00003011)
    MenuAddItem(1, '▼第Ⅱ部02オル編①★帝国各地を回る１', 0x00003030)
    MenuAddItem(1, '▼第Ⅱ部02オル編②オルディス潜入', 0x00003036)
    MenuAddItem(1, '▽第Ⅱ部02オル編③地下水道から城館へ浸入する', 0x0000303D)
    MenuAddItem(1, '▼第Ⅱ部03ドレ編①★帝国各地を回る２', 0x00003062)
    MenuAddItem(1, '▼第Ⅱ部03ドレ編②セントアーク潜入', 0x00003069)
    MenuAddItem(1, '▽第Ⅱ部03ドレ編③ドレックノール要塞潜入準備', 0x0000306D)
    MenuAddItem(1, '▼第Ⅱ部03ドレ編④ドレックノール要塞攻略', 0x00003074)
    MenuAddItem(1, '▼第Ⅱ部04リー編①★帝国各地を回る３', 0x00003092)
    MenuAddItem(1, '▼第Ⅱ部04リー編②リーヴス潜入', 0x00003099)
    MenuAddItem(1, '▼第Ⅱ部04リー編③人気のないリーヴス', 0x000030A0)
    MenuAddItem(1, '▼第Ⅱ部04リー編④第二分校攻略', 0x000030A6)
    MenuAddItem(1, '▼第Ⅱ部04リー編⑤アインヘル小要塞攻略', 0x000030B4)
    MenuAddItem(1, '▼第Ⅱ部05パン編①★帝国各地を回る４', 0x000030D2)
    MenuAddItem(1, '▼第Ⅱ部05パン編②パンタグリュエル探索', 0x000030D9)
    MenuAddItem(1, '▼第Ⅱ部05パン編③各国首脳に挨拶する', 0x000030DB)
    MenuAddItem(1, '▼第Ⅱ部05パン編④パンタグリュエル迎撃戦', 0x000030E1)
    MenuAddItem(1, '　★断章＆第Ⅱ部リセット', 0x00000000)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)
    MenuCmd(0x03, 1)

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11DC8',
    )

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_11E75')

    def _loc_11DC8(): pass

    label('loc_11DC8')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11DF0',
    )

    Call(ScriptId.Current, 'Reset_FLG_ippan_2')

    Jump('loc_11E75')

    def _loc_11DF0(): pass

    label('loc_11DF0')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x3000),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11E17',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_01X')

    Jump('loc_11E38')

    def _loc_11E17(): pass

    label('loc_11E17')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x4000),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_11E38',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_02')

    def _loc_11E38(): pass

    label('loc_11E38')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6A),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11E6C',
    )

    Call(ScriptId.Current, 'EV_Party_Set', (0xFF, 0x0, 0x0))
    OP_43(0x64, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)

    def _loc_11E6C(): pass

    label('loc_11E6C')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_11E75(): pass

    label('loc_11E75')

    Jump('loc_13836')

    def _loc_11E7A(): pass

    label('loc_11E7A')

    MenuCreate(1, 0, 24.0, 0)
    MenuAddItem(1, '▼第Ⅲ部00カレイジャスⅡ探索', 0x0000400D)
    MenuAddItem(1, '▼第Ⅲ部01月霊編・月の霊場攻略', 0x0000400F)
    MenuAddItem(1, '▼第Ⅲ部02ガル編①★帝国各地を回る５', 0x00004032)
    MenuAddItem(1, '▽第Ⅲ部02ガル編③ガルガンチュア攻略', 0x0000403C)
    MenuAddItem(1, '▽第Ⅲ部02ガル編④ガルガンチュアを制圧した', 0x00004062)
    MenuAddItem(1, '▽第Ⅲ部03龍霊編・龍の霊場攻略', 0x00004065)
    MenuAddItem(1, '▽第Ⅲ部04裏オ編①★帝国各地を回る６', 0x00004082)
    MenuAddItem(1, '▽第Ⅲ部04裏オ編②オルキスタワー潜入作戦準備', 0x00004089)
    MenuAddItem(1, '▽第Ⅲ部04裏オ編③ジオフロントＸ～オルキスタワー攻略', 0x00004096)
    MenuAddItem(1, '▽第Ⅲ部05星霊編①公演＆攻略後の小休止', 0x000040B2)
    MenuAddItem(1, '▽第Ⅲ部05星霊編②星の霊場攻略', 0x000040B6)
    MenuAddItem(1, '▼前日譚・夜のテーマパークを楽しむ（夜）', 0x00005011)
    MenuAddItem(1, '☆リィンが剣聖になる', 0x0000824B)
    MenuAddItem(1, '▼最終幕00★帝国各地を回る７', 0x00006006)
    MenuAddItem(1, '▼最終幕01塩の杭攻略', 0x00006029)
    MenuAddItem(1, '▼最終幕02幻想機動要塞攻略', 0x00006051)
    MenuAddItem(1, '▼クレア＆レクター撃破後', 0x00006059)
    MenuAddItem(1, '▼セドリック＆シャーリィ撃破後', 0x00006061)
    MenuAddItem(1, '▽マリアベル＆カンパネルラ撃破後', 0x00006066)
    MenuAddItem(1, '▼ルーファス＆アルベリヒ撃破後', 0x0000606E)
    MenuAddItem(1, '▽マクバーン撃破後', 0x00006075)
    MenuAddItem(1, '　★第Ⅲ部～最終幕リセット', 0x00000000)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)
    MenuCmd(0x03, 1)

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_12369',
    )

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1245D')

    def _loc_12369(): pass

    label('loc_12369')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12391',
    )

    Call(ScriptId.Current, 'Reset_FLG_ippan_3')

    Jump('loc_1245D')

    def _loc_12391(): pass

    label('loc_12391')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x5000),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_123B7',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_03')

    Jump('loc_12420')

    def _loc_123B7(): pass

    label('loc_123B7')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x6000),
            Expr.Lss,
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x824B),
            Expr.Equ,
            Expr.Or,
            Expr.Return,
        ),
        'loc_123E7',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_03X')

    Jump('loc_12420')

    def _loc_123E7(): pass

    label('loc_123E7')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0x6A00),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_1240D',
    )

    Call(ScriptId.Current, 'EV_DoJumpSet_04')

    Jump('loc_12420')

    def _loc_1240D(): pass

    label('loc_1240D')

    Call(ScriptId.Current, 'EV_DoJumpSet_05')

    def _loc_12420(): pass

    label('loc_12420')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x6B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12454',
    )

    Call(ScriptId.Current, 'EV_Party_Set', (0xFF, 0x0, 0x0))
    OP_43(0x64, 1000, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)

    def _loc_12454(): pass

    label('loc_12454')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1245D(): pass

    label('loc_1245D')

    Jump('loc_13836')

    def _loc_12462(): pass

    label('loc_12462')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1246B(): pass

    label('loc_1246B')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13755',
    )

    MenuCreate(1, 35, 24.0, 99)
    MenuAddItem(1, '#3C★絆イベント：最終誰もいなーい　　', 0x00000063)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B61, 2, 0x5B0A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：ユウナ・最終絆　　', 0x00000000, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B64, 1, 0x5B21)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：アルティナ・最終絆', 0x00000001, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B65, 4, 0x5B2C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：ミュゼ・最終絆　　', 0x00000002, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B67, 3, 0x5B3B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：アリサ・最終絆　　', 0x00000003, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B68, 6, 0x5B46)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：ラウラ・最終絆　　', 0x00000004, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6A, 7, 0x5B57)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：エマ・最終絆　　　', 0x00000005, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6C, 3, 0x5B63)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：フィー・最終絆　　', 0x00000006, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6F, 0, 0x5B78)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：サラ・最終絆　　　', 0x00000007, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6F, 6, 0x5B7E)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：トワ・最終絆　　　', 0x00000008, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B73, 1, 0x5B99)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：アルフィン・最終絆', 0x00000009, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B74, 1, 0x5BA1)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '#3C★絆イベント：エリゼ・最終絆　　', 0x0000000A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B61, 1, 0x5B09)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：ユウナ・アトラクション後', 0x0000000B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B64, 0, 0x5B20)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：アルティナ・アトラクション後　', 0x0000000C, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B65, 3, 0x5B2B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：ミュゼ・アトラクション後　', 0x0000000D, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B67, 2, 0x5B3A)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：アリサ・アトラクション後　　', 0x0000000E, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B68, 5, 0x5B45)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：ラウラ・アトラクション後　　', 0x0000000F, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6A, 6, 0x5B56)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：エマ・アトラクション後　　　', 0x00000010, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6C, 2, 0x5B62)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：フィー・アトラクション後　　', 0x00000011, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6E, 7, 0x5B77)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：サラ・アトラクション後　　　', 0x00000012, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6F, 5, 0x5B7D)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：トワ・アトラクション後　　　', 0x00000013, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B73, 0, 0x5B98)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：アルフィン・前日譚・誘われる　', 0x00000014, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B74, 0, 0x5BA0)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：エリゼ・前日譚・誘いを受ける　', 0x00000015, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B62, 4, 0x5B14)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：クルト・アトラクション後　　　', 0x00000016, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B66, 4, 0x5B34)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：アッシュ・アトラクション後　　', 0x00000017, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B68, 0, 0x5B40)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：エリオット・アトラクション後　', 0x00000018, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B69, 3, 0x5B4B)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：マキアス・アトラクション後　　', 0x00000019, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6B, 4, 0x5B5C)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：ユーシス・アトラクション後　　', 0x0000001A, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6C, 7, 0x5B67)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：ガイウス・アトラクション後　　', 0x0000001B, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B6E, 0, 0x5B70)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：クロウ・アトラクション後　　　', 0x0000001C, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B70, 6, 0x5B86)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：デュバリィ・アトラクション後　', 0x0000001D, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0B72, 1, 0x5B91)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 1, '絆イベント：セリーヌ・アトラクション後　　', 0x0000001E, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuAddItem(1, '絆イベント：アトラクション全部取得　\x09\x09　', 0x00000064)
    MenuAddItem(1, '絆イベント：アトラクション全部消す　\x09\x09　', 0x00000065)
    MenuAddItem(1, '絆イベント：通常絆フラグ全部取得　\x09\x09　', 0x00000066)
    MenuAddItem(1, '絆イベント：通常絆フラグ全部消す　\x09\x09　', 0x00000067)
    MenuSetPos(1, 0x01, 24, 24, 0x01)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000063, 'loc_13141'),
        (0x00000000, 'loc_13167'),
        (0x00000001, 'loc_1318D'),
        (0x00000002, 'loc_131B3'),
        (0x00000003, 'loc_131D9'),
        (0x00000004, 'loc_131FF'),
        (0x00000005, 'loc_13225'),
        (0x00000006, 'loc_1324B'),
        (0x00000007, 'loc_13271'),
        (0x00000008, 'loc_13297'),
        (0x00000009, 'loc_132BD'),
        (0x0000000A, 'loc_132E3'),
        (0x0000000B, 'loc_13309'),
        (0x0000000C, 'loc_13311'),
        (0x0000000D, 'loc_13319'),
        (0x0000000E, 'loc_13321'),
        (0x0000000F, 'loc_13329'),
        (0x00000010, 'loc_13331'),
        (0x00000011, 'loc_13339'),
        (0x00000012, 'loc_13341'),
        (0x00000013, 'loc_13349'),
        (0x00000014, 'loc_13351'),
        (0x00000015, 'loc_13359'),
        (0x00000016, 'loc_13361'),
        (0x00000017, 'loc_13369'),
        (0x00000018, 'loc_13371'),
        (0x00000019, 'loc_13379'),
        (0x0000001A, 'loc_13381'),
        (0x0000001B, 'loc_13389'),
        (0x0000001C, 'loc_13391'),
        (0x0000001D, 'loc_13399'),
        (0x0000001E, 'loc_133A1'),
        (0x00000064, 'loc_133A9'),
        (0x00000065, 'loc_133EA'),
        (0x00000066, 'loc_1342B'),
        (0x00000067, 'loc_135B9'),
        (-1, 'loc_13747'),
    )

    def _loc_13141(): pass

    label('loc_13141')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_13167(): pass

    label('loc_13167')

    SetScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_1318D(): pass

    label('loc_1318D')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    SetScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_131B3(): pass

    label('loc_131B3')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    SetScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_131D9(): pass

    label('loc_131D9')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    SetScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_131FF(): pass

    label('loc_131FF')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    SetScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_13225(): pass

    label('loc_13225')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    SetScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_1324B(): pass

    label('loc_1324B')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    SetScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_13271(): pass

    label('loc_13271')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    SetScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_13297(): pass

    label('loc_13297')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    SetScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_132BD(): pass

    label('loc_132BD')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    SetScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    ClearScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_132E3(): pass

    label('loc_132E3')

    ClearScenaFlags(ScenaFlag(0x0B61, 2, 0x5B0A))
    ClearScenaFlags(ScenaFlag(0x0B64, 1, 0x5B21))
    ClearScenaFlags(ScenaFlag(0x0B65, 4, 0x5B2C))
    ClearScenaFlags(ScenaFlag(0x0B67, 3, 0x5B3B))
    ClearScenaFlags(ScenaFlag(0x0B68, 6, 0x5B46))
    ClearScenaFlags(ScenaFlag(0x0B6A, 7, 0x5B57))
    ClearScenaFlags(ScenaFlag(0x0B6C, 3, 0x5B63))
    ClearScenaFlags(ScenaFlag(0x0B6F, 0, 0x5B78))
    ClearScenaFlags(ScenaFlag(0x0B6F, 6, 0x5B7E))
    ClearScenaFlags(ScenaFlag(0x0B73, 1, 0x5B99))
    SetScenaFlags(ScenaFlag(0x0B74, 1, 0x5BA1))

    Jump('loc_13750')

    def _loc_13309(): pass

    label('loc_13309')

    XorScenaFlags(ScenaFlag(0x0B61, 1, 0x5B09))

    Jump('loc_13750')

    def _loc_13311(): pass

    label('loc_13311')

    XorScenaFlags(ScenaFlag(0x0B64, 0, 0x5B20))

    Jump('loc_13750')

    def _loc_13319(): pass

    label('loc_13319')

    XorScenaFlags(ScenaFlag(0x0B65, 3, 0x5B2B))

    Jump('loc_13750')

    def _loc_13321(): pass

    label('loc_13321')

    XorScenaFlags(ScenaFlag(0x0B67, 2, 0x5B3A))

    Jump('loc_13750')

    def _loc_13329(): pass

    label('loc_13329')

    XorScenaFlags(ScenaFlag(0x0B68, 5, 0x5B45))

    Jump('loc_13750')

    def _loc_13331(): pass

    label('loc_13331')

    XorScenaFlags(ScenaFlag(0x0B6A, 6, 0x5B56))

    Jump('loc_13750')

    def _loc_13339(): pass

    label('loc_13339')

    XorScenaFlags(ScenaFlag(0x0B6C, 2, 0x5B62))

    Jump('loc_13750')

    def _loc_13341(): pass

    label('loc_13341')

    XorScenaFlags(ScenaFlag(0x0B6E, 7, 0x5B77))

    Jump('loc_13750')

    def _loc_13349(): pass

    label('loc_13349')

    XorScenaFlags(ScenaFlag(0x0B6F, 5, 0x5B7D))

    Jump('loc_13750')

    def _loc_13351(): pass

    label('loc_13351')

    XorScenaFlags(ScenaFlag(0x0B73, 0, 0x5B98))

    Jump('loc_13750')

    def _loc_13359(): pass

    label('loc_13359')

    XorScenaFlags(ScenaFlag(0x0B74, 0, 0x5BA0))

    Jump('loc_13750')

    def _loc_13361(): pass

    label('loc_13361')

    XorScenaFlags(ScenaFlag(0x0B62, 4, 0x5B14))

    Jump('loc_13750')

    def _loc_13369(): pass

    label('loc_13369')

    XorScenaFlags(ScenaFlag(0x0B66, 4, 0x5B34))

    Jump('loc_13750')

    def _loc_13371(): pass

    label('loc_13371')

    XorScenaFlags(ScenaFlag(0x0B68, 0, 0x5B40))

    Jump('loc_13750')

    def _loc_13379(): pass

    label('loc_13379')

    XorScenaFlags(ScenaFlag(0x0B69, 3, 0x5B4B))

    Jump('loc_13750')

    def _loc_13381(): pass

    label('loc_13381')

    XorScenaFlags(ScenaFlag(0x0B6B, 4, 0x5B5C))

    Jump('loc_13750')

    def _loc_13389(): pass

    label('loc_13389')

    XorScenaFlags(ScenaFlag(0x0B6C, 7, 0x5B67))

    Jump('loc_13750')

    def _loc_13391(): pass

    label('loc_13391')

    XorScenaFlags(ScenaFlag(0x0B6E, 0, 0x5B70))

    Jump('loc_13750')

    def _loc_13399(): pass

    label('loc_13399')

    XorScenaFlags(ScenaFlag(0x0B70, 6, 0x5B86))

    Jump('loc_13750')

    def _loc_133A1(): pass

    label('loc_133A1')

    XorScenaFlags(ScenaFlag(0x0B72, 1, 0x5B91))

    Jump('loc_13750')

    def _loc_133A9(): pass

    label('loc_133A9')

    SetScenaFlags(ScenaFlag(0x0B61, 1, 0x5B09))
    SetScenaFlags(ScenaFlag(0x0B64, 0, 0x5B20))
    SetScenaFlags(ScenaFlag(0x0B65, 3, 0x5B2B))
    SetScenaFlags(ScenaFlag(0x0B67, 2, 0x5B3A))
    SetScenaFlags(ScenaFlag(0x0B68, 5, 0x5B45))
    SetScenaFlags(ScenaFlag(0x0B6A, 6, 0x5B56))
    SetScenaFlags(ScenaFlag(0x0B6C, 2, 0x5B62))
    SetScenaFlags(ScenaFlag(0x0B6E, 7, 0x5B77))
    SetScenaFlags(ScenaFlag(0x0B6F, 5, 0x5B7D))
    SetScenaFlags(ScenaFlag(0x0B73, 0, 0x5B98))
    SetScenaFlags(ScenaFlag(0x0B74, 0, 0x5BA0))
    SetScenaFlags(ScenaFlag(0x0B62, 4, 0x5B14))
    SetScenaFlags(ScenaFlag(0x0B66, 4, 0x5B34))
    SetScenaFlags(ScenaFlag(0x0B68, 0, 0x5B40))
    SetScenaFlags(ScenaFlag(0x0B69, 3, 0x5B4B))
    SetScenaFlags(ScenaFlag(0x0B6B, 4, 0x5B5C))
    SetScenaFlags(ScenaFlag(0x0B6C, 7, 0x5B67))
    SetScenaFlags(ScenaFlag(0x0B6E, 0, 0x5B70))
    SetScenaFlags(ScenaFlag(0x0B70, 6, 0x5B86))
    SetScenaFlags(ScenaFlag(0x0B72, 1, 0x5B91))

    Jump('loc_13750')

    def _loc_133EA(): pass

    label('loc_133EA')

    ClearScenaFlags(ScenaFlag(0x0B61, 1, 0x5B09))
    ClearScenaFlags(ScenaFlag(0x0B64, 0, 0x5B20))
    ClearScenaFlags(ScenaFlag(0x0B65, 3, 0x5B2B))
    ClearScenaFlags(ScenaFlag(0x0B67, 2, 0x5B3A))
    ClearScenaFlags(ScenaFlag(0x0B68, 5, 0x5B45))
    ClearScenaFlags(ScenaFlag(0x0B6A, 6, 0x5B56))
    ClearScenaFlags(ScenaFlag(0x0B6C, 2, 0x5B62))
    ClearScenaFlags(ScenaFlag(0x0B6E, 7, 0x5B77))
    ClearScenaFlags(ScenaFlag(0x0B6F, 5, 0x5B7D))
    ClearScenaFlags(ScenaFlag(0x0B73, 0, 0x5B98))
    ClearScenaFlags(ScenaFlag(0x0B74, 0, 0x5BA0))
    ClearScenaFlags(ScenaFlag(0x0B62, 4, 0x5B14))
    ClearScenaFlags(ScenaFlag(0x0B66, 4, 0x5B34))
    ClearScenaFlags(ScenaFlag(0x0B68, 0, 0x5B40))
    ClearScenaFlags(ScenaFlag(0x0B69, 3, 0x5B4B))
    ClearScenaFlags(ScenaFlag(0x0B6B, 4, 0x5B5C))
    ClearScenaFlags(ScenaFlag(0x0B6C, 7, 0x5B67))
    ClearScenaFlags(ScenaFlag(0x0B6E, 0, 0x5B70))
    ClearScenaFlags(ScenaFlag(0x0B70, 6, 0x5B86))
    ClearScenaFlags(ScenaFlag(0x0B72, 1, 0x5B91))

    Jump('loc_13750')

    def _loc_1342B(): pass

    label('loc_1342B')

    SetScenaFlags(ScenaFlag(0x0B60, 0, 0x5B00))
    SetScenaFlags(ScenaFlag(0x0B60, 1, 0x5B01))
    SetScenaFlags(ScenaFlag(0x0B60, 2, 0x5B02))
    SetScenaFlags(ScenaFlag(0x0B60, 3, 0x5B03))
    SetScenaFlags(ScenaFlag(0x0B60, 4, 0x5B04))
    SetScenaFlags(ScenaFlag(0x0B60, 5, 0x5B05))
    SetScenaFlags(ScenaFlag(0x0B60, 6, 0x5B06))
    SetScenaFlags(ScenaFlag(0x0B60, 7, 0x5B07))
    SetScenaFlags(ScenaFlag(0x0B61, 0, 0x5B08))
    SetScenaFlags(ScenaFlag(0x0B61, 3, 0x5B0B))
    SetScenaFlags(ScenaFlag(0x0B61, 4, 0x5B0C))
    SetScenaFlags(ScenaFlag(0x0B61, 5, 0x5B0D))
    SetScenaFlags(ScenaFlag(0x0B61, 6, 0x5B0E))
    SetScenaFlags(ScenaFlag(0x0B61, 7, 0x5B0F))
    SetScenaFlags(ScenaFlag(0x0B62, 0, 0x5B10))
    SetScenaFlags(ScenaFlag(0x0B62, 1, 0x5B11))
    SetScenaFlags(ScenaFlag(0x0B62, 2, 0x5B12))
    SetScenaFlags(ScenaFlag(0x0B62, 3, 0x5B13))
    SetScenaFlags(ScenaFlag(0x0B62, 5, 0x5B15))
    SetScenaFlags(ScenaFlag(0x0B62, 6, 0x5B16))
    SetScenaFlags(ScenaFlag(0x0B62, 7, 0x5B17))
    SetScenaFlags(ScenaFlag(0x0B63, 0, 0x5B18))
    SetScenaFlags(ScenaFlag(0x0B63, 1, 0x5B19))
    SetScenaFlags(ScenaFlag(0x0B63, 2, 0x5B1A))
    SetScenaFlags(ScenaFlag(0x0B63, 3, 0x5B1B))
    SetScenaFlags(ScenaFlag(0x0B63, 4, 0x5B1C))
    SetScenaFlags(ScenaFlag(0x0B63, 5, 0x5B1D))
    SetScenaFlags(ScenaFlag(0x0B63, 6, 0x5B1E))
    SetScenaFlags(ScenaFlag(0x0B63, 7, 0x5B1F))
    SetScenaFlags(ScenaFlag(0x0B64, 2, 0x5B22))
    SetScenaFlags(ScenaFlag(0x0B64, 3, 0x5B23))
    SetScenaFlags(ScenaFlag(0x0B64, 4, 0x5B24))
    SetScenaFlags(ScenaFlag(0x0B64, 5, 0x5B25))
    SetScenaFlags(ScenaFlag(0x0B64, 6, 0x5B26))
    SetScenaFlags(ScenaFlag(0x0B64, 7, 0x5B27))
    SetScenaFlags(ScenaFlag(0x0B65, 0, 0x5B28))
    SetScenaFlags(ScenaFlag(0x0B65, 1, 0x5B29))
    SetScenaFlags(ScenaFlag(0x0B65, 2, 0x5B2A))
    SetScenaFlags(ScenaFlag(0x0B65, 5, 0x5B2D))
    SetScenaFlags(ScenaFlag(0x0B65, 6, 0x5B2E))
    SetScenaFlags(ScenaFlag(0x0B65, 7, 0x5B2F))
    SetScenaFlags(ScenaFlag(0x0B66, 0, 0x5B30))
    SetScenaFlags(ScenaFlag(0x0B66, 1, 0x5B31))
    SetScenaFlags(ScenaFlag(0x0B66, 2, 0x5B32))
    SetScenaFlags(ScenaFlag(0x0B66, 3, 0x5B33))
    SetScenaFlags(ScenaFlag(0x0B66, 5, 0x5B35))
    SetScenaFlags(ScenaFlag(0x0B66, 6, 0x5B36))
    SetScenaFlags(ScenaFlag(0x0B66, 7, 0x5B37))
    SetScenaFlags(ScenaFlag(0x0B67, 0, 0x5B38))
    SetScenaFlags(ScenaFlag(0x0B67, 1, 0x5B39))
    SetScenaFlags(ScenaFlag(0x0B67, 4, 0x5B3C))
    SetScenaFlags(ScenaFlag(0x0B67, 5, 0x5B3D))
    SetScenaFlags(ScenaFlag(0x0B67, 6, 0x5B3E))
    SetScenaFlags(ScenaFlag(0x0B67, 7, 0x5B3F))
    SetScenaFlags(ScenaFlag(0x0B68, 1, 0x5B41))
    SetScenaFlags(ScenaFlag(0x0B68, 2, 0x5B42))
    SetScenaFlags(ScenaFlag(0x0B68, 3, 0x5B43))
    SetScenaFlags(ScenaFlag(0x0B68, 4, 0x5B44))
    SetScenaFlags(ScenaFlag(0x0B68, 7, 0x5B47))
    SetScenaFlags(ScenaFlag(0x0B69, 0, 0x5B48))
    SetScenaFlags(ScenaFlag(0x0B69, 1, 0x5B49))
    SetScenaFlags(ScenaFlag(0x0B69, 2, 0x5B4A))
    SetScenaFlags(ScenaFlag(0x0B69, 4, 0x5B4C))
    SetScenaFlags(ScenaFlag(0x0B69, 5, 0x5B4D))
    SetScenaFlags(ScenaFlag(0x0B69, 6, 0x5B4E))
    SetScenaFlags(ScenaFlag(0x0B69, 7, 0x5B4F))
    SetScenaFlags(ScenaFlag(0x0B6A, 0, 0x5B50))
    SetScenaFlags(ScenaFlag(0x0B6A, 1, 0x5B51))
    SetScenaFlags(ScenaFlag(0x0B6A, 2, 0x5B52))
    SetScenaFlags(ScenaFlag(0x0B6A, 3, 0x5B53))
    SetScenaFlags(ScenaFlag(0x0B6A, 4, 0x5B54))
    SetScenaFlags(ScenaFlag(0x0B6A, 5, 0x5B55))
    SetScenaFlags(ScenaFlag(0x0B6B, 0, 0x5B58))
    SetScenaFlags(ScenaFlag(0x0B6B, 1, 0x5B59))
    SetScenaFlags(ScenaFlag(0x0B6B, 2, 0x5B5A))
    SetScenaFlags(ScenaFlag(0x0B6B, 3, 0x5B5B))
    SetScenaFlags(ScenaFlag(0x0B6B, 5, 0x5B5D))
    SetScenaFlags(ScenaFlag(0x0B6B, 6, 0x5B5E))
    SetScenaFlags(ScenaFlag(0x0B6B, 7, 0x5B5F))
    SetScenaFlags(ScenaFlag(0x0B6C, 0, 0x5B60))
    SetScenaFlags(ScenaFlag(0x0B6C, 1, 0x5B61))
    SetScenaFlags(ScenaFlag(0x0B6C, 4, 0x5B64))
    SetScenaFlags(ScenaFlag(0x0B6C, 5, 0x5B65))
    SetScenaFlags(ScenaFlag(0x0B6C, 6, 0x5B66))
    SetScenaFlags(ScenaFlag(0x0B6D, 0, 0x5B68))
    SetScenaFlags(ScenaFlag(0x0B6D, 1, 0x5B69))
    SetScenaFlags(ScenaFlag(0x0B6D, 2, 0x5B6A))
    SetScenaFlags(ScenaFlag(0x0B6D, 3, 0x5B6B))
    SetScenaFlags(ScenaFlag(0x0B6D, 4, 0x5B6C))
    SetScenaFlags(ScenaFlag(0x0B6D, 5, 0x5B6D))
    SetScenaFlags(ScenaFlag(0x0B6D, 6, 0x5B6E))
    SetScenaFlags(ScenaFlag(0x0B6D, 7, 0x5B6F))
    SetScenaFlags(ScenaFlag(0x0B6E, 1, 0x5B71))
    SetScenaFlags(ScenaFlag(0x0B6E, 2, 0x5B72))
    SetScenaFlags(ScenaFlag(0x0B6E, 3, 0x5B73))
    SetScenaFlags(ScenaFlag(0x0B6E, 4, 0x5B74))
    SetScenaFlags(ScenaFlag(0x0B6E, 5, 0x5B75))
    SetScenaFlags(ScenaFlag(0x0B6E, 6, 0x5B76))
    SetScenaFlags(ScenaFlag(0x0B6F, 1, 0x5B79))
    SetScenaFlags(ScenaFlag(0x0B6F, 2, 0x5B7A))
    SetScenaFlags(ScenaFlag(0x0B6F, 3, 0x5B7B))
    SetScenaFlags(ScenaFlag(0x0B6F, 4, 0x5B7C))
    SetScenaFlags(ScenaFlag(0x0B6F, 7, 0x5B7F))
    SetScenaFlags(ScenaFlag(0x0B70, 0, 0x5B80))
    SetScenaFlags(ScenaFlag(0x0B70, 1, 0x5B81))
    SetScenaFlags(ScenaFlag(0x0B70, 2, 0x5B82))
    SetScenaFlags(ScenaFlag(0x0B70, 3, 0x5B83))
    SetScenaFlags(ScenaFlag(0x0B70, 4, 0x5B84))
    SetScenaFlags(ScenaFlag(0x0B70, 5, 0x5B85))
    SetScenaFlags(ScenaFlag(0x0B70, 7, 0x5B87))
    SetScenaFlags(ScenaFlag(0x0B71, 0, 0x5B88))
    SetScenaFlags(ScenaFlag(0x0B71, 1, 0x5B89))
    SetScenaFlags(ScenaFlag(0x0B71, 2, 0x5B8A))
    SetScenaFlags(ScenaFlag(0x0B71, 3, 0x5B8B))
    SetScenaFlags(ScenaFlag(0x0B71, 4, 0x5B8C))
    SetScenaFlags(ScenaFlag(0x0B71, 5, 0x5B8D))
    SetScenaFlags(ScenaFlag(0x0B71, 6, 0x5B8E))
    SetScenaFlags(ScenaFlag(0x0B71, 7, 0x5B8F))
    SetScenaFlags(ScenaFlag(0x0B72, 0, 0x5B90))
    SetScenaFlags(ScenaFlag(0x0B72, 2, 0x5B92))
    SetScenaFlags(ScenaFlag(0x0B72, 3, 0x5B93))
    SetScenaFlags(ScenaFlag(0x0B72, 4, 0x5B94))
    SetScenaFlags(ScenaFlag(0x0B72, 5, 0x5B95))
    SetScenaFlags(ScenaFlag(0x0B72, 6, 0x5B96))
    SetScenaFlags(ScenaFlag(0x0B72, 7, 0x5B97))
    SetScenaFlags(ScenaFlag(0x0B73, 2, 0x5B9A))
    SetScenaFlags(ScenaFlag(0x0B73, 3, 0x5B9B))
    SetScenaFlags(ScenaFlag(0x0B73, 4, 0x5B9C))
    SetScenaFlags(ScenaFlag(0x0B73, 5, 0x5B9D))
    SetScenaFlags(ScenaFlag(0x0B73, 6, 0x5B9E))
    SetScenaFlags(ScenaFlag(0x0B73, 7, 0x5B9F))

    Jump('loc_13750')

    def _loc_135B9(): pass

    label('loc_135B9')

    ClearScenaFlags(ScenaFlag(0x0B60, 0, 0x5B00))
    ClearScenaFlags(ScenaFlag(0x0B60, 1, 0x5B01))
    ClearScenaFlags(ScenaFlag(0x0B60, 2, 0x5B02))
    ClearScenaFlags(ScenaFlag(0x0B60, 3, 0x5B03))
    ClearScenaFlags(ScenaFlag(0x0B60, 4, 0x5B04))
    ClearScenaFlags(ScenaFlag(0x0B60, 5, 0x5B05))
    ClearScenaFlags(ScenaFlag(0x0B60, 6, 0x5B06))
    ClearScenaFlags(ScenaFlag(0x0B60, 7, 0x5B07))
    ClearScenaFlags(ScenaFlag(0x0B61, 0, 0x5B08))
    ClearScenaFlags(ScenaFlag(0x0B61, 3, 0x5B0B))
    ClearScenaFlags(ScenaFlag(0x0B61, 4, 0x5B0C))
    ClearScenaFlags(ScenaFlag(0x0B61, 5, 0x5B0D))
    ClearScenaFlags(ScenaFlag(0x0B61, 6, 0x5B0E))
    ClearScenaFlags(ScenaFlag(0x0B61, 7, 0x5B0F))
    ClearScenaFlags(ScenaFlag(0x0B62, 0, 0x5B10))
    ClearScenaFlags(ScenaFlag(0x0B62, 1, 0x5B11))
    ClearScenaFlags(ScenaFlag(0x0B62, 2, 0x5B12))
    ClearScenaFlags(ScenaFlag(0x0B62, 3, 0x5B13))
    ClearScenaFlags(ScenaFlag(0x0B62, 5, 0x5B15))
    ClearScenaFlags(ScenaFlag(0x0B62, 6, 0x5B16))
    ClearScenaFlags(ScenaFlag(0x0B62, 7, 0x5B17))
    ClearScenaFlags(ScenaFlag(0x0B63, 0, 0x5B18))
    ClearScenaFlags(ScenaFlag(0x0B63, 1, 0x5B19))
    ClearScenaFlags(ScenaFlag(0x0B63, 2, 0x5B1A))
    ClearScenaFlags(ScenaFlag(0x0B63, 3, 0x5B1B))
    ClearScenaFlags(ScenaFlag(0x0B63, 4, 0x5B1C))
    ClearScenaFlags(ScenaFlag(0x0B63, 5, 0x5B1D))
    ClearScenaFlags(ScenaFlag(0x0B63, 6, 0x5B1E))
    ClearScenaFlags(ScenaFlag(0x0B63, 7, 0x5B1F))
    ClearScenaFlags(ScenaFlag(0x0B64, 2, 0x5B22))
    ClearScenaFlags(ScenaFlag(0x0B64, 3, 0x5B23))
    ClearScenaFlags(ScenaFlag(0x0B64, 4, 0x5B24))
    ClearScenaFlags(ScenaFlag(0x0B64, 5, 0x5B25))
    ClearScenaFlags(ScenaFlag(0x0B64, 6, 0x5B26))
    ClearScenaFlags(ScenaFlag(0x0B64, 7, 0x5B27))
    ClearScenaFlags(ScenaFlag(0x0B65, 0, 0x5B28))
    ClearScenaFlags(ScenaFlag(0x0B65, 1, 0x5B29))
    ClearScenaFlags(ScenaFlag(0x0B65, 2, 0x5B2A))
    ClearScenaFlags(ScenaFlag(0x0B65, 5, 0x5B2D))
    ClearScenaFlags(ScenaFlag(0x0B65, 6, 0x5B2E))
    ClearScenaFlags(ScenaFlag(0x0B65, 7, 0x5B2F))
    ClearScenaFlags(ScenaFlag(0x0B66, 0, 0x5B30))
    ClearScenaFlags(ScenaFlag(0x0B66, 1, 0x5B31))
    ClearScenaFlags(ScenaFlag(0x0B66, 2, 0x5B32))
    ClearScenaFlags(ScenaFlag(0x0B66, 3, 0x5B33))
    ClearScenaFlags(ScenaFlag(0x0B66, 5, 0x5B35))
    ClearScenaFlags(ScenaFlag(0x0B66, 6, 0x5B36))
    ClearScenaFlags(ScenaFlag(0x0B66, 7, 0x5B37))
    ClearScenaFlags(ScenaFlag(0x0B67, 0, 0x5B38))
    ClearScenaFlags(ScenaFlag(0x0B67, 1, 0x5B39))
    ClearScenaFlags(ScenaFlag(0x0B67, 4, 0x5B3C))
    ClearScenaFlags(ScenaFlag(0x0B67, 5, 0x5B3D))
    ClearScenaFlags(ScenaFlag(0x0B67, 6, 0x5B3E))
    ClearScenaFlags(ScenaFlag(0x0B67, 7, 0x5B3F))
    ClearScenaFlags(ScenaFlag(0x0B68, 1, 0x5B41))
    ClearScenaFlags(ScenaFlag(0x0B68, 2, 0x5B42))
    ClearScenaFlags(ScenaFlag(0x0B68, 3, 0x5B43))
    ClearScenaFlags(ScenaFlag(0x0B68, 4, 0x5B44))
    ClearScenaFlags(ScenaFlag(0x0B68, 7, 0x5B47))
    ClearScenaFlags(ScenaFlag(0x0B69, 0, 0x5B48))
    ClearScenaFlags(ScenaFlag(0x0B69, 1, 0x5B49))
    ClearScenaFlags(ScenaFlag(0x0B69, 2, 0x5B4A))
    ClearScenaFlags(ScenaFlag(0x0B69, 4, 0x5B4C))
    ClearScenaFlags(ScenaFlag(0x0B69, 5, 0x5B4D))
    ClearScenaFlags(ScenaFlag(0x0B69, 6, 0x5B4E))
    ClearScenaFlags(ScenaFlag(0x0B69, 7, 0x5B4F))
    ClearScenaFlags(ScenaFlag(0x0B6A, 0, 0x5B50))
    ClearScenaFlags(ScenaFlag(0x0B6A, 1, 0x5B51))
    ClearScenaFlags(ScenaFlag(0x0B6A, 2, 0x5B52))
    ClearScenaFlags(ScenaFlag(0x0B6A, 3, 0x5B53))
    ClearScenaFlags(ScenaFlag(0x0B6A, 4, 0x5B54))
    ClearScenaFlags(ScenaFlag(0x0B6A, 5, 0x5B55))
    ClearScenaFlags(ScenaFlag(0x0B6B, 0, 0x5B58))
    ClearScenaFlags(ScenaFlag(0x0B6B, 1, 0x5B59))
    ClearScenaFlags(ScenaFlag(0x0B6B, 2, 0x5B5A))
    ClearScenaFlags(ScenaFlag(0x0B6B, 3, 0x5B5B))
    ClearScenaFlags(ScenaFlag(0x0B6B, 5, 0x5B5D))
    ClearScenaFlags(ScenaFlag(0x0B6B, 6, 0x5B5E))
    ClearScenaFlags(ScenaFlag(0x0B6B, 7, 0x5B5F))
    ClearScenaFlags(ScenaFlag(0x0B6C, 0, 0x5B60))
    ClearScenaFlags(ScenaFlag(0x0B6C, 1, 0x5B61))
    ClearScenaFlags(ScenaFlag(0x0B6C, 4, 0x5B64))
    ClearScenaFlags(ScenaFlag(0x0B6C, 5, 0x5B65))
    ClearScenaFlags(ScenaFlag(0x0B6C, 6, 0x5B66))
    ClearScenaFlags(ScenaFlag(0x0B6D, 0, 0x5B68))
    ClearScenaFlags(ScenaFlag(0x0B6D, 1, 0x5B69))
    ClearScenaFlags(ScenaFlag(0x0B6D, 2, 0x5B6A))
    ClearScenaFlags(ScenaFlag(0x0B6D, 3, 0x5B6B))
    ClearScenaFlags(ScenaFlag(0x0B6D, 4, 0x5B6C))
    ClearScenaFlags(ScenaFlag(0x0B6D, 5, 0x5B6D))
    ClearScenaFlags(ScenaFlag(0x0B6D, 6, 0x5B6E))
    ClearScenaFlags(ScenaFlag(0x0B6D, 7, 0x5B6F))
    ClearScenaFlags(ScenaFlag(0x0B6E, 1, 0x5B71))
    ClearScenaFlags(ScenaFlag(0x0B6E, 2, 0x5B72))
    ClearScenaFlags(ScenaFlag(0x0B6E, 3, 0x5B73))
    ClearScenaFlags(ScenaFlag(0x0B6E, 4, 0x5B74))
    ClearScenaFlags(ScenaFlag(0x0B6E, 5, 0x5B75))
    ClearScenaFlags(ScenaFlag(0x0B6E, 6, 0x5B76))
    ClearScenaFlags(ScenaFlag(0x0B6F, 1, 0x5B79))
    ClearScenaFlags(ScenaFlag(0x0B6F, 2, 0x5B7A))
    ClearScenaFlags(ScenaFlag(0x0B6F, 3, 0x5B7B))
    ClearScenaFlags(ScenaFlag(0x0B6F, 4, 0x5B7C))
    ClearScenaFlags(ScenaFlag(0x0B6F, 7, 0x5B7F))
    ClearScenaFlags(ScenaFlag(0x0B70, 0, 0x5B80))
    ClearScenaFlags(ScenaFlag(0x0B70, 1, 0x5B81))
    ClearScenaFlags(ScenaFlag(0x0B70, 2, 0x5B82))
    ClearScenaFlags(ScenaFlag(0x0B70, 3, 0x5B83))
    ClearScenaFlags(ScenaFlag(0x0B70, 4, 0x5B84))
    ClearScenaFlags(ScenaFlag(0x0B70, 5, 0x5B85))
    ClearScenaFlags(ScenaFlag(0x0B70, 7, 0x5B87))
    ClearScenaFlags(ScenaFlag(0x0B71, 0, 0x5B88))
    ClearScenaFlags(ScenaFlag(0x0B71, 1, 0x5B89))
    ClearScenaFlags(ScenaFlag(0x0B71, 2, 0x5B8A))
    ClearScenaFlags(ScenaFlag(0x0B71, 3, 0x5B8B))
    ClearScenaFlags(ScenaFlag(0x0B71, 4, 0x5B8C))
    ClearScenaFlags(ScenaFlag(0x0B71, 5, 0x5B8D))
    ClearScenaFlags(ScenaFlag(0x0B71, 6, 0x5B8E))
    ClearScenaFlags(ScenaFlag(0x0B71, 7, 0x5B8F))
    ClearScenaFlags(ScenaFlag(0x0B72, 0, 0x5B90))
    ClearScenaFlags(ScenaFlag(0x0B72, 2, 0x5B92))
    ClearScenaFlags(ScenaFlag(0x0B72, 3, 0x5B93))
    ClearScenaFlags(ScenaFlag(0x0B72, 4, 0x5B94))
    ClearScenaFlags(ScenaFlag(0x0B72, 5, 0x5B95))
    ClearScenaFlags(ScenaFlag(0x0B72, 6, 0x5B96))
    ClearScenaFlags(ScenaFlag(0x0B72, 7, 0x5B97))
    ClearScenaFlags(ScenaFlag(0x0B73, 2, 0x5B9A))
    ClearScenaFlags(ScenaFlag(0x0B73, 3, 0x5B9B))
    ClearScenaFlags(ScenaFlag(0x0B73, 4, 0x5B9C))
    ClearScenaFlags(ScenaFlag(0x0B73, 5, 0x5B9D))
    ClearScenaFlags(ScenaFlag(0x0B73, 6, 0x5B9E))
    ClearScenaFlags(ScenaFlag(0x0B73, 7, 0x5B9F))

    Jump('loc_13750')

    def _loc_13747(): pass

    label('loc_13747')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_13750(): pass

    label('loc_13750')

    Jump('loc_1246B')

    def _loc_13755(): pass

    label('loc_13755')

    MenuCmd(0x03, 1)

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13836')

    def _loc_13766(): pass

    label('loc_13766')

    MenuAddItem(1, '★全夏至祭イベントＯＮ', 0x00000065)
    MenuAddItem(1, '★全最終絆フラグＯＮ', 0x00000066)
    MenuAddItem(1, '★全クエストフラグＯＮ', 0x00000067)
    MenuSetPos(1, 0x01, 224, 24, 0x00)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000064, 'loc_13814'),
        (0x00000065, 'loc_13819'),
        (0x00000066, 'loc_1381E'),
        (0x00000067, 'loc_13823'),
        (-1, 'loc_13828'),
    )

    def _loc_13814(): pass

    label('loc_13814')

    Jump('loc_13828')

    def _loc_13819(): pass

    label('loc_13819')

    Jump('loc_13828')

    def _loc_1381E(): pass

    label('loc_1381E')

    Jump('loc_13828')

    def _loc_13823(): pass

    label('loc_13823')

    Jump('loc_13828')

    def _loc_13828(): pass

    label('loc_13828')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_13836')

    def _loc_13836(): pass

    label('loc_13836')

    Jump('loc_11198')

    def _loc_1383B(): pass

    label('loc_1383B')

    Return()

# id: 0x000D offset: 0x1383C
@scena.Code('Reset_FLG_ippan_1')
def Reset_FLG_ippan_1():
    OP_71(0x01, 0x2A00, 0x2AFF)
    OP_71(0x01, 0x3000, 0x34FF)

    Return()

# id: 0x000E offset: 0x1384C
@scena.Code('Reset_FLG_ippan_2')
def Reset_FLG_ippan_2():
    OP_71(0x01, 0x3600, 0x36FF)
    OP_71(0x01, 0x3C00, 0x40FF)

    Return()

# id: 0x000F offset: 0x1385C
@scena.Code('Reset_FLG_ippan_3')
def Reset_FLG_ippan_3():
    OP_71(0x01, 0x4600, 0x4AFF)
    OP_71(0x01, 0x4D00, 0x4EFF)
    OP_71(0x01, 0x5400, 0x58FF)
    OP_71(0x01, 0x5A00, 0x5AFF)

    Return()

# id: 0x0010 offset: 0x13878
@scena.Code('EV_Flag_Set_00_All')
def EV_Flag_Set_00_All():
    OP_71(0x00, 0x2900, 0x297F)
    SetScenaFlags(ScenaFlag(0x0534, 0, 0x29A0))
    SetScenaFlags(ScenaFlag(0x0534, 1, 0x29A1))
    OP_71(0x00, 0x29C0, 0x29CA)
    ClearScenaFlags(ScenaFlag(0x006B, 0, 0x358))
    SetScenaFlags(ScenaFlag(0x0BA4, 4, 0x5D24))
    SetScenaFlags(ScenaFlag(0x0076, 1, 0x3B1))
    SetScenaFlags(ScenaFlag(0x0076, 2, 0x3B2))
    SetScenaFlags(ScenaFlag(0x0076, 3, 0x3B3))
    SetScenaFlags(ScenaFlag(0x0076, 4, 0x3B4))
    SetScenaFlags(ScenaFlag(0x0076, 5, 0x3B5))
    SetScenaFlags(ScenaFlag(0x0077, 3, 0x3BB))
    ClearScenaFlags(ScenaFlag(0x006B, 0, 0x358))
    ClearScenaFlags(ScenaFlag(0x006E, 0, 0x370))
    ClearScenaFlags(ScenaFlag(0x006E, 3, 0x373))
    ClearScenaFlags(ScenaFlag(0x006E, 7, 0x377))
    Call(ScriptId.System, 'SetKisinChange_ValimarS0')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0011 offset: 0x138D0
@scena.Code('EV_Flag_Set_01_All')
def EV_Flag_Set_01_All():
    OP_71(0x00, 0x2B00, 0x2B11)
    OP_71(0x00, 0x2B20, 0x2B7D)
    OP_71(0x00, 0x2B90, 0x2BE1)
    OP_71(0x00, 0x2BF0, 0x2C8F)
    OP_71(0x00, 0x2D00, 0x2D04)
    SetScenaFlags(ScenaFlag(0x05A0, 5, 0x2D05))
    OP_71(0x00, 0x2D06, 0x2D0A)
    OP_71(0x00, 0x2D0B, 0x2D0C)
    OP_71(0x00, 0x2D0D, 0x2D0E)
    OP_71(0x00, 0x2D80, 0x2DB3)
    OP_71(0x00, 0x2F80, 0x2F98)
    QuestCtrl(0x0001, 0x05)
    QuestCtrl(0x0002, 0x05)
    QuestCtrl(0x0003, 0x05)
    QuestCtrl(0x0004, 0x05)
    QuestCtrl(0x0005, 0x05)
    QuestCtrl(0x0006, 0x05)
    QuestCtrl(0x0007, 0x05)
    QuestCtrl(0x0008, 0x05)
    QuestCtrl(0x0009, 0x05)
    QuestCtrl(0x000A, 0x05)
    QuestCtrl(0x000B, 0x05)
    QuestCtrl(0x000C, 0x05)
    ClearScenaFlags(ScenaFlag(0x006E, 1, 0x371))
    ClearScenaFlags(ScenaFlag(0x006E, 2, 0x372))
    ClearScenaFlags(ScenaFlag(0x006E, 4, 0x374))
    ClearScenaFlags(ScenaFlag(0x006E, 5, 0x375))
    ClearScenaFlags(ScenaFlag(0x006E, 6, 0x376))
    SetScenaFlags(ScenaFlag(0x0073, 2, 0x39A))
    Call(ScriptId.System, 'SetKisinChange_ValimarS0')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0012 offset: 0x13974
@scena.Code('EV_Flag_Set_01X_All')
def EV_Flag_Set_01X_All():
    OP_71(0x00, 0x3500, 0x357D)
    OP_71(0x00, 0x3590, 0x3591)
    SetScenaFlags(ScenaFlag(0x06B2, 2, 0x3592))
    OP_71(0x00, 0x35B0, 0x35B5)
    QuestCtrl(0x000D, 0x05)
    Call(ScriptId.System, 'SetKisinChange_ValimarS1')

    Return()

# id: 0x0013 offset: 0x139AC
@scena.Code('EV_Flag_Set_02_All')
def EV_Flag_Set_02_All():
    OP_71(0x00, 0x3700, 0x3739)
    OP_71(0x00, 0x3750, 0x3789)
    OP_71(0x00, 0x37A0, 0x37D7)
    OP_71(0x00, 0x3800, 0x385D)
    OP_71(0x00, 0x3880, 0x38D1)
    OP_71(0x00, 0x3900, 0x3904)
    OP_71(0x00, 0x390B, 0x390F)
    SetScenaFlags(ScenaFlag(0x0721, 4, 0x390C))
    OP_71(0x00, 0x3980, 0x399A)
    OP_71(0x00, 0x399D, 0x39D4)
    OP_71(0x00, 0x3B80, 0x3B86)
    QuestCtrl(0x000E, 0x05)
    QuestCtrl(0x000F, 0x05)
    QuestCtrl(0x0010, 0x05)
    QuestCtrl(0x0011, 0x05)
    QuestCtrl(0x0012, 0x05)
    QuestCtrl(0x0013, 0x05)
    QuestCtrl(0x0014, 0x05)
    QuestCtrl(0x0015, 0x05)
    QuestCtrl(0x0016, 0x05)
    QuestCtrl(0x0017, 0x05)
    QuestCtrl(0x0018, 0x05)
    QuestCtrl(0x0019, 0x05)
    QuestCtrl(0x001A, 0x05)
    QuestCtrl(0x001B, 0x05)
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    SetScenaFlags(ScenaFlag(0x0062, 1, 0x311))
    SetScenaFlags(ScenaFlag(0x0BAA, 2, 0x5D52))
    OP_13(0x00400000)
    Call(ScriptId.System, 'SetKisinChange_ValimarS1')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0014 offset: 0x13A54
@scena.Code('EV_Flag_Set_03_All')
def EV_Flag_Set_03_All():
    OP_71(0x00, 0x4100, 0x4137)
    OP_71(0x00, 0x4150, 0x4179)
    OP_71(0x00, 0x4190, 0x41AD)
    OP_71(0x00, 0x41C0, 0x41F9)
    OP_71(0x00, 0x4210, 0x423F)
    OP_71(0x00, 0x4301, 0x4302)
    OP_71(0x00, 0x4380, 0x439D)
    OP_71(0x00, 0x4580, 0x4582)
    QuestCtrl(0x001C, 0x05)
    QuestCtrl(0x001D, 0x05)
    QuestCtrl(0x001E, 0x05)
    QuestCtrl(0x001F, 0x05)
    QuestCtrl(0x0020, 0x05)
    QuestCtrl(0x0021, 0x05)
    QuestCtrl(0x0022, 0x05)
    QuestCtrl(0x0023, 0x05)
    QuestCtrl(0x0024, 0x05)
    QuestCtrl(0x0025, 0x05)
    QuestCtrl(0x0026, 0x05)
    QuestCtrl(0x0027, 0x05)
    QuestCtrl(0x0028, 0x05)
    SetScenaFlags(ScenaFlag(0x0BAA, 3, 0x5D53))
    SetScenaFlags(ScenaFlag(0x0BAA, 4, 0x5D54))
    Call(ScriptId.System, 'SetKisinChange_ValimarS2')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0015 offset: 0x13AE0
@scena.Code('EV_Flag_Set_03X_All')
def EV_Flag_Set_03X_All():
    OP_71(0x00, 0x4B00, 0x4B23)
    OP_71(0x00, 0x4C00, 0x4C0F)
    OP_71(0x00, 0x4C10, 0x4C13)
    OP_71(0x00, 0x5BB3, 0x5BB6)
    Call(ScriptId.System, 'SetKisinChange_ValimarS2')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))
    QuestCtrl(0x0029, 0x05)

    Return()

# id: 0x0016 offset: 0x13B1C
@scena.Code('EV_Flag_Set_04_All')
def EV_Flag_Set_04_All():
    OP_71(0x00, 0x4F00, 0x4FF5)
    OP_71(0x00, 0x5180, 0x5190)
    QuestCtrl(0x002A, 0x05)
    QuestCtrl(0x002B, 0x05)
    QuestCtrl(0x002C, 0x05)
    QuestCtrl(0x002D, 0x05)
    QuestCtrl(0x002E, 0x05)
    QuestCtrl(0x002F, 0x05)
    Call(ScriptId.System, 'SetKisinChange_ValimarS3')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0017 offset: 0x13B60
@scena.Code('EV_Flag_Set_05_All')
def EV_Flag_Set_05_All():
    OP_71(0x00, 0x5900, 0x5927)
    Call(ScriptId.System, 'SetKisinChange_ValimarS3')
    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    Return()

# id: 0x0018 offset: 0x13B88
@scena.Code('EV_Flag_Reset')
def EV_Flag_Reset():
    OP_71(0x01, 0x05D1, 0x05D6)
    OP_71(0x01, 0x2900, 0x2AFF)
    OP_71(0x01, 0x2B00, 0x34FF)
    OP_71(0x01, 0x3500, 0x36FF)
    OP_71(0x01, 0x3700, 0x40FF)
    OP_71(0x01, 0x4100, 0x4AFF)
    OP_71(0x01, 0x4B00, 0x4EFF)
    OP_71(0x01, 0x4F00, 0x58FF)
    OP_71(0x01, 0x5900, 0x5AFF)
    OP_71(0x01, 0x5B00, 0x5BFF)
    OP_71(0x01, 0x5C90, 0x5CAF)
    OP_71(0x01, 0x2F80, 0x2FFF)
    OP_71(0x01, 0x3B80, 0x3BFF)
    OP_71(0x01, 0x4580, 0x45FF)
    ClearScenaFlags(ScenaFlag(0x0BA4, 4, 0x5D24))
    SetScenaFlags(ScenaFlag(0x006E, 1, 0x371))
    SetScenaFlags(ScenaFlag(0x006E, 2, 0x372))
    SetScenaFlags(ScenaFlag(0x006E, 4, 0x374))
    SetScenaFlags(ScenaFlag(0x006E, 5, 0x375))
    SetScenaFlags(ScenaFlag(0x006E, 6, 0x376))
    ClearScenaFlags(ScenaFlag(0x0073, 2, 0x39A))
    ClearScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    ClearScenaFlags(ScenaFlag(0x0062, 1, 0x311))
    OP_14(0x00400000)
    ClearScenaFlags(ScenaFlag(0x0BAA, 2, 0x5D52))
    ClearScenaFlags(ScenaFlag(0x0BAA, 3, 0x5D53))
    ClearScenaFlags(ScenaFlag(0x0BAA, 4, 0x5D54))

    Return()

# id: 0x0019 offset: 0x13C08
@scena.Code('EV_DoJumpSet_00')
def EV_DoJumpSet_00():
    Call(ScriptId.Current, 'EV_Flag_Reset')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS0')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000040, 'loc_13E4A'),
        (0x0000003F, 'loc_13E50'),
        (0x0000003E, 'loc_13E56'),
        (0x0000003D, 'loc_13E5C'),
        (0x0000003C, 'loc_13E62'),
        (0x0000003B, 'loc_13E68'),
        (0x0000003A, 'loc_13E6E'),
        (0x00000039, 'loc_13E7D'),
        (0x00000038, 'loc_13E83'),
        (0x00000037, 'loc_13E89'),
        (0x00000036, 'loc_13E8F'),
        (0x00000035, 'loc_13E95'),
        (0x00000034, 'loc_13E9B'),
        (0x00000033, 'loc_13EA1'),
        (0x00000032, 'loc_13EA7'),
        (0x00000031, 'loc_13EAD'),
        (0x00000030, 'loc_13EB6'),
        (0x0000002F, 'loc_13EBC'),
        (0x0000002E, 'loc_13EC2'),
        (0x0000002D, 'loc_13ECB'),
        (0x0000002C, 'loc_13ED1'),
        (0x0000002B, 'loc_13ED7'),
        (0x0000002A, 'loc_13EDD'),
        (0x00000029, 'loc_13EE3'),
        (0x00000028, 'loc_13EE9'),
        (0x00000027, 'loc_13EEF'),
        (0x00000026, 'loc_13EF5'),
        (0x00000025, 'loc_13EFB'),
        (0x00000024, 'loc_13F01'),
        (0x00000023, 'loc_13F07'),
        (0x00000022, 'loc_13F0D'),
        (0x00000021, 'loc_13F13'),
        (0x00000020, 'loc_13F19'),
        (0x0000001F, 'loc_13F1F'),
        (0x0000001E, 'loc_13F25'),
        (0x0000001D, 'loc_13F2B'),
        (0x0000001C, 'loc_13F31'),
        (0x0000001B, 'loc_13F37'),
        (0x0000001A, 'loc_13F3D'),
        (0x00000019, 'loc_13F43'),
        (0x00000018, 'loc_13F49'),
        (0x00000017, 'loc_13F4F'),
        (0x00000016, 'loc_13F55'),
        (0x00000015, 'loc_13F5B'),
        (0x00000014, 'loc_13F61'),
        (0x00000013, 'loc_13F67'),
        (0x00000012, 'loc_13F6D'),
        (0x00000011, 'loc_13F73'),
        (0x00000010, 'loc_13F79'),
        (0x0000000F, 'loc_13F7F'),
        (0x0000000E, 'loc_13F85'),
        (0x0000000D, 'loc_13F8B'),
        (0x0000000C, 'loc_13F91'),
        (0x0000000B, 'loc_13F97'),
        (0x0000000A, 'loc_13F9D'),
        (0x00000009, 'loc_13FA3'),
        (0x00000008, 'loc_13FA9'),
        (0x00000007, 'loc_13FAF'),
        (0x00000006, 'loc_13FB5'),
        (0x00000005, 'loc_13FBB'),
        (0x00000004, 'loc_13FC1'),
        (0x00000003, 'loc_13FC7'),
        (0x00000002, 'loc_13FCD'),
        (0x00000001, 'loc_13FD3'),
        (-1, 'loc_13FDB'),
    )

    def _loc_13E4A(): pass

    label('loc_13E4A')

    SetScenaFlags(ScenaFlag(0x052F, 6, 0x297E))
    SetScenaFlags(ScenaFlag(0x052F, 5, 0x297D))

    def _loc_13E50(): pass

    label('loc_13E50')

    SetScenaFlags(ScenaFlag(0x052F, 4, 0x297C))
    SetScenaFlags(ScenaFlag(0x052F, 3, 0x297B))

    def _loc_13E56(): pass

    label('loc_13E56')

    SetScenaFlags(ScenaFlag(0x052F, 2, 0x297A))
    SetScenaFlags(ScenaFlag(0x052F, 1, 0x2979))

    def _loc_13E5C(): pass

    label('loc_13E5C')

    SetScenaFlags(ScenaFlag(0x052F, 0, 0x2978))
    SetScenaFlags(ScenaFlag(0x052E, 7, 0x2977))

    def _loc_13E62(): pass

    label('loc_13E62')

    SetScenaFlags(ScenaFlag(0x052E, 6, 0x2976))
    SetScenaFlags(ScenaFlag(0x052E, 5, 0x2975))

    def _loc_13E68(): pass

    label('loc_13E68')

    SetScenaFlags(ScenaFlag(0x052E, 4, 0x2974))
    SetScenaFlags(ScenaFlag(0x052E, 3, 0x2973))

    def _loc_13E6E(): pass

    label('loc_13E6E')

    SetScenaFlags(ScenaFlag(0x052E, 2, 0x2972))
    SetScenaFlags(ScenaFlag(0x0534, 1, 0x29A1))
    OP_71(0x00, 0x29C0, 0x29CA)
    SetScenaFlags(ScenaFlag(0x052E, 1, 0x2971))

    def _loc_13E7D(): pass

    label('loc_13E7D')

    SetScenaFlags(ScenaFlag(0x052E, 0, 0x2970))
    SetScenaFlags(ScenaFlag(0x052D, 7, 0x296F))

    def _loc_13E83(): pass

    label('loc_13E83')

    SetScenaFlags(ScenaFlag(0x052D, 6, 0x296E))
    SetScenaFlags(ScenaFlag(0x052D, 5, 0x296D))

    def _loc_13E89(): pass

    label('loc_13E89')

    SetScenaFlags(ScenaFlag(0x052D, 4, 0x296C))
    SetScenaFlags(ScenaFlag(0x052D, 3, 0x296B))

    def _loc_13E8F(): pass

    label('loc_13E8F')

    SetScenaFlags(ScenaFlag(0x052D, 2, 0x296A))
    SetScenaFlags(ScenaFlag(0x052D, 1, 0x2969))

    def _loc_13E95(): pass

    label('loc_13E95')

    SetScenaFlags(ScenaFlag(0x052D, 0, 0x2968))
    SetScenaFlags(ScenaFlag(0x052C, 7, 0x2967))

    def _loc_13E9B(): pass

    label('loc_13E9B')

    SetScenaFlags(ScenaFlag(0x052C, 6, 0x2966))
    SetScenaFlags(ScenaFlag(0x052C, 5, 0x2965))

    def _loc_13EA1(): pass

    label('loc_13EA1')

    SetScenaFlags(ScenaFlag(0x052C, 4, 0x2964))
    SetScenaFlags(ScenaFlag(0x052C, 3, 0x2963))

    def _loc_13EA7(): pass

    label('loc_13EA7')

    SetScenaFlags(ScenaFlag(0x052C, 2, 0x2962))
    SetScenaFlags(ScenaFlag(0x052C, 1, 0x2961))

    def _loc_13EAD(): pass

    label('loc_13EAD')

    SetScenaFlags(ScenaFlag(0x052C, 0, 0x2960))
    SetScenaFlags(ScenaFlag(0x052B, 7, 0x295F))
    SetScenaFlags(ScenaFlag(0x0534, 0, 0x29A0))

    def _loc_13EB6(): pass

    label('loc_13EB6')

    SetScenaFlags(ScenaFlag(0x052B, 6, 0x295E))
    SetScenaFlags(ScenaFlag(0x052B, 5, 0x295D))

    def _loc_13EBC(): pass

    label('loc_13EBC')

    SetScenaFlags(ScenaFlag(0x052B, 4, 0x295C))
    SetScenaFlags(ScenaFlag(0x052B, 3, 0x295B))

    def _loc_13EC2(): pass

    label('loc_13EC2')

    SetScenaFlags(ScenaFlag(0x052B, 2, 0x295A))
    SetScenaFlags(ScenaFlag(0x052B, 1, 0x2959))
    SetScenaFlags(ScenaFlag(0x0BA4, 4, 0x5D24))

    def _loc_13ECB(): pass

    label('loc_13ECB')

    SetScenaFlags(ScenaFlag(0x052B, 0, 0x2958))
    SetScenaFlags(ScenaFlag(0x052A, 7, 0x2957))

    def _loc_13ED1(): pass

    label('loc_13ED1')

    SetScenaFlags(ScenaFlag(0x052A, 6, 0x2956))
    SetScenaFlags(ScenaFlag(0x052A, 5, 0x2955))

    def _loc_13ED7(): pass

    label('loc_13ED7')

    SetScenaFlags(ScenaFlag(0x052A, 4, 0x2954))
    SetScenaFlags(ScenaFlag(0x052A, 3, 0x2953))

    def _loc_13EDD(): pass

    label('loc_13EDD')

    SetScenaFlags(ScenaFlag(0x052A, 2, 0x2952))
    SetScenaFlags(ScenaFlag(0x052A, 1, 0x2951))

    def _loc_13EE3(): pass

    label('loc_13EE3')

    SetScenaFlags(ScenaFlag(0x052A, 0, 0x2950))
    SetScenaFlags(ScenaFlag(0x0529, 7, 0x294F))

    def _loc_13EE9(): pass

    label('loc_13EE9')

    SetScenaFlags(ScenaFlag(0x0529, 6, 0x294E))
    SetScenaFlags(ScenaFlag(0x0529, 5, 0x294D))

    def _loc_13EEF(): pass

    label('loc_13EEF')

    SetScenaFlags(ScenaFlag(0x0529, 4, 0x294C))
    SetScenaFlags(ScenaFlag(0x0529, 3, 0x294B))

    def _loc_13EF5(): pass

    label('loc_13EF5')

    SetScenaFlags(ScenaFlag(0x0529, 2, 0x294A))
    SetScenaFlags(ScenaFlag(0x0529, 1, 0x2949))

    def _loc_13EFB(): pass

    label('loc_13EFB')

    SetScenaFlags(ScenaFlag(0x0529, 0, 0x2948))
    SetScenaFlags(ScenaFlag(0x0528, 7, 0x2947))

    def _loc_13F01(): pass

    label('loc_13F01')

    SetScenaFlags(ScenaFlag(0x0528, 6, 0x2946))
    SetScenaFlags(ScenaFlag(0x0528, 5, 0x2945))

    def _loc_13F07(): pass

    label('loc_13F07')

    SetScenaFlags(ScenaFlag(0x0528, 4, 0x2944))
    SetScenaFlags(ScenaFlag(0x0528, 3, 0x2943))

    def _loc_13F0D(): pass

    label('loc_13F0D')

    SetScenaFlags(ScenaFlag(0x0528, 2, 0x2942))
    SetScenaFlags(ScenaFlag(0x0528, 1, 0x2941))

    def _loc_13F13(): pass

    label('loc_13F13')

    SetScenaFlags(ScenaFlag(0x0528, 0, 0x2940))
    SetScenaFlags(ScenaFlag(0x0527, 7, 0x293F))

    def _loc_13F19(): pass

    label('loc_13F19')

    SetScenaFlags(ScenaFlag(0x0527, 6, 0x293E))
    SetScenaFlags(ScenaFlag(0x0527, 5, 0x293D))

    def _loc_13F1F(): pass

    label('loc_13F1F')

    SetScenaFlags(ScenaFlag(0x0527, 4, 0x293C))
    SetScenaFlags(ScenaFlag(0x0527, 3, 0x293B))

    def _loc_13F25(): pass

    label('loc_13F25')

    SetScenaFlags(ScenaFlag(0x0527, 2, 0x293A))
    SetScenaFlags(ScenaFlag(0x0527, 1, 0x2939))

    def _loc_13F2B(): pass

    label('loc_13F2B')

    SetScenaFlags(ScenaFlag(0x0527, 0, 0x2938))
    SetScenaFlags(ScenaFlag(0x0526, 7, 0x2937))

    def _loc_13F31(): pass

    label('loc_13F31')

    SetScenaFlags(ScenaFlag(0x0526, 6, 0x2936))
    SetScenaFlags(ScenaFlag(0x0526, 5, 0x2935))

    def _loc_13F37(): pass

    label('loc_13F37')

    SetScenaFlags(ScenaFlag(0x0526, 4, 0x2934))
    SetScenaFlags(ScenaFlag(0x0526, 3, 0x2933))

    def _loc_13F3D(): pass

    label('loc_13F3D')

    SetScenaFlags(ScenaFlag(0x0526, 2, 0x2932))
    SetScenaFlags(ScenaFlag(0x0526, 1, 0x2931))

    def _loc_13F43(): pass

    label('loc_13F43')

    SetScenaFlags(ScenaFlag(0x0526, 0, 0x2930))
    SetScenaFlags(ScenaFlag(0x0525, 7, 0x292F))

    def _loc_13F49(): pass

    label('loc_13F49')

    SetScenaFlags(ScenaFlag(0x0525, 6, 0x292E))
    SetScenaFlags(ScenaFlag(0x0525, 5, 0x292D))

    def _loc_13F4F(): pass

    label('loc_13F4F')

    SetScenaFlags(ScenaFlag(0x0525, 4, 0x292C))
    SetScenaFlags(ScenaFlag(0x0525, 3, 0x292B))

    def _loc_13F55(): pass

    label('loc_13F55')

    SetScenaFlags(ScenaFlag(0x0525, 2, 0x292A))
    SetScenaFlags(ScenaFlag(0x0525, 1, 0x2929))

    def _loc_13F5B(): pass

    label('loc_13F5B')

    SetScenaFlags(ScenaFlag(0x0525, 0, 0x2928))
    SetScenaFlags(ScenaFlag(0x0524, 7, 0x2927))

    def _loc_13F61(): pass

    label('loc_13F61')

    SetScenaFlags(ScenaFlag(0x0524, 6, 0x2926))
    SetScenaFlags(ScenaFlag(0x0524, 5, 0x2925))

    def _loc_13F67(): pass

    label('loc_13F67')

    SetScenaFlags(ScenaFlag(0x0524, 4, 0x2924))
    SetScenaFlags(ScenaFlag(0x0524, 3, 0x2923))

    def _loc_13F6D(): pass

    label('loc_13F6D')

    SetScenaFlags(ScenaFlag(0x0524, 2, 0x2922))
    SetScenaFlags(ScenaFlag(0x0524, 1, 0x2921))

    def _loc_13F73(): pass

    label('loc_13F73')

    SetScenaFlags(ScenaFlag(0x0524, 0, 0x2920))
    SetScenaFlags(ScenaFlag(0x0523, 7, 0x291F))

    def _loc_13F79(): pass

    label('loc_13F79')

    SetScenaFlags(ScenaFlag(0x0523, 6, 0x291E))
    SetScenaFlags(ScenaFlag(0x0523, 5, 0x291D))

    def _loc_13F7F(): pass

    label('loc_13F7F')

    SetScenaFlags(ScenaFlag(0x0523, 4, 0x291C))
    SetScenaFlags(ScenaFlag(0x0523, 3, 0x291B))

    def _loc_13F85(): pass

    label('loc_13F85')

    SetScenaFlags(ScenaFlag(0x0523, 2, 0x291A))
    SetScenaFlags(ScenaFlag(0x0523, 1, 0x2919))

    def _loc_13F8B(): pass

    label('loc_13F8B')

    SetScenaFlags(ScenaFlag(0x0523, 0, 0x2918))
    SetScenaFlags(ScenaFlag(0x0522, 7, 0x2917))

    def _loc_13F91(): pass

    label('loc_13F91')

    SetScenaFlags(ScenaFlag(0x0522, 6, 0x2916))
    SetScenaFlags(ScenaFlag(0x0522, 5, 0x2915))

    def _loc_13F97(): pass

    label('loc_13F97')

    SetScenaFlags(ScenaFlag(0x0522, 4, 0x2914))
    SetScenaFlags(ScenaFlag(0x0522, 3, 0x2913))

    def _loc_13F9D(): pass

    label('loc_13F9D')

    SetScenaFlags(ScenaFlag(0x0522, 2, 0x2912))
    SetScenaFlags(ScenaFlag(0x0522, 1, 0x2911))

    def _loc_13FA3(): pass

    label('loc_13FA3')

    SetScenaFlags(ScenaFlag(0x0522, 0, 0x2910))
    SetScenaFlags(ScenaFlag(0x0521, 7, 0x290F))

    def _loc_13FA9(): pass

    label('loc_13FA9')

    SetScenaFlags(ScenaFlag(0x0521, 6, 0x290E))
    SetScenaFlags(ScenaFlag(0x0521, 5, 0x290D))

    def _loc_13FAF(): pass

    label('loc_13FAF')

    SetScenaFlags(ScenaFlag(0x0521, 4, 0x290C))
    SetScenaFlags(ScenaFlag(0x0521, 3, 0x290B))

    def _loc_13FB5(): pass

    label('loc_13FB5')

    SetScenaFlags(ScenaFlag(0x0521, 2, 0x290A))
    SetScenaFlags(ScenaFlag(0x0521, 1, 0x2909))

    def _loc_13FBB(): pass

    label('loc_13FBB')

    SetScenaFlags(ScenaFlag(0x0521, 0, 0x2908))
    SetScenaFlags(ScenaFlag(0x0520, 7, 0x2907))

    def _loc_13FC1(): pass

    label('loc_13FC1')

    SetScenaFlags(ScenaFlag(0x0520, 6, 0x2906))
    SetScenaFlags(ScenaFlag(0x0520, 5, 0x2905))

    def _loc_13FC7(): pass

    label('loc_13FC7')

    SetScenaFlags(ScenaFlag(0x0520, 4, 0x2904))
    SetScenaFlags(ScenaFlag(0x0520, 3, 0x2903))

    def _loc_13FCD(): pass

    label('loc_13FCD')

    SetScenaFlags(ScenaFlag(0x0520, 2, 0x2902))
    SetScenaFlags(ScenaFlag(0x0520, 1, 0x2901))

    def _loc_13FD3(): pass

    label('loc_13FD3')

    SetScenaFlags(ScenaFlag(0x0520, 0, 0x2900))

    Jump('loc_13FDB')

    def _loc_13FDB(): pass

    label('loc_13FDB')

    Return()

# id: 0x001A offset: 0x13FDC
@scena.Code('EV_DoJumpSet_01')
def EV_DoJumpSet_01():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS0')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000010CF, 'loc_145B4'),
        (0x000010CE, 'loc_145BA'),
        (0x000010CD, 'loc_145C0'),
        (0x000010CC, 'loc_145C6'),
        (0x000010CB, 'loc_145CC'),
        (0x000010CA, 'loc_145D2'),
        (0x000010C9, 'loc_145D8'),
        (0x000010C8, 'loc_145DE'),
        (0x000010C7, 'loc_145E4'),
        (0x000010C6, 'loc_145EA'),
        (0x000010C5, 'loc_145F0'),
        (0x000010C4, 'loc_145FF'),
        (0x000010C3, 'loc_14605'),
        (0x000010C2, 'loc_1460B'),
        (0x000010C1, 'loc_14611'),
        (0x000010C0, 'loc_14617'),
        (0x000010BF, 'loc_1461D'),
        (0x000010BE, 'loc_14623'),
        (0x000010BD, 'loc_14629'),
        (0x000010BC, 'loc_1462F'),
        (0x000010BB, 'loc_14635'),
        (0x000010BA, 'loc_1463B'),
        (0x000010B9, 'loc_14641'),
        (0x000010B8, 'loc_14647'),
        (0x000010B7, 'loc_1464D'),
        (0x000010B6, 'loc_14653'),
        (0x000010B5, 'loc_14659'),
        (0x000010B4, 'loc_1465F'),
        (0x000010B3, 'loc_14665'),
        (0x000010D0, 'loc_1466B'),
        (0x000010B2, 'loc_14671'),
        (0x000010B1, 'loc_1467B'),
        (0x000010B0, 'loc_14681'),
        (0x000010AF, 'loc_14687'),
        (0x000010AE, 'loc_1468D'),
        (0x000010AD, 'loc_14693'),
        (0x000010AC, 'loc_14699'),
        (0x000010AB, 'loc_1469F'),
        (0x000010AA, 'loc_146A5'),
        (0x000010A9, 'loc_146AB'),
        (0x000010A8, 'loc_146B1'),
        (0x000010A7, 'loc_146B7'),
        (0x000010A6, 'loc_146BD'),
        (0x000010A5, 'loc_146C3'),
        (0x000010A4, 'loc_146C9'),
        (0x000010A3, 'loc_146CF'),
        (0x000010A2, 'loc_146D5'),
        (0x000010A1, 'loc_146DB'),
        (0x000010A0, 'loc_146E1'),
        (0x0000109F, 'loc_146E7'),
        (0x0000109E, 'loc_146ED'),
        (0x0000109D, 'loc_146F3'),
        (0x0000109C, 'loc_146F9'),
        (0x0000109B, 'loc_146FF'),
        (0x0000109A, 'loc_1470E'),
        (0x00001099, 'loc_14714'),
        (0x00001098, 'loc_1471A'),
        (0x00001096, 'loc_14720'),
        (0x00001095, 'loc_14726'),
        (0x00001094, 'loc_1472C'),
        (0x00001093, 'loc_14732'),
        (0x00001092, 'loc_14738'),
        (0x00001091, 'loc_1473E'),
        (0x00001090, 'loc_14744'),
        (0x0000108F, 'loc_1474A'),
        (0x0000108E, 'loc_14750'),
        (0x0000108D, 'loc_14756'),
        (0x0000108C, 'loc_1475C'),
        (0x0000108B, 'loc_14771'),
        (0x0000108A, 'loc_14777'),
        (0x00001089, 'loc_1477D'),
        (0x00001088, 'loc_14783'),
        (0x00001087, 'loc_14789'),
        (0x00001086, 'loc_1478F'),
        (0x00001085, 'loc_14799'),
        (0x00001084, 'loc_1479F'),
        (0x00001083, 'loc_147B1'),
        (0x00001082, 'loc_147C3'),
        (0x00001081, 'loc_147C9'),
        (0x00001080, 'loc_147CF'),
        (0x00001078, 'loc_147D5'),
        (0x00001077, 'loc_147DB'),
        (0x00001076, 'loc_147E1'),
        (0x00001075, 'loc_147E7'),
        (0x00001074, 'loc_147ED'),
        (0x00001073, 'loc_147F3'),
        (0x00001072, 'loc_147F9'),
        (0x00001071, 'loc_147FF'),
        (0x00001070, 'loc_14805'),
        (0x0000106F, 'loc_14814'),
        (0x0000106E, 'loc_1481A'),
        (0x0000106D, 'loc_14820'),
        (0x0000106C, 'loc_14826'),
        (0x0000106B, 'loc_1482C'),
        (0x0000106A, 'loc_14832'),
        (0x00001069, 'loc_14838'),
        (0x00001068, 'loc_1483E'),
        (0x00001067, 'loc_14844'),
        (0x00001066, 'loc_1484A'),
        (0x00001065, 'loc_14850'),
        (0x00001064, 'loc_14856'),
        (0x00001063, 'loc_1485C'),
        (0x00001062, 'loc_14862'),
        (0x00001061, 'loc_14871'),
        (0x00001060, 'loc_14877'),
        (0x0000105F, 'loc_1487D'),
        (0x0000105E, 'loc_14883'),
        (0x0000105D, 'loc_14889'),
        (0x0000105C, 'loc_1489B'),
        (0x0000105B, 'loc_148A1'),
        (0x0000105A, 'loc_148A7'),
        (0x00001059, 'loc_148AD'),
        (0x00001057, 'loc_148B9'),
        (0x00001056, 'loc_148BF'),
        (0x00001055, 'loc_148C9'),
        (0x00001054, 'loc_148CF'),
        (0x00001053, 'loc_148D8'),
        (0x00001052, 'loc_148F9'),
        (0x00001051, 'loc_148FF'),
        (0x00001050, 'loc_14905'),
        (0x0000103E, 'loc_1490B'),
        (0x0000103D, 'loc_14911'),
        (0x0000103C, 'loc_14917'),
        (0x0000103B, 'loc_1491D'),
        (0x0000103A, 'loc_14923'),
        (0x00001039, 'loc_14929'),
        (0x00001038, 'loc_1492F'),
        (0x00001037, 'loc_14935'),
        (0x00001036, 'loc_1493B'),
        (0x00001035, 'loc_14941'),
        (0x00001034, 'loc_14947'),
        (0x00001033, 'loc_1494D'),
        (0x00001032, 'loc_14953'),
        (0x00001031, 'loc_14959'),
        (0x00001030, 'loc_1495F'),
        (0x0000102F, 'loc_14965'),
        (0x0000102E, 'loc_1496B'),
        (0x0000102D, 'loc_14977'),
        (0x0000102C, 'loc_1497D'),
        (0x0000102B, 'loc_14983'),
        (0x0000102A, 'loc_14989'),
        (0x00001029, 'loc_1498F'),
        (0x00001028, 'loc_14995'),
        (0x00001027, 'loc_1499B'),
        (0x00001026, 'loc_149A1'),
        (0x00001025, 'loc_149A7'),
        (0x00001024, 'loc_149B0'),
        (0x00001023, 'loc_149B6'),
        (0x00001022, 'loc_149BC'),
        (0x00001021, 'loc_149C2'),
        (0x00001020, 'loc_149C8'),
        (0x0000101F, 'loc_149CE'),
        (0x0000101E, 'loc_149D4'),
        (0x0000101D, 'loc_149E3'),
        (0x0000101C, 'loc_149E9'),
        (0x0000101B, 'loc_149EF'),
        (0x0000101A, 'loc_149F5'),
        (0x00001019, 'loc_14A04'),
        (0x00001018, 'loc_14A0A'),
        (0x00001017, 'loc_14A10'),
        (0x00001016, 'loc_14A16'),
        (0x00001015, 'loc_14A1C'),
        (0x00001014, 'loc_14A22'),
        (0x00001013, 'loc_14A2B'),
        (0x00001012, 'loc_14A31'),
        (0x00001011, 'loc_14A4C'),
        (0x00001010, 'loc_14A52'),
        (0x00001008, 'loc_14A58'),
        (0x00001007, 'loc_14A5E'),
        (0x00001006, 'loc_14A64'),
        (0x00001005, 'loc_14A85'),
        (0x00001004, 'loc_14A8B'),
        (0x00001003, 'loc_14A91'),
        (0x00001002, 'loc_14A97'),
        (0x00001001, 'loc_14A9D'),
        (0x00001000, 'loc_14AA3'),
        (-1, 'loc_14AAB'),
    )

    def _loc_145B4(): pass

    label('loc_145B4')

    SetScenaFlags(ScenaFlag(0x0591, 6, 0x2C8E))
    SetScenaFlags(ScenaFlag(0x0591, 5, 0x2C8D))

    def _loc_145BA(): pass

    label('loc_145BA')

    SetScenaFlags(ScenaFlag(0x0591, 4, 0x2C8C))
    SetScenaFlags(ScenaFlag(0x0591, 3, 0x2C8B))

    def _loc_145C0(): pass

    label('loc_145C0')

    SetScenaFlags(ScenaFlag(0x0591, 2, 0x2C8A))
    SetScenaFlags(ScenaFlag(0x0591, 1, 0x2C89))

    def _loc_145C6(): pass

    label('loc_145C6')

    SetScenaFlags(ScenaFlag(0x0591, 0, 0x2C88))
    SetScenaFlags(ScenaFlag(0x0590, 7, 0x2C87))

    def _loc_145CC(): pass

    label('loc_145CC')

    SetScenaFlags(ScenaFlag(0x0590, 6, 0x2C86))
    SetScenaFlags(ScenaFlag(0x0590, 5, 0x2C85))

    def _loc_145D2(): pass

    label('loc_145D2')

    SetScenaFlags(ScenaFlag(0x0590, 4, 0x2C84))
    SetScenaFlags(ScenaFlag(0x0590, 3, 0x2C83))

    def _loc_145D8(): pass

    label('loc_145D8')

    SetScenaFlags(ScenaFlag(0x0590, 2, 0x2C82))
    SetScenaFlags(ScenaFlag(0x0590, 1, 0x2C81))

    def _loc_145DE(): pass

    label('loc_145DE')

    SetScenaFlags(ScenaFlag(0x0590, 0, 0x2C80))
    SetScenaFlags(ScenaFlag(0x058F, 7, 0x2C7F))

    def _loc_145E4(): pass

    label('loc_145E4')

    SetScenaFlags(ScenaFlag(0x058F, 6, 0x2C7E))
    SetScenaFlags(ScenaFlag(0x058F, 5, 0x2C7D))

    def _loc_145EA(): pass

    label('loc_145EA')

    SetScenaFlags(ScenaFlag(0x058F, 4, 0x2C7C))
    SetScenaFlags(ScenaFlag(0x058F, 3, 0x2C7B))

    def _loc_145F0(): pass

    label('loc_145F0')

    SetScenaFlags(ScenaFlag(0x058F, 2, 0x2C7A))
    SetScenaFlags(ScenaFlag(0x05A1, 6, 0x2D0E))
    OP_71(0x00, 0x2DA6, 0x2DAF)
    SetScenaFlags(ScenaFlag(0x058F, 1, 0x2C79))

    def _loc_145FF(): pass

    label('loc_145FF')

    SetScenaFlags(ScenaFlag(0x058F, 0, 0x2C78))
    SetScenaFlags(ScenaFlag(0x058E, 7, 0x2C77))

    def _loc_14605(): pass

    label('loc_14605')

    SetScenaFlags(ScenaFlag(0x058E, 6, 0x2C76))
    SetScenaFlags(ScenaFlag(0x058E, 5, 0x2C75))

    def _loc_1460B(): pass

    label('loc_1460B')

    SetScenaFlags(ScenaFlag(0x058E, 4, 0x2C74))
    SetScenaFlags(ScenaFlag(0x058E, 3, 0x2C73))

    def _loc_14611(): pass

    label('loc_14611')

    SetScenaFlags(ScenaFlag(0x058E, 2, 0x2C72))
    SetScenaFlags(ScenaFlag(0x058E, 1, 0x2C71))

    def _loc_14617(): pass

    label('loc_14617')

    SetScenaFlags(ScenaFlag(0x058E, 0, 0x2C70))
    SetScenaFlags(ScenaFlag(0x058D, 7, 0x2C6F))

    def _loc_1461D(): pass

    label('loc_1461D')

    SetScenaFlags(ScenaFlag(0x058D, 6, 0x2C6E))
    SetScenaFlags(ScenaFlag(0x058D, 5, 0x2C6D))

    def _loc_14623(): pass

    label('loc_14623')

    SetScenaFlags(ScenaFlag(0x058D, 4, 0x2C6C))
    SetScenaFlags(ScenaFlag(0x058D, 3, 0x2C6B))

    def _loc_14629(): pass

    label('loc_14629')

    SetScenaFlags(ScenaFlag(0x058D, 2, 0x2C6A))
    SetScenaFlags(ScenaFlag(0x058D, 1, 0x2C69))

    def _loc_1462F(): pass

    label('loc_1462F')

    SetScenaFlags(ScenaFlag(0x058D, 0, 0x2C68))
    SetScenaFlags(ScenaFlag(0x058C, 7, 0x2C67))

    def _loc_14635(): pass

    label('loc_14635')

    SetScenaFlags(ScenaFlag(0x058C, 6, 0x2C66))
    SetScenaFlags(ScenaFlag(0x058C, 5, 0x2C65))

    def _loc_1463B(): pass

    label('loc_1463B')

    SetScenaFlags(ScenaFlag(0x058C, 4, 0x2C64))
    SetScenaFlags(ScenaFlag(0x058C, 3, 0x2C63))

    def _loc_14641(): pass

    label('loc_14641')

    SetScenaFlags(ScenaFlag(0x058C, 2, 0x2C62))
    SetScenaFlags(ScenaFlag(0x058C, 1, 0x2C61))

    def _loc_14647(): pass

    label('loc_14647')

    SetScenaFlags(ScenaFlag(0x058C, 0, 0x2C60))
    SetScenaFlags(ScenaFlag(0x058B, 7, 0x2C5F))

    def _loc_1464D(): pass

    label('loc_1464D')

    SetScenaFlags(ScenaFlag(0x058B, 6, 0x2C5E))
    SetScenaFlags(ScenaFlag(0x058B, 5, 0x2C5D))

    def _loc_14653(): pass

    label('loc_14653')

    SetScenaFlags(ScenaFlag(0x058B, 4, 0x2C5C))
    SetScenaFlags(ScenaFlag(0x058B, 3, 0x2C5B))

    def _loc_14659(): pass

    label('loc_14659')

    SetScenaFlags(ScenaFlag(0x058B, 2, 0x2C5A))
    SetScenaFlags(ScenaFlag(0x058B, 1, 0x2C59))

    def _loc_1465F(): pass

    label('loc_1465F')

    SetScenaFlags(ScenaFlag(0x058B, 0, 0x2C58))
    SetScenaFlags(ScenaFlag(0x058A, 7, 0x2C57))

    def _loc_14665(): pass

    label('loc_14665')

    SetScenaFlags(ScenaFlag(0x058A, 6, 0x2C56))
    SetScenaFlags(ScenaFlag(0x0592, 1, 0x2C91))

    def _loc_1466B(): pass

    label('loc_1466B')

    SetScenaFlags(ScenaFlag(0x0592, 0, 0x2C90))
    SetScenaFlags(ScenaFlag(0x058A, 5, 0x2C55))

    def _loc_14671(): pass

    label('loc_14671')

    SetScenaFlags(ScenaFlag(0x058A, 4, 0x2C54))
    SetScenaFlags(ScenaFlag(0x058A, 3, 0x2C53))
    QuestCtrl(0x0009, 0x05)

    def _loc_1467B(): pass

    label('loc_1467B')

    SetScenaFlags(ScenaFlag(0x058A, 2, 0x2C52))
    SetScenaFlags(ScenaFlag(0x058A, 1, 0x2C51))

    def _loc_14681(): pass

    label('loc_14681')

    SetScenaFlags(ScenaFlag(0x058A, 0, 0x2C50))
    SetScenaFlags(ScenaFlag(0x0589, 7, 0x2C4F))

    def _loc_14687(): pass

    label('loc_14687')

    SetScenaFlags(ScenaFlag(0x0589, 6, 0x2C4E))
    SetScenaFlags(ScenaFlag(0x0589, 5, 0x2C4D))

    def _loc_1468D(): pass

    label('loc_1468D')

    SetScenaFlags(ScenaFlag(0x0589, 4, 0x2C4C))
    SetScenaFlags(ScenaFlag(0x0589, 3, 0x2C4B))

    def _loc_14693(): pass

    label('loc_14693')

    SetScenaFlags(ScenaFlag(0x0589, 2, 0x2C4A))
    SetScenaFlags(ScenaFlag(0x0589, 1, 0x2C49))

    def _loc_14699(): pass

    label('loc_14699')

    SetScenaFlags(ScenaFlag(0x0589, 0, 0x2C48))
    SetScenaFlags(ScenaFlag(0x0588, 7, 0x2C47))

    def _loc_1469F(): pass

    label('loc_1469F')

    SetScenaFlags(ScenaFlag(0x0588, 6, 0x2C46))
    SetScenaFlags(ScenaFlag(0x0588, 5, 0x2C45))

    def _loc_146A5(): pass

    label('loc_146A5')

    SetScenaFlags(ScenaFlag(0x0588, 4, 0x2C44))
    SetScenaFlags(ScenaFlag(0x0588, 3, 0x2C43))

    def _loc_146AB(): pass

    label('loc_146AB')

    SetScenaFlags(ScenaFlag(0x0588, 2, 0x2C42))
    SetScenaFlags(ScenaFlag(0x0588, 1, 0x2C41))

    def _loc_146B1(): pass

    label('loc_146B1')

    SetScenaFlags(ScenaFlag(0x0588, 0, 0x2C40))
    SetScenaFlags(ScenaFlag(0x0587, 7, 0x2C3F))

    def _loc_146B7(): pass

    label('loc_146B7')

    SetScenaFlags(ScenaFlag(0x0587, 6, 0x2C3E))
    SetScenaFlags(ScenaFlag(0x0587, 5, 0x2C3D))

    def _loc_146BD(): pass

    label('loc_146BD')

    SetScenaFlags(ScenaFlag(0x0587, 4, 0x2C3C))
    SetScenaFlags(ScenaFlag(0x0587, 3, 0x2C3B))

    def _loc_146C3(): pass

    label('loc_146C3')

    SetScenaFlags(ScenaFlag(0x0587, 2, 0x2C3A))
    SetScenaFlags(ScenaFlag(0x0587, 1, 0x2C39))

    def _loc_146C9(): pass

    label('loc_146C9')

    SetScenaFlags(ScenaFlag(0x0587, 0, 0x2C38))
    SetScenaFlags(ScenaFlag(0x0586, 7, 0x2C37))

    def _loc_146CF(): pass

    label('loc_146CF')

    SetScenaFlags(ScenaFlag(0x0586, 6, 0x2C36))
    SetScenaFlags(ScenaFlag(0x0586, 5, 0x2C35))

    def _loc_146D5(): pass

    label('loc_146D5')

    SetScenaFlags(ScenaFlag(0x0586, 4, 0x2C34))
    SetScenaFlags(ScenaFlag(0x0586, 3, 0x2C33))

    def _loc_146DB(): pass

    label('loc_146DB')

    SetScenaFlags(ScenaFlag(0x0586, 2, 0x2C32))
    SetScenaFlags(ScenaFlag(0x0586, 1, 0x2C31))

    def _loc_146E1(): pass

    label('loc_146E1')

    SetScenaFlags(ScenaFlag(0x0586, 0, 0x2C30))
    SetScenaFlags(ScenaFlag(0x0585, 7, 0x2C2F))

    def _loc_146E7(): pass

    label('loc_146E7')

    SetScenaFlags(ScenaFlag(0x0585, 6, 0x2C2E))
    SetScenaFlags(ScenaFlag(0x0585, 5, 0x2C2D))

    def _loc_146ED(): pass

    label('loc_146ED')

    SetScenaFlags(ScenaFlag(0x0585, 4, 0x2C2C))
    SetScenaFlags(ScenaFlag(0x0585, 3, 0x2C2B))

    def _loc_146F3(): pass

    label('loc_146F3')

    SetScenaFlags(ScenaFlag(0x0585, 2, 0x2C2A))
    SetScenaFlags(ScenaFlag(0x0585, 1, 0x2C29))

    def _loc_146F9(): pass

    label('loc_146F9')

    SetScenaFlags(ScenaFlag(0x0585, 0, 0x2C28))
    SetScenaFlags(ScenaFlag(0x0584, 7, 0x2C27))

    def _loc_146FF(): pass

    label('loc_146FF')

    SetScenaFlags(ScenaFlag(0x0584, 6, 0x2C26))
    SetScenaFlags(ScenaFlag(0x05A1, 5, 0x2D0D))
    OP_71(0x00, 0x2D99, 0x2DA5)
    SetScenaFlags(ScenaFlag(0x0584, 5, 0x2C25))

    def _loc_1470E(): pass

    label('loc_1470E')

    SetScenaFlags(ScenaFlag(0x0584, 4, 0x2C24))
    SetScenaFlags(ScenaFlag(0x0584, 3, 0x2C23))

    def _loc_14714(): pass

    label('loc_14714')

    SetScenaFlags(ScenaFlag(0x0584, 2, 0x2C22))
    SetScenaFlags(ScenaFlag(0x0584, 1, 0x2C21))

    def _loc_1471A(): pass

    label('loc_1471A')

    SetScenaFlags(ScenaFlag(0x0584, 0, 0x2C20))
    SetScenaFlags(ScenaFlag(0x0583, 5, 0x2C1D))

    def _loc_14720(): pass

    label('loc_14720')

    SetScenaFlags(ScenaFlag(0x0583, 4, 0x2C1C))
    SetScenaFlags(ScenaFlag(0x0583, 3, 0x2C1B))

    def _loc_14726(): pass

    label('loc_14726')

    SetScenaFlags(ScenaFlag(0x0583, 2, 0x2C1A))
    SetScenaFlags(ScenaFlag(0x0583, 1, 0x2C19))

    def _loc_1472C(): pass

    label('loc_1472C')

    SetScenaFlags(ScenaFlag(0x0583, 0, 0x2C18))
    SetScenaFlags(ScenaFlag(0x0582, 7, 0x2C17))

    def _loc_14732(): pass

    label('loc_14732')

    SetScenaFlags(ScenaFlag(0x0582, 6, 0x2C16))
    SetScenaFlags(ScenaFlag(0x0582, 5, 0x2C15))

    def _loc_14738(): pass

    label('loc_14738')

    SetScenaFlags(ScenaFlag(0x0582, 4, 0x2C14))
    SetScenaFlags(ScenaFlag(0x0582, 3, 0x2C13))

    def _loc_1473E(): pass

    label('loc_1473E')

    SetScenaFlags(ScenaFlag(0x0582, 2, 0x2C12))
    SetScenaFlags(ScenaFlag(0x0582, 1, 0x2C11))

    def _loc_14744(): pass

    label('loc_14744')

    SetScenaFlags(ScenaFlag(0x0582, 0, 0x2C10))
    SetScenaFlags(ScenaFlag(0x0581, 7, 0x2C0F))

    def _loc_1474A(): pass

    label('loc_1474A')

    SetScenaFlags(ScenaFlag(0x0581, 6, 0x2C0E))
    SetScenaFlags(ScenaFlag(0x0581, 5, 0x2C0D))

    def _loc_14750(): pass

    label('loc_14750')

    SetScenaFlags(ScenaFlag(0x0581, 4, 0x2C0C))
    SetScenaFlags(ScenaFlag(0x0581, 3, 0x2C0B))

    def _loc_14756(): pass

    label('loc_14756')

    SetScenaFlags(ScenaFlag(0x0581, 2, 0x2C0A))
    SetScenaFlags(ScenaFlag(0x0581, 1, 0x2C09))

    def _loc_1475C(): pass

    label('loc_1475C')

    SetScenaFlags(ScenaFlag(0x0581, 0, 0x2C08))
    SetScenaFlags(ScenaFlag(0x05A1, 4, 0x2D0C))
    OP_71(0x00, 0x2D97, 0x2D98)
    OP_71(0x00, 0x2DB2, 0x2DB3)
    SetScenaFlags(ScenaFlag(0x0580, 7, 0x2C07))

    def _loc_14771(): pass

    label('loc_14771')

    SetScenaFlags(ScenaFlag(0x0580, 6, 0x2C06))
    SetScenaFlags(ScenaFlag(0x0580, 5, 0x2C05))

    def _loc_14777(): pass

    label('loc_14777')

    SetScenaFlags(ScenaFlag(0x0580, 4, 0x2C04))
    SetScenaFlags(ScenaFlag(0x0580, 3, 0x2C03))

    def _loc_1477D(): pass

    label('loc_1477D')

    SetScenaFlags(ScenaFlag(0x0580, 2, 0x2C02))
    SetScenaFlags(ScenaFlag(0x0580, 1, 0x2C01))

    def _loc_14783(): pass

    label('loc_14783')

    SetScenaFlags(ScenaFlag(0x0580, 0, 0x2C00))
    SetScenaFlags(ScenaFlag(0x057F, 7, 0x2BFF))

    def _loc_14789(): pass

    label('loc_14789')

    SetScenaFlags(ScenaFlag(0x057F, 6, 0x2BFE))
    SetScenaFlags(ScenaFlag(0x057F, 5, 0x2BFD))

    def _loc_1478F(): pass

    label('loc_1478F')

    SetScenaFlags(ScenaFlag(0x057F, 4, 0x2BFC))
    SetScenaFlags(ScenaFlag(0x057F, 3, 0x2BFB))
    QuestCtrl(0x0008, 0x05)

    def _loc_14799(): pass

    label('loc_14799')

    SetScenaFlags(ScenaFlag(0x057F, 2, 0x2BFA))
    SetScenaFlags(ScenaFlag(0x057F, 1, 0x2BF9))

    def _loc_1479F(): pass

    label('loc_1479F')

    SetScenaFlags(ScenaFlag(0x057F, 0, 0x2BF8))
    SetScenaFlags(ScenaFlag(0x05A1, 3, 0x2D0B))
    OP_71(0x00, 0x2D95, 0x2D96)
    SetScenaFlags(ScenaFlag(0x05B6, 1, 0x2DB1))
    SetScenaFlags(ScenaFlag(0x057E, 7, 0x2BF7))

    def _loc_147B1(): pass

    label('loc_147B1')

    SetScenaFlags(ScenaFlag(0x057E, 6, 0x2BF6))
    SetScenaFlags(ScenaFlag(0x057E, 5, 0x2BF5))
    QuestCtrl(0x0005, 0x05)
    QuestCtrl(0x0006, 0x05)
    QuestCtrl(0x0007, 0x05)

    def _loc_147C3(): pass

    label('loc_147C3')

    SetScenaFlags(ScenaFlag(0x057E, 4, 0x2BF4))
    SetScenaFlags(ScenaFlag(0x057E, 3, 0x2BF3))

    def _loc_147C9(): pass

    label('loc_147C9')

    SetScenaFlags(ScenaFlag(0x057E, 2, 0x2BF2))
    SetScenaFlags(ScenaFlag(0x057E, 1, 0x2BF1))

    def _loc_147CF(): pass

    label('loc_147CF')

    SetScenaFlags(ScenaFlag(0x057E, 0, 0x2BF0))
    SetScenaFlags(ScenaFlag(0x057C, 1, 0x2BE1))

    def _loc_147D5(): pass

    label('loc_147D5')

    SetScenaFlags(ScenaFlag(0x057C, 0, 0x2BE0))
    SetScenaFlags(ScenaFlag(0x057B, 7, 0x2BDF))

    def _loc_147DB(): pass

    label('loc_147DB')

    SetScenaFlags(ScenaFlag(0x057B, 6, 0x2BDE))
    SetScenaFlags(ScenaFlag(0x057B, 5, 0x2BDD))

    def _loc_147E1(): pass

    label('loc_147E1')

    SetScenaFlags(ScenaFlag(0x057B, 4, 0x2BDC))
    SetScenaFlags(ScenaFlag(0x057B, 3, 0x2BDB))

    def _loc_147E7(): pass

    label('loc_147E7')

    SetScenaFlags(ScenaFlag(0x057B, 2, 0x2BDA))
    SetScenaFlags(ScenaFlag(0x057B, 1, 0x2BD9))

    def _loc_147ED(): pass

    label('loc_147ED')

    SetScenaFlags(ScenaFlag(0x057B, 0, 0x2BD8))
    SetScenaFlags(ScenaFlag(0x057A, 7, 0x2BD7))

    def _loc_147F3(): pass

    label('loc_147F3')

    SetScenaFlags(ScenaFlag(0x057A, 6, 0x2BD6))
    SetScenaFlags(ScenaFlag(0x057A, 5, 0x2BD5))

    def _loc_147F9(): pass

    label('loc_147F9')

    SetScenaFlags(ScenaFlag(0x057A, 4, 0x2BD4))
    SetScenaFlags(ScenaFlag(0x057A, 3, 0x2BD3))

    def _loc_147FF(): pass

    label('loc_147FF')

    SetScenaFlags(ScenaFlag(0x057A, 2, 0x2BD2))
    SetScenaFlags(ScenaFlag(0x057A, 1, 0x2BD1))

    def _loc_14805(): pass

    label('loc_14805')

    SetScenaFlags(ScenaFlag(0x057A, 0, 0x2BD0))
    SetScenaFlags(ScenaFlag(0x05A1, 2, 0x2D0A))
    OP_71(0x00, 0x2D90, 0x2D94)
    SetScenaFlags(ScenaFlag(0x0579, 7, 0x2BCF))

    def _loc_14814(): pass

    label('loc_14814')

    SetScenaFlags(ScenaFlag(0x0579, 6, 0x2BCE))
    SetScenaFlags(ScenaFlag(0x0579, 5, 0x2BCD))

    def _loc_1481A(): pass

    label('loc_1481A')

    SetScenaFlags(ScenaFlag(0x0579, 4, 0x2BCC))
    SetScenaFlags(ScenaFlag(0x0579, 3, 0x2BCB))

    def _loc_14820(): pass

    label('loc_14820')

    SetScenaFlags(ScenaFlag(0x0579, 2, 0x2BCA))
    SetScenaFlags(ScenaFlag(0x0579, 1, 0x2BC9))

    def _loc_14826(): pass

    label('loc_14826')

    SetScenaFlags(ScenaFlag(0x0579, 0, 0x2BC8))
    SetScenaFlags(ScenaFlag(0x0578, 7, 0x2BC7))

    def _loc_1482C(): pass

    label('loc_1482C')

    SetScenaFlags(ScenaFlag(0x0578, 6, 0x2BC6))
    SetScenaFlags(ScenaFlag(0x0578, 5, 0x2BC5))

    def _loc_14832(): pass

    label('loc_14832')

    SetScenaFlags(ScenaFlag(0x0578, 4, 0x2BC4))
    SetScenaFlags(ScenaFlag(0x0578, 3, 0x2BC3))

    def _loc_14838(): pass

    label('loc_14838')

    SetScenaFlags(ScenaFlag(0x0578, 2, 0x2BC2))
    SetScenaFlags(ScenaFlag(0x0578, 1, 0x2BC1))

    def _loc_1483E(): pass

    label('loc_1483E')

    SetScenaFlags(ScenaFlag(0x0578, 0, 0x2BC0))
    SetScenaFlags(ScenaFlag(0x0577, 7, 0x2BBF))

    def _loc_14844(): pass

    label('loc_14844')

    SetScenaFlags(ScenaFlag(0x0577, 6, 0x2BBE))
    SetScenaFlags(ScenaFlag(0x0577, 5, 0x2BBD))

    def _loc_1484A(): pass

    label('loc_1484A')

    SetScenaFlags(ScenaFlag(0x0577, 4, 0x2BBC))
    SetScenaFlags(ScenaFlag(0x0577, 3, 0x2BBB))

    def _loc_14850(): pass

    label('loc_14850')

    SetScenaFlags(ScenaFlag(0x0577, 2, 0x2BBA))
    SetScenaFlags(ScenaFlag(0x0577, 1, 0x2BB9))

    def _loc_14856(): pass

    label('loc_14856')

    SetScenaFlags(ScenaFlag(0x0577, 0, 0x2BB8))
    SetScenaFlags(ScenaFlag(0x0576, 7, 0x2BB7))

    def _loc_1485C(): pass

    label('loc_1485C')

    SetScenaFlags(ScenaFlag(0x0576, 6, 0x2BB6))
    SetScenaFlags(ScenaFlag(0x0576, 5, 0x2BB5))

    def _loc_14862(): pass

    label('loc_14862')

    SetScenaFlags(ScenaFlag(0x0576, 4, 0x2BB4))
    SetScenaFlags(ScenaFlag(0x05A1, 1, 0x2D09))
    OP_71(0x00, 0x2D8A, 0x2D8C)
    SetScenaFlags(ScenaFlag(0x0576, 3, 0x2BB3))

    def _loc_14871(): pass

    label('loc_14871')

    SetScenaFlags(ScenaFlag(0x0576, 2, 0x2BB2))
    SetScenaFlags(ScenaFlag(0x0576, 1, 0x2BB1))

    def _loc_14877(): pass

    label('loc_14877')

    SetScenaFlags(ScenaFlag(0x0576, 0, 0x2BB0))
    SetScenaFlags(ScenaFlag(0x0575, 7, 0x2BAF))

    def _loc_1487D(): pass

    label('loc_1487D')

    SetScenaFlags(ScenaFlag(0x0575, 6, 0x2BAE))
    SetScenaFlags(ScenaFlag(0x0575, 5, 0x2BAD))

    def _loc_14883(): pass

    label('loc_14883')

    SetScenaFlags(ScenaFlag(0x0575, 4, 0x2BAC))
    SetScenaFlags(ScenaFlag(0x0575, 3, 0x2BAB))

    def _loc_14889(): pass

    label('loc_14889')

    SetScenaFlags(ScenaFlag(0x0575, 2, 0x2BAA))
    SetScenaFlags(ScenaFlag(0x05A0, 7, 0x2D07))
    SetScenaFlags(ScenaFlag(0x05A1, 0, 0x2D08))
    OP_71(0x00, 0x2D85, 0x2D87)
    SetScenaFlags(ScenaFlag(0x0575, 1, 0x2BA9))

    def _loc_1489B(): pass

    label('loc_1489B')

    SetScenaFlags(ScenaFlag(0x0575, 0, 0x2BA8))
    SetScenaFlags(ScenaFlag(0x0574, 7, 0x2BA7))

    def _loc_148A1(): pass

    label('loc_148A1')

    SetScenaFlags(ScenaFlag(0x0574, 6, 0x2BA6))
    SetScenaFlags(ScenaFlag(0x0574, 5, 0x2BA5))

    def _loc_148A7(): pass

    label('loc_148A7')

    SetScenaFlags(ScenaFlag(0x0574, 4, 0x2BA4))
    SetScenaFlags(ScenaFlag(0x0574, 3, 0x2BA3))

    def _loc_148AD(): pass

    label('loc_148AD')

    SetScenaFlags(ScenaFlag(0x0574, 2, 0x2BA2))
    SetScenaFlags(ScenaFlag(0x0574, 1, 0x2BA1))
    SetScenaFlags(ScenaFlag(0x0573, 6, 0x2B9E))
    SetScenaFlags(ScenaFlag(0x0573, 7, 0x2B9F))

    def _loc_148B9(): pass

    label('loc_148B9')

    SetScenaFlags(ScenaFlag(0x0573, 6, 0x2B9E))
    SetScenaFlags(ScenaFlag(0x0573, 5, 0x2B9D))

    def _loc_148BF(): pass

    label('loc_148BF')

    SetScenaFlags(ScenaFlag(0x0573, 4, 0x2B9C))
    SetScenaFlags(ScenaFlag(0x0573, 3, 0x2B9B))
    QuestCtrl(0x0004, 0x05)

    def _loc_148C9(): pass

    label('loc_148C9')

    SetScenaFlags(ScenaFlag(0x0573, 2, 0x2B9A))
    SetScenaFlags(ScenaFlag(0x0573, 1, 0x2B99))

    def _loc_148CF(): pass

    label('loc_148CF')

    SetScenaFlags(ScenaFlag(0x0573, 0, 0x2B98))
    SetScenaFlags(ScenaFlag(0x05A0, 6, 0x2D06))
    SetScenaFlags(ScenaFlag(0x0572, 7, 0x2B97))

    def _loc_148D8(): pass

    label('loc_148D8')

    SetScenaFlags(ScenaFlag(0x0572, 6, 0x2B96))
    SetScenaFlags(ScenaFlag(0x05A0, 6, 0x2D06))
    SetScenaFlags(ScenaFlag(0x05B6, 0, 0x2DB0))
    SetScenaFlags(ScenaFlag(0x0572, 5, 0x2B95))
    SetScenaFlags(ScenaFlag(0x05F2, 3, 0x2F93))
    SetScenaFlags(ScenaFlag(0x05F2, 4, 0x2F94))
    SetScenaFlags(ScenaFlag(0x05F2, 5, 0x2F95))
    QuestCtrl(0x0001, 0x05)
    QuestCtrl(0x0002, 0x05)
    QuestCtrl(0x0003, 0x05)

    def _loc_148F9(): pass

    label('loc_148F9')

    SetScenaFlags(ScenaFlag(0x0572, 4, 0x2B94))
    SetScenaFlags(ScenaFlag(0x0572, 3, 0x2B93))

    def _loc_148FF(): pass

    label('loc_148FF')

    SetScenaFlags(ScenaFlag(0x0572, 2, 0x2B92))
    SetScenaFlags(ScenaFlag(0x0572, 1, 0x2B91))

    def _loc_14905(): pass

    label('loc_14905')

    SetScenaFlags(ScenaFlag(0x0572, 0, 0x2B90))
    SetScenaFlags(ScenaFlag(0x056F, 5, 0x2B7D))

    def _loc_1490B(): pass

    label('loc_1490B')

    SetScenaFlags(ScenaFlag(0x056F, 4, 0x2B7C))
    SetScenaFlags(ScenaFlag(0x056F, 3, 0x2B7B))

    def _loc_14911(): pass

    label('loc_14911')

    SetScenaFlags(ScenaFlag(0x056F, 2, 0x2B7A))
    SetScenaFlags(ScenaFlag(0x056F, 1, 0x2B79))

    def _loc_14917(): pass

    label('loc_14917')

    SetScenaFlags(ScenaFlag(0x056F, 0, 0x2B78))
    SetScenaFlags(ScenaFlag(0x056E, 7, 0x2B77))

    def _loc_1491D(): pass

    label('loc_1491D')

    SetScenaFlags(ScenaFlag(0x056E, 6, 0x2B76))
    SetScenaFlags(ScenaFlag(0x056E, 5, 0x2B75))

    def _loc_14923(): pass

    label('loc_14923')

    SetScenaFlags(ScenaFlag(0x056E, 4, 0x2B74))
    SetScenaFlags(ScenaFlag(0x056E, 3, 0x2B73))

    def _loc_14929(): pass

    label('loc_14929')

    SetScenaFlags(ScenaFlag(0x056E, 2, 0x2B72))
    SetScenaFlags(ScenaFlag(0x056E, 1, 0x2B71))

    def _loc_1492F(): pass

    label('loc_1492F')

    SetScenaFlags(ScenaFlag(0x056E, 0, 0x2B70))
    SetScenaFlags(ScenaFlag(0x056D, 7, 0x2B6F))

    def _loc_14935(): pass

    label('loc_14935')

    SetScenaFlags(ScenaFlag(0x056D, 6, 0x2B6E))
    SetScenaFlags(ScenaFlag(0x056D, 5, 0x2B6D))

    def _loc_1493B(): pass

    label('loc_1493B')

    SetScenaFlags(ScenaFlag(0x056D, 4, 0x2B6C))
    SetScenaFlags(ScenaFlag(0x056D, 3, 0x2B6B))

    def _loc_14941(): pass

    label('loc_14941')

    SetScenaFlags(ScenaFlag(0x056D, 2, 0x2B6A))
    SetScenaFlags(ScenaFlag(0x056D, 1, 0x2B69))

    def _loc_14947(): pass

    label('loc_14947')

    SetScenaFlags(ScenaFlag(0x056D, 0, 0x2B68))
    SetScenaFlags(ScenaFlag(0x056C, 7, 0x2B67))

    def _loc_1494D(): pass

    label('loc_1494D')

    SetScenaFlags(ScenaFlag(0x056C, 6, 0x2B66))
    SetScenaFlags(ScenaFlag(0x056C, 5, 0x2B65))

    def _loc_14953(): pass

    label('loc_14953')

    SetScenaFlags(ScenaFlag(0x056C, 4, 0x2B64))
    SetScenaFlags(ScenaFlag(0x056C, 3, 0x2B63))

    def _loc_14959(): pass

    label('loc_14959')

    SetScenaFlags(ScenaFlag(0x056C, 2, 0x2B62))
    SetScenaFlags(ScenaFlag(0x056C, 1, 0x2B61))

    def _loc_1495F(): pass

    label('loc_1495F')

    SetScenaFlags(ScenaFlag(0x056C, 0, 0x2B60))
    SetScenaFlags(ScenaFlag(0x056B, 7, 0x2B5F))

    def _loc_14965(): pass

    label('loc_14965')

    SetScenaFlags(ScenaFlag(0x056B, 6, 0x2B5E))
    SetScenaFlags(ScenaFlag(0x056B, 5, 0x2B5D))

    def _loc_1496B(): pass

    label('loc_1496B')

    SetScenaFlags(ScenaFlag(0x056B, 4, 0x2B5C))
    SetScenaFlags(ScenaFlag(0x056B, 3, 0x2B5B))
    SetScenaFlags(ScenaFlag(0x05F2, 1, 0x2F91))
    SetScenaFlags(ScenaFlag(0x0073, 2, 0x39A))

    def _loc_14977(): pass

    label('loc_14977')

    SetScenaFlags(ScenaFlag(0x056B, 2, 0x2B5A))
    SetScenaFlags(ScenaFlag(0x056B, 1, 0x2B59))

    def _loc_1497D(): pass

    label('loc_1497D')

    SetScenaFlags(ScenaFlag(0x056B, 0, 0x2B58))
    SetScenaFlags(ScenaFlag(0x056A, 7, 0x2B57))

    def _loc_14983(): pass

    label('loc_14983')

    SetScenaFlags(ScenaFlag(0x056A, 6, 0x2B56))
    SetScenaFlags(ScenaFlag(0x056A, 5, 0x2B55))

    def _loc_14989(): pass

    label('loc_14989')

    SetScenaFlags(ScenaFlag(0x056A, 4, 0x2B54))
    SetScenaFlags(ScenaFlag(0x056A, 3, 0x2B53))

    def _loc_1498F(): pass

    label('loc_1498F')

    SetScenaFlags(ScenaFlag(0x056A, 2, 0x2B52))
    SetScenaFlags(ScenaFlag(0x056A, 1, 0x2B51))

    def _loc_14995(): pass

    label('loc_14995')

    SetScenaFlags(ScenaFlag(0x056A, 0, 0x2B50))
    SetScenaFlags(ScenaFlag(0x0569, 7, 0x2B4F))

    def _loc_1499B(): pass

    label('loc_1499B')

    SetScenaFlags(ScenaFlag(0x0569, 6, 0x2B4E))
    SetScenaFlags(ScenaFlag(0x0569, 5, 0x2B4D))

    def _loc_149A1(): pass

    label('loc_149A1')

    SetScenaFlags(ScenaFlag(0x0569, 4, 0x2B4C))
    SetScenaFlags(ScenaFlag(0x0569, 3, 0x2B4B))

    def _loc_149A7(): pass

    label('loc_149A7')

    SetScenaFlags(ScenaFlag(0x0569, 2, 0x2B4A))
    SetScenaFlags(ScenaFlag(0x0569, 1, 0x2B49))
    SetScenaFlags(ScenaFlag(0x05F1, 7, 0x2F8F))

    def _loc_149B0(): pass

    label('loc_149B0')

    SetScenaFlags(ScenaFlag(0x0569, 0, 0x2B48))
    SetScenaFlags(ScenaFlag(0x0568, 7, 0x2B47))

    def _loc_149B6(): pass

    label('loc_149B6')

    SetScenaFlags(ScenaFlag(0x0568, 6, 0x2B46))
    SetScenaFlags(ScenaFlag(0x0568, 5, 0x2B45))

    def _loc_149BC(): pass

    label('loc_149BC')

    SetScenaFlags(ScenaFlag(0x0568, 4, 0x2B44))
    SetScenaFlags(ScenaFlag(0x0568, 3, 0x2B43))

    def _loc_149C2(): pass

    label('loc_149C2')

    SetScenaFlags(ScenaFlag(0x0568, 2, 0x2B42))
    SetScenaFlags(ScenaFlag(0x0568, 1, 0x2B41))

    def _loc_149C8(): pass

    label('loc_149C8')

    SetScenaFlags(ScenaFlag(0x0568, 0, 0x2B40))
    SetScenaFlags(ScenaFlag(0x0567, 7, 0x2B3F))

    def _loc_149CE(): pass

    label('loc_149CE')

    SetScenaFlags(ScenaFlag(0x0567, 6, 0x2B3E))
    SetScenaFlags(ScenaFlag(0x0567, 5, 0x2B3D))

    def _loc_149D4(): pass

    label('loc_149D4')

    SetScenaFlags(ScenaFlag(0x0567, 4, 0x2B3C))
    SetScenaFlags(ScenaFlag(0x0567, 3, 0x2B3B))
    SetScenaFlags(ScenaFlag(0x05A0, 5, 0x2D05))
    OP_71(0x00, 0x2D80, 0x2D82)

    def _loc_149E3(): pass

    label('loc_149E3')

    SetScenaFlags(ScenaFlag(0x0567, 2, 0x2B3A))
    SetScenaFlags(ScenaFlag(0x0567, 1, 0x2B39))

    def _loc_149E9(): pass

    label('loc_149E9')

    SetScenaFlags(ScenaFlag(0x0567, 0, 0x2B38))
    SetScenaFlags(ScenaFlag(0x0566, 7, 0x2B37))

    def _loc_149EF(): pass

    label('loc_149EF')

    SetScenaFlags(ScenaFlag(0x0566, 6, 0x2B36))
    SetScenaFlags(ScenaFlag(0x0566, 5, 0x2B35))

    def _loc_149F5(): pass

    label('loc_149F5')

    SetScenaFlags(ScenaFlag(0x0566, 4, 0x2B34))
    SetScenaFlags(ScenaFlag(0x0566, 3, 0x2B33))
    SetScenaFlags(ScenaFlag(0x05F1, 5, 0x2F8D))
    SetScenaFlags(ScenaFlag(0x05F1, 6, 0x2F8E))
    ClearScenaFlags(ScenaFlag(0x006E, 1, 0x371))

    def _loc_14A04(): pass

    label('loc_14A04')

    SetScenaFlags(ScenaFlag(0x0566, 2, 0x2B32))
    SetScenaFlags(ScenaFlag(0x0566, 1, 0x2B31))

    def _loc_14A0A(): pass

    label('loc_14A0A')

    SetScenaFlags(ScenaFlag(0x0566, 0, 0x2B30))
    SetScenaFlags(ScenaFlag(0x0565, 7, 0x2B2F))

    def _loc_14A10(): pass

    label('loc_14A10')

    SetScenaFlags(ScenaFlag(0x0565, 6, 0x2B2E))
    SetScenaFlags(ScenaFlag(0x0565, 5, 0x2B2D))

    def _loc_14A16(): pass

    label('loc_14A16')

    SetScenaFlags(ScenaFlag(0x0565, 4, 0x2B2C))
    SetScenaFlags(ScenaFlag(0x0565, 3, 0x2B2B))

    def _loc_14A1C(): pass

    label('loc_14A1C')

    SetScenaFlags(ScenaFlag(0x0565, 2, 0x2B2A))
    SetScenaFlags(ScenaFlag(0x0565, 1, 0x2B29))

    def _loc_14A22(): pass

    label('loc_14A22')

    SetScenaFlags(ScenaFlag(0x0565, 0, 0x2B28))
    SetScenaFlags(ScenaFlag(0x0564, 7, 0x2B27))
    SetScenaFlags(ScenaFlag(0x05F1, 4, 0x2F8C))

    def _loc_14A2B(): pass

    label('loc_14A2B')

    SetScenaFlags(ScenaFlag(0x0564, 6, 0x2B26))
    SetScenaFlags(ScenaFlag(0x0564, 5, 0x2B25))

    def _loc_14A31(): pass

    label('loc_14A31')

    SetScenaFlags(ScenaFlag(0x0564, 4, 0x2B24))
    SetScenaFlags(ScenaFlag(0x0564, 3, 0x2B23))
    SetScenaFlags(ScenaFlag(0x05F1, 0, 0x2F88))
    SetScenaFlags(ScenaFlag(0x05F1, 1, 0x2F89))
    SetScenaFlags(ScenaFlag(0x05F1, 2, 0x2F8A))
    SetScenaFlags(ScenaFlag(0x05F1, 3, 0x2F8B))
    SetScenaFlags(ScenaFlag(0x05F2, 2, 0x2F92))
    ClearScenaFlags(ScenaFlag(0x006E, 4, 0x374))
    ClearScenaFlags(ScenaFlag(0x006E, 5, 0x375))

    def _loc_14A4C(): pass

    label('loc_14A4C')

    SetScenaFlags(ScenaFlag(0x0564, 2, 0x2B22))
    SetScenaFlags(ScenaFlag(0x0564, 1, 0x2B21))

    def _loc_14A52(): pass

    label('loc_14A52')

    SetScenaFlags(ScenaFlag(0x0564, 0, 0x2B20))
    SetScenaFlags(ScenaFlag(0x0562, 1, 0x2B11))

    def _loc_14A58(): pass

    label('loc_14A58')

    SetScenaFlags(ScenaFlag(0x0562, 0, 0x2B10))
    SetScenaFlags(ScenaFlag(0x0561, 7, 0x2B0F))

    def _loc_14A5E(): pass

    label('loc_14A5E')

    SetScenaFlags(ScenaFlag(0x0561, 6, 0x2B0E))
    SetScenaFlags(ScenaFlag(0x0561, 5, 0x2B0D))

    def _loc_14A64(): pass

    label('loc_14A64')

    SetScenaFlags(ScenaFlag(0x0561, 4, 0x2B0C))
    SetScenaFlags(ScenaFlag(0x0561, 3, 0x2B0B))
    SetScenaFlags(ScenaFlag(0x05F0, 0, 0x2F80))
    SetScenaFlags(ScenaFlag(0x05F0, 1, 0x2F81))
    SetScenaFlags(ScenaFlag(0x05F0, 2, 0x2F82))
    SetScenaFlags(ScenaFlag(0x05F0, 3, 0x2F83))
    SetScenaFlags(ScenaFlag(0x05F0, 4, 0x2F84))
    SetScenaFlags(ScenaFlag(0x05F0, 5, 0x2F85))
    SetScenaFlags(ScenaFlag(0x05F0, 6, 0x2F86))
    SetScenaFlags(ScenaFlag(0x05F0, 7, 0x2F87))
    ClearScenaFlags(ScenaFlag(0x006E, 2, 0x372))

    def _loc_14A85(): pass

    label('loc_14A85')

    SetScenaFlags(ScenaFlag(0x0561, 2, 0x2B0A))
    SetScenaFlags(ScenaFlag(0x0561, 1, 0x2B09))

    def _loc_14A8B(): pass

    label('loc_14A8B')

    SetScenaFlags(ScenaFlag(0x0561, 0, 0x2B08))
    SetScenaFlags(ScenaFlag(0x0560, 7, 0x2B07))

    def _loc_14A91(): pass

    label('loc_14A91')

    SetScenaFlags(ScenaFlag(0x0560, 6, 0x2B06))
    SetScenaFlags(ScenaFlag(0x0560, 5, 0x2B05))

    def _loc_14A97(): pass

    label('loc_14A97')

    SetScenaFlags(ScenaFlag(0x0560, 4, 0x2B04))
    SetScenaFlags(ScenaFlag(0x0560, 3, 0x2B03))

    def _loc_14A9D(): pass

    label('loc_14A9D')

    SetScenaFlags(ScenaFlag(0x0560, 2, 0x2B02))
    SetScenaFlags(ScenaFlag(0x0560, 1, 0x2B01))

    def _loc_14AA3(): pass

    label('loc_14AA3')

    SetScenaFlags(ScenaFlag(0x0560, 0, 0x2B00))

    Jump('loc_14AAB')

    def _loc_14AAB(): pass

    label('loc_14AAB')

    Return()

# id: 0x001B offset: 0x14AAC
@scena.Code('EV_DoJumpSet_01X')
def EV_DoJumpSet_01X():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS0')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0000203E, 'loc_14D03'),
        (0x0000203D, 'loc_14D28'),
        (0x0000203C, 'loc_14D2E'),
        (0x0000203B, 'loc_14D34'),
        (0x0000203A, 'loc_14D3A'),
        (0x00002039, 'loc_14D40'),
        (0x00002038, 'loc_14D46'),
        (0x00002037, 'loc_14D4C'),
        (0x00002036, 'loc_14D52'),
        (0x00002035, 'loc_14D58'),
        (0x00002034, 'loc_14D5E'),
        (0x00002033, 'loc_14D70'),
        (0x00002032, 'loc_14D76'),
        (0x00002031, 'loc_14D7C'),
        (0x00002030, 'loc_14D82'),
        (0x0000202F, 'loc_14D88'),
        (0x0000202E, 'loc_14D8E'),
        (0x0000202C, 'loc_14D94'),
        (0x0000202A, 'loc_14D9A'),
        (0x00002029, 'loc_14DA0'),
        (0x00002028, 'loc_14DA6'),
        (0x00002027, 'loc_14DAC'),
        (0x00002026, 'loc_14DB2'),
        (0x00002025, 'loc_14DB8'),
        (0x00002024, 'loc_14DBE'),
        (0x00002023, 'loc_14DC4'),
        (0x00002022, 'loc_14DCA'),
        (0x00002021, 'loc_14DD0'),
        (0x00002020, 'loc_14DD6'),
        (0x0000201F, 'loc_14DDC'),
        (0x0000201E, 'loc_14DE8'),
        (0x0000201D, 'loc_14DEE'),
        (0x0000201C, 'loc_14DF4'),
        (0x0000201B, 'loc_14DFA'),
        (0x0000201A, 'loc_14E00'),
        (0x00002019, 'loc_14E06'),
        (0x00002018, 'loc_14E10'),
        (0x00002017, 'loc_14E16'),
        (0x00002015, 'loc_14E1C'),
        (0x00002014, 'loc_14E22'),
        (0x00002013, 'loc_14E28'),
        (0x00002012, 'loc_14E2E'),
        (0x00002011, 'loc_14E45'),
        (0x00002010, 'loc_14E4B'),
        (0x0000200F, 'loc_14E51'),
        (0x0000200E, 'loc_14E57'),
        (0x0000200D, 'loc_14E5D'),
        (0x0000200C, 'loc_14E63'),
        (0x0000200B, 'loc_14E69'),
        (0x0000200A, 'loc_14E6F'),
        (0x00002009, 'loc_14E75'),
        (0x00002008, 'loc_14E90'),
        (0x00002007, 'loc_14E96'),
        (0x00002006, 'loc_14E9C'),
        (0x00002005, 'loc_14EA2'),
        (0x00002004, 'loc_14EA8'),
        (0x00002003, 'loc_14EAE'),
        (0x00002002, 'loc_14EB4'),
        (0x00002001, 'loc_14EBA'),
        (0x00002000, 'loc_14EC0'),
        (-1, 'loc_14EC8'),
    )

    def _loc_14D03(): pass

    label('loc_14D03')

    SetScenaFlags(ScenaFlag(0x06AF, 4, 0x357C))
    SetScenaFlags(ScenaFlag(0x06AF, 3, 0x357B))
    SetScenaFlags(ScenaFlag(0x0086, 3, 0x433))
    Call(ScriptId.System, 'SetKisinChange_ValimarS1')

    def _loc_14D28(): pass

    label('loc_14D28')

    SetScenaFlags(ScenaFlag(0x06AF, 2, 0x357A))
    SetScenaFlags(ScenaFlag(0x06AF, 1, 0x3579))

    def _loc_14D2E(): pass

    label('loc_14D2E')

    SetScenaFlags(ScenaFlag(0x06AF, 0, 0x3578))
    SetScenaFlags(ScenaFlag(0x06AE, 7, 0x3577))

    def _loc_14D34(): pass

    label('loc_14D34')

    SetScenaFlags(ScenaFlag(0x06AE, 6, 0x3576))
    SetScenaFlags(ScenaFlag(0x06AE, 5, 0x3575))

    def _loc_14D3A(): pass

    label('loc_14D3A')

    SetScenaFlags(ScenaFlag(0x06AE, 4, 0x3574))
    SetScenaFlags(ScenaFlag(0x06AE, 3, 0x3573))

    def _loc_14D40(): pass

    label('loc_14D40')

    SetScenaFlags(ScenaFlag(0x06AE, 2, 0x3572))
    SetScenaFlags(ScenaFlag(0x06AE, 1, 0x3571))

    def _loc_14D46(): pass

    label('loc_14D46')

    SetScenaFlags(ScenaFlag(0x06AE, 0, 0x3570))
    SetScenaFlags(ScenaFlag(0x06AD, 7, 0x356F))

    def _loc_14D4C(): pass

    label('loc_14D4C')

    SetScenaFlags(ScenaFlag(0x06AD, 6, 0x356E))
    SetScenaFlags(ScenaFlag(0x06AD, 5, 0x356D))

    def _loc_14D52(): pass

    label('loc_14D52')

    SetScenaFlags(ScenaFlag(0x06AD, 4, 0x356C))
    SetScenaFlags(ScenaFlag(0x06AD, 3, 0x356B))

    def _loc_14D58(): pass

    label('loc_14D58')

    SetScenaFlags(ScenaFlag(0x06AD, 2, 0x356A))
    SetScenaFlags(ScenaFlag(0x06AD, 1, 0x3569))

    def _loc_14D5E(): pass

    label('loc_14D5E')

    SetScenaFlags(ScenaFlag(0x06AD, 0, 0x3568))
    SetScenaFlags(ScenaFlag(0x06AC, 7, 0x3567))

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    def _loc_14D70(): pass

    label('loc_14D70')

    SetScenaFlags(ScenaFlag(0x06AC, 6, 0x3566))
    SetScenaFlags(ScenaFlag(0x06AC, 5, 0x3565))

    def _loc_14D76(): pass

    label('loc_14D76')

    SetScenaFlags(ScenaFlag(0x06AC, 4, 0x3564))
    SetScenaFlags(ScenaFlag(0x06AC, 3, 0x3563))

    def _loc_14D7C(): pass

    label('loc_14D7C')

    SetScenaFlags(ScenaFlag(0x06AC, 2, 0x3562))
    SetScenaFlags(ScenaFlag(0x06AC, 1, 0x3561))

    def _loc_14D82(): pass

    label('loc_14D82')

    SetScenaFlags(ScenaFlag(0x06AC, 0, 0x3560))
    SetScenaFlags(ScenaFlag(0x06AB, 7, 0x355F))

    def _loc_14D88(): pass

    label('loc_14D88')

    SetScenaFlags(ScenaFlag(0x06AB, 6, 0x355E))
    SetScenaFlags(ScenaFlag(0x06AB, 5, 0x355D))

    def _loc_14D8E(): pass

    label('loc_14D8E')

    SetScenaFlags(ScenaFlag(0x06AB, 4, 0x355C))
    SetScenaFlags(ScenaFlag(0x06AB, 1, 0x3559))

    def _loc_14D94(): pass

    label('loc_14D94')

    SetScenaFlags(ScenaFlag(0x06AB, 0, 0x3558))
    SetScenaFlags(ScenaFlag(0x06AA, 5, 0x3555))

    def _loc_14D9A(): pass

    label('loc_14D9A')

    SetScenaFlags(ScenaFlag(0x06AA, 4, 0x3554))
    SetScenaFlags(ScenaFlag(0x06AA, 3, 0x3553))

    def _loc_14DA0(): pass

    label('loc_14DA0')

    SetScenaFlags(ScenaFlag(0x06AA, 2, 0x3552))
    SetScenaFlags(ScenaFlag(0x06AA, 1, 0x3551))

    def _loc_14DA6(): pass

    label('loc_14DA6')

    SetScenaFlags(ScenaFlag(0x06AA, 0, 0x3550))
    SetScenaFlags(ScenaFlag(0x06A9, 7, 0x354F))

    def _loc_14DAC(): pass

    label('loc_14DAC')

    SetScenaFlags(ScenaFlag(0x06A9, 6, 0x354E))
    SetScenaFlags(ScenaFlag(0x06A9, 5, 0x354D))

    def _loc_14DB2(): pass

    label('loc_14DB2')

    SetScenaFlags(ScenaFlag(0x06A9, 4, 0x354C))
    SetScenaFlags(ScenaFlag(0x06A9, 3, 0x354B))

    def _loc_14DB8(): pass

    label('loc_14DB8')

    SetScenaFlags(ScenaFlag(0x06A9, 2, 0x354A))
    SetScenaFlags(ScenaFlag(0x06A9, 1, 0x3549))

    def _loc_14DBE(): pass

    label('loc_14DBE')

    SetScenaFlags(ScenaFlag(0x06A9, 0, 0x3548))
    SetScenaFlags(ScenaFlag(0x06A8, 7, 0x3547))

    def _loc_14DC4(): pass

    label('loc_14DC4')

    SetScenaFlags(ScenaFlag(0x06A8, 6, 0x3546))
    SetScenaFlags(ScenaFlag(0x06A8, 5, 0x3545))

    def _loc_14DCA(): pass

    label('loc_14DCA')

    SetScenaFlags(ScenaFlag(0x06A8, 4, 0x3544))
    SetScenaFlags(ScenaFlag(0x06A8, 3, 0x3543))

    def _loc_14DD0(): pass

    label('loc_14DD0')

    SetScenaFlags(ScenaFlag(0x06A8, 2, 0x3542))
    SetScenaFlags(ScenaFlag(0x06A8, 1, 0x3541))

    def _loc_14DD6(): pass

    label('loc_14DD6')

    SetScenaFlags(ScenaFlag(0x06A8, 0, 0x3540))
    SetScenaFlags(ScenaFlag(0x06A7, 7, 0x353F))

    def _loc_14DDC(): pass

    label('loc_14DDC')

    SetScenaFlags(ScenaFlag(0x06A7, 6, 0x353E))
    SetScenaFlags(ScenaFlag(0x06A7, 5, 0x353D))
    SetScenaFlags(ScenaFlag(0x06B2, 0, 0x3590))
    SetScenaFlags(ScenaFlag(0x06B2, 1, 0x3591))

    def _loc_14DE8(): pass

    label('loc_14DE8')

    SetScenaFlags(ScenaFlag(0x06A7, 4, 0x353C))
    SetScenaFlags(ScenaFlag(0x06A7, 3, 0x353B))

    def _loc_14DEE(): pass

    label('loc_14DEE')

    SetScenaFlags(ScenaFlag(0x06A7, 2, 0x353A))
    SetScenaFlags(ScenaFlag(0x06A7, 1, 0x3539))

    def _loc_14DF4(): pass

    label('loc_14DF4')

    SetScenaFlags(ScenaFlag(0x06A7, 0, 0x3538))
    SetScenaFlags(ScenaFlag(0x06A6, 7, 0x3537))

    def _loc_14DFA(): pass

    label('loc_14DFA')

    SetScenaFlags(ScenaFlag(0x06A6, 6, 0x3536))
    SetScenaFlags(ScenaFlag(0x06A6, 5, 0x3535))

    def _loc_14E00(): pass

    label('loc_14E00')

    SetScenaFlags(ScenaFlag(0x06A6, 4, 0x3534))
    SetScenaFlags(ScenaFlag(0x06A6, 3, 0x3533))

    def _loc_14E06(): pass

    label('loc_14E06')

    SetScenaFlags(ScenaFlag(0x06A6, 2, 0x3532))
    SetScenaFlags(ScenaFlag(0x06A6, 1, 0x3531))
    QuestCtrl(0x000D, 0x05)

    def _loc_14E10(): pass

    label('loc_14E10')

    SetScenaFlags(ScenaFlag(0x06A6, 0, 0x3530))
    SetScenaFlags(ScenaFlag(0x06A5, 7, 0x352F))

    def _loc_14E16(): pass

    label('loc_14E16')

    SetScenaFlags(ScenaFlag(0x06A5, 6, 0x352E))
    SetScenaFlags(ScenaFlag(0x06A5, 3, 0x352B))

    def _loc_14E1C(): pass

    label('loc_14E1C')

    SetScenaFlags(ScenaFlag(0x06A5, 2, 0x352A))
    SetScenaFlags(ScenaFlag(0x06A5, 1, 0x3529))

    def _loc_14E22(): pass

    label('loc_14E22')

    SetScenaFlags(ScenaFlag(0x06A5, 0, 0x3528))
    SetScenaFlags(ScenaFlag(0x06A4, 7, 0x3527))

    def _loc_14E28(): pass

    label('loc_14E28')

    SetScenaFlags(ScenaFlag(0x06A4, 6, 0x3526))
    SetScenaFlags(ScenaFlag(0x06A4, 5, 0x3525))

    def _loc_14E2E(): pass

    label('loc_14E2E')

    SetScenaFlags(ScenaFlag(0x06A4, 4, 0x3524))
    SetScenaFlags(ScenaFlag(0x06A4, 3, 0x3523))

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_14E45',
    )

    SetScenaFlags(ScenaFlag(0x009E, 2, 0x4F2))

    def _loc_14E45(): pass

    label('loc_14E45')

    SetScenaFlags(ScenaFlag(0x06A4, 2, 0x3522))
    SetScenaFlags(ScenaFlag(0x06A4, 1, 0x3521))

    def _loc_14E4B(): pass

    label('loc_14E4B')

    SetScenaFlags(ScenaFlag(0x06A4, 0, 0x3520))
    SetScenaFlags(ScenaFlag(0x06A3, 7, 0x351F))

    def _loc_14E51(): pass

    label('loc_14E51')

    SetScenaFlags(ScenaFlag(0x06A3, 6, 0x351E))
    SetScenaFlags(ScenaFlag(0x06A3, 5, 0x351D))

    def _loc_14E57(): pass

    label('loc_14E57')

    SetScenaFlags(ScenaFlag(0x06A3, 4, 0x351C))
    SetScenaFlags(ScenaFlag(0x06A3, 3, 0x351B))

    def _loc_14E5D(): pass

    label('loc_14E5D')

    SetScenaFlags(ScenaFlag(0x06A3, 2, 0x351A))
    SetScenaFlags(ScenaFlag(0x06A3, 1, 0x3519))

    def _loc_14E63(): pass

    label('loc_14E63')

    SetScenaFlags(ScenaFlag(0x06A3, 0, 0x3518))
    SetScenaFlags(ScenaFlag(0x06A2, 7, 0x3517))

    def _loc_14E69(): pass

    label('loc_14E69')

    SetScenaFlags(ScenaFlag(0x06A2, 6, 0x3516))
    SetScenaFlags(ScenaFlag(0x06A2, 5, 0x3515))

    def _loc_14E6F(): pass

    label('loc_14E6F')

    SetScenaFlags(ScenaFlag(0x06A2, 4, 0x3514))
    SetScenaFlags(ScenaFlag(0x06A2, 3, 0x3513))

    def _loc_14E75(): pass

    label('loc_14E75')

    SetScenaFlags(ScenaFlag(0x06A2, 2, 0x3512))
    SetScenaFlags(ScenaFlag(0x06B2, 2, 0x3592))
    OP_71(0x00, 0x35B0, 0x35B5)
    SetScenaFlags(ScenaFlag(0x06A2, 1, 0x3511))
    QuestCtrl(0x000A, 0x05)
    QuestCtrl(0x000B, 0x05)
    QuestCtrl(0x000C, 0x05)

    def _loc_14E90(): pass

    label('loc_14E90')

    SetScenaFlags(ScenaFlag(0x06A2, 0, 0x3510))
    SetScenaFlags(ScenaFlag(0x06A1, 7, 0x350F))

    def _loc_14E96(): pass

    label('loc_14E96')

    SetScenaFlags(ScenaFlag(0x06A1, 6, 0x350E))
    SetScenaFlags(ScenaFlag(0x06A1, 5, 0x350D))

    def _loc_14E9C(): pass

    label('loc_14E9C')

    SetScenaFlags(ScenaFlag(0x06A1, 4, 0x350C))
    SetScenaFlags(ScenaFlag(0x06A1, 3, 0x350B))

    def _loc_14EA2(): pass

    label('loc_14EA2')

    SetScenaFlags(ScenaFlag(0x06A1, 2, 0x350A))
    SetScenaFlags(ScenaFlag(0x06A1, 1, 0x3509))

    def _loc_14EA8(): pass

    label('loc_14EA8')

    SetScenaFlags(ScenaFlag(0x06A1, 0, 0x3508))
    SetScenaFlags(ScenaFlag(0x06A0, 7, 0x3507))

    def _loc_14EAE(): pass

    label('loc_14EAE')

    SetScenaFlags(ScenaFlag(0x06A0, 6, 0x3506))
    SetScenaFlags(ScenaFlag(0x06A0, 5, 0x3505))

    def _loc_14EB4(): pass

    label('loc_14EB4')

    SetScenaFlags(ScenaFlag(0x06A0, 4, 0x3504))
    SetScenaFlags(ScenaFlag(0x06A0, 3, 0x3503))

    def _loc_14EBA(): pass

    label('loc_14EBA')

    SetScenaFlags(ScenaFlag(0x06A0, 2, 0x3502))
    SetScenaFlags(ScenaFlag(0x06A0, 1, 0x3501))

    def _loc_14EC0(): pass

    label('loc_14EC0')

    SetScenaFlags(ScenaFlag(0x06A0, 0, 0x3500))

    Jump('loc_14EC8')

    def _loc_14EC8(): pass

    label('loc_14EC8')

    Return()

# id: 0x001C offset: 0x14ECC
@scena.Code('EV_DoJumpSet_02')
def EV_DoJumpSet_02():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01X_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS1')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000030F8, 'loc_154C1'),
        (0x000030F7, 'loc_154C7'),
        (0x000030F6, 'loc_154CD'),
        (0x000030F5, 'loc_154D3'),
        (0x000030F4, 'loc_154D9'),
        (0x000030F3, 'loc_154DF'),
        (0x000030F2, 'loc_154E5'),
        (0x000030F1, 'loc_154EB'),
        (0x000030F0, 'loc_154F1'),
        (0x000030EF, 'loc_154F7'),
        (0x000030EE, 'loc_154FD'),
        (0x000030ED, 'loc_15503'),
        (0x000030EC, 'loc_15509'),
        (0x000030EB, 'loc_1550F'),
        (0x000030EA, 'loc_15515'),
        (0x000030E9, 'loc_1551B'),
        (0x000030E8, 'loc_15521'),
        (0x000030E7, 'loc_15527'),
        (0x000030E6, 'loc_15530'),
        (0x000030E5, 'loc_15536'),
        (0x000030E4, 'loc_1553C'),
        (0x000030E3, 'loc_15542'),
        (0x000030E2, 'loc_15548'),
        (0x000030E1, 'loc_1554E'),
        (0x000030E0, 'loc_15554'),
        (0x000030DF, 'loc_1555A'),
        (0x000030DE, 'loc_15560'),
        (0x000030DD, 'loc_15566'),
        (0x000030DC, 'loc_1556C'),
        (0x000030DB, 'loc_15587'),
        (0x000030DA, 'loc_1558D'),
        (0x000030D9, 'loc_155B4'),
        (0x000030D8, 'loc_155BA'),
        (0x000030D7, 'loc_155C0'),
        (0x000030D6, 'loc_155C6'),
        (0x000030D5, 'loc_155CC'),
        (0x000030D4, 'loc_155D2'),
        (0x000030D3, 'loc_155D8'),
        (0x000030D2, 'loc_155EA'),
        (0x000030D1, 'loc_155F0'),
        (0x000030D0, 'loc_155F6'),
        (0x000030BE, 'loc_155FC'),
        (0x000030BD, 'loc_15602'),
        (0x000030BC, 'loc_15608'),
        (0x000030BB, 'loc_1560E'),
        (0x000030BA, 'loc_15614'),
        (0x000030B9, 'loc_1561A'),
        (0x000030B8, 'loc_15620'),
        (0x000030B7, 'loc_15626'),
        (0x000030B6, 'loc_1562C'),
        (0x000030B5, 'loc_15632'),
        (0x000030B4, 'loc_15638'),
        (0x000030B3, 'loc_1563E'),
        (0x000030B2, 'loc_15644'),
        (0x000030B1, 'loc_1564A'),
        (0x000030B0, 'loc_15650'),
        (0x000030AF, 'loc_15656'),
        (0x000030AE, 'loc_1565C'),
        (0x000030AD, 'loc_15662'),
        (0x000030AC, 'loc_15668'),
        (0x000030AB, 'loc_1566E'),
        (0x000030AA, 'loc_15674'),
        (0x000030A9, 'loc_1567A'),
        (0x000030A8, 'loc_15680'),
        (0x000030A7, 'loc_15686'),
        (0x000030A6, 'loc_15692'),
        (0x000030A5, 'loc_15698'),
        (0x000030A4, 'loc_1569E'),
        (0x000030A3, 'loc_156A4'),
        (0x000030A2, 'loc_156AA'),
        (0x000030A1, 'loc_156B0'),
        (0x000030A0, 'loc_156BF'),
        (0x0000309F, 'loc_156C5'),
        (0x0000309E, 'loc_156CB'),
        (0x0000309D, 'loc_156D1'),
        (0x0000309C, 'loc_156D7'),
        (0x0000309B, 'loc_156DD'),
        (0x0000309A, 'loc_156E6'),
        (0x00003099, 'loc_156F8'),
        (0x00003098, 'loc_156FE'),
        (0x00003097, 'loc_15704'),
        (0x00003096, 'loc_1570A'),
        (0x00003095, 'loc_15710'),
        (0x00003094, 'loc_15716'),
        (0x00003093, 'loc_1571C'),
        (0x00003092, 'loc_15722'),
        (0x00003091, 'loc_15728'),
        (0x00003090, 'loc_1572E'),
        (0x0000307B, 'loc_15734'),
        (0x0000307A, 'loc_1573A'),
        (0x00003079, 'loc_15740'),
        (0x00003078, 'loc_15746'),
        (0x00003077, 'loc_1574C'),
        (0x00003076, 'loc_15752'),
        (0x00003075, 'loc_15758'),
        (0x00003074, 'loc_1575E'),
        (0x00003073, 'loc_15768'),
        (0x00003072, 'loc_1576E'),
        (0x00003071, 'loc_15774'),
        (0x00003070, 'loc_1577A'),
        (0x0000306F, 'loc_15780'),
        (0x0000306E, 'loc_15786'),
        (0x0000306D, 'loc_1578C'),
        (0x0000306C, 'loc_15792'),
        (0x0000306B, 'loc_1579E'),
        (0x0000306A, 'loc_157A4'),
        (0x00003069, 'loc_157AA'),
        (0x00003068, 'loc_157BC'),
        (0x00003067, 'loc_157C2'),
        (0x00003066, 'loc_157C8'),
        (0x00003065, 'loc_157CE'),
        (0x00003064, 'loc_157D4'),
        (0x00003063, 'loc_157DA'),
        (0x00003062, 'loc_157E0'),
        (0x00003061, 'loc_157E6'),
        (0x00003060, 'loc_157EC'),
        (0x0000304C, 'loc_157F2'),
        (0x0000304B, 'loc_157F8'),
        (0x0000304A, 'loc_157FE'),
        (0x00003049, 'loc_15804'),
        (0x00003048, 'loc_1580A'),
        (0x00003047, 'loc_15810'),
        (0x00003046, 'loc_15816'),
        (0x00003045, 'loc_1581C'),
        (0x00003044, 'loc_15822'),
        (0x00003043, 'loc_15828'),
        (0x00003042, 'loc_1582E'),
        (0x00003041, 'loc_15834'),
        (0x00003040, 'loc_1583A'),
        (0x0000303F, 'loc_15840'),
        (0x0000303E, 'loc_1584A'),
        (0x0000303D, 'loc_15850'),
        (0x0000303C, 'loc_15856'),
        (0x0000303B, 'loc_1585C'),
        (0x0000303A, 'loc_15862'),
        (0x00003039, 'loc_15871'),
        (0x00003038, 'loc_15877'),
        (0x00003037, 'loc_1587D'),
        (0x00003036, 'loc_15883'),
        (0x00003035, 'loc_15895'),
        (0x00003034, 'loc_1589B'),
        (0x00003033, 'loc_158A1'),
        (0x00003032, 'loc_158A7'),
        (0x00003031, 'loc_158AD'),
        (0x00003030, 'loc_158B3'),
        (0x0000301C, 'loc_158CA'),
        (0x0000301B, 'loc_158D0'),
        (0x0000301A, 'loc_158D6'),
        (0x00003019, 'loc_158DC'),
        (0x00003018, 'loc_158E2'),
        (0x00003017, 'loc_158E8'),
        (0x00003016, 'loc_158EE'),
        (0x00003015, 'loc_158F4'),
        (0x00003014, 'loc_158FA'),
        (0x00003013, 'loc_15900'),
        (0x00003012, 'loc_15906'),
        (0x00003011, 'loc_15912'),
        (0x00003010, 'loc_15918'),
        (0x0000300F, 'loc_1591E'),
        (0x0000300E, 'loc_15924'),
        (0x0000300D, 'loc_1592A'),
        (0x0000300C, 'loc_1593F'),
        (0x0000300B, 'loc_15945'),
        (0x0000300A, 'loc_1594B'),
        (0x00003009, 'loc_15951'),
        (0x00003008, 'loc_15957'),
        (0x00003007, 'loc_1595D'),
        (0x00003006, 'loc_15975'),
        (0x00003005, 'loc_1597B'),
        (0x00003004, 'loc_15981'),
        (0x00003003, 'loc_15987'),
        (0x00003002, 'loc_1598D'),
        (0x00003001, 'loc_15993'),
        (0x00003000, 'loc_15999'),
        (-1, 'loc_159A1'),
    )

    def _loc_154C1(): pass

    label('loc_154C1')

    SetScenaFlags(ScenaFlag(0x071A, 0, 0x38D0))
    SetScenaFlags(ScenaFlag(0x0719, 7, 0x38CF))

    def _loc_154C7(): pass

    label('loc_154C7')

    SetScenaFlags(ScenaFlag(0x0719, 6, 0x38CE))
    SetScenaFlags(ScenaFlag(0x0719, 5, 0x38CD))

    def _loc_154CD(): pass

    label('loc_154CD')

    SetScenaFlags(ScenaFlag(0x0719, 4, 0x38CC))
    SetScenaFlags(ScenaFlag(0x0719, 3, 0x38CB))

    def _loc_154D3(): pass

    label('loc_154D3')

    SetScenaFlags(ScenaFlag(0x0719, 2, 0x38CA))
    SetScenaFlags(ScenaFlag(0x0719, 1, 0x38C9))

    def _loc_154D9(): pass

    label('loc_154D9')

    SetScenaFlags(ScenaFlag(0x0719, 0, 0x38C8))
    SetScenaFlags(ScenaFlag(0x0718, 7, 0x38C7))

    def _loc_154DF(): pass

    label('loc_154DF')

    SetScenaFlags(ScenaFlag(0x0718, 6, 0x38C6))
    SetScenaFlags(ScenaFlag(0x0718, 5, 0x38C5))

    def _loc_154E5(): pass

    label('loc_154E5')

    SetScenaFlags(ScenaFlag(0x0718, 4, 0x38C4))
    SetScenaFlags(ScenaFlag(0x0718, 3, 0x38C3))

    def _loc_154EB(): pass

    label('loc_154EB')

    SetScenaFlags(ScenaFlag(0x0718, 2, 0x38C2))
    SetScenaFlags(ScenaFlag(0x0718, 1, 0x38C1))

    def _loc_154F1(): pass

    label('loc_154F1')

    SetScenaFlags(ScenaFlag(0x0718, 0, 0x38C0))
    SetScenaFlags(ScenaFlag(0x0717, 7, 0x38BF))

    def _loc_154F7(): pass

    label('loc_154F7')

    SetScenaFlags(ScenaFlag(0x0717, 6, 0x38BE))
    SetScenaFlags(ScenaFlag(0x0717, 5, 0x38BD))

    def _loc_154FD(): pass

    label('loc_154FD')

    SetScenaFlags(ScenaFlag(0x0717, 4, 0x38BC))
    SetScenaFlags(ScenaFlag(0x0717, 3, 0x38BB))

    def _loc_15503(): pass

    label('loc_15503')

    SetScenaFlags(ScenaFlag(0x0717, 2, 0x38BA))
    SetScenaFlags(ScenaFlag(0x0717, 1, 0x38B9))

    def _loc_15509(): pass

    label('loc_15509')

    SetScenaFlags(ScenaFlag(0x0717, 0, 0x38B8))
    SetScenaFlags(ScenaFlag(0x0716, 7, 0x38B7))

    def _loc_1550F(): pass

    label('loc_1550F')

    SetScenaFlags(ScenaFlag(0x0716, 6, 0x38B6))
    SetScenaFlags(ScenaFlag(0x0716, 5, 0x38B5))

    def _loc_15515(): pass

    label('loc_15515')

    SetScenaFlags(ScenaFlag(0x0716, 4, 0x38B4))
    SetScenaFlags(ScenaFlag(0x0716, 3, 0x38B3))

    def _loc_1551B(): pass

    label('loc_1551B')

    SetScenaFlags(ScenaFlag(0x0716, 2, 0x38B2))
    SetScenaFlags(ScenaFlag(0x0716, 1, 0x38B1))

    def _loc_15521(): pass

    label('loc_15521')

    SetScenaFlags(ScenaFlag(0x0716, 0, 0x38B0))
    SetScenaFlags(ScenaFlag(0x0715, 7, 0x38AF))

    def _loc_15527(): pass

    label('loc_15527')

    SetScenaFlags(ScenaFlag(0x0715, 6, 0x38AE))
    SetScenaFlags(ScenaFlag(0x0720, 0, 0x3900))
    SetScenaFlags(ScenaFlag(0x0715, 5, 0x38AD))

    def _loc_15530(): pass

    label('loc_15530')

    SetScenaFlags(ScenaFlag(0x0715, 4, 0x38AC))
    SetScenaFlags(ScenaFlag(0x0715, 3, 0x38AB))

    def _loc_15536(): pass

    label('loc_15536')

    SetScenaFlags(ScenaFlag(0x0715, 2, 0x38AA))
    SetScenaFlags(ScenaFlag(0x0715, 1, 0x38A9))

    def _loc_1553C(): pass

    label('loc_1553C')

    SetScenaFlags(ScenaFlag(0x0715, 0, 0x38A8))
    SetScenaFlags(ScenaFlag(0x0714, 7, 0x38A7))

    def _loc_15542(): pass

    label('loc_15542')

    SetScenaFlags(ScenaFlag(0x0714, 6, 0x38A6))
    SetScenaFlags(ScenaFlag(0x0714, 5, 0x38A5))

    def _loc_15548(): pass

    label('loc_15548')

    SetScenaFlags(ScenaFlag(0x0714, 4, 0x38A4))
    SetScenaFlags(ScenaFlag(0x0714, 3, 0x38A3))

    def _loc_1554E(): pass

    label('loc_1554E')

    SetScenaFlags(ScenaFlag(0x0714, 2, 0x38A2))
    SetScenaFlags(ScenaFlag(0x0714, 1, 0x38A1))

    def _loc_15554(): pass

    label('loc_15554')

    SetScenaFlags(ScenaFlag(0x0714, 0, 0x38A0))
    SetScenaFlags(ScenaFlag(0x0713, 7, 0x389F))

    def _loc_1555A(): pass

    label('loc_1555A')

    SetScenaFlags(ScenaFlag(0x0713, 6, 0x389E))
    SetScenaFlags(ScenaFlag(0x0713, 5, 0x389D))

    def _loc_15560(): pass

    label('loc_15560')

    SetScenaFlags(ScenaFlag(0x0713, 4, 0x389C))
    SetScenaFlags(ScenaFlag(0x0713, 3, 0x389B))

    def _loc_15566(): pass

    label('loc_15566')

    SetScenaFlags(ScenaFlag(0x0713, 2, 0x389A))
    SetScenaFlags(ScenaFlag(0x0713, 1, 0x3899))

    def _loc_1556C(): pass

    label('loc_1556C')

    SetScenaFlags(ScenaFlag(0x0713, 0, 0x3898))
    SetScenaFlags(ScenaFlag(0x0721, 6, 0x390E))
    OP_71(0x00, 0x39AF, 0x39BD)
    OP_71(0x00, 0x39C6, 0x39CB)
    OP_71(0x00, 0x39D0, 0x39D4)
    SetScenaFlags(ScenaFlag(0x0712, 7, 0x3897))

    def _loc_15587(): pass

    label('loc_15587')

    SetScenaFlags(ScenaFlag(0x0712, 6, 0x3896))
    SetScenaFlags(ScenaFlag(0x0712, 5, 0x3895))

    def _loc_1558D(): pass

    label('loc_1558D')

    SetScenaFlags(ScenaFlag(0x0712, 4, 0x3894))
    SetScenaFlags(ScenaFlag(0x0721, 5, 0x390D))
    OP_71(0x00, 0x39A6, 0x39AE)
    OP_71(0x00, 0x39C2, 0x39C5)
    OP_71(0x00, 0x39CE, 0x39CF)
    SetScenaFlags(ScenaFlag(0x0712, 3, 0x3893))
    QuestCtrl(0x0019, 0x05)
    QuestCtrl(0x001A, 0x05)
    QuestCtrl(0x001B, 0x05)

    def _loc_155B4(): pass

    label('loc_155B4')

    SetScenaFlags(ScenaFlag(0x0712, 2, 0x3892))
    SetScenaFlags(ScenaFlag(0x0712, 1, 0x3891))

    def _loc_155BA(): pass

    label('loc_155BA')

    SetScenaFlags(ScenaFlag(0x0712, 0, 0x3890))
    SetScenaFlags(ScenaFlag(0x0711, 7, 0x388F))

    def _loc_155C0(): pass

    label('loc_155C0')

    SetScenaFlags(ScenaFlag(0x0711, 6, 0x388E))
    SetScenaFlags(ScenaFlag(0x0711, 5, 0x388D))

    def _loc_155C6(): pass

    label('loc_155C6')

    SetScenaFlags(ScenaFlag(0x0711, 4, 0x388C))
    SetScenaFlags(ScenaFlag(0x0711, 3, 0x388B))

    def _loc_155CC(): pass

    label('loc_155CC')

    SetScenaFlags(ScenaFlag(0x0711, 2, 0x388A))
    SetScenaFlags(ScenaFlag(0x0711, 1, 0x3889))

    def _loc_155D2(): pass

    label('loc_155D2')

    SetScenaFlags(ScenaFlag(0x0711, 0, 0x3888))
    SetScenaFlags(ScenaFlag(0x0710, 7, 0x3887))

    def _loc_155D8(): pass

    label('loc_155D8')

    SetScenaFlags(ScenaFlag(0x0710, 6, 0x3886))
    OP_71(0x00, 0x39A4, 0x39A5)
    SetScenaFlags(ScenaFlag(0x0710, 5, 0x3885))
    SetScenaFlags(ScenaFlag(0x0062, 1, 0x311))
    SetScenaFlags(ScenaFlag(0x0BAA, 2, 0x5D52))

    def _loc_155EA(): pass

    label('loc_155EA')

    SetScenaFlags(ScenaFlag(0x0710, 4, 0x3884))
    SetScenaFlags(ScenaFlag(0x0710, 3, 0x3883))

    def _loc_155F0(): pass

    label('loc_155F0')

    SetScenaFlags(ScenaFlag(0x0710, 2, 0x3882))
    SetScenaFlags(ScenaFlag(0x0710, 1, 0x3881))

    def _loc_155F6(): pass

    label('loc_155F6')

    SetScenaFlags(ScenaFlag(0x0710, 0, 0x3880))
    SetScenaFlags(ScenaFlag(0x070B, 5, 0x385D))

    def _loc_155FC(): pass

    label('loc_155FC')

    SetScenaFlags(ScenaFlag(0x070B, 4, 0x385C))
    SetScenaFlags(ScenaFlag(0x070B, 3, 0x385B))

    def _loc_15602(): pass

    label('loc_15602')

    SetScenaFlags(ScenaFlag(0x070B, 2, 0x385A))
    SetScenaFlags(ScenaFlag(0x070B, 1, 0x3859))

    def _loc_15608(): pass

    label('loc_15608')

    SetScenaFlags(ScenaFlag(0x070B, 0, 0x3858))
    SetScenaFlags(ScenaFlag(0x070A, 7, 0x3857))

    def _loc_1560E(): pass

    label('loc_1560E')

    SetScenaFlags(ScenaFlag(0x070A, 6, 0x3856))
    SetScenaFlags(ScenaFlag(0x070A, 5, 0x3855))

    def _loc_15614(): pass

    label('loc_15614')

    SetScenaFlags(ScenaFlag(0x070A, 4, 0x3854))
    SetScenaFlags(ScenaFlag(0x070A, 3, 0x3853))

    def _loc_1561A(): pass

    label('loc_1561A')

    SetScenaFlags(ScenaFlag(0x070A, 2, 0x3852))
    SetScenaFlags(ScenaFlag(0x070A, 1, 0x3851))

    def _loc_15620(): pass

    label('loc_15620')

    SetScenaFlags(ScenaFlag(0x070A, 0, 0x3850))
    SetScenaFlags(ScenaFlag(0x0709, 7, 0x384F))

    def _loc_15626(): pass

    label('loc_15626')

    SetScenaFlags(ScenaFlag(0x0709, 6, 0x384E))
    SetScenaFlags(ScenaFlag(0x0709, 5, 0x384D))

    def _loc_1562C(): pass

    label('loc_1562C')

    SetScenaFlags(ScenaFlag(0x0709, 4, 0x384C))
    SetScenaFlags(ScenaFlag(0x0709, 3, 0x384B))

    def _loc_15632(): pass

    label('loc_15632')

    SetScenaFlags(ScenaFlag(0x0709, 2, 0x384A))
    SetScenaFlags(ScenaFlag(0x0709, 1, 0x3849))

    def _loc_15638(): pass

    label('loc_15638')

    SetScenaFlags(ScenaFlag(0x0709, 0, 0x3848))
    SetScenaFlags(ScenaFlag(0x0708, 7, 0x3847))

    def _loc_1563E(): pass

    label('loc_1563E')

    SetScenaFlags(ScenaFlag(0x0708, 6, 0x3846))
    SetScenaFlags(ScenaFlag(0x0708, 5, 0x3845))

    def _loc_15644(): pass

    label('loc_15644')

    SetScenaFlags(ScenaFlag(0x0708, 4, 0x3844))
    SetScenaFlags(ScenaFlag(0x0708, 3, 0x3843))

    def _loc_1564A(): pass

    label('loc_1564A')

    SetScenaFlags(ScenaFlag(0x0708, 2, 0x3842))
    SetScenaFlags(ScenaFlag(0x0708, 1, 0x3841))

    def _loc_15650(): pass

    label('loc_15650')

    SetScenaFlags(ScenaFlag(0x0708, 0, 0x3840))
    SetScenaFlags(ScenaFlag(0x0707, 7, 0x383F))

    def _loc_15656(): pass

    label('loc_15656')

    SetScenaFlags(ScenaFlag(0x0707, 6, 0x383E))
    SetScenaFlags(ScenaFlag(0x0707, 5, 0x383D))

    def _loc_1565C(): pass

    label('loc_1565C')

    SetScenaFlags(ScenaFlag(0x0707, 4, 0x383C))
    SetScenaFlags(ScenaFlag(0x0707, 3, 0x383B))

    def _loc_15662(): pass

    label('loc_15662')

    SetScenaFlags(ScenaFlag(0x0707, 2, 0x383A))
    SetScenaFlags(ScenaFlag(0x0707, 1, 0x3839))

    def _loc_15668(): pass

    label('loc_15668')

    SetScenaFlags(ScenaFlag(0x0707, 0, 0x3838))
    SetScenaFlags(ScenaFlag(0x0706, 7, 0x3837))

    def _loc_1566E(): pass

    label('loc_1566E')

    SetScenaFlags(ScenaFlag(0x0706, 6, 0x3836))
    SetScenaFlags(ScenaFlag(0x0706, 5, 0x3835))

    def _loc_15674(): pass

    label('loc_15674')

    SetScenaFlags(ScenaFlag(0x0706, 4, 0x3834))
    SetScenaFlags(ScenaFlag(0x0706, 3, 0x3833))

    def _loc_1567A(): pass

    label('loc_1567A')

    SetScenaFlags(ScenaFlag(0x0706, 2, 0x3832))
    SetScenaFlags(ScenaFlag(0x0706, 1, 0x3831))

    def _loc_15680(): pass

    label('loc_15680')

    SetScenaFlags(ScenaFlag(0x0706, 0, 0x3830))
    SetScenaFlags(ScenaFlag(0x0705, 7, 0x382F))

    def _loc_15686(): pass

    label('loc_15686')

    SetScenaFlags(ScenaFlag(0x0705, 6, 0x382E))
    OP_71(0x00, 0x39A2, 0x39A3)
    SetScenaFlags(ScenaFlag(0x0705, 5, 0x382D))

    def _loc_15692(): pass

    label('loc_15692')

    SetScenaFlags(ScenaFlag(0x0705, 4, 0x382C))
    SetScenaFlags(ScenaFlag(0x0705, 3, 0x382B))

    def _loc_15698(): pass

    label('loc_15698')

    SetScenaFlags(ScenaFlag(0x0705, 2, 0x382A))
    SetScenaFlags(ScenaFlag(0x0705, 1, 0x3829))

    def _loc_1569E(): pass

    label('loc_1569E')

    SetScenaFlags(ScenaFlag(0x0705, 0, 0x3828))
    SetScenaFlags(ScenaFlag(0x0704, 7, 0x3827))

    def _loc_156A4(): pass

    label('loc_156A4')

    SetScenaFlags(ScenaFlag(0x0704, 6, 0x3826))
    SetScenaFlags(ScenaFlag(0x0704, 5, 0x3825))

    def _loc_156AA(): pass

    label('loc_156AA')

    SetScenaFlags(ScenaFlag(0x0704, 4, 0x3824))
    SetScenaFlags(ScenaFlag(0x0704, 3, 0x3823))

    def _loc_156B0(): pass

    label('loc_156B0')

    SetScenaFlags(ScenaFlag(0x0704, 2, 0x3822))
    SetScenaFlags(ScenaFlag(0x0721, 7, 0x390F))
    OP_71(0x00, 0x399F, 0x39A0)
    SetScenaFlags(ScenaFlag(0x0704, 1, 0x3821))

    def _loc_156BF(): pass

    label('loc_156BF')

    SetScenaFlags(ScenaFlag(0x0704, 0, 0x3820))
    SetScenaFlags(ScenaFlag(0x0703, 7, 0x381F))

    def _loc_156C5(): pass

    label('loc_156C5')

    SetScenaFlags(ScenaFlag(0x0703, 6, 0x381E))
    SetScenaFlags(ScenaFlag(0x0703, 5, 0x381D))

    def _loc_156CB(): pass

    label('loc_156CB')

    SetScenaFlags(ScenaFlag(0x0703, 4, 0x381C))
    SetScenaFlags(ScenaFlag(0x0703, 3, 0x381B))

    def _loc_156D1(): pass

    label('loc_156D1')

    SetScenaFlags(ScenaFlag(0x0703, 2, 0x381A))
    SetScenaFlags(ScenaFlag(0x0703, 1, 0x3819))

    def _loc_156D7(): pass

    label('loc_156D7')

    SetScenaFlags(ScenaFlag(0x0703, 0, 0x3818))
    SetScenaFlags(ScenaFlag(0x0702, 7, 0x3817))

    def _loc_156DD(): pass

    label('loc_156DD')

    SetScenaFlags(ScenaFlag(0x0702, 6, 0x3816))
    SetScenaFlags(ScenaFlag(0x0733, 5, 0x399D))
    SetScenaFlags(ScenaFlag(0x0702, 5, 0x3815))

    def _loc_156E6(): pass

    label('loc_156E6')

    SetScenaFlags(ScenaFlag(0x0702, 4, 0x3814))
    SetScenaFlags(ScenaFlag(0x0702, 3, 0x3813))
    QuestCtrl(0x0016, 0x05)
    QuestCtrl(0x0017, 0x05)
    QuestCtrl(0x0018, 0x05)

    def _loc_156F8(): pass

    label('loc_156F8')

    SetScenaFlags(ScenaFlag(0x0702, 2, 0x3812))
    SetScenaFlags(ScenaFlag(0x0702, 1, 0x3811))

    def _loc_156FE(): pass

    label('loc_156FE')

    SetScenaFlags(ScenaFlag(0x0702, 0, 0x3810))
    SetScenaFlags(ScenaFlag(0x0701, 7, 0x380F))

    def _loc_15704(): pass

    label('loc_15704')

    SetScenaFlags(ScenaFlag(0x0701, 6, 0x380E))
    SetScenaFlags(ScenaFlag(0x0701, 5, 0x380D))

    def _loc_1570A(): pass

    label('loc_1570A')

    SetScenaFlags(ScenaFlag(0x0701, 4, 0x380C))
    SetScenaFlags(ScenaFlag(0x0701, 3, 0x380B))

    def _loc_15710(): pass

    label('loc_15710')

    SetScenaFlags(ScenaFlag(0x0701, 2, 0x380A))
    SetScenaFlags(ScenaFlag(0x0701, 1, 0x3809))

    def _loc_15716(): pass

    label('loc_15716')

    SetScenaFlags(ScenaFlag(0x0701, 0, 0x3808))
    SetScenaFlags(ScenaFlag(0x0700, 7, 0x3807))

    def _loc_1571C(): pass

    label('loc_1571C')

    SetScenaFlags(ScenaFlag(0x0700, 6, 0x3806))
    SetScenaFlags(ScenaFlag(0x0700, 5, 0x3805))

    def _loc_15722(): pass

    label('loc_15722')

    SetScenaFlags(ScenaFlag(0x0700, 4, 0x3804))
    SetScenaFlags(ScenaFlag(0x0700, 3, 0x3803))

    def _loc_15728(): pass

    label('loc_15728')

    SetScenaFlags(ScenaFlag(0x0700, 2, 0x3802))
    SetScenaFlags(ScenaFlag(0x0700, 1, 0x3801))

    def _loc_1572E(): pass

    label('loc_1572E')

    SetScenaFlags(ScenaFlag(0x0700, 0, 0x3800))
    SetScenaFlags(ScenaFlag(0x06FA, 7, 0x37D7))

    def _loc_15734(): pass

    label('loc_15734')

    SetScenaFlags(ScenaFlag(0x06FA, 6, 0x37D6))
    SetScenaFlags(ScenaFlag(0x06FA, 5, 0x37D5))

    def _loc_1573A(): pass

    label('loc_1573A')

    SetScenaFlags(ScenaFlag(0x06FA, 4, 0x37D4))
    SetScenaFlags(ScenaFlag(0x06FA, 3, 0x37D3))

    def _loc_15740(): pass

    label('loc_15740')

    SetScenaFlags(ScenaFlag(0x06FA, 2, 0x37D2))
    SetScenaFlags(ScenaFlag(0x06FA, 1, 0x37D1))

    def _loc_15746(): pass

    label('loc_15746')

    SetScenaFlags(ScenaFlag(0x06FA, 0, 0x37D0))
    SetScenaFlags(ScenaFlag(0x06F9, 7, 0x37CF))

    def _loc_1574C(): pass

    label('loc_1574C')

    SetScenaFlags(ScenaFlag(0x06F9, 6, 0x37CE))
    SetScenaFlags(ScenaFlag(0x06F9, 5, 0x37CD))

    def _loc_15752(): pass

    label('loc_15752')

    SetScenaFlags(ScenaFlag(0x06F9, 4, 0x37CC))
    SetScenaFlags(ScenaFlag(0x06F9, 3, 0x37CB))

    def _loc_15758(): pass

    label('loc_15758')

    SetScenaFlags(ScenaFlag(0x06F9, 2, 0x37CA))
    SetScenaFlags(ScenaFlag(0x06F9, 1, 0x37C9))

    def _loc_1575E(): pass

    label('loc_1575E')

    SetScenaFlags(ScenaFlag(0x06F9, 0, 0x37C8))
    SetScenaFlags(ScenaFlag(0x06F8, 7, 0x37C7))
    QuestCtrl(0x0015, 0x05)

    def _loc_15768(): pass

    label('loc_15768')

    SetScenaFlags(ScenaFlag(0x06F8, 6, 0x37C6))
    SetScenaFlags(ScenaFlag(0x06F8, 5, 0x37C5))

    def _loc_1576E(): pass

    label('loc_1576E')

    SetScenaFlags(ScenaFlag(0x06F8, 4, 0x37C4))
    SetScenaFlags(ScenaFlag(0x06F8, 3, 0x37C3))

    def _loc_15774(): pass

    label('loc_15774')

    SetScenaFlags(ScenaFlag(0x06F8, 2, 0x37C2))
    SetScenaFlags(ScenaFlag(0x06F8, 1, 0x37C1))

    def _loc_1577A(): pass

    label('loc_1577A')

    SetScenaFlags(ScenaFlag(0x06F8, 0, 0x37C0))
    SetScenaFlags(ScenaFlag(0x06F7, 7, 0x37BF))

    def _loc_15780(): pass

    label('loc_15780')

    SetScenaFlags(ScenaFlag(0x06F7, 6, 0x37BE))
    SetScenaFlags(ScenaFlag(0x06F7, 5, 0x37BD))

    def _loc_15786(): pass

    label('loc_15786')

    SetScenaFlags(ScenaFlag(0x06F7, 4, 0x37BC))
    SetScenaFlags(ScenaFlag(0x06F7, 3, 0x37BB))

    def _loc_1578C(): pass

    label('loc_1578C')

    SetScenaFlags(ScenaFlag(0x06F7, 2, 0x37BA))
    SetScenaFlags(ScenaFlag(0x06F7, 1, 0x37B9))

    def _loc_15792(): pass

    label('loc_15792')

    SetScenaFlags(ScenaFlag(0x06F7, 0, 0x37B8))
    OP_71(0x00, 0x3998, 0x3999)
    SetScenaFlags(ScenaFlag(0x06F6, 7, 0x37B7))

    def _loc_1579E(): pass

    label('loc_1579E')

    SetScenaFlags(ScenaFlag(0x06F6, 6, 0x37B6))
    SetScenaFlags(ScenaFlag(0x06F6, 5, 0x37B5))

    def _loc_157A4(): pass

    label('loc_157A4')

    SetScenaFlags(ScenaFlag(0x06F6, 4, 0x37B4))
    SetScenaFlags(ScenaFlag(0x06F6, 3, 0x37B3))

    def _loc_157AA(): pass

    label('loc_157AA')

    SetScenaFlags(ScenaFlag(0x06F6, 2, 0x37B2))
    SetScenaFlags(ScenaFlag(0x06F6, 1, 0x37B1))
    QuestCtrl(0x0012, 0x05)
    QuestCtrl(0x0013, 0x05)
    QuestCtrl(0x0014, 0x05)

    def _loc_157BC(): pass

    label('loc_157BC')

    SetScenaFlags(ScenaFlag(0x06F6, 0, 0x37B0))
    SetScenaFlags(ScenaFlag(0x06F5, 7, 0x37AF))

    def _loc_157C2(): pass

    label('loc_157C2')

    SetScenaFlags(ScenaFlag(0x06F5, 6, 0x37AE))
    SetScenaFlags(ScenaFlag(0x06F5, 5, 0x37AD))

    def _loc_157C8(): pass

    label('loc_157C8')

    SetScenaFlags(ScenaFlag(0x06F5, 4, 0x37AC))
    SetScenaFlags(ScenaFlag(0x06F5, 3, 0x37AB))

    def _loc_157CE(): pass

    label('loc_157CE')

    SetScenaFlags(ScenaFlag(0x06F5, 2, 0x37AA))
    SetScenaFlags(ScenaFlag(0x06F5, 1, 0x37A9))

    def _loc_157D4(): pass

    label('loc_157D4')

    SetScenaFlags(ScenaFlag(0x06F5, 0, 0x37A8))
    SetScenaFlags(ScenaFlag(0x06F4, 7, 0x37A7))

    def _loc_157DA(): pass

    label('loc_157DA')

    SetScenaFlags(ScenaFlag(0x06F4, 6, 0x37A6))
    SetScenaFlags(ScenaFlag(0x06F4, 5, 0x37A5))

    def _loc_157E0(): pass

    label('loc_157E0')

    SetScenaFlags(ScenaFlag(0x06F4, 4, 0x37A4))
    SetScenaFlags(ScenaFlag(0x06F4, 3, 0x37A3))

    def _loc_157E6(): pass

    label('loc_157E6')

    SetScenaFlags(ScenaFlag(0x06F4, 2, 0x37A2))
    SetScenaFlags(ScenaFlag(0x06F4, 1, 0x37A1))

    def _loc_157EC(): pass

    label('loc_157EC')

    SetScenaFlags(ScenaFlag(0x06F4, 0, 0x37A0))
    SetScenaFlags(ScenaFlag(0x06F1, 1, 0x3789))

    def _loc_157F2(): pass

    label('loc_157F2')

    SetScenaFlags(ScenaFlag(0x06F1, 0, 0x3788))
    SetScenaFlags(ScenaFlag(0x06F0, 7, 0x3787))

    def _loc_157F8(): pass

    label('loc_157F8')

    SetScenaFlags(ScenaFlag(0x06F0, 6, 0x3786))
    SetScenaFlags(ScenaFlag(0x06F0, 5, 0x3785))

    def _loc_157FE(): pass

    label('loc_157FE')

    SetScenaFlags(ScenaFlag(0x06F0, 4, 0x3784))
    SetScenaFlags(ScenaFlag(0x06F0, 3, 0x3783))

    def _loc_15804(): pass

    label('loc_15804')

    SetScenaFlags(ScenaFlag(0x06F0, 2, 0x3782))
    SetScenaFlags(ScenaFlag(0x06F0, 1, 0x3781))

    def _loc_1580A(): pass

    label('loc_1580A')

    SetScenaFlags(ScenaFlag(0x06F0, 0, 0x3780))
    SetScenaFlags(ScenaFlag(0x06EF, 7, 0x377F))

    def _loc_15810(): pass

    label('loc_15810')

    SetScenaFlags(ScenaFlag(0x06EF, 6, 0x377E))
    SetScenaFlags(ScenaFlag(0x06EF, 5, 0x377D))

    def _loc_15816(): pass

    label('loc_15816')

    SetScenaFlags(ScenaFlag(0x06EF, 4, 0x377C))
    SetScenaFlags(ScenaFlag(0x06EF, 3, 0x377B))

    def _loc_1581C(): pass

    label('loc_1581C')

    SetScenaFlags(ScenaFlag(0x06EF, 2, 0x377A))
    SetScenaFlags(ScenaFlag(0x06EF, 1, 0x3779))

    def _loc_15822(): pass

    label('loc_15822')

    SetScenaFlags(ScenaFlag(0x06EF, 0, 0x3778))
    SetScenaFlags(ScenaFlag(0x06EE, 7, 0x3777))

    def _loc_15828(): pass

    label('loc_15828')

    SetScenaFlags(ScenaFlag(0x06EE, 6, 0x3776))
    SetScenaFlags(ScenaFlag(0x06EE, 5, 0x3775))

    def _loc_1582E(): pass

    label('loc_1582E')

    SetScenaFlags(ScenaFlag(0x06EE, 4, 0x3774))
    SetScenaFlags(ScenaFlag(0x06EE, 3, 0x3773))

    def _loc_15834(): pass

    label('loc_15834')

    SetScenaFlags(ScenaFlag(0x06EE, 2, 0x3772))
    SetScenaFlags(ScenaFlag(0x06EE, 1, 0x3771))

    def _loc_1583A(): pass

    label('loc_1583A')

    SetScenaFlags(ScenaFlag(0x06EE, 0, 0x3770))
    SetScenaFlags(ScenaFlag(0x06ED, 7, 0x376F))

    def _loc_15840(): pass

    label('loc_15840')

    SetScenaFlags(ScenaFlag(0x06ED, 6, 0x376E))
    SetScenaFlags(ScenaFlag(0x06ED, 5, 0x376D))
    QuestCtrl(0x0011, 0x05)

    def _loc_1584A(): pass

    label('loc_1584A')

    SetScenaFlags(ScenaFlag(0x06ED, 4, 0x376C))
    SetScenaFlags(ScenaFlag(0x06ED, 3, 0x376B))

    def _loc_15850(): pass

    label('loc_15850')

    SetScenaFlags(ScenaFlag(0x06ED, 2, 0x376A))
    SetScenaFlags(ScenaFlag(0x06ED, 1, 0x3769))

    def _loc_15856(): pass

    label('loc_15856')

    SetScenaFlags(ScenaFlag(0x06ED, 0, 0x3768))
    SetScenaFlags(ScenaFlag(0x06EC, 7, 0x3767))

    def _loc_1585C(): pass

    label('loc_1585C')

    SetScenaFlags(ScenaFlag(0x06EC, 6, 0x3766))
    SetScenaFlags(ScenaFlag(0x06EC, 5, 0x3765))

    def _loc_15862(): pass

    label('loc_15862')

    SetScenaFlags(ScenaFlag(0x06EC, 4, 0x3764))
    OP_71(0x00, 0x3993, 0x3995)
    SetScenaFlags(ScenaFlag(0x0739, 5, 0x39CD))
    SetScenaFlags(ScenaFlag(0x06EC, 3, 0x3763))

    def _loc_15871(): pass

    label('loc_15871')

    SetScenaFlags(ScenaFlag(0x06EC, 2, 0x3762))
    SetScenaFlags(ScenaFlag(0x06EC, 1, 0x3761))

    def _loc_15877(): pass

    label('loc_15877')

    SetScenaFlags(ScenaFlag(0x06EC, 0, 0x3760))
    SetScenaFlags(ScenaFlag(0x06EB, 7, 0x375F))

    def _loc_1587D(): pass

    label('loc_1587D')

    SetScenaFlags(ScenaFlag(0x06EB, 6, 0x375E))
    SetScenaFlags(ScenaFlag(0x06EB, 5, 0x375D))

    def _loc_15883(): pass

    label('loc_15883')

    SetScenaFlags(ScenaFlag(0x06EB, 4, 0x375C))
    SetScenaFlags(ScenaFlag(0x06EB, 3, 0x375B))
    QuestCtrl(0x000E, 0x05)
    QuestCtrl(0x000F, 0x05)
    QuestCtrl(0x0010, 0x05)

    def _loc_15895(): pass

    label('loc_15895')

    SetScenaFlags(ScenaFlag(0x06EB, 2, 0x375A))
    SetScenaFlags(ScenaFlag(0x06EB, 1, 0x3759))

    def _loc_1589B(): pass

    label('loc_1589B')

    SetScenaFlags(ScenaFlag(0x06EB, 0, 0x3758))
    SetScenaFlags(ScenaFlag(0x06EA, 7, 0x3757))

    def _loc_158A1(): pass

    label('loc_158A1')

    SetScenaFlags(ScenaFlag(0x06EA, 6, 0x3756))
    SetScenaFlags(ScenaFlag(0x06EA, 5, 0x3755))

    def _loc_158A7(): pass

    label('loc_158A7')

    SetScenaFlags(ScenaFlag(0x06EA, 4, 0x3754))
    SetScenaFlags(ScenaFlag(0x06EA, 3, 0x3753))

    def _loc_158AD(): pass

    label('loc_158AD')

    SetScenaFlags(ScenaFlag(0x06EA, 2, 0x3752))
    SetScenaFlags(ScenaFlag(0x06EA, 1, 0x3751))

    def _loc_158B3(): pass

    label('loc_158B3')

    SetScenaFlags(ScenaFlag(0x06EA, 0, 0x3750))
    SetScenaFlags(ScenaFlag(0x06E7, 1, 0x3739))
    SetScenaFlags(ScenaFlag(0x0770, 3, 0x3B83))
    SetScenaFlags(ScenaFlag(0x0770, 4, 0x3B84))
    SetScenaFlags(ScenaFlag(0x0770, 5, 0x3B85))
    SetScenaFlags(ScenaFlag(0x0062, 0, 0x310))
    OP_13(0x00400000)

    def _loc_158CA(): pass

    label('loc_158CA')

    SetScenaFlags(ScenaFlag(0x06E7, 0, 0x3738))
    SetScenaFlags(ScenaFlag(0x06E6, 7, 0x3737))

    def _loc_158D0(): pass

    label('loc_158D0')

    SetScenaFlags(ScenaFlag(0x06E6, 6, 0x3736))
    SetScenaFlags(ScenaFlag(0x06E6, 5, 0x3735))

    def _loc_158D6(): pass

    label('loc_158D6')

    SetScenaFlags(ScenaFlag(0x06E6, 4, 0x3734))
    SetScenaFlags(ScenaFlag(0x06E6, 3, 0x3733))

    def _loc_158DC(): pass

    label('loc_158DC')

    SetScenaFlags(ScenaFlag(0x06E6, 2, 0x3732))
    SetScenaFlags(ScenaFlag(0x06E6, 1, 0x3731))

    def _loc_158E2(): pass

    label('loc_158E2')

    SetScenaFlags(ScenaFlag(0x06E6, 0, 0x3730))
    SetScenaFlags(ScenaFlag(0x06E5, 7, 0x372F))

    def _loc_158E8(): pass

    label('loc_158E8')

    SetScenaFlags(ScenaFlag(0x06E5, 6, 0x372E))
    SetScenaFlags(ScenaFlag(0x06E5, 5, 0x372D))

    def _loc_158EE(): pass

    label('loc_158EE')

    SetScenaFlags(ScenaFlag(0x06E5, 4, 0x372C))
    SetScenaFlags(ScenaFlag(0x06E5, 3, 0x372B))

    def _loc_158F4(): pass

    label('loc_158F4')

    SetScenaFlags(ScenaFlag(0x06E5, 2, 0x372A))
    SetScenaFlags(ScenaFlag(0x06E5, 1, 0x3729))

    def _loc_158FA(): pass

    label('loc_158FA')

    SetScenaFlags(ScenaFlag(0x06E5, 0, 0x3728))
    SetScenaFlags(ScenaFlag(0x06E4, 7, 0x3727))

    def _loc_15900(): pass

    label('loc_15900')

    SetScenaFlags(ScenaFlag(0x06E4, 6, 0x3726))
    SetScenaFlags(ScenaFlag(0x06E4, 5, 0x3725))

    def _loc_15906(): pass

    label('loc_15906')

    SetScenaFlags(ScenaFlag(0x06E4, 4, 0x3724))
    SetScenaFlags(ScenaFlag(0x06E4, 3, 0x3723))
    SetScenaFlags(ScenaFlag(0x0770, 1, 0x3B81))
    SetScenaFlags(ScenaFlag(0x0770, 2, 0x3B82))

    def _loc_15912(): pass

    label('loc_15912')

    SetScenaFlags(ScenaFlag(0x06E4, 2, 0x3722))
    SetScenaFlags(ScenaFlag(0x06E4, 1, 0x3721))

    def _loc_15918(): pass

    label('loc_15918')

    SetScenaFlags(ScenaFlag(0x06E4, 0, 0x3720))
    SetScenaFlags(ScenaFlag(0x06E3, 7, 0x371F))

    def _loc_1591E(): pass

    label('loc_1591E')

    SetScenaFlags(ScenaFlag(0x06E3, 6, 0x371E))
    SetScenaFlags(ScenaFlag(0x06E3, 5, 0x371D))

    def _loc_15924(): pass

    label('loc_15924')

    SetScenaFlags(ScenaFlag(0x06E3, 4, 0x371C))
    SetScenaFlags(ScenaFlag(0x06E3, 3, 0x371B))

    def _loc_1592A(): pass

    label('loc_1592A')

    SetScenaFlags(ScenaFlag(0x06E3, 2, 0x371A))
    SetScenaFlags(ScenaFlag(0x0721, 4, 0x390C))
    OP_71(0x00, 0x3989, 0x398E)
    SetScenaFlags(ScenaFlag(0x0738, 1, 0x39C1))
    SetScenaFlags(ScenaFlag(0x06E3, 1, 0x3719))
    SetScenaFlags(ScenaFlag(0x0770, 0, 0x3B80))

    def _loc_1593F(): pass

    label('loc_1593F')

    SetScenaFlags(ScenaFlag(0x06E3, 0, 0x3718))
    SetScenaFlags(ScenaFlag(0x06E2, 7, 0x3717))

    def _loc_15945(): pass

    label('loc_15945')

    SetScenaFlags(ScenaFlag(0x06E2, 6, 0x3716))
    SetScenaFlags(ScenaFlag(0x06E2, 5, 0x3715))

    def _loc_1594B(): pass

    label('loc_1594B')

    SetScenaFlags(ScenaFlag(0x06E2, 4, 0x3714))
    SetScenaFlags(ScenaFlag(0x06E2, 3, 0x3713))

    def _loc_15951(): pass

    label('loc_15951')

    SetScenaFlags(ScenaFlag(0x06E2, 2, 0x3712))
    SetScenaFlags(ScenaFlag(0x06E2, 1, 0x3711))

    def _loc_15957(): pass

    label('loc_15957')

    SetScenaFlags(ScenaFlag(0x06E2, 0, 0x3710))
    SetScenaFlags(ScenaFlag(0x06E1, 7, 0x370F))

    def _loc_1595D(): pass

    label('loc_1595D')

    SetScenaFlags(ScenaFlag(0x06E1, 6, 0x370E))
    SetScenaFlags(ScenaFlag(0x0721, 3, 0x390B))
    OP_71(0x00, 0x3980, 0x3988)
    OP_71(0x00, 0x39BE, 0x39C0)
    SetScenaFlags(ScenaFlag(0x0739, 4, 0x39CC))
    SetScenaFlags(ScenaFlag(0x06E1, 5, 0x370D))

    def _loc_15975(): pass

    label('loc_15975')

    SetScenaFlags(ScenaFlag(0x06E1, 4, 0x370C))
    SetScenaFlags(ScenaFlag(0x06E1, 3, 0x370B))

    def _loc_1597B(): pass

    label('loc_1597B')

    SetScenaFlags(ScenaFlag(0x06E1, 2, 0x370A))
    SetScenaFlags(ScenaFlag(0x06E1, 1, 0x3709))

    def _loc_15981(): pass

    label('loc_15981')

    SetScenaFlags(ScenaFlag(0x06E1, 0, 0x3708))
    SetScenaFlags(ScenaFlag(0x06E0, 7, 0x3707))

    def _loc_15987(): pass

    label('loc_15987')

    SetScenaFlags(ScenaFlag(0x06E0, 6, 0x3706))
    SetScenaFlags(ScenaFlag(0x06E0, 5, 0x3705))

    def _loc_1598D(): pass

    label('loc_1598D')

    SetScenaFlags(ScenaFlag(0x06E0, 4, 0x3704))
    SetScenaFlags(ScenaFlag(0x06E0, 3, 0x3703))

    def _loc_15993(): pass

    label('loc_15993')

    SetScenaFlags(ScenaFlag(0x06E0, 2, 0x3702))
    SetScenaFlags(ScenaFlag(0x06E0, 1, 0x3701))

    def _loc_15999(): pass

    label('loc_15999')

    SetScenaFlags(ScenaFlag(0x06E0, 0, 0x3700))

    Jump('loc_159A1')

    def _loc_159A1(): pass

    label('loc_159A1')

    Return()

# id: 0x001D offset: 0x159A4
@scena.Code('EV_DoJumpSet_03')
def EV_DoJumpSet_03():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01X_All')
    Call(ScriptId.Current, 'EV_Flag_Set_02_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS1')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x000040C7, 'loc_15DE7'),
        (0x000040C6, 'loc_15DED'),
        (0x000040C5, 'loc_15DF3'),
        (0x000040C4, 'loc_15DF9'),
        (0x000040C3, 'loc_15DFF'),
        (0x000040C2, 'loc_15E05'),
        (0x000040C1, 'loc_15E0B'),
        (0x000040C0, 'loc_15E11'),
        (0x000040BF, 'loc_15E17'),
        (0x000040BE, 'loc_15E3A'),
        (0x000040BD, 'loc_15E40'),
        (0x000040BC, 'loc_15E46'),
        (0x000040BB, 'loc_15E4C'),
        (0x000040BA, 'loc_15E52'),
        (0x000040B9, 'loc_15E58'),
        (0x000040B8, 'loc_15E5E'),
        (0x000040B7, 'loc_15E64'),
        (0x000040B6, 'loc_15E6A'),
        (0x000040B5, 'loc_15E70'),
        (0x000040B4, 'loc_15E76'),
        (0x000040B3, 'loc_15E7C'),
        (0x000040B2, 'loc_15E82'),
        (0x000040B1, 'loc_15E8C'),
        (0x000040B0, 'loc_15E92'),
        (0x0000409C, 'loc_15E98'),
        (0x0000409B, 'loc_15E9E'),
        (0x0000409A, 'loc_15EA4'),
        (0x00004099, 'loc_15EAA'),
        (0x00004098, 'loc_15EB0'),
        (0x00004097, 'loc_15EB6'),
        (0x00004096, 'loc_15EBC'),
        (0x00004095, 'loc_15EC2'),
        (0x00004094, 'loc_15EC8'),
        (0x00004093, 'loc_15ECE'),
        (0x00004092, 'loc_15ED4'),
        (0x00004091, 'loc_15EDA'),
        (0x00004090, 'loc_15EE0'),
        (0x0000408F, 'loc_15EE6'),
        (0x0000408E, 'loc_15EEC'),
        (0x0000408D, 'loc_15EF2'),
        (0x0000408C, 'loc_15EF8'),
        (0x0000408B, 'loc_15EFE'),
        (0x0000408A, 'loc_15F04'),
        (0x00004089, 'loc_15F0A'),
        (0x00004088, 'loc_15F28'),
        (0x00004087, 'loc_15F2E'),
        (0x00004086, 'loc_15F34'),
        (0x00004085, 'loc_15F3A'),
        (0x00004084, 'loc_15F40'),
        (0x00004083, 'loc_15F46'),
        (0x00004082, 'loc_15F4F'),
        (0x00004081, 'loc_15F55'),
        (0x00004080, 'loc_15F5B'),
        (0x0000406E, 'loc_15F87'),
        (0x0000406D, 'loc_15F8D'),
        (0x0000406C, 'loc_15F93'),
        (0x0000406B, 'loc_15F9C'),
        (0x0000406A, 'loc_15FA2'),
        (0x00004069, 'loc_15FA8'),
        (0x00004068, 'loc_15FAE'),
        (0x00004067, 'loc_15FB4'),
        (0x00004066, 'loc_15FBA'),
        (0x00004065, 'loc_15FC0'),
        (0x00004064, 'loc_15FC6'),
        (0x00004063, 'loc_15FCC'),
        (0x00004062, 'loc_15FD2'),
        (0x00004061, 'loc_15FD8'),
        (0x00004060, 'loc_15FDE'),
        (0x00004044, 'loc_15FE4'),
        (0x00004043, 'loc_15FEA'),
        (0x00004042, 'loc_15FF0'),
        (0x00004041, 'loc_15FF6'),
        (0x00004040, 'loc_15FFC'),
        (0x0000403F, 'loc_16002'),
        (0x0000403E, 'loc_16008'),
        (0x0000403D, 'loc_1600E'),
        (0x0000403C, 'loc_16014'),
        (0x0000403B, 'loc_16032'),
        (0x0000403A, 'loc_16038'),
        (0x00004039, 'loc_1603E'),
        (0x00004038, 'loc_16044'),
        (0x00004037, 'loc_1604A'),
        (0x00004036, 'loc_16050'),
        (0x00004035, 'loc_16056'),
        (0x00004034, 'loc_1605C'),
        (0x00004033, 'loc_16062'),
        (0x00004032, 'loc_1606B'),
        (0x00004031, 'loc_16071'),
        (0x00004030, 'loc_16077'),
        (0x0000401B, 'loc_1607D'),
        (0x0000401A, 'loc_160AA'),
        (0x00004019, 'loc_160B0'),
        (0x00004018, 'loc_160B6'),
        (0x00004017, 'loc_160BC'),
        (0x00004016, 'loc_160C2'),
        (0x00004015, 'loc_160C8'),
        (0x00004014, 'loc_160CE'),
        (0x00004013, 'loc_160D4'),
        (0x00004012, 'loc_160DA'),
        (0x00004011, 'loc_160E0'),
        (0x00004010, 'loc_160E6'),
        (0x0000400F, 'loc_160EC'),
        (0x0000400E, 'loc_160F2'),
        (0x0000400D, 'loc_16116'),
        (0x0000400C, 'loc_1611C'),
        (0x0000400B, 'loc_16122'),
        (0x0000400A, 'loc_16128'),
        (0x00004009, 'loc_1612E'),
        (0x00004008, 'loc_16134'),
        (0x00004007, 'loc_1613A'),
        (0x00004006, 'loc_16140'),
        (0x00004005, 'loc_16146'),
        (0x00004004, 'loc_1614C'),
        (0x00004003, 'loc_16152'),
        (0x00004002, 'loc_16158'),
        (0x00004001, 'loc_1615E'),
        (0x00004000, 'loc_16164'),
        (-1, 'loc_1616C'),
    )

    def _loc_15DE7(): pass

    label('loc_15DE7')

    SetScenaFlags(ScenaFlag(0x0847, 6, 0x423E))
    SetScenaFlags(ScenaFlag(0x0847, 5, 0x423D))

    def _loc_15DED(): pass

    label('loc_15DED')

    SetScenaFlags(ScenaFlag(0x0847, 4, 0x423C))
    SetScenaFlags(ScenaFlag(0x0847, 3, 0x423B))

    def _loc_15DF3(): pass

    label('loc_15DF3')

    SetScenaFlags(ScenaFlag(0x0847, 2, 0x423A))
    SetScenaFlags(ScenaFlag(0x0847, 1, 0x4239))

    def _loc_15DF9(): pass

    label('loc_15DF9')

    SetScenaFlags(ScenaFlag(0x0847, 0, 0x4238))
    SetScenaFlags(ScenaFlag(0x0846, 7, 0x4237))

    def _loc_15DFF(): pass

    label('loc_15DFF')

    SetScenaFlags(ScenaFlag(0x0846, 6, 0x4236))
    SetScenaFlags(ScenaFlag(0x0846, 5, 0x4235))

    def _loc_15E05(): pass

    label('loc_15E05')

    SetScenaFlags(ScenaFlag(0x0846, 4, 0x4234))
    SetScenaFlags(ScenaFlag(0x0846, 3, 0x4233))

    def _loc_15E0B(): pass

    label('loc_15E0B')

    SetScenaFlags(ScenaFlag(0x0846, 2, 0x4232))
    SetScenaFlags(ScenaFlag(0x0846, 1, 0x4231))

    def _loc_15E11(): pass

    label('loc_15E11')

    SetScenaFlags(ScenaFlag(0x0846, 0, 0x4230))
    SetScenaFlags(ScenaFlag(0x0845, 7, 0x422F))

    def _loc_15E17(): pass

    label('loc_15E17')

    SetScenaFlags(ScenaFlag(0x0845, 6, 0x422E))
    SetScenaFlags(ScenaFlag(0x0845, 5, 0x422D))
    Call(ScriptId.System, 'SetKisinChange_ValimarS2A')

    def _loc_15E3A(): pass

    label('loc_15E3A')

    SetScenaFlags(ScenaFlag(0x0845, 4, 0x422C))
    SetScenaFlags(ScenaFlag(0x0845, 3, 0x422B))

    def _loc_15E40(): pass

    label('loc_15E40')

    SetScenaFlags(ScenaFlag(0x0845, 2, 0x422A))
    SetScenaFlags(ScenaFlag(0x0845, 1, 0x4229))

    def _loc_15E46(): pass

    label('loc_15E46')

    SetScenaFlags(ScenaFlag(0x0845, 0, 0x4228))
    SetScenaFlags(ScenaFlag(0x0844, 7, 0x4227))

    def _loc_15E4C(): pass

    label('loc_15E4C')

    SetScenaFlags(ScenaFlag(0x0844, 6, 0x4226))
    SetScenaFlags(ScenaFlag(0x0844, 5, 0x4225))

    def _loc_15E52(): pass

    label('loc_15E52')

    SetScenaFlags(ScenaFlag(0x0844, 4, 0x4224))
    SetScenaFlags(ScenaFlag(0x0844, 3, 0x4223))

    def _loc_15E58(): pass

    label('loc_15E58')

    SetScenaFlags(ScenaFlag(0x0844, 2, 0x4222))
    SetScenaFlags(ScenaFlag(0x0844, 1, 0x4221))

    def _loc_15E5E(): pass

    label('loc_15E5E')

    SetScenaFlags(ScenaFlag(0x0844, 0, 0x4220))
    SetScenaFlags(ScenaFlag(0x0843, 7, 0x421F))

    def _loc_15E64(): pass

    label('loc_15E64')

    SetScenaFlags(ScenaFlag(0x0843, 6, 0x421E))
    SetScenaFlags(ScenaFlag(0x0843, 5, 0x421D))

    def _loc_15E6A(): pass

    label('loc_15E6A')

    SetScenaFlags(ScenaFlag(0x0843, 4, 0x421C))
    SetScenaFlags(ScenaFlag(0x0843, 3, 0x421B))

    def _loc_15E70(): pass

    label('loc_15E70')

    SetScenaFlags(ScenaFlag(0x0843, 2, 0x421A))
    SetScenaFlags(ScenaFlag(0x0843, 1, 0x4219))

    def _loc_15E76(): pass

    label('loc_15E76')

    SetScenaFlags(ScenaFlag(0x0843, 0, 0x4218))
    SetScenaFlags(ScenaFlag(0x0842, 7, 0x4217))

    def _loc_15E7C(): pass

    label('loc_15E7C')

    SetScenaFlags(ScenaFlag(0x0842, 6, 0x4216))
    SetScenaFlags(ScenaFlag(0x0842, 5, 0x4215))

    def _loc_15E82(): pass

    label('loc_15E82')

    SetScenaFlags(ScenaFlag(0x0842, 4, 0x4214))
    SetScenaFlags(ScenaFlag(0x0842, 3, 0x4213))
    QuestCtrl(0x0028, 0x05)

    def _loc_15E8C(): pass

    label('loc_15E8C')

    SetScenaFlags(ScenaFlag(0x0842, 2, 0x4212))
    SetScenaFlags(ScenaFlag(0x0842, 1, 0x4211))

    def _loc_15E92(): pass

    label('loc_15E92')

    SetScenaFlags(ScenaFlag(0x0842, 0, 0x4210))
    SetScenaFlags(ScenaFlag(0x083F, 1, 0x41F9))

    def _loc_15E98(): pass

    label('loc_15E98')

    SetScenaFlags(ScenaFlag(0x083F, 0, 0x41F8))
    SetScenaFlags(ScenaFlag(0x083E, 7, 0x41F7))

    def _loc_15E9E(): pass

    label('loc_15E9E')

    SetScenaFlags(ScenaFlag(0x083E, 6, 0x41F6))
    SetScenaFlags(ScenaFlag(0x083E, 5, 0x41F5))

    def _loc_15EA4(): pass

    label('loc_15EA4')

    SetScenaFlags(ScenaFlag(0x083E, 4, 0x41F4))
    SetScenaFlags(ScenaFlag(0x083E, 3, 0x41F3))

    def _loc_15EAA(): pass

    label('loc_15EAA')

    SetScenaFlags(ScenaFlag(0x083E, 2, 0x41F2))
    SetScenaFlags(ScenaFlag(0x083E, 1, 0x41F1))

    def _loc_15EB0(): pass

    label('loc_15EB0')

    SetScenaFlags(ScenaFlag(0x083E, 0, 0x41F0))
    SetScenaFlags(ScenaFlag(0x083D, 7, 0x41EF))

    def _loc_15EB6(): pass

    label('loc_15EB6')

    SetScenaFlags(ScenaFlag(0x083D, 6, 0x41EE))
    SetScenaFlags(ScenaFlag(0x083D, 5, 0x41ED))

    def _loc_15EBC(): pass

    label('loc_15EBC')

    SetScenaFlags(ScenaFlag(0x083D, 4, 0x41EC))
    SetScenaFlags(ScenaFlag(0x083D, 3, 0x41EB))

    def _loc_15EC2(): pass

    label('loc_15EC2')

    SetScenaFlags(ScenaFlag(0x083D, 2, 0x41EA))
    SetScenaFlags(ScenaFlag(0x083D, 1, 0x41E9))

    def _loc_15EC8(): pass

    label('loc_15EC8')

    SetScenaFlags(ScenaFlag(0x083D, 0, 0x41E8))
    SetScenaFlags(ScenaFlag(0x083C, 7, 0x41E7))

    def _loc_15ECE(): pass

    label('loc_15ECE')

    SetScenaFlags(ScenaFlag(0x083C, 6, 0x41E6))
    SetScenaFlags(ScenaFlag(0x083C, 5, 0x41E5))

    def _loc_15ED4(): pass

    label('loc_15ED4')

    SetScenaFlags(ScenaFlag(0x083C, 4, 0x41E4))
    SetScenaFlags(ScenaFlag(0x083C, 3, 0x41E3))

    def _loc_15EDA(): pass

    label('loc_15EDA')

    SetScenaFlags(ScenaFlag(0x083C, 2, 0x41E2))
    SetScenaFlags(ScenaFlag(0x083C, 1, 0x41E1))

    def _loc_15EE0(): pass

    label('loc_15EE0')

    SetScenaFlags(ScenaFlag(0x083C, 0, 0x41E0))
    SetScenaFlags(ScenaFlag(0x083B, 7, 0x41DF))

    def _loc_15EE6(): pass

    label('loc_15EE6')

    SetScenaFlags(ScenaFlag(0x083B, 6, 0x41DE))
    SetScenaFlags(ScenaFlag(0x083B, 5, 0x41DD))

    def _loc_15EEC(): pass

    label('loc_15EEC')

    SetScenaFlags(ScenaFlag(0x083B, 4, 0x41DC))
    SetScenaFlags(ScenaFlag(0x083B, 3, 0x41DB))

    def _loc_15EF2(): pass

    label('loc_15EF2')

    SetScenaFlags(ScenaFlag(0x083B, 2, 0x41DA))
    SetScenaFlags(ScenaFlag(0x083B, 1, 0x41D9))

    def _loc_15EF8(): pass

    label('loc_15EF8')

    SetScenaFlags(ScenaFlag(0x083B, 0, 0x41D8))
    SetScenaFlags(ScenaFlag(0x083A, 7, 0x41D7))

    def _loc_15EFE(): pass

    label('loc_15EFE')

    SetScenaFlags(ScenaFlag(0x083A, 6, 0x41D6))
    SetScenaFlags(ScenaFlag(0x083A, 5, 0x41D5))

    def _loc_15F04(): pass

    label('loc_15F04')

    SetScenaFlags(ScenaFlag(0x083A, 4, 0x41D4))
    SetScenaFlags(ScenaFlag(0x083A, 3, 0x41D3))

    def _loc_15F0A(): pass

    label('loc_15F0A')

    SetScenaFlags(ScenaFlag(0x083A, 2, 0x41D2))
    SetScenaFlags(ScenaFlag(0x083A, 1, 0x41D1))
    QuestCtrl(0x0022, 0x05)
    QuestCtrl(0x0023, 0x05)
    QuestCtrl(0x0024, 0x05)
    QuestCtrl(0x0025, 0x05)
    QuestCtrl(0x0026, 0x05)
    QuestCtrl(0x0027, 0x05)

    def _loc_15F28(): pass

    label('loc_15F28')

    SetScenaFlags(ScenaFlag(0x083A, 0, 0x41D0))
    SetScenaFlags(ScenaFlag(0x0839, 7, 0x41CF))

    def _loc_15F2E(): pass

    label('loc_15F2E')

    SetScenaFlags(ScenaFlag(0x0839, 6, 0x41CE))
    SetScenaFlags(ScenaFlag(0x0839, 5, 0x41CD))

    def _loc_15F34(): pass

    label('loc_15F34')

    SetScenaFlags(ScenaFlag(0x0839, 4, 0x41CC))
    SetScenaFlags(ScenaFlag(0x0839, 3, 0x41CB))

    def _loc_15F3A(): pass

    label('loc_15F3A')

    SetScenaFlags(ScenaFlag(0x0839, 2, 0x41CA))
    SetScenaFlags(ScenaFlag(0x0839, 1, 0x41C9))

    def _loc_15F40(): pass

    label('loc_15F40')

    SetScenaFlags(ScenaFlag(0x0839, 0, 0x41C8))
    SetScenaFlags(ScenaFlag(0x0838, 7, 0x41C7))

    def _loc_15F46(): pass

    label('loc_15F46')

    SetScenaFlags(ScenaFlag(0x0838, 6, 0x41C6))
    SetScenaFlags(ScenaFlag(0x0838, 5, 0x41C5))
    SetScenaFlags(ScenaFlag(0x0BAA, 4, 0x5D54))

    def _loc_15F4F(): pass

    label('loc_15F4F')

    SetScenaFlags(ScenaFlag(0x0838, 4, 0x41C4))
    SetScenaFlags(ScenaFlag(0x0838, 3, 0x41C3))

    def _loc_15F55(): pass

    label('loc_15F55')

    SetScenaFlags(ScenaFlag(0x0838, 2, 0x41C2))
    SetScenaFlags(ScenaFlag(0x0838, 1, 0x41C1))

    def _loc_15F5B(): pass

    label('loc_15F5B')

    SetScenaFlags(ScenaFlag(0x0838, 0, 0x41C0))
    SetScenaFlags(ScenaFlag(0x0835, 5, 0x41AD))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0088, 1, 0x441)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15F87',
    )

    Call(ScriptId.System, 'SetKisinChange_ValimarS2')

    def _loc_15F87(): pass

    label('loc_15F87')

    SetScenaFlags(ScenaFlag(0x0835, 4, 0x41AC))
    SetScenaFlags(ScenaFlag(0x0835, 3, 0x41AB))

    def _loc_15F8D(): pass

    label('loc_15F8D')

    SetScenaFlags(ScenaFlag(0x0835, 2, 0x41AA))
    SetScenaFlags(ScenaFlag(0x0835, 1, 0x41A9))

    def _loc_15F93(): pass

    label('loc_15F93')

    SetScenaFlags(ScenaFlag(0x0835, 0, 0x41A8))
    SetScenaFlags(ScenaFlag(0x0860, 2, 0x4302))
    SetScenaFlags(ScenaFlag(0x0834, 7, 0x41A7))

    def _loc_15F9C(): pass

    label('loc_15F9C')

    SetScenaFlags(ScenaFlag(0x0834, 6, 0x41A6))
    SetScenaFlags(ScenaFlag(0x0834, 5, 0x41A5))

    def _loc_15FA2(): pass

    label('loc_15FA2')

    SetScenaFlags(ScenaFlag(0x0834, 4, 0x41A4))
    SetScenaFlags(ScenaFlag(0x0834, 3, 0x41A3))

    def _loc_15FA8(): pass

    label('loc_15FA8')

    SetScenaFlags(ScenaFlag(0x0834, 2, 0x41A2))
    SetScenaFlags(ScenaFlag(0x0834, 1, 0x41A1))

    def _loc_15FAE(): pass

    label('loc_15FAE')

    SetScenaFlags(ScenaFlag(0x0834, 0, 0x41A0))
    SetScenaFlags(ScenaFlag(0x0833, 7, 0x419F))

    def _loc_15FB4(): pass

    label('loc_15FB4')

    SetScenaFlags(ScenaFlag(0x0833, 6, 0x419E))
    SetScenaFlags(ScenaFlag(0x0833, 5, 0x419D))

    def _loc_15FBA(): pass

    label('loc_15FBA')

    SetScenaFlags(ScenaFlag(0x0833, 4, 0x419C))
    SetScenaFlags(ScenaFlag(0x0833, 3, 0x419B))

    def _loc_15FC0(): pass

    label('loc_15FC0')

    SetScenaFlags(ScenaFlag(0x0833, 2, 0x419A))
    SetScenaFlags(ScenaFlag(0x0833, 1, 0x4199))

    def _loc_15FC6(): pass

    label('loc_15FC6')

    SetScenaFlags(ScenaFlag(0x0833, 0, 0x4198))
    SetScenaFlags(ScenaFlag(0x0832, 7, 0x4197))

    def _loc_15FCC(): pass

    label('loc_15FCC')

    SetScenaFlags(ScenaFlag(0x0832, 6, 0x4196))
    SetScenaFlags(ScenaFlag(0x0832, 5, 0x4195))

    def _loc_15FD2(): pass

    label('loc_15FD2')

    SetScenaFlags(ScenaFlag(0x0832, 4, 0x4194))
    SetScenaFlags(ScenaFlag(0x0832, 3, 0x4193))

    def _loc_15FD8(): pass

    label('loc_15FD8')

    SetScenaFlags(ScenaFlag(0x0832, 2, 0x4192))
    SetScenaFlags(ScenaFlag(0x0832, 1, 0x4191))

    def _loc_15FDE(): pass

    label('loc_15FDE')

    SetScenaFlags(ScenaFlag(0x0832, 0, 0x4190))
    SetScenaFlags(ScenaFlag(0x082F, 1, 0x4179))

    def _loc_15FE4(): pass

    label('loc_15FE4')

    SetScenaFlags(ScenaFlag(0x082F, 0, 0x4178))
    SetScenaFlags(ScenaFlag(0x082E, 7, 0x4177))

    def _loc_15FEA(): pass

    label('loc_15FEA')

    SetScenaFlags(ScenaFlag(0x082E, 6, 0x4176))
    SetScenaFlags(ScenaFlag(0x082E, 5, 0x4175))

    def _loc_15FF0(): pass

    label('loc_15FF0')

    SetScenaFlags(ScenaFlag(0x082E, 4, 0x4174))
    SetScenaFlags(ScenaFlag(0x082E, 3, 0x4173))

    def _loc_15FF6(): pass

    label('loc_15FF6')

    SetScenaFlags(ScenaFlag(0x082E, 2, 0x4172))
    SetScenaFlags(ScenaFlag(0x082E, 1, 0x4171))

    def _loc_15FFC(): pass

    label('loc_15FFC')

    SetScenaFlags(ScenaFlag(0x082E, 0, 0x4170))
    SetScenaFlags(ScenaFlag(0x082D, 7, 0x416F))

    def _loc_16002(): pass

    label('loc_16002')

    SetScenaFlags(ScenaFlag(0x082D, 6, 0x416E))
    SetScenaFlags(ScenaFlag(0x082D, 5, 0x416D))

    def _loc_16008(): pass

    label('loc_16008')

    SetScenaFlags(ScenaFlag(0x082D, 4, 0x416C))
    SetScenaFlags(ScenaFlag(0x082D, 3, 0x416B))

    def _loc_1600E(): pass

    label('loc_1600E')

    SetScenaFlags(ScenaFlag(0x082D, 2, 0x416A))
    SetScenaFlags(ScenaFlag(0x082D, 1, 0x4169))

    def _loc_16014(): pass

    label('loc_16014')

    SetScenaFlags(ScenaFlag(0x082D, 0, 0x4168))
    SetScenaFlags(ScenaFlag(0x082C, 7, 0x4167))
    QuestCtrl(0x001C, 0x05)
    QuestCtrl(0x001D, 0x05)
    QuestCtrl(0x001E, 0x05)
    QuestCtrl(0x001F, 0x05)
    QuestCtrl(0x0020, 0x05)
    QuestCtrl(0x0021, 0x05)

    def _loc_16032(): pass

    label('loc_16032')

    SetScenaFlags(ScenaFlag(0x082C, 6, 0x4166))
    SetScenaFlags(ScenaFlag(0x082C, 5, 0x4165))

    def _loc_16038(): pass

    label('loc_16038')

    SetScenaFlags(ScenaFlag(0x082C, 4, 0x4164))
    SetScenaFlags(ScenaFlag(0x082C, 3, 0x4163))

    def _loc_1603E(): pass

    label('loc_1603E')

    SetScenaFlags(ScenaFlag(0x082C, 2, 0x4162))
    SetScenaFlags(ScenaFlag(0x082C, 1, 0x4161))

    def _loc_16044(): pass

    label('loc_16044')

    SetScenaFlags(ScenaFlag(0x082C, 0, 0x4160))
    SetScenaFlags(ScenaFlag(0x082B, 7, 0x415F))

    def _loc_1604A(): pass

    label('loc_1604A')

    SetScenaFlags(ScenaFlag(0x082B, 6, 0x415E))
    SetScenaFlags(ScenaFlag(0x082B, 5, 0x415D))

    def _loc_16050(): pass

    label('loc_16050')

    SetScenaFlags(ScenaFlag(0x082B, 4, 0x415C))
    SetScenaFlags(ScenaFlag(0x082B, 3, 0x415B))

    def _loc_16056(): pass

    label('loc_16056')

    SetScenaFlags(ScenaFlag(0x082B, 2, 0x415A))
    SetScenaFlags(ScenaFlag(0x082B, 1, 0x4159))

    def _loc_1605C(): pass

    label('loc_1605C')

    SetScenaFlags(ScenaFlag(0x082B, 0, 0x4158))
    SetScenaFlags(ScenaFlag(0x082A, 7, 0x4157))

    def _loc_16062(): pass

    label('loc_16062')

    SetScenaFlags(ScenaFlag(0x082A, 6, 0x4156))
    SetScenaFlags(ScenaFlag(0x082A, 5, 0x4155))
    SetScenaFlags(ScenaFlag(0x0BAA, 3, 0x5D53))

    def _loc_1606B(): pass

    label('loc_1606B')

    SetScenaFlags(ScenaFlag(0x082A, 4, 0x4154))
    SetScenaFlags(ScenaFlag(0x082A, 3, 0x4153))

    def _loc_16071(): pass

    label('loc_16071')

    SetScenaFlags(ScenaFlag(0x082A, 2, 0x4152))
    SetScenaFlags(ScenaFlag(0x082A, 1, 0x4151))

    def _loc_16077(): pass

    label('loc_16077')

    SetScenaFlags(ScenaFlag(0x082A, 0, 0x4150))
    SetScenaFlags(ScenaFlag(0x0826, 7, 0x4137))

    def _loc_1607D(): pass

    label('loc_1607D')

    SetScenaFlags(ScenaFlag(0x0826, 6, 0x4136))
    SetScenaFlags(ScenaFlag(0x0826, 5, 0x4135))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_160AA',
    )

    Call(ScriptId.System, 'SetKisinChange_ValimarS1A')

    def _loc_160AA(): pass

    label('loc_160AA')

    SetScenaFlags(ScenaFlag(0x0826, 4, 0x4134))
    SetScenaFlags(ScenaFlag(0x0826, 3, 0x4133))

    def _loc_160B0(): pass

    label('loc_160B0')

    SetScenaFlags(ScenaFlag(0x0826, 2, 0x4132))
    SetScenaFlags(ScenaFlag(0x0826, 1, 0x4131))

    def _loc_160B6(): pass

    label('loc_160B6')

    SetScenaFlags(ScenaFlag(0x0826, 0, 0x4130))
    SetScenaFlags(ScenaFlag(0x0825, 7, 0x412F))

    def _loc_160BC(): pass

    label('loc_160BC')

    SetScenaFlags(ScenaFlag(0x0825, 6, 0x412E))
    SetScenaFlags(ScenaFlag(0x0825, 5, 0x412D))

    def _loc_160C2(): pass

    label('loc_160C2')

    SetScenaFlags(ScenaFlag(0x0825, 4, 0x412C))
    SetScenaFlags(ScenaFlag(0x0825, 3, 0x412B))

    def _loc_160C8(): pass

    label('loc_160C8')

    SetScenaFlags(ScenaFlag(0x0825, 2, 0x412A))
    SetScenaFlags(ScenaFlag(0x0825, 1, 0x4129))

    def _loc_160CE(): pass

    label('loc_160CE')

    SetScenaFlags(ScenaFlag(0x0825, 0, 0x4128))
    SetScenaFlags(ScenaFlag(0x0824, 7, 0x4127))

    def _loc_160D4(): pass

    label('loc_160D4')

    SetScenaFlags(ScenaFlag(0x0824, 6, 0x4126))
    SetScenaFlags(ScenaFlag(0x0824, 5, 0x4125))

    def _loc_160DA(): pass

    label('loc_160DA')

    SetScenaFlags(ScenaFlag(0x0824, 4, 0x4124))
    SetScenaFlags(ScenaFlag(0x0824, 3, 0x4123))

    def _loc_160E0(): pass

    label('loc_160E0')

    SetScenaFlags(ScenaFlag(0x0824, 2, 0x4122))
    SetScenaFlags(ScenaFlag(0x0824, 1, 0x4121))

    def _loc_160E6(): pass

    label('loc_160E6')

    SetScenaFlags(ScenaFlag(0x0824, 0, 0x4120))
    SetScenaFlags(ScenaFlag(0x0823, 7, 0x411F))

    def _loc_160EC(): pass

    label('loc_160EC')

    SetScenaFlags(ScenaFlag(0x0823, 6, 0x411E))
    SetScenaFlags(ScenaFlag(0x0823, 5, 0x411D))

    def _loc_160F2(): pass

    label('loc_160F2')

    SetScenaFlags(ScenaFlag(0x0823, 4, 0x411C))
    SetScenaFlags(ScenaFlag(0x0860, 1, 0x4301))
    OP_71(0x00, 0x4380, 0x438B)
    OP_71(0x00, 0x4390, 0x439D)
    OP_71(0x00, 0x4580, 0x4582)
    SetScenaFlags(ScenaFlag(0x0823, 3, 0x411B))
    SetScenaFlags(ScenaFlag(0x08B0, 0, 0x4580))
    SetScenaFlags(ScenaFlag(0x08B0, 1, 0x4581))
    SetScenaFlags(ScenaFlag(0x08B0, 2, 0x4582))

    def _loc_16116(): pass

    label('loc_16116')

    SetScenaFlags(ScenaFlag(0x0823, 2, 0x411A))
    SetScenaFlags(ScenaFlag(0x0823, 1, 0x4119))

    def _loc_1611C(): pass

    label('loc_1611C')

    SetScenaFlags(ScenaFlag(0x0823, 0, 0x4118))
    SetScenaFlags(ScenaFlag(0x0822, 7, 0x4117))

    def _loc_16122(): pass

    label('loc_16122')

    SetScenaFlags(ScenaFlag(0x0822, 6, 0x4116))
    SetScenaFlags(ScenaFlag(0x0822, 5, 0x4115))

    def _loc_16128(): pass

    label('loc_16128')

    SetScenaFlags(ScenaFlag(0x0822, 4, 0x4114))
    SetScenaFlags(ScenaFlag(0x0822, 3, 0x4113))

    def _loc_1612E(): pass

    label('loc_1612E')

    SetScenaFlags(ScenaFlag(0x0822, 2, 0x4112))
    SetScenaFlags(ScenaFlag(0x0822, 1, 0x4111))

    def _loc_16134(): pass

    label('loc_16134')

    SetScenaFlags(ScenaFlag(0x0822, 0, 0x4110))
    SetScenaFlags(ScenaFlag(0x0821, 7, 0x410F))

    def _loc_1613A(): pass

    label('loc_1613A')

    SetScenaFlags(ScenaFlag(0x0821, 6, 0x410E))
    SetScenaFlags(ScenaFlag(0x0821, 5, 0x410D))

    def _loc_16140(): pass

    label('loc_16140')

    SetScenaFlags(ScenaFlag(0x0821, 4, 0x410C))
    SetScenaFlags(ScenaFlag(0x0821, 3, 0x410B))

    def _loc_16146(): pass

    label('loc_16146')

    SetScenaFlags(ScenaFlag(0x0821, 2, 0x410A))
    SetScenaFlags(ScenaFlag(0x0821, 1, 0x4109))

    def _loc_1614C(): pass

    label('loc_1614C')

    SetScenaFlags(ScenaFlag(0x0821, 0, 0x4108))
    SetScenaFlags(ScenaFlag(0x0820, 7, 0x4107))

    def _loc_16152(): pass

    label('loc_16152')

    SetScenaFlags(ScenaFlag(0x0820, 6, 0x4106))
    SetScenaFlags(ScenaFlag(0x0820, 5, 0x4105))

    def _loc_16158(): pass

    label('loc_16158')

    SetScenaFlags(ScenaFlag(0x0820, 4, 0x4104))
    SetScenaFlags(ScenaFlag(0x0820, 3, 0x4103))

    def _loc_1615E(): pass

    label('loc_1615E')

    SetScenaFlags(ScenaFlag(0x0820, 2, 0x4102))
    SetScenaFlags(ScenaFlag(0x0820, 1, 0x4101))

    def _loc_16164(): pass

    label('loc_16164')

    SetScenaFlags(ScenaFlag(0x0820, 0, 0x4100))

    Jump('loc_1616C')

    def _loc_1616C(): pass

    label('loc_1616C')

    Return()

# id: 0x001E offset: 0x16170
@scena.Code('EV_DoJumpSet_03X')
def EV_DoJumpSet_03X():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01X_All')
    Call(ScriptId.Current, 'EV_Flag_Set_02_All')
    Call(ScriptId.Current, 'EV_Flag_Set_03_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS2A')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x0000824B, 'loc_162BA'),
        (0x00005011, 'loc_162C0'),
        (0x00005010, 'loc_162C6'),
        (0x0000500F, 'loc_162CC'),
        (0x0000500E, 'loc_162D2'),
        (0x0000500D, 'loc_162D8'),
        (0x0000500C, 'loc_162DE'),
        (0x0000500B, 'loc_162E4'),
        (0x0000500A, 'loc_162EA'),
        (0x00005009, 'loc_162F0'),
        (0x00005008, 'loc_162F6'),
        (0x00005007, 'loc_162FC'),
        (0x00005006, 'loc_16302'),
        (0x00005005, 'loc_16308'),
        (0x00005004, 'loc_1630E'),
        (0x00005003, 'loc_16314'),
        (0x00005002, 'loc_1631A'),
        (0x00005001, 'loc_16320'),
        (0x00005000, 'loc_16326'),
        (-1, 'loc_1632E'),
    )

    def _loc_162BA(): pass

    label('loc_162BA')

    SetScenaFlags(ScenaFlag(0x0981, 2, 0x4C0A))
    SetScenaFlags(ScenaFlag(0x0981, 3, 0x4C0B))

    def _loc_162C0(): pass

    label('loc_162C0')

    SetScenaFlags(ScenaFlag(0x0964, 2, 0x4B22))
    SetScenaFlags(ScenaFlag(0x0964, 1, 0x4B21))

    def _loc_162C6(): pass

    label('loc_162C6')

    SetScenaFlags(ScenaFlag(0x0964, 0, 0x4B20))
    SetScenaFlags(ScenaFlag(0x0963, 7, 0x4B1F))

    def _loc_162CC(): pass

    label('loc_162CC')

    SetScenaFlags(ScenaFlag(0x0963, 6, 0x4B1E))
    SetScenaFlags(ScenaFlag(0x0963, 5, 0x4B1D))

    def _loc_162D2(): pass

    label('loc_162D2')

    SetScenaFlags(ScenaFlag(0x0963, 4, 0x4B1C))
    SetScenaFlags(ScenaFlag(0x0963, 3, 0x4B1B))

    def _loc_162D8(): pass

    label('loc_162D8')

    SetScenaFlags(ScenaFlag(0x0963, 2, 0x4B1A))
    SetScenaFlags(ScenaFlag(0x0963, 1, 0x4B19))

    def _loc_162DE(): pass

    label('loc_162DE')

    SetScenaFlags(ScenaFlag(0x0963, 0, 0x4B18))
    SetScenaFlags(ScenaFlag(0x0962, 7, 0x4B17))

    def _loc_162E4(): pass

    label('loc_162E4')

    SetScenaFlags(ScenaFlag(0x0962, 6, 0x4B16))
    SetScenaFlags(ScenaFlag(0x0962, 5, 0x4B15))

    def _loc_162EA(): pass

    label('loc_162EA')

    SetScenaFlags(ScenaFlag(0x0962, 4, 0x4B14))
    SetScenaFlags(ScenaFlag(0x0962, 3, 0x4B13))

    def _loc_162F0(): pass

    label('loc_162F0')

    SetScenaFlags(ScenaFlag(0x0962, 2, 0x4B12))
    SetScenaFlags(ScenaFlag(0x0962, 1, 0x4B11))

    def _loc_162F6(): pass

    label('loc_162F6')

    SetScenaFlags(ScenaFlag(0x0962, 0, 0x4B10))
    SetScenaFlags(ScenaFlag(0x0961, 7, 0x4B0F))

    def _loc_162FC(): pass

    label('loc_162FC')

    SetScenaFlags(ScenaFlag(0x0961, 6, 0x4B0E))
    SetScenaFlags(ScenaFlag(0x0961, 5, 0x4B0D))

    def _loc_16302(): pass

    label('loc_16302')

    SetScenaFlags(ScenaFlag(0x0961, 4, 0x4B0C))
    SetScenaFlags(ScenaFlag(0x0961, 3, 0x4B0B))

    def _loc_16308(): pass

    label('loc_16308')

    SetScenaFlags(ScenaFlag(0x0961, 2, 0x4B0A))
    SetScenaFlags(ScenaFlag(0x0961, 1, 0x4B09))

    def _loc_1630E(): pass

    label('loc_1630E')

    SetScenaFlags(ScenaFlag(0x0961, 0, 0x4B08))
    SetScenaFlags(ScenaFlag(0x0960, 7, 0x4B07))

    def _loc_16314(): pass

    label('loc_16314')

    SetScenaFlags(ScenaFlag(0x0960, 6, 0x4B06))
    SetScenaFlags(ScenaFlag(0x0960, 5, 0x4B05))

    def _loc_1631A(): pass

    label('loc_1631A')

    SetScenaFlags(ScenaFlag(0x0960, 4, 0x4B04))
    SetScenaFlags(ScenaFlag(0x0960, 3, 0x4B03))

    def _loc_16320(): pass

    label('loc_16320')

    SetScenaFlags(ScenaFlag(0x0960, 2, 0x4B02))
    SetScenaFlags(ScenaFlag(0x0960, 1, 0x4B01))

    def _loc_16326(): pass

    label('loc_16326')

    SetScenaFlags(ScenaFlag(0x0960, 0, 0x4B00))

    Jump('loc_1632E')

    def _loc_1632E(): pass

    label('loc_1632E')

    Return()

# id: 0x001F offset: 0x16330
@scena.Code('EV_DoJumpSet_04')
def EV_DoJumpSet_04():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01X_All')
    Call(ScriptId.Current, 'EV_Flag_Set_02_All')
    Call(ScriptId.Current, 'EV_Flag_Set_03_All')
    Call(ScriptId.Current, 'EV_Flag_Set_03X_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))
    Call(ScriptId.System, 'SetKisinChange_ValimarS2A')

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00006082, 'loc_16741'),
        (0x00006081, 'loc_16747'),
        (0x00006080, 'loc_1674D'),
        (0x0000607F, 'loc_16753'),
        (0x0000607E, 'loc_16759'),
        (0x0000607D, 'loc_1675F'),
        (0x0000607C, 'loc_16765'),
        (0x0000607B, 'loc_1676B'),
        (0x0000607A, 'loc_16771'),
        (0x00006079, 'loc_16777'),
        (0x00006078, 'loc_1677D'),
        (0x00006077, 'loc_16783'),
        (0x00006076, 'loc_16789'),
        (0x00006075, 'loc_1678F'),
        (0x00006074, 'loc_16795'),
        (0x00006073, 'loc_1679B'),
        (0x00006072, 'loc_167A1'),
        (0x00006071, 'loc_167A7'),
        (0x00006070, 'loc_167AD'),
        (0x0000606F, 'loc_167B3'),
        (0x0000606E, 'loc_167B9'),
        (0x0000606D, 'loc_167BF'),
        (0x0000606C, 'loc_167C5'),
        (0x0000606B, 'loc_167CB'),
        (0x0000606A, 'loc_167ED'),
        (0x00006069, 'loc_167F3'),
        (0x00006068, 'loc_167F9'),
        (0x00006067, 'loc_167FF'),
        (0x00006066, 'loc_16805'),
        (0x00006065, 'loc_1680B'),
        (0x00006064, 'loc_16811'),
        (0x00006063, 'loc_16817'),
        (0x00006062, 'loc_1681D'),
        (0x00006061, 'loc_16823'),
        (0x00006060, 'loc_16829'),
        (0x0000605F, 'loc_1682F'),
        (0x0000605E, 'loc_16835'),
        (0x0000605D, 'loc_16862'),
        (0x0000605C, 'loc_16868'),
        (0x0000605B, 'loc_1686E'),
        (0x0000605A, 'loc_16874'),
        (0x00006059, 'loc_1687A'),
        (0x00006058, 'loc_16880'),
        (0x00006057, 'loc_16886'),
        (0x00006056, 'loc_1688C'),
        (0x00006055, 'loc_16892'),
        (0x00006054, 'loc_16898'),
        (0x00006053, 'loc_1689E'),
        (0x00006052, 'loc_168A4'),
        (0x00006051, 'loc_168AA'),
        (0x00006050, 'loc_168B0'),
        (0x0000603E, 'loc_168B6'),
        (0x0000603D, 'loc_168BC'),
        (0x0000603C, 'loc_168C2'),
        (0x0000603B, 'loc_168C8'),
        (0x0000603A, 'loc_168CE'),
        (0x00006039, 'loc_168D4'),
        (0x00006038, 'loc_168DA'),
        (0x00006037, 'loc_168E0'),
        (0x00006036, 'loc_168E6'),
        (0x00006035, 'loc_168EC'),
        (0x00006034, 'loc_168F2'),
        (0x00006033, 'loc_168F8'),
        (0x00006032, 'loc_168FE'),
        (0x00006031, 'loc_16904'),
        (0x00006030, 'loc_1690A'),
        (0x0000602F, 'loc_16910'),
        (0x0000602E, 'loc_16916'),
        (0x0000602D, 'loc_1691C'),
        (0x0000602C, 'loc_16922'),
        (0x0000602B, 'loc_16928'),
        (0x0000602A, 'loc_1692E'),
        (0x00006029, 'loc_16934'),
        (0x00006028, 'loc_16952'),
        (0x00006027, 'loc_16958'),
        (0x00006026, 'loc_1695E'),
        (0x00006025, 'loc_16964'),
        (0x00006024, 'loc_1696A'),
        (0x00006023, 'loc_16970'),
        (0x00006022, 'loc_16976'),
        (0x00006021, 'loc_1697C'),
        (0x00006020, 'loc_16982'),
        (0x0000601F, 'loc_16988'),
        (0x0000601E, 'loc_1698E'),
        (0x0000601D, 'loc_16994'),
        (0x0000601C, 'loc_1699A'),
        (0x0000601B, 'loc_169A0'),
        (0x0000601A, 'loc_169A6'),
        (0x00006019, 'loc_169AC'),
        (0x00006018, 'loc_169B2'),
        (0x00006017, 'loc_169B8'),
        (0x00006016, 'loc_169BE'),
        (0x00006015, 'loc_169C4'),
        (0x00006014, 'loc_169CA'),
        (0x00006013, 'loc_169D0'),
        (0x00006012, 'loc_169D6'),
        (0x00006011, 'loc_169DC'),
        (0x00006010, 'loc_169E2'),
        (0x00006006, 'loc_169EE'),
        (0x00006005, 'loc_169F4'),
        (0x00006004, 'loc_169FA'),
        (0x00006003, 'loc_16A00'),
        (0x00006002, 'loc_16A06'),
        (0x00006001, 'loc_16A0C'),
        (0x00006000, 'loc_16A12'),
        (-1, 'loc_16A1A'),
    )

    def _loc_16741(): pass

    label('loc_16741')

    SetScenaFlags(ScenaFlag(0x09FE, 4, 0x4FF4))
    SetScenaFlags(ScenaFlag(0x09FE, 3, 0x4FF3))

    def _loc_16747(): pass

    label('loc_16747')

    SetScenaFlags(ScenaFlag(0x09FE, 2, 0x4FF2))
    SetScenaFlags(ScenaFlag(0x09FE, 1, 0x4FF1))

    def _loc_1674D(): pass

    label('loc_1674D')

    SetScenaFlags(ScenaFlag(0x09FE, 0, 0x4FF0))
    SetScenaFlags(ScenaFlag(0x09FD, 7, 0x4FEF))

    def _loc_16753(): pass

    label('loc_16753')

    SetScenaFlags(ScenaFlag(0x09FD, 6, 0x4FEE))
    SetScenaFlags(ScenaFlag(0x09FD, 5, 0x4FED))

    def _loc_16759(): pass

    label('loc_16759')

    SetScenaFlags(ScenaFlag(0x09FD, 4, 0x4FEC))
    SetScenaFlags(ScenaFlag(0x09FD, 3, 0x4FEB))

    def _loc_1675F(): pass

    label('loc_1675F')

    SetScenaFlags(ScenaFlag(0x09FD, 2, 0x4FEA))
    SetScenaFlags(ScenaFlag(0x09FD, 1, 0x4FE9))

    def _loc_16765(): pass

    label('loc_16765')

    SetScenaFlags(ScenaFlag(0x09FD, 0, 0x4FE8))
    SetScenaFlags(ScenaFlag(0x09FC, 7, 0x4FE7))

    def _loc_1676B(): pass

    label('loc_1676B')

    SetScenaFlags(ScenaFlag(0x09FC, 6, 0x4FE6))
    SetScenaFlags(ScenaFlag(0x09FC, 5, 0x4FE5))

    def _loc_16771(): pass

    label('loc_16771')

    SetScenaFlags(ScenaFlag(0x09FC, 3, 0x4FE3))
    SetScenaFlags(ScenaFlag(0x09FC, 4, 0x4FE4))

    def _loc_16777(): pass

    label('loc_16777')

    SetScenaFlags(ScenaFlag(0x09FC, 1, 0x4FE1))
    SetScenaFlags(ScenaFlag(0x09FC, 2, 0x4FE2))

    def _loc_1677D(): pass

    label('loc_1677D')

    SetScenaFlags(ScenaFlag(0x09FC, 0, 0x4FE0))
    SetScenaFlags(ScenaFlag(0x09FB, 7, 0x4FDF))

    def _loc_16783(): pass

    label('loc_16783')

    SetScenaFlags(ScenaFlag(0x09FB, 6, 0x4FDE))
    SetScenaFlags(ScenaFlag(0x09FB, 5, 0x4FDD))

    def _loc_16789(): pass

    label('loc_16789')

    SetScenaFlags(ScenaFlag(0x09FB, 4, 0x4FDC))
    SetScenaFlags(ScenaFlag(0x09FB, 3, 0x4FDB))

    def _loc_1678F(): pass

    label('loc_1678F')

    SetScenaFlags(ScenaFlag(0x09FB, 2, 0x4FDA))
    SetScenaFlags(ScenaFlag(0x09FB, 1, 0x4FD9))

    def _loc_16795(): pass

    label('loc_16795')

    SetScenaFlags(ScenaFlag(0x09FB, 0, 0x4FD8))
    SetScenaFlags(ScenaFlag(0x09FA, 7, 0x4FD7))

    def _loc_1679B(): pass

    label('loc_1679B')

    SetScenaFlags(ScenaFlag(0x09FA, 6, 0x4FD6))
    SetScenaFlags(ScenaFlag(0x09FA, 5, 0x4FD5))

    def _loc_167A1(): pass

    label('loc_167A1')

    SetScenaFlags(ScenaFlag(0x09FA, 4, 0x4FD4))
    SetScenaFlags(ScenaFlag(0x09FA, 3, 0x4FD3))

    def _loc_167A7(): pass

    label('loc_167A7')

    SetScenaFlags(ScenaFlag(0x09FA, 2, 0x4FD2))
    SetScenaFlags(ScenaFlag(0x09FA, 1, 0x4FD1))

    def _loc_167AD(): pass

    label('loc_167AD')

    SetScenaFlags(ScenaFlag(0x09FA, 0, 0x4FD0))
    SetScenaFlags(ScenaFlag(0x09F9, 7, 0x4FCF))

    def _loc_167B3(): pass

    label('loc_167B3')

    SetScenaFlags(ScenaFlag(0x09F9, 6, 0x4FCE))
    SetScenaFlags(ScenaFlag(0x09F9, 5, 0x4FCD))

    def _loc_167B9(): pass

    label('loc_167B9')

    SetScenaFlags(ScenaFlag(0x09F9, 4, 0x4FCC))
    SetScenaFlags(ScenaFlag(0x09F9, 3, 0x4FCB))

    def _loc_167BF(): pass

    label('loc_167BF')

    SetScenaFlags(ScenaFlag(0x09F9, 2, 0x4FCA))
    SetScenaFlags(ScenaFlag(0x09F9, 1, 0x4FC9))

    def _loc_167C5(): pass

    label('loc_167C5')

    SetScenaFlags(ScenaFlag(0x09F9, 0, 0x4FC8))
    SetScenaFlags(ScenaFlag(0x09F8, 7, 0x4FC7))

    def _loc_167CB(): pass

    label('loc_167CB')

    SetScenaFlags(ScenaFlag(0x09F8, 6, 0x4FC6))
    SetScenaFlags(ScenaFlag(0x09F8, 5, 0x4FC5))
    Call(ScriptId.System, 'SetKisinChange_ValimarS3')

    def _loc_167ED(): pass

    label('loc_167ED')

    SetScenaFlags(ScenaFlag(0x09F8, 4, 0x4FC4))
    SetScenaFlags(ScenaFlag(0x09F8, 3, 0x4FC3))

    def _loc_167F3(): pass

    label('loc_167F3')

    SetScenaFlags(ScenaFlag(0x09F8, 2, 0x4FC2))
    SetScenaFlags(ScenaFlag(0x09F8, 1, 0x4FC1))

    def _loc_167F9(): pass

    label('loc_167F9')

    SetScenaFlags(ScenaFlag(0x09F8, 0, 0x4FC0))
    SetScenaFlags(ScenaFlag(0x09F7, 7, 0x4FBF))

    def _loc_167FF(): pass

    label('loc_167FF')

    SetScenaFlags(ScenaFlag(0x09F7, 6, 0x4FBE))
    SetScenaFlags(ScenaFlag(0x09F7, 5, 0x4FBD))

    def _loc_16805(): pass

    label('loc_16805')

    SetScenaFlags(ScenaFlag(0x09F7, 4, 0x4FBC))
    SetScenaFlags(ScenaFlag(0x09F7, 3, 0x4FBB))

    def _loc_1680B(): pass

    label('loc_1680B')

    SetScenaFlags(ScenaFlag(0x09F7, 2, 0x4FBA))
    SetScenaFlags(ScenaFlag(0x09F7, 1, 0x4FB9))

    def _loc_16811(): pass

    label('loc_16811')

    SetScenaFlags(ScenaFlag(0x09F7, 0, 0x4FB8))
    SetScenaFlags(ScenaFlag(0x09F6, 7, 0x4FB7))

    def _loc_16817(): pass

    label('loc_16817')

    SetScenaFlags(ScenaFlag(0x09F6, 6, 0x4FB6))
    SetScenaFlags(ScenaFlag(0x09F6, 5, 0x4FB5))

    def _loc_1681D(): pass

    label('loc_1681D')

    SetScenaFlags(ScenaFlag(0x09F6, 4, 0x4FB4))
    SetScenaFlags(ScenaFlag(0x09F6, 3, 0x4FB3))

    def _loc_16823(): pass

    label('loc_16823')

    SetScenaFlags(ScenaFlag(0x09F6, 2, 0x4FB2))
    SetScenaFlags(ScenaFlag(0x09F6, 1, 0x4FB1))

    def _loc_16829(): pass

    label('loc_16829')

    SetScenaFlags(ScenaFlag(0x09F6, 0, 0x4FB0))
    SetScenaFlags(ScenaFlag(0x09F5, 7, 0x4FAF))

    def _loc_1682F(): pass

    label('loc_1682F')

    SetScenaFlags(ScenaFlag(0x09F5, 6, 0x4FAE))
    SetScenaFlags(ScenaFlag(0x09F5, 5, 0x4FAD))

    def _loc_16835(): pass

    label('loc_16835')

    SetScenaFlags(ScenaFlag(0x09F5, 4, 0x4FAC))
    SetScenaFlags(ScenaFlag(0x09F5, 3, 0x4FAB))

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 5, 0x435)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_16862',
    )

    Call(ScriptId.System, 'SetKisinChange_ValimarS2B')

    def _loc_16862(): pass

    label('loc_16862')

    SetScenaFlags(ScenaFlag(0x09F5, 2, 0x4FAA))
    SetScenaFlags(ScenaFlag(0x09F5, 1, 0x4FA9))

    def _loc_16868(): pass

    label('loc_16868')

    SetScenaFlags(ScenaFlag(0x09F5, 0, 0x4FA8))
    SetScenaFlags(ScenaFlag(0x09F4, 7, 0x4FA7))

    def _loc_1686E(): pass

    label('loc_1686E')

    SetScenaFlags(ScenaFlag(0x09F4, 6, 0x4FA6))
    SetScenaFlags(ScenaFlag(0x09F4, 5, 0x4FA5))

    def _loc_16874(): pass

    label('loc_16874')

    SetScenaFlags(ScenaFlag(0x09F4, 4, 0x4FA4))
    SetScenaFlags(ScenaFlag(0x09F4, 3, 0x4FA3))

    def _loc_1687A(): pass

    label('loc_1687A')

    SetScenaFlags(ScenaFlag(0x09F4, 2, 0x4FA2))
    SetScenaFlags(ScenaFlag(0x09F4, 1, 0x4FA1))

    def _loc_16880(): pass

    label('loc_16880')

    SetScenaFlags(ScenaFlag(0x09F4, 0, 0x4FA0))
    SetScenaFlags(ScenaFlag(0x09F3, 7, 0x4F9F))

    def _loc_16886(): pass

    label('loc_16886')

    SetScenaFlags(ScenaFlag(0x09F3, 6, 0x4F9E))
    SetScenaFlags(ScenaFlag(0x09F3, 5, 0x4F9D))

    def _loc_1688C(): pass

    label('loc_1688C')

    SetScenaFlags(ScenaFlag(0x09F3, 4, 0x4F9C))
    SetScenaFlags(ScenaFlag(0x09F3, 3, 0x4F9B))

    def _loc_16892(): pass

    label('loc_16892')

    SetScenaFlags(ScenaFlag(0x09F3, 2, 0x4F9A))
    SetScenaFlags(ScenaFlag(0x09F3, 1, 0x4F99))

    def _loc_16898(): pass

    label('loc_16898')

    SetScenaFlags(ScenaFlag(0x09F3, 0, 0x4F98))
    SetScenaFlags(ScenaFlag(0x09F2, 7, 0x4F97))

    def _loc_1689E(): pass

    label('loc_1689E')

    SetScenaFlags(ScenaFlag(0x09F2, 6, 0x4F96))
    SetScenaFlags(ScenaFlag(0x09F2, 5, 0x4F95))

    def _loc_168A4(): pass

    label('loc_168A4')

    SetScenaFlags(ScenaFlag(0x09F2, 4, 0x4F94))
    SetScenaFlags(ScenaFlag(0x09F2, 3, 0x4F93))

    def _loc_168AA(): pass

    label('loc_168AA')

    SetScenaFlags(ScenaFlag(0x09F2, 2, 0x4F92))
    SetScenaFlags(ScenaFlag(0x09F2, 1, 0x4F91))

    def _loc_168B0(): pass

    label('loc_168B0')

    SetScenaFlags(ScenaFlag(0x09F2, 0, 0x4F90))
    SetScenaFlags(ScenaFlag(0x09EF, 5, 0x4F7D))

    def _loc_168B6(): pass

    label('loc_168B6')

    SetScenaFlags(ScenaFlag(0x09EF, 4, 0x4F7C))
    SetScenaFlags(ScenaFlag(0x09EF, 3, 0x4F7B))

    def _loc_168BC(): pass

    label('loc_168BC')

    SetScenaFlags(ScenaFlag(0x09EF, 2, 0x4F7A))
    SetScenaFlags(ScenaFlag(0x09EF, 1, 0x4F79))

    def _loc_168C2(): pass

    label('loc_168C2')

    SetScenaFlags(ScenaFlag(0x09EF, 0, 0x4F78))
    SetScenaFlags(ScenaFlag(0x09EE, 7, 0x4F77))

    def _loc_168C8(): pass

    label('loc_168C8')

    SetScenaFlags(ScenaFlag(0x09EE, 6, 0x4F76))
    SetScenaFlags(ScenaFlag(0x09EE, 5, 0x4F75))

    def _loc_168CE(): pass

    label('loc_168CE')

    SetScenaFlags(ScenaFlag(0x09EE, 4, 0x4F74))
    SetScenaFlags(ScenaFlag(0x09EE, 3, 0x4F73))

    def _loc_168D4(): pass

    label('loc_168D4')

    SetScenaFlags(ScenaFlag(0x09EE, 2, 0x4F72))
    SetScenaFlags(ScenaFlag(0x09EE, 1, 0x4F71))

    def _loc_168DA(): pass

    label('loc_168DA')

    SetScenaFlags(ScenaFlag(0x09EE, 0, 0x4F70))
    SetScenaFlags(ScenaFlag(0x09ED, 7, 0x4F6F))

    def _loc_168E0(): pass

    label('loc_168E0')

    SetScenaFlags(ScenaFlag(0x09ED, 6, 0x4F6E))
    SetScenaFlags(ScenaFlag(0x09ED, 5, 0x4F6D))

    def _loc_168E6(): pass

    label('loc_168E6')

    SetScenaFlags(ScenaFlag(0x09ED, 4, 0x4F6C))
    SetScenaFlags(ScenaFlag(0x09ED, 3, 0x4F6B))

    def _loc_168EC(): pass

    label('loc_168EC')

    SetScenaFlags(ScenaFlag(0x09ED, 2, 0x4F6A))
    SetScenaFlags(ScenaFlag(0x09ED, 1, 0x4F69))

    def _loc_168F2(): pass

    label('loc_168F2')

    SetScenaFlags(ScenaFlag(0x09ED, 0, 0x4F68))
    SetScenaFlags(ScenaFlag(0x09EC, 7, 0x4F67))

    def _loc_168F8(): pass

    label('loc_168F8')

    SetScenaFlags(ScenaFlag(0x09EC, 6, 0x4F66))
    SetScenaFlags(ScenaFlag(0x09EC, 5, 0x4F65))

    def _loc_168FE(): pass

    label('loc_168FE')

    SetScenaFlags(ScenaFlag(0x09EC, 4, 0x4F64))
    SetScenaFlags(ScenaFlag(0x09EC, 3, 0x4F63))

    def _loc_16904(): pass

    label('loc_16904')

    SetScenaFlags(ScenaFlag(0x09EC, 2, 0x4F62))
    SetScenaFlags(ScenaFlag(0x09EC, 1, 0x4F61))

    def _loc_1690A(): pass

    label('loc_1690A')

    SetScenaFlags(ScenaFlag(0x09EC, 0, 0x4F60))
    SetScenaFlags(ScenaFlag(0x09EB, 7, 0x4F5F))

    def _loc_16910(): pass

    label('loc_16910')

    SetScenaFlags(ScenaFlag(0x09EB, 6, 0x4F5E))
    SetScenaFlags(ScenaFlag(0x09EB, 5, 0x4F5D))

    def _loc_16916(): pass

    label('loc_16916')

    SetScenaFlags(ScenaFlag(0x09EB, 4, 0x4F5C))
    SetScenaFlags(ScenaFlag(0x09EB, 3, 0x4F5B))

    def _loc_1691C(): pass

    label('loc_1691C')

    SetScenaFlags(ScenaFlag(0x09EB, 2, 0x4F5A))
    SetScenaFlags(ScenaFlag(0x09EB, 1, 0x4F59))

    def _loc_16922(): pass

    label('loc_16922')

    SetScenaFlags(ScenaFlag(0x09EB, 0, 0x4F58))
    SetScenaFlags(ScenaFlag(0x09EA, 7, 0x4F57))

    def _loc_16928(): pass

    label('loc_16928')

    SetScenaFlags(ScenaFlag(0x09EA, 6, 0x4F56))
    SetScenaFlags(ScenaFlag(0x09EA, 5, 0x4F55))

    def _loc_1692E(): pass

    label('loc_1692E')

    SetScenaFlags(ScenaFlag(0x09EA, 4, 0x4F54))
    SetScenaFlags(ScenaFlag(0x09EA, 3, 0x4F53))

    def _loc_16934(): pass

    label('loc_16934')

    SetScenaFlags(ScenaFlag(0x09EA, 2, 0x4F52))
    SetScenaFlags(ScenaFlag(0x09EA, 1, 0x4F51))
    QuestCtrl(0x002A, 0x05)
    QuestCtrl(0x002B, 0x05)
    QuestCtrl(0x002C, 0x05)
    QuestCtrl(0x002D, 0x05)
    QuestCtrl(0x002E, 0x05)
    QuestCtrl(0x002F, 0x05)

    def _loc_16952(): pass

    label('loc_16952')

    SetScenaFlags(ScenaFlag(0x09EA, 0, 0x4F50))
    SetScenaFlags(ScenaFlag(0x09E9, 7, 0x4F4F))

    def _loc_16958(): pass

    label('loc_16958')

    SetScenaFlags(ScenaFlag(0x09E9, 6, 0x4F4E))
    SetScenaFlags(ScenaFlag(0x09E9, 5, 0x4F4D))

    def _loc_1695E(): pass

    label('loc_1695E')

    SetScenaFlags(ScenaFlag(0x09E9, 4, 0x4F4C))
    SetScenaFlags(ScenaFlag(0x09E9, 3, 0x4F4B))

    def _loc_16964(): pass

    label('loc_16964')

    SetScenaFlags(ScenaFlag(0x09E9, 2, 0x4F4A))
    SetScenaFlags(ScenaFlag(0x09E9, 1, 0x4F49))

    def _loc_1696A(): pass

    label('loc_1696A')

    SetScenaFlags(ScenaFlag(0x09E9, 0, 0x4F48))
    SetScenaFlags(ScenaFlag(0x09E8, 7, 0x4F47))

    def _loc_16970(): pass

    label('loc_16970')

    SetScenaFlags(ScenaFlag(0x09E8, 6, 0x4F46))
    SetScenaFlags(ScenaFlag(0x09E8, 5, 0x4F45))

    def _loc_16976(): pass

    label('loc_16976')

    SetScenaFlags(ScenaFlag(0x09E8, 4, 0x4F44))
    SetScenaFlags(ScenaFlag(0x09E8, 3, 0x4F43))

    def _loc_1697C(): pass

    label('loc_1697C')

    SetScenaFlags(ScenaFlag(0x09E8, 2, 0x4F42))
    SetScenaFlags(ScenaFlag(0x09E8, 1, 0x4F41))

    def _loc_16982(): pass

    label('loc_16982')

    SetScenaFlags(ScenaFlag(0x09E8, 0, 0x4F40))
    SetScenaFlags(ScenaFlag(0x09E7, 7, 0x4F3F))

    def _loc_16988(): pass

    label('loc_16988')

    SetScenaFlags(ScenaFlag(0x09E7, 6, 0x4F3E))
    SetScenaFlags(ScenaFlag(0x09E7, 5, 0x4F3D))

    def _loc_1698E(): pass

    label('loc_1698E')

    SetScenaFlags(ScenaFlag(0x09E7, 4, 0x4F3C))
    SetScenaFlags(ScenaFlag(0x09E7, 3, 0x4F3B))

    def _loc_16994(): pass

    label('loc_16994')

    SetScenaFlags(ScenaFlag(0x09E7, 2, 0x4F3A))
    SetScenaFlags(ScenaFlag(0x09E7, 1, 0x4F39))

    def _loc_1699A(): pass

    label('loc_1699A')

    SetScenaFlags(ScenaFlag(0x09E7, 0, 0x4F38))
    SetScenaFlags(ScenaFlag(0x09E6, 7, 0x4F37))

    def _loc_169A0(): pass

    label('loc_169A0')

    SetScenaFlags(ScenaFlag(0x09E6, 6, 0x4F36))
    SetScenaFlags(ScenaFlag(0x09E6, 5, 0x4F35))

    def _loc_169A6(): pass

    label('loc_169A6')

    SetScenaFlags(ScenaFlag(0x09E6, 4, 0x4F34))
    SetScenaFlags(ScenaFlag(0x09E6, 3, 0x4F33))

    def _loc_169AC(): pass

    label('loc_169AC')

    SetScenaFlags(ScenaFlag(0x09E6, 2, 0x4F32))
    SetScenaFlags(ScenaFlag(0x09E6, 1, 0x4F31))

    def _loc_169B2(): pass

    label('loc_169B2')

    SetScenaFlags(ScenaFlag(0x09E6, 0, 0x4F30))
    SetScenaFlags(ScenaFlag(0x09E5, 7, 0x4F2F))

    def _loc_169B8(): pass

    label('loc_169B8')

    SetScenaFlags(ScenaFlag(0x09E5, 6, 0x4F2E))
    SetScenaFlags(ScenaFlag(0x09E5, 5, 0x4F2D))

    def _loc_169BE(): pass

    label('loc_169BE')

    SetScenaFlags(ScenaFlag(0x09E5, 4, 0x4F2C))
    SetScenaFlags(ScenaFlag(0x09E5, 3, 0x4F2B))

    def _loc_169C4(): pass

    label('loc_169C4')

    SetScenaFlags(ScenaFlag(0x09E5, 2, 0x4F2A))
    SetScenaFlags(ScenaFlag(0x09E5, 1, 0x4F29))

    def _loc_169CA(): pass

    label('loc_169CA')

    SetScenaFlags(ScenaFlag(0x09E5, 0, 0x4F28))
    SetScenaFlags(ScenaFlag(0x09E4, 7, 0x4F27))

    def _loc_169D0(): pass

    label('loc_169D0')

    SetScenaFlags(ScenaFlag(0x09E4, 6, 0x4F26))
    SetScenaFlags(ScenaFlag(0x09E4, 5, 0x4F25))

    def _loc_169D6(): pass

    label('loc_169D6')

    SetScenaFlags(ScenaFlag(0x09E4, 4, 0x4F24))
    SetScenaFlags(ScenaFlag(0x09E4, 3, 0x4F23))

    def _loc_169DC(): pass

    label('loc_169DC')

    SetScenaFlags(ScenaFlag(0x09E4, 2, 0x4F22))
    SetScenaFlags(ScenaFlag(0x09E4, 1, 0x4F21))

    def _loc_169E2(): pass

    label('loc_169E2')

    SetScenaFlags(ScenaFlag(0x09E4, 0, 0x4F20))
    OP_71(0x00, 0x518F, 0x5190)
    SetScenaFlags(ScenaFlag(0x09E1, 5, 0x4F0D))

    def _loc_169EE(): pass

    label('loc_169EE')

    SetScenaFlags(ScenaFlag(0x09E1, 4, 0x4F0C))
    SetScenaFlags(ScenaFlag(0x09E1, 3, 0x4F0B))

    def _loc_169F4(): pass

    label('loc_169F4')

    SetScenaFlags(ScenaFlag(0x09E1, 2, 0x4F0A))
    SetScenaFlags(ScenaFlag(0x09E1, 1, 0x4F09))

    def _loc_169FA(): pass

    label('loc_169FA')

    SetScenaFlags(ScenaFlag(0x09E1, 0, 0x4F08))
    SetScenaFlags(ScenaFlag(0x09E0, 7, 0x4F07))

    def _loc_16A00(): pass

    label('loc_16A00')

    SetScenaFlags(ScenaFlag(0x09E0, 6, 0x4F06))
    SetScenaFlags(ScenaFlag(0x09E0, 5, 0x4F05))

    def _loc_16A06(): pass

    label('loc_16A06')

    SetScenaFlags(ScenaFlag(0x09E0, 4, 0x4F04))
    SetScenaFlags(ScenaFlag(0x09E0, 3, 0x4F03))

    def _loc_16A0C(): pass

    label('loc_16A0C')

    SetScenaFlags(ScenaFlag(0x09E0, 2, 0x4F02))
    SetScenaFlags(ScenaFlag(0x09E0, 1, 0x4F01))

    def _loc_16A12(): pass

    label('loc_16A12')

    SetScenaFlags(ScenaFlag(0x09E0, 0, 0x4F00))

    Jump('loc_16A1A')

    def _loc_16A1A(): pass

    label('loc_16A1A')

    Return()

# id: 0x0020 offset: 0x16A1C
@scena.Code('EV_DoJumpSet_05')
def EV_DoJumpSet_05():
    Call(ScriptId.Current, 'EV_Flag_Reset')
    Call(ScriptId.Current, 'EV_Flag_Set_00_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01_All')
    Call(ScriptId.Current, 'EV_Flag_Set_01X_All')
    Call(ScriptId.Current, 'EV_Flag_Set_02_All')
    Call(ScriptId.Current, 'EV_Flag_Set_03_All')
    Call(ScriptId.Current, 'EV_Flag_Set_03X_All')
    Call(ScriptId.Current, 'EV_Flag_Set_04_All')

    ExecExpressionWithVar(
        0x03,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0060, 0, 0x300))

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00006A13, 'loc_16B3E'),
        (0x00006A12, 'loc_16B44'),
        (0x00006A10, 'loc_16B4A'),
        (0x00006A10, 'loc_16B50'),
        (0x00006A0A, 'loc_16B56'),
        (0x00006A09, 'loc_16B5C'),
        (0x00006A08, 'loc_16B62'),
        (0x00006A04, 'loc_16B68'),
        (0x00006A03, 'loc_16B6E'),
        (0x00006A02, 'loc_16B74'),
        (0x00006A01, 'loc_16B7A'),
        (0x00006A00, 'loc_16B80'),
        (-1, 'loc_16B88'),
    )

    def _loc_16B3E(): pass

    label('loc_16B3E')

    SetScenaFlags(ScenaFlag(0x0B24, 6, 0x5926))
    SetScenaFlags(ScenaFlag(0x0B24, 5, 0x5925))

    def _loc_16B44(): pass

    label('loc_16B44')

    SetScenaFlags(ScenaFlag(0x0B24, 4, 0x5924))
    SetScenaFlags(ScenaFlag(0x0B24, 3, 0x5923))

    def _loc_16B4A(): pass

    label('loc_16B4A')

    SetScenaFlags(ScenaFlag(0x0B24, 2, 0x5922))
    SetScenaFlags(ScenaFlag(0x0B24, 1, 0x5921))

    def _loc_16B50(): pass

    label('loc_16B50')

    SetScenaFlags(ScenaFlag(0x0B24, 0, 0x5920))
    SetScenaFlags(ScenaFlag(0x0B22, 5, 0x5915))

    def _loc_16B56(): pass

    label('loc_16B56')

    SetScenaFlags(ScenaFlag(0x0B22, 4, 0x5914))
    SetScenaFlags(ScenaFlag(0x0B22, 3, 0x5913))

    def _loc_16B5C(): pass

    label('loc_16B5C')

    SetScenaFlags(ScenaFlag(0x0B22, 2, 0x5912))
    SetScenaFlags(ScenaFlag(0x0B22, 1, 0x5911))

    def _loc_16B62(): pass

    label('loc_16B62')

    SetScenaFlags(ScenaFlag(0x0B22, 0, 0x5910))
    SetScenaFlags(ScenaFlag(0x0B21, 1, 0x5909))

    def _loc_16B68(): pass

    label('loc_16B68')

    SetScenaFlags(ScenaFlag(0x0B21, 0, 0x5908))
    SetScenaFlags(ScenaFlag(0x0B20, 7, 0x5907))

    def _loc_16B6E(): pass

    label('loc_16B6E')

    SetScenaFlags(ScenaFlag(0x0B20, 6, 0x5906))
    SetScenaFlags(ScenaFlag(0x0B20, 5, 0x5905))

    def _loc_16B74(): pass

    label('loc_16B74')

    SetScenaFlags(ScenaFlag(0x0B20, 4, 0x5904))
    SetScenaFlags(ScenaFlag(0x0B20, 3, 0x5903))

    def _loc_16B7A(): pass

    label('loc_16B7A')

    SetScenaFlags(ScenaFlag(0x0B20, 2, 0x5902))
    SetScenaFlags(ScenaFlag(0x0B20, 1, 0x5901))

    def _loc_16B80(): pass

    label('loc_16B80')

    SetScenaFlags(ScenaFlag(0x0B20, 0, 0x5900))

    Jump('loc_16B88')

    def _loc_16B88(): pass

    label('loc_16B88')

    Return()

# id: 0x0021 offset: 0x16B8C
@scena.Code('EV_Party_Set')
def EV_Party_Set():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    OP_43(0x00, 300, 1.0, 0)
    OP_43(0xFF, 0, 0x0000)

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16BB7',
    )

    OP_13(0x00001000)

    def _loc_16BB7(): pass

    label('loc_16BB7')

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    Call(ScriptId.System, 'FC_TSMenu_Reset')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Switch(
        (
            (Expr.PushVar, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_16C4B'),
        (0x00000001, 'loc_16D13'),
        (0x00000002, 'loc_174B5'),
        (0x00000003, 'loc_17D7F'),
        (0x00000004, 'loc_196CB'),
        (0x00000005, 'loc_1A484'),
        (0x00000006, 'loc_1A49E'),
        (0x00000007, 'loc_1A7A5'),
        (-1, 'loc_1A7F7'),
    )

    def _loc_16C4B(): pass

    label('loc_16C4B')

    MenuChrFlagCmd(0x01, ChrTable['黎恩'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x052B, 3, 0x295B)),
            Expr.Return,
        ),
        'loc_16C91',
    )

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])

    Jump('loc_16D0E')

    def _loc_16C91(): pass

    label('loc_16C91')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0529, 4, 0x294C)),
            Expr.Return,
        ),
        'loc_16CBA',
    )

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])

    Jump('loc_16D0E')

    def _loc_16CBA(): pass

    label('loc_16CBA')

    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000001)
    FormationReset(0x00)
    FormationAddMember(ChrTable['羅伊德'])
    FormationAddMember(ChrTable['艾莉'])
    FormationAddMember(ChrTable['艾絲蒂爾'])
    FormationAddMember(ChrTable['約修亞'])
    FormationAddMember(ChrTable['玲'])
    MenuChrFlagCmd(0x00, ChrTable['琪雅'], 0x01000000)
    FormationAddMember(ChrTable['琪雅'])

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_16D0E(): pass

    label('loc_16D0E')

    Jump('loc_1A7F7')

    def _loc_16D13(): pass

    label('loc_16D13')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x057F, 7, 0x2BFF)),
            Expr.Return,
        ),
        'loc_170D4',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    ClearScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    ClearScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    ClearScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    ClearScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])

    ExecExpressionWithVar(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 65535, 80, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '同行する旧Ⅶ組メンバーの組み合わせを選んでください',
            TxtCtl.ShowAll,
            0x8,
            TxtCtl.Enter,
        ),
    )

    OP_75(0x00, 0x02, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x02, 'アリサ/エマ', 0x00000001)
    OP_75(0x01, 0x02, 'アリサ/ラウラ', 0x00000002)
    OP_75(0x01, 0x02, 'アリサ/マキアス', 0x00000003)
    OP_75(0x01, 0x02, 'アリサ/ガイウス', 0x00000004)
    OP_75(0x01, 0x02, 'ユーシス/エマ', 0x00000005)
    OP_75(0x01, 0x02, 'ユーシス/ラウラ', 0x00000006)
    OP_75(0x01, 0x02, 'ユーシス/マキアス', 0x00000007)
    OP_75(0x01, 0x02, 'ユーシス/ガイウス', 0x00000008)
    OP_75(0x02, 0x02, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x02, 0xF9)
    OP_75(0x03, 0x02)
    OP_25(0x00)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F21',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_17073')

    def _loc_16F21(): pass

    label('loc_16F21')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F52',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_17073')

    def _loc_16F52(): pass

    label('loc_16F52')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16F83',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_17073')

    def _loc_16F83(): pass

    label('loc_16F83')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16FB4',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['蓋烏斯'])

    Jump('loc_17073')

    def _loc_16FB4(): pass

    label('loc_16FB4')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16FE5',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_17073')

    def _loc_16FE5(): pass

    label('loc_16FE5')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17016',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_17073')

    def _loc_17016(): pass

    label('loc_17016')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17047',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_17073')

    def _loc_17047(): pass

    label('loc_17047')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17073',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['蓋烏斯'])

    def _loc_17073(): pass

    label('loc_17073')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0580, 3, 0x2C03)),
            (Expr.TestScenaFlags, ScenaFlag(0x0580, 7, 0x2C07)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17097',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationSetLeader(ChrTable['尤娜'])
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)

    def _loc_17097(): pass

    label('loc_17097')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0587, 1, 0x2C39)),
            (Expr.TestScenaFlags, ScenaFlag(0x0588, 5, 0x2C45)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_170CF',
    )

    MenuChrFlagCmd(0x00, ChrTable['約納'], 0x01000000)
    MenuChrFlagCmd(0x00, ChrTable['修利'], 0x01000000)
    FormationAddMember(ChrTable['約納'])
    FormationAddMember(ChrTable['修利'])

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_170CF(): pass

    label('loc_170CF')

    Jump('loc_174B0')

    def _loc_170D4(): pass

    label('loc_170D4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x057F, 3, 0x2BFB)),
            Expr.Return,
        ),
        'loc_17176',
    )

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationSetLeader(ChrTable['尤娜'])
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)

    Jump('loc_174B0')

    def _loc_17176(): pass

    label('loc_17176')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x057E, 3, 0x2BF3)),
            Expr.Return,
        ),
        'loc_1722A',
    )

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationSetLeader(ChrTable['尤娜'])
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)

    Jump('loc_174B0')

    def _loc_1722A(): pass

    label('loc_1722A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x057A, 5, 0x2BD5)),
            Expr.Return,
        ),
        'loc_172BC',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x000F)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_174B0')

    def _loc_172BC(): pass

    label('loc_172BC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0573, 7, 0x2B9F)),
            Expr.Return,
        ),
        'loc_17341',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x000F)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_174B0')

    def _loc_17341(): pass

    label('loc_17341')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0573, 3, 0x2B9B)),
            Expr.Return,
        ),
        'loc_173AF',
    )

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['莎拉'])

    Jump('loc_174B0')

    def _loc_173AF(): pass

    label('loc_173AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0561, 1, 0x2B09)),
            Expr.Return,
        ),
        'loc_17480',
    )

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['蘭迪'])

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x056D, 7, 0x2B6F)),
            Expr.Return,
        ),
        'loc_17414',
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['蘭迪'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞爾緹娜'])

    def _loc_17414(): pass

    label('loc_17414')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0572, 3, 0x2B93)),
            Expr.Return,
        ),
        'loc_1747B',
    )

    FormationCtrl(0x01, ChrTable['蘭迪'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['莎拉'])
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['庫爾特'])
    FormationSetLeader(ChrTable['庫爾特'])
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)

    def _loc_1747B(): pass

    label('loc_1747B')

    Jump('loc_174B0')

    def _loc_17480(): pass

    label('loc_17480')

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])

    def _loc_174B0(): pass

    label('loc_174B0')

    Jump('loc_1A7F7')

    def _loc_174B5(): pass

    label('loc_174B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06AE, 7, 0x3577)),
            Expr.Return,
        ),
        'loc_17517',
    )

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞修'])

    Jump('loc_17D7A')

    def _loc_17517(): pass

    label('loc_17517')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06AC, 3, 0x3563)),
            Expr.Return,
        ),
        'loc_1756D',
    )

    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞修'])

    Jump('loc_17D7A')

    def _loc_1756D(): pass

    label('loc_1756D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06AB, 1, 0x3559)),
            Expr.Return,
        ),
        'loc_17657',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    OP_C4(0x02, 0x02, 0x0000)
    OP_C4(0x02, 0x02, 0x0028)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x04, 0x00, (0xDD, 'm6010'), -400.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x01, (0xDD, 'm6030'), -0.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x02, (0xDD, 'm6050'), 400.0, -0.0, -70.0, 180.0)
    FormationReset(0x00)
    OP_C4(0x01, 0x02)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17D7A')

    def _loc_17657(): pass

    label('loc_17657')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06A9, 6, 0x354E)),
            Expr.Return,
        ),
        'loc_17741',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    OP_C4(0x02, 0x02, 0x0000)
    OP_C4(0x02, 0x02, 0x0028)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x04, 0x00, (0xDD, 'm6010'), -400.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x01, (0xDD, 'm6030'), -0.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x02, (0xDD, 'm6050'), 400.0, -0.0, -70.0, 180.0)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17D7A')

    def _loc_17741(): pass

    label('loc_17741')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06A8, 5, 0x3545)),
            Expr.Return,
        ),
        'loc_17825',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    OP_C4(0x02, 0x02, 0x0000)
    OP_C4(0x02, 0x02, 0x0028)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x04, 0x00, (0xDD, 'm6010'), -400.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x01, (0xDD, 'm6030'), -0.0, -0.0, -70.0, 180.0)
    OP_C4(0x04, 0x02, (0xDD, 'm6050'), 400.0, -0.0, -70.0, 180.0)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17D7A')

    def _loc_17825(): pass

    label('loc_17825')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06A6, 1, 0x3531)),
            Expr.Return,
        ),
        'loc_178FF',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x000F)
    OP_C4(0x02, 0x02, 0x0000)
    OP_C4(0x02, 0x02, 0x0028)
    OP_C4(0x04, 0x00, (0xDD, 'm6000'), -400.0, -1.0, 292.5, 180.0)
    OP_C4(0x04, 0x01, (0xDD, 'm6020'), 20.0, -1.0, 264.5, 180.0)
    OP_C4(0x04, 0x02, (0xDD, 'm6040'), 435.25, -2.0, 280.25, 180.0)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_17D7A')

    def _loc_178FF(): pass

    label('loc_178FF')

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    ClearScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    ClearScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    ClearScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    ClearScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])

    ExecExpressionWithVar(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 65535, 80, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '同行する旧Ⅶ組メンバーの組み合わせを選んでください',
            TxtCtl.ShowAll,
            0x8,
            TxtCtl.Enter,
        ),
    )

    OP_75(0x00, 0x02, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x02, 'アリサ/エマ', 0x00000001)
    OP_75(0x01, 0x02, 'アリサ/ラウラ', 0x00000002)
    OP_75(0x01, 0x02, 'アリサ/マキアス', 0x00000003)
    OP_75(0x01, 0x02, 'アリサ/ガイウス', 0x00000004)
    OP_75(0x01, 0x02, 'ユーシス/エマ', 0x00000005)
    OP_75(0x01, 0x02, 'ユーシス/ラウラ', 0x00000006)
    OP_75(0x01, 0x02, 'ユーシス/マキアス', 0x00000007)
    OP_75(0x01, 0x02, 'ユーシス/ガイウス', 0x00000008)
    OP_75(0x02, 0x02, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x02, 0xF9)
    OP_75(0x03, 0x02)
    OP_25(0x00)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17B04',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_17C56')

    def _loc_17B04(): pass

    label('loc_17B04')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17B35',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_17C56')

    def _loc_17B35(): pass

    label('loc_17B35')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17B66',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_17C56')

    def _loc_17B66(): pass

    label('loc_17B66')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17B97',
    )

    SetScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['蓋烏斯'])

    Jump('loc_17C56')

    def _loc_17B97(): pass

    label('loc_17B97')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17BC8',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 1, 0x2D01))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['艾瑪'])

    Jump('loc_17C56')

    def _loc_17BC8(): pass

    label('loc_17BC8')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17BF9',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 2, 0x2D02))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['勞拉'])

    Jump('loc_17C56')

    def _loc_17BF9(): pass

    label('loc_17BF9')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17C2A',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 3, 0x2D03))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['馬奇亞斯'])

    Jump('loc_17C56')

    def _loc_17C2A(): pass

    label('loc_17C2A')

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17C56',
    )

    ClearScenaFlags(ScenaFlag(0x05A0, 0, 0x2D00))
    SetScenaFlags(ScenaFlag(0x05A0, 4, 0x2D04))
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['蓋烏斯'])

    def _loc_17C56(): pass

    label('loc_17C56')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06A1, 7, 0x350F)),
            Expr.Return,
        ),
        'loc_17D7A',
    )

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞莉莎'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C6F',
    )

    FormationAddMember(ChrTable['亞莉莎'])

    def _loc_17C6F(): pass

    label('loc_17C6F')

    FormationAddMember(ChrTable['艾略特'])

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['勞拉'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C83',
    )

    FormationAddMember(ChrTable['勞拉'])

    def _loc_17C83(): pass

    label('loc_17C83')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['馬奇亞斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17C93',
    )

    FormationAddMember(ChrTable['馬奇亞斯'])

    def _loc_17C93(): pass

    label('loc_17C93')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾瑪'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17CA3',
    )

    FormationAddMember(ChrTable['艾瑪'])

    def _loc_17CA3(): pass

    label('loc_17CA3')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤西斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17CB3',
    )

    FormationAddMember(ChrTable['尤西斯'])

    def _loc_17CB3(): pass

    label('loc_17CB3')

    FormationAddMember(ChrTable['菲'])

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['蓋烏斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17CC7',
    )

    FormationAddMember(ChrTable['蓋烏斯'])

    def _loc_17CC7(): pass

    label('loc_17CC7')

    FormationAddMember(ChrTable['莎拉'])
    FormationAddMember(ChrTable['玲'])
    MenuChrFlagCmd(0x00, ChrTable['琪雅'], 0x01000000)
    FormationAddMember(ChrTable['琪雅'])

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationSetLeader(ChrTable['亞爾緹娜'])
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['琪雅'], 0x02000000)

    def _loc_17D7A(): pass

    label('loc_17D7A')

    Jump('loc_1A7F7')

    def _loc_17D7F(): pass

    label('loc_17D7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0715, 5, 0x38AD)),
            Expr.Return,
        ),
        'loc_18754',
    )

    ExecExpressionWithVar(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x02, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x02, 'ランダム編成※注・チーム分けはデフォルトです', 0x00000001)
    OP_75(0x01, 0x02, '自分で編成＆チーム分け', 0x00000002)
    OP_75(0x02, 0x02, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x02, 0xF9)
    OP_75(0x03, 0x02)
    OP_25(0x00)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_18185',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x05, 0x0002)
    OP_C4(0x02, 0x05, 0x0004)
    OP_C4(0x02, 0x05, 0x0006)
    OP_C4(0x02, 0x05, 0x0011)
    OP_C4(0x02, 0x05, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C4(0x02, 0x01, 0x001A)
    OP_C4(0x02, 0x01, 0x001C)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x0023)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x05, 0x0001)
    OP_C4(0x02, 0x05, 0x0005)
    OP_C4(0x02, 0x05, 0x0007)
    OP_C4(0x02, 0x05, 0x0003)
    OP_C4(0x02, 0x05, 0x000F)
    OP_C4(0x02, 0x05, 0x0014)
    OP_C4(0x02, 0x05, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    FormationCtrl(0x0D, ChrTable['艾略特'], ChrTable['馬奇亞斯'], ChrTable['尤西斯'], ChrTable['阿加特'], ChrTable['蘭迪'], 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    FormationCtrl(0x0D, ChrTable['艾略特'], ChrTable['馬奇亞斯'], ChrTable['尤西斯'], ChrTable['阿加特'], ChrTable['蘭迪'], 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    OP_C4(0x01, 0x01)
    FormationCtrl(0x0D, ChrTable['亞莉莎'], ChrTable['艾瑪'], ChrTable['菲'], ChrTable['勞拉'], ChrTable['莎拉'], ChrTable['提妲'], ChrTable['安潔莉卡'], 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x01, 0x001B)
    OP_C4(0x02, 0x01, 0x000E)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾略特'])"),
            Expr.Return,
        ),
        'loc_1804A',
    )

    OP_C4(0x02, 0x01, 0x0002)

    def _loc_1804A(): pass

    label('loc_1804A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['馬奇亞斯'])"),
            Expr.Return,
        ),
        'loc_1805A',
    )

    OP_C4(0x02, 0x01, 0x0004)

    def _loc_1805A(): pass

    label('loc_1805A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤西斯'])"),
            Expr.Return,
        ),
        'loc_1806A',
    )

    OP_C4(0x02, 0x01, 0x0006)

    def _loc_1806A(): pass

    label('loc_1806A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['阿加特'])"),
            Expr.Return,
        ),
        'loc_1807A',
    )

    OP_C4(0x02, 0x01, 0x0011)

    def _loc_1807A(): pass

    label('loc_1807A')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['蘭迪'])"),
            Expr.Return,
        ),
        'loc_1808A',
    )

    OP_C4(0x02, 0x01, 0x001F)

    def _loc_1808A(): pass

    label('loc_1808A')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C4(0x02, 0x02, 0x001A)
    OP_C4(0x02, 0x02, 0x000A)
    OP_C4(0x02, 0x02, 0x001E)
    OP_C4(0x02, 0x02, 0x0015)
    OP_C4(0x02, 0x03, 0x0023)
    OP_C4(0x02, 0x03, 0x000C)
    OP_C4(0x02, 0x03, 0x001C)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞莉莎'])"),
            Expr.Return,
        ),
        'loc_180CF',
    )

    OP_C4(0x02, 0x03, 0x0001)

    def _loc_180CF(): pass

    label('loc_180CF')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾瑪'])"),
            Expr.Return,
        ),
        'loc_180DF',
    )

    OP_C4(0x02, 0x03, 0x0005)

    def _loc_180DF(): pass

    label('loc_180DF')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['菲'])"),
            Expr.Return,
        ),
        'loc_180EF',
    )

    OP_C4(0x02, 0x03, 0x0007)

    def _loc_180EF(): pass

    label('loc_180EF')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['勞拉'])"),
            Expr.Return,
        ),
        'loc_180FF',
    )

    OP_C4(0x02, 0x03, 0x0003)

    def _loc_180FF(): pass

    label('loc_180FF')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['莎拉'])"),
            Expr.Return,
        ),
        'loc_1810F',
    )

    OP_C4(0x02, 0x03, 0x000F)

    def _loc_1810F(): pass

    label('loc_1810F')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['提妲'])"),
            Expr.Return,
        ),
        'loc_1811F',
    )

    OP_C4(0x02, 0x03, 0x0014)

    def _loc_1811F(): pass

    label('loc_1811F')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['安潔莉卡'])"),
            Expr.Return,
        ),
        'loc_1812F',
    )

    OP_C4(0x02, 0x03, 0x0012)

    def _loc_1812F(): pass

    label('loc_1812F')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0716, 5, 0x38B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18171',
    )

    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_18180')

    def _loc_18171(): pass

    label('loc_18171')

    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_C4(0x01, 0x01)
    OP_C4(0x01, 0x02)
    OP_C4(0x01, 0x03)

    def _loc_18180(): pass

    label('loc_18180')

    Jump('loc_1874F')

    def _loc_18185(): pass

    label('loc_18185')

    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＡチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x05, 0x0002)
    OP_C4(0x02, 0x05, 0x0004)
    OP_C4(0x02, 0x05, 0x0006)
    OP_C4(0x02, 0x05, 0x0011)
    OP_C4(0x02, 0x05, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＢチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    OP_C4(0x02, 0x01, 0x001A)
    OP_C4(0x02, 0x01, 0x001C)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x0023)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x05, 0x0001)
    OP_C4(0x02, 0x05, 0x0005)
    OP_C4(0x02, 0x05, 0x0007)
    OP_C4(0x02, 0x05, 0x0003)
    OP_C4(0x02, 0x05, 0x000F)
    OP_C4(0x02, 0x05, 0x0014)
    OP_C4(0x02, 0x05, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_C4(0x01, 0x01)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            'Ａチーム、Ｂチームを\n',
            '４つのグループに分けてください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3C男性メンバーを２組に分けてください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x01, 0x001B)
    OP_C4(0x02, 0x01, 0x000E)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾略特'])"),
            Expr.Return,
        ),
        'loc_18562',
    )

    OP_C4(0x02, 0x01, 0x0002)

    def _loc_18562(): pass

    label('loc_18562')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['馬奇亞斯'])"),
            Expr.Return,
        ),
        'loc_18572',
    )

    OP_C4(0x02, 0x01, 0x0004)

    def _loc_18572(): pass

    label('loc_18572')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤西斯'])"),
            Expr.Return,
        ),
        'loc_18582',
    )

    OP_C4(0x02, 0x01, 0x0006)

    def _loc_18582(): pass

    label('loc_18582')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['阿加特'])"),
            Expr.Return,
        ),
        'loc_18592',
    )

    OP_C4(0x02, 0x01, 0x0011)

    def _loc_18592(): pass

    label('loc_18592')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['蘭迪'])"),
            Expr.Return,
        ),
        'loc_185A2',
    )

    OP_C4(0x02, 0x01, 0x001F)

    def _loc_185A2(): pass

    label('loc_185A2')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3C女性メンバーを２組に分けてください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    OP_C4(0x02, 0x02, 0x001A)
    OP_C4(0x02, 0x02, 0x000A)
    OP_C4(0x02, 0x02, 0x001E)
    OP_C4(0x02, 0x02, 0x0015)
    OP_C4(0x02, 0x03, 0x0023)
    OP_C4(0x02, 0x03, 0x000C)
    OP_C4(0x02, 0x03, 0x001C)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞莉莎'])"),
            Expr.Return,
        ),
        'loc_18698',
    )

    OP_C4(0x02, 0x03, 0x0001)

    def _loc_18698(): pass

    label('loc_18698')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾瑪'])"),
            Expr.Return,
        ),
        'loc_186A8',
    )

    OP_C4(0x02, 0x03, 0x0005)

    def _loc_186A8(): pass

    label('loc_186A8')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['菲'])"),
            Expr.Return,
        ),
        'loc_186B8',
    )

    OP_C4(0x02, 0x03, 0x0007)

    def _loc_186B8(): pass

    label('loc_186B8')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['勞拉'])"),
            Expr.Return,
        ),
        'loc_186C8',
    )

    OP_C4(0x02, 0x03, 0x0003)

    def _loc_186C8(): pass

    label('loc_186C8')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['莎拉'])"),
            Expr.Return,
        ),
        'loc_186D8',
    )

    OP_C4(0x02, 0x03, 0x000F)

    def _loc_186D8(): pass

    label('loc_186D8')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['提妲'])"),
            Expr.Return,
        ),
        'loc_186E8',
    )

    OP_C4(0x02, 0x03, 0x0014)

    def _loc_186E8(): pass

    label('loc_186E8')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['安潔莉卡'])"),
            Expr.Return,
        ),
        'loc_186F8',
    )

    OP_C4(0x02, 0x03, 0x0012)

    def _loc_186F8(): pass

    label('loc_186F8')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0716, 5, 0x38B5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_18740',
    )

    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_1874F')

    def _loc_18740(): pass

    label('loc_18740')

    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_C4(0x01, 0x01)
    OP_C4(0x01, 0x02)
    OP_C4(0x01, 0x03)

    def _loc_1874F(): pass

    label('loc_1874F')

    Jump('loc_196C6')

    def _loc_18754(): pass

    label('loc_18754')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0713, 7, 0x389F)),
            Expr.Return,
        ),
        'loc_189E3',
    )

    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＡチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x001D)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x05, 0x0002)
    OP_C4(0x02, 0x05, 0x0004)
    OP_C4(0x02, 0x05, 0x0006)
    OP_C4(0x02, 0x05, 0x0011)
    OP_C4(0x02, 0x05, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    OP_3B(0x00, (0xFF, 0x2F49, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_23(0x05, 65535, 750, 1100, 186, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            '#3CＢチームを編成してください。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    OP_C4(0x02, 0x01, 0x001A)
    OP_C4(0x02, 0x01, 0x001C)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x0023)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x05, 0x0001)
    OP_C4(0x02, 0x05, 0x0005)
    OP_C4(0x02, 0x05, 0x0007)
    OP_C4(0x02, 0x05, 0x0003)
    OP_C4(0x02, 0x05, 0x000F)
    OP_C4(0x02, 0x05, 0x0014)
    OP_C4(0x02, 0x05, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x30,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_196C6')

    def _loc_189E3(): pass

    label('loc_189E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0712, 1, 0x3891)),
            Expr.Return,
        ),
        'loc_18A04',
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)

    Jump('loc_196C6')

    def _loc_18A04(): pass

    label('loc_18A04')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0710, 3, 0x3883)),
            Expr.Return,
        ),
        'loc_18BA4',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    OP_C4(0x02, 0x03, 0x0011)
    OP_C4(0x02, 0x03, 0x0015)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000100)

    Jump('loc_196C6')

    def _loc_18BA4(): pass

    label('loc_18BA4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0701, 5, 0x380D)),
            Expr.Return,
        ),
        'loc_18C24',
    )

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['提妲'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000001)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0703, 5, 0x381D)),
            Expr.Return,
        ),
        'loc_18C1F',
    )

    FormationAddMember(ChrTable['蘭迪'])
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000001)

    def _loc_18C1F(): pass

    label('loc_18C1F')

    Jump('loc_196C6')

    def _loc_18C24(): pass

    label('loc_18C24')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0700, 3, 0x3803)),
            Expr.Return,
        ),
        'loc_18F67',
    )

    If(
        (
            (Expr.Eval, "OP_73(0x0016, 0x00, 0x01, 0x02)"),
            (Expr.TestScenaFlags, ScenaFlag(0x0750, 3, 0x3A83)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0751, 0, 0x3A88)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_18DD9',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x03, 0x0011)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    If(
        (
            (Expr.Eval, "IsMapEqualTo('v50?0')"),
            (Expr.Eval, "IsMapEqualTo('a0000')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_18DD4',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000100)

    def _loc_18DD4(): pass

    label('loc_18DD4')

    Jump('loc_18F62')

    def _loc_18DD9(): pass

    label('loc_18DD9')

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x03, 0x0014)
    OP_C4(0x02, 0x03, 0x0011)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    If(
        (
            (Expr.Eval, "IsMapEqualTo('v50?0')"),
            (Expr.Eval, "IsMapEqualTo('a0000')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_18F62',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000100)

    def _loc_18F62(): pass

    label('loc_18F62')

    Jump('loc_196C6')

    def _loc_18F67(): pass

    label('loc_18F67')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06F5, 5, 0x37AD)),
            Expr.Return,
        ),
        'loc_19178',
    )

    OP_23(0x05, 65535, 160, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            0x8,
            '★DEBUG:フィーかサラを選んでください。',
            TxtCtl.ShowAll,
            0x8,
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0xF9,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_75(0x00, 0x00, 0x0000, 0x42200000, 0x00000000)
    OP_75(0x01, 0x00, '★DEBUG:フィー', 0x00000001)
    OP_75(0x01, 0x00, '★DEBUG:サラ', 0x00000002)
    OP_75(0x02, 0x00, 0x00, 0xFFFF, 0xFFFF, 0x00)
    OP_75(0x04, 0x00, 0xF9)
    OP_75(0x03, 0x00)
    OP_25(0x00)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x00, 0x0002)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19063',
    )

    OP_C4(0x02, 0x00, 0x0007)

    Jump('loc_19068')

    def _loc_19063(): pass

    label('loc_19063')

    OP_C4(0x02, 0x00, 0x000F)

    def _loc_19068(): pass

    label('loc_19068')

    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000010)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_190E2',
    )

    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000010)

    Jump('loc_190EA')

    def _loc_190E2(): pass

    label('loc_190E2')

    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000010)

    def _loc_190EA(): pass

    label('loc_190EA')

    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    If(
        (
            (Expr.PushVar, 0xF9),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1912A',
    )

    SetScenaFlags(ScenaFlag(0x0720, 5, 0x3905))

    Jump('loc_1912D')

    def _loc_1912A(): pass

    label('loc_1912A')

    ClearScenaFlags(ScenaFlag(0x0720, 5, 0x3905))

    def _loc_1912D(): pass

    label('loc_1912D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06F8, 7, 0x37C7)),
            Expr.Return,
        ),
        'loc_19142',
    )

    FormationAddMember(ChrTable['阿加特'])
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000011)

    def _loc_19142(): pass

    label('loc_19142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06F9, 1, 0x37C9)),
            Expr.Return,
        ),
        'loc_19173',
    )

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['菲'])"),
            Expr.Return,
        ),
        'loc_19167',
    )

    FormationCtrl(0x01, ChrTable['菲'])
    MenuChrFlagCmd(0x01, ChrTable['菲'], 0x00000001)

    Jump('loc_19173')

    def _loc_19167(): pass

    label('loc_19167')

    FormationCtrl(0x01, ChrTable['莎拉'])
    MenuChrFlagCmd(0x01, ChrTable['莎拉'], 0x00000001)

    def _loc_19173(): pass

    label('loc_19173')

    Jump('loc_196C6')

    def _loc_19178(): pass

    label('loc_19178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06F4, 3, 0x37A3)),
            Expr.Return,
        ),
        'loc_192D3',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)

    Jump('loc_196C6')

    def _loc_192D3(): pass

    label('loc_192D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06EA, 7, 0x3757)),
            Expr.Return,
        ),
        'loc_1939B',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x00, 0x0004)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0023)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    Jump('loc_196C6')

    def _loc_1939B(): pass

    label('loc_1939B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06E7, 1, 0x3739)),
            Expr.Return,
        ),
        'loc_194E9',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000C)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)

    Jump('loc_196C6')

    def _loc_194E9(): pass

    label('loc_194E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06E4, 1, 0x3721)),
            Expr.Return,
        ),
        'loc_195B7',
    )

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])

    Jump('loc_196C6')

    def _loc_195B7(): pass

    label('loc_195B7')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞修'])

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x06E2, 7, 0x3717)),
            Expr.Return,
        ),
        'loc_196C6',
    )

    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])
    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)

    def _loc_196C6(): pass

    label('loc_196C6')

    Jump('loc_1A7F7')

    def _loc_196CB(): pass

    label('loc_196CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0842, 3, 0x4213)),
            Expr.Return,
        ),
        'loc_197E2',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x000A)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x0023)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x02, 0x001F)
    OP_C4(0x02, 0x03, 0x0016)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000010)

    Jump('loc_1A47F')

    def _loc_197E2(): pass

    label('loc_197E2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x083A, 5, 0x41D5)),
            Expr.Return,
        ),
        'loc_198F6',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x00, 0x000B)
    OP_C4(0x02, 0x00, 0x0004)
    OP_C4(0x02, 0x00, 0x0016)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x02, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000010)

    Jump('loc_1A47F')

    def _loc_198F6(): pass

    label('loc_198F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x083A, 1, 0x41D1)),
            Expr.Return,
        ),
        'loc_19AC2',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0016)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤娜'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199A5',
    )

    FormationAddMember(ChrTable['尤娜'])

    def _loc_199A5(): pass

    label('loc_199A5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['庫爾特'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199B5',
    )

    FormationAddMember(ChrTable['庫爾特'])

    def _loc_199B5(): pass

    label('loc_199B5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['繆潔'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199C5',
    )

    FormationAddMember(ChrTable['繆潔'])

    def _loc_199C5(): pass

    label('loc_199C5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞修'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199D5',
    )

    FormationAddMember(ChrTable['亞修'])

    def _loc_199D5(): pass

    label('loc_199D5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞莉莎'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199E5',
    )

    FormationAddMember(ChrTable['亞莉莎'])

    def _loc_199E5(): pass

    label('loc_199E5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['勞拉'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199F5',
    )

    FormationAddMember(ChrTable['勞拉'])

    def _loc_199F5(): pass

    label('loc_199F5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['馬奇亞斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19A05',
    )

    FormationAddMember(ChrTable['馬奇亞斯'])

    def _loc_19A05(): pass

    label('loc_19A05')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['菲'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19A15',
    )

    FormationAddMember(ChrTable['菲'])

    def _loc_19A15(): pass

    label('loc_19A15')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['莎拉'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19A25',
    )

    FormationAddMember(ChrTable['莎拉'])

    def _loc_19A25(): pass

    label('loc_19A25')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['雪倫'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19A35',
    )

    FormationAddMember(ChrTable['雪倫'])

    def _loc_19A35(): pass

    label('loc_19A35')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000011)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000001)

    Jump('loc_1A47F')

    def _loc_19AC2(): pass

    label('loc_19AC2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0838, 3, 0x41C3)),
            Expr.Return,
        ),
        'loc_19CB4',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x03, 0x0012)
    OP_C4(0x02, 0x03, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    OP_C4(0x02, 0x03, 0x0016)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['愛麗榭'], 0x01000000)
    MenuChrFlagCmd(0x00, ChrTable['艾爾芬皇女'], 0x01000000)
    FormationAddMember(ChrTable['愛麗榭'])
    FormationAddMember(ChrTable['艾爾芬皇女'])

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0838, 5, 0x41C5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_19CAF',
    )

    If(
        (
            (Expr.Eval, "IsMapEqualTo('v30?0')"),
            (Expr.Eval, "IsMapEqualTo('a0000')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_19CAF',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000100)

    def _loc_19CAF(): pass

    label('loc_19CAF')

    Jump('loc_1A47F')

    def _loc_19CB4(): pass

    label('loc_19CB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0832, 3, 0x4193)),
            Expr.Return,
        ),
        'loc_19DCD',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0007)
    OP_C4(0x02, 0x00, 0x0017)
    OP_C4(0x02, 0x00, 0x0008)
    OP_C4(0x02, 0x00, 0x000E)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x02, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000010)

    Jump('loc_1A47F')

    def _loc_19DCD(): pass

    label('loc_19DCD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x082B, 3, 0x415B)),
            Expr.Return,
        ),
        'loc_19EEA',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0012)
    OP_C4(0x02, 0x00, 0x000F)
    OP_C4(0x02, 0x00, 0x000D)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x01, 0x0004)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x02, 0x0014)
    OP_C4(0x02, 0x02, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)

    ExecExpressionWithVar(
        0xF6,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000010)

    Jump('loc_1A47F')

    def _loc_19EEA(): pass

    label('loc_19EEA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x082A, 3, 0x4153)),
            Expr.Return,
        ),
        'loc_1A0BA',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x03, 0x0012)
    OP_C4(0x02, 0x03, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['托娃'], 0x01000000)
    FormationAddMember(ChrTable['托娃'])

    ExecExpressionWithVar(
        0x27,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x082A, 5, 0x4155)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A0B5',
    )

    If(
        (
            (Expr.Eval, "IsMapEqualTo('v30?0')"),
            (Expr.Eval, "IsMapEqualTo('a0000')"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1A0B5',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000100)

    def _loc_1A0B5(): pass

    label('loc_1A0B5')

    Jump('loc_1A47F')

    def _loc_1A0BA(): pass

    label('loc_1A0BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0824, 3, 0x4123)),
            Expr.Return,
        ),
        'loc_1A302',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x00, 0x0028)
    OP_C4(0x02, 0x00, 0x0005)
    OP_C4(0x02, 0x00, 0x0006)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    FormationReset(0x00)
    OP_C4(0x01, 0x00)

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤娜'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A185',
    )

    FormationAddMember(ChrTable['尤娜'])

    def _loc_1A185(): pass

    label('loc_1A185')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['庫爾特'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A195',
    )

    FormationAddMember(ChrTable['庫爾特'])

    def _loc_1A195(): pass

    label('loc_1A195')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞爾緹娜'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1A5',
    )

    FormationAddMember(ChrTable['亞爾緹娜'])

    def _loc_1A1A5(): pass

    label('loc_1A1A5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['繆潔'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1B5',
    )

    FormationAddMember(ChrTable['繆潔'])

    def _loc_1A1B5(): pass

    label('loc_1A1B5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞修'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1C5',
    )

    FormationAddMember(ChrTable['亞修'])

    def _loc_1A1C5(): pass

    label('loc_1A1C5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['亞莉莎'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1D5',
    )

    FormationAddMember(ChrTable['亞莉莎'])

    def _loc_1A1D5(): pass

    label('loc_1A1D5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['艾略特'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1E5',
    )

    FormationAddMember(ChrTable['艾略特'])

    def _loc_1A1E5(): pass

    label('loc_1A1E5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['勞拉'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A1F5',
    )

    FormationAddMember(ChrTable['勞拉'])

    def _loc_1A1F5(): pass

    label('loc_1A1F5')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['馬奇亞斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A205',
    )

    FormationAddMember(ChrTable['馬奇亞斯'])

    def _loc_1A205(): pass

    label('loc_1A205')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['尤西斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A215',
    )

    FormationAddMember(ChrTable['尤西斯'])

    def _loc_1A215(): pass

    label('loc_1A215')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['菲'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A225',
    )

    FormationAddMember(ChrTable['菲'])

    def _loc_1A225(): pass

    label('loc_1A225')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['蓋烏斯'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A235',
    )

    FormationAddMember(ChrTable['蓋烏斯'])

    def _loc_1A235(): pass

    label('loc_1A235')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['莎拉'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A245',
    )

    FormationAddMember(ChrTable['莎拉'])

    def _loc_1A245(): pass

    label('loc_1A245')

    If(
        (
            (Expr.Eval, "FormationCtrl(0x05, ChrTable['克洛'])"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A255',
    )

    FormationAddMember(ChrTable['克洛'])

    def _loc_1A255(): pass

    label('loc_1A255')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000010)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000010)

    Jump('loc_1A47F')

    def _loc_1A302(): pass

    label('loc_1A302')

    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['瑟蕾奴'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])
    FormationAddMember(ChrTable['克洛'])
    OP_69(0x01, 0xFFF8)
    OP_69(0x00, 0x0000, 0x0028, 0xFF, 0x00, 0x00)
    OP_69(0x00, 0x000B, 0x000A, 0xFF, 0x00, 0x00)
    FormationCtrl(0x08, ChrTable['黎恩'], -1.0, 0.0, 0x00)
    FormationCtrl(0x08, ChrTable['瑟蕾奴'], -2.0, 1.0, 0x00)
    FormationCtrl(0x08, ChrTable['庫爾特'], 1.0, 0.0, 0x00)
    FormationCtrl(0x08, ChrTable['尤娜'], 2.0, 1.0, 0x00)
    FormationCtrl(0x08, ChrTable['亞修'], -1.0, 2.0, 0x00)
    FormationCtrl(0x08, ChrTable['亞莉莎'], 1.0, 2.0, 0x00)
    FormationCtrl(0x08, ChrTable['亞爾緹娜'], -2.0, 2.0, 0x00)
    FormationCtrl(0x08, ChrTable['繆潔'], 2.0, 2.0, 0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0823, 5, 0x411D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A47F',
    )

    FormationCtrl(0x1B, 0x01)
    FormationReset(0x00)
    FormationAddMember(ChrTable['黎恩'])
    FormationSetLeader(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000110)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000100)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000100)

    def _loc_1A47F(): pass

    label('loc_1A47F')

    Jump('loc_1A7F7')

    def _loc_1A484(): pass

    label('loc_1A484')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)

    Jump('loc_1A7F7')

    def _loc_1A49E(): pass

    label('loc_1A49E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x09FB, 7, 0x4FDF)),
            (Expr.TestScenaFlags, ScenaFlag(0x09FC, 5, 0x4FE5)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A59F',
    )

    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            '★DEBUG:オズボーン戦のチーム設定',
            TxtCtl.ShowAll,
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    FormationCtrl(0x0E, 0x00)
    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0001)
    OP_C4(0x02, 0x00, 0x0002)
    OP_C4(0x02, 0x00, 0x0003)
    OP_C4(0x02, 0x00, 0x0004)
    OP_C4(0x02, 0x00, 0x000F)
    OP_C4(0x02, 0x01, 0x0005)
    OP_C4(0x02, 0x01, 0x0006)
    OP_C4(0x02, 0x01, 0x0007)
    OP_C4(0x02, 0x01, 0x0008)
    OP_C4(0x02, 0x01, 0x0017)
    OP_C4(0x02, 0x02, 0x0000)
    OP_C4(0x02, 0x02, 0x000A)
    OP_C4(0x02, 0x02, 0x000B)
    OP_C4(0x02, 0x02, 0x000C)
    OP_C4(0x02, 0x02, 0x000D)
    OP_C4(0x02, 0x02, 0x000E)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationSetLeader(ChrTable['黎恩'])

    Jump('loc_1A7A0')

    def _loc_1A59F(): pass

    label('loc_1A59F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x09F2, 1, 0x4F91)),
            Expr.Return,
        ),
        'loc_1A5FA',
    )

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])
    FormationAddMember(ChrTable['克洛'])
    FormationSetLeader(ChrTable['黎恩'])

    Jump('loc_1A7A0')

    def _loc_1A5FA(): pass

    label('loc_1A5FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x09EA, 1, 0x4F51)),
            Expr.Return,
        ),
        'loc_1A6AD',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x001A)
    OP_C4(0x02, 0x00, 0x001B)
    OP_C4(0x02, 0x00, 0x0011)
    OP_C4(0x02, 0x00, 0x0014)
    OP_C4(0x02, 0x00, 0x001C)
    OP_C4(0x02, 0x01, 0x001D)
    OP_C4(0x02, 0x01, 0x001E)
    OP_C4(0x02, 0x01, 0x0015)
    OP_C4(0x02, 0x01, 0x001F)
    OP_C4(0x02, 0x02, 0x0012)
    OP_C4(0x02, 0x02, 0x0021)
    OP_C4(0x02, 0x02, 0x0016)
    OP_C4(0x02, 0x02, 0x0020)
    OP_C4(0x02, 0x03, 0x0023)
    OP_C4(0x02, 0x03, 0x0024)
    OP_C4(0x02, 0x03, 0x0025)
    OP_C4(0x02, 0x03, 0x0026)
    OP_C4(0x02, 0x03, 0x0027)
    OP_C4(0x02, 0x04, 0x0010)
    OP_C4(0x02, 0x04, 0x0018)
    OP_C4(0x02, 0x04, 0x0022)
    OP_C4(0x02, 0x04, 0x0019)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    OP_69(0x14, 0x01, 0x00)

    Jump('loc_1A7A0')

    def _loc_1A6AD(): pass

    label('loc_1A6AD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x09E1, 3, 0x4F0B)),
            Expr.Return,
        ),
        'loc_1A794',
    )

    Call(ScriptId.System, 'FC_TSMenu_Reset')
    OP_C4(0x02, 0x00, 0x0000)
    OP_C4(0x02, 0x01, 0x000A)
    OP_C4(0x02, 0x01, 0x000B)
    OP_C4(0x02, 0x01, 0x000C)
    OP_C4(0x02, 0x01, 0x000D)
    OP_C4(0x02, 0x01, 0x000E)
    OP_C4(0x02, 0x01, 0x0001)
    OP_C4(0x02, 0x01, 0x0002)
    OP_C4(0x02, 0x01, 0x0003)
    OP_C4(0x02, 0x02, 0x0004)
    OP_C4(0x02, 0x02, 0x0005)
    OP_C4(0x02, 0x02, 0x0006)
    OP_C4(0x02, 0x02, 0x0007)
    OP_C4(0x02, 0x02, 0x0008)
    OP_C4(0x02, 0x02, 0x000F)
    OP_C4(0x02, 0x02, 0x0017)
    OP_C4(0x02, 0x02, 0x0023)
    OP_C4(0x02, 0x03, 0x0012)
    OP_C4(0x02, 0x03, 0x0014)
    OP_C4(0x02, 0x03, 0x001F)
    OP_C4(0x02, 0x03, 0x0016)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)
    SetScenaFlags(ScenaFlag(0x0072, 1, 0x391))

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2C,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2D,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x2E,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_C5(0x00, 0x01, 0x00)
    OP_C5(0x01)
    Call(ScriptId.System, 'FC_ResetMenuChrFlagALL')
    FormationReset(0x00)
    OP_C4(0x01, 0x00)
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000010)

    Jump('loc_1A7A0')

    def _loc_1A794(): pass

    label('loc_1A794')

    FormationAddMember(ChrTable['黎恩'])
    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)

    def _loc_1A7A0(): pass

    label('loc_1A7A0')

    Jump('loc_1A7F7')

    def _loc_1A7A5(): pass

    label('loc_1A7A5')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FormationAddMember(ChrTable['黎恩'])
    FormationAddMember(ChrTable['尤娜'])
    FormationAddMember(ChrTable['庫爾特'])
    FormationAddMember(ChrTable['亞爾緹娜'])
    FormationAddMember(ChrTable['繆潔'])
    FormationAddMember(ChrTable['亞修'])
    FormationAddMember(ChrTable['亞莉莎'])
    FormationAddMember(ChrTable['艾略特'])
    FormationAddMember(ChrTable['勞拉'])
    FormationAddMember(ChrTable['馬奇亞斯'])
    FormationAddMember(ChrTable['艾瑪'])
    FormationAddMember(ChrTable['尤西斯'])
    FormationAddMember(ChrTable['菲'])
    FormationAddMember(ChrTable['蓋烏斯'])
    FormationAddMember(ChrTable['莎拉'])
    FormationAddMember(ChrTable['克洛'])
    FormationSetLeader(ChrTable['黎恩'])

    Jump('loc_1A7F7')

    def _loc_1A7F7(): pass

    label('loc_1A7F7')

    Call(ScriptId.System, 'FC_CreateCeline')

    If(
        (
            (Expr.Expr25, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1A81E',
    )

    OP_14(0x00001000)

    def _loc_1A81E(): pass

    label('loc_1A81E')

    FormationSetLeader(0xF000)
    Sleep(0)

    Return()

# id: 0x0022 offset: 0x1A828
@scena.Code('ArgumentTest')
def ArgumentTest():
    Call(ScriptId.Current, 'ArgumentTest0', (0xFF, 0x6F, 0x0), (0xFF, 0xDE, 0x0))

    Return()

# id: 0x0023 offset: 0x1A848
@scena.Code('ArgumentTest0')
def ArgumentTest0():
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x01, 0x01)
    DebugLog(0x00, (0x33, 0x0, 0x0))
    Call(ScriptId.Current, 'ArgumentTest1', (0xDD, '333'), (0xFF, 0x7B, 0x0), (0x33, 0x0, 0x0))
    DebugLog(0x00, (0x33, 0x1, 0x0))

    Return()

# id: 0x0024 offset: 0x1A88C
@scena.Code('ArgumentTest1')
def ArgumentTest1():
    OP_0C(0x01, 0x01)
    OP_0E(0x01, 0x00, 0x00)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x01)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x01, 0x02)
    DebugLog(0x02, (0x44, 0x0, 0x0))
    DebugLog(0x01, (0x33, 0x0, 0x0))
    DebugLog(0x00, (0x33, 0x1, 0x0))

    OP_0D(
        0x00,
        0x00,
        (
            (Expr.PushLong, 0x22B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    DebugLog(0x00, (0x33, 0x0, 0x0))

    Return()

# id: 0x0025 offset: 0x1A8CC
@scena.Code('Mg01_Parts')
def Mg01_Parts():
    Call(ScriptId.Current, 'BeginDebugScript')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1A8E9(): pass

    label('loc_1A8E9')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AF08',
    )

    MenuCreate(0, 14, 24.0, 99)
    MenuAddItem(0, 'ダブルフック　　：（針の速度が一段階遅くなる）', 0x00000035)
    MenuAddItem(0, 'キャッチ判定　　：（針の速度がさらに一段階遅くなる）', 0x00000035)
    MenuAddItem(0, 'アミノジェル　　：（リング一回転が遅くなる）', 0x00000036)
    MenuAddItem(0, 'Ｗアミノ　　　　：（リング一回転がさらに遅くなる）', 0x00000037)
    MenuAddItem(0, '拡張スプール　　：（ラインの上限が50ｍから60ｍに伸びる）', 0x00000038)
    MenuAddItem(0, '拡張スプールＧ　：（ラインの上限が60ｍから70ｍに伸びる）', 0x00000039)
    MenuAddItem(0, 'デュエルライン　：（テンション上限が25％増える）', 0x0000003A)
    MenuAddItem(0, 'テクノロッド　　：（テンション上限が25％増える）', 0x0000003B)
    MenuAddItem(0, 'ショックリーダー：（テンション上升値が10％減る）', 0x0000003C)
    MenuAddItem(0, 'オートドラグ　　：（テンション上升値が10％減る）', 0x0000003D)
    MenuAddItem(0, 'カスタムハンドル：（巻き上げ速度が0.5m/s上がる）', 0x0000003E)
    MenuAddItem(0, 'チューンドギア　：（巻き上げ速度が0.5m/s上がる）', 0x0000003F)
    MenuAddItem(0, '釣りパーツ全入手', 0x00000040)
    MenuAddItem(0, '釣りパーツ全破棄', 0x00000041)
    MenuSetPos(0, 0x01, 24, 24, 0x00)
    MenuShow(0, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000040, 'loc_1AD94'),
        (0x00000041, 'loc_1ADF9'),
        (0x00000035, 'loc_1AE5E'),
        (0x00000035, 'loc_1AE6B'),
        (0x00000036, 'loc_1AE78'),
        (0x00000037, 'loc_1AE85'),
        (0x00000038, 'loc_1AE92'),
        (0x00000039, 'loc_1AE9F'),
        (0x0000003A, 'loc_1AEAC'),
        (0x0000003B, 'loc_1AEB9'),
        (0x0000003C, 'loc_1AEC6'),
        (0x0000003D, 'loc_1AED3'),
        (0x0000003E, 'loc_1AEE0'),
        (0x0000003F, 'loc_1AEED'),
        (-1, 'loc_1AEFA'),
    )

    def _loc_1AD94(): pass

    label('loc_1AD94')

    AddItem(0x00, 0x085C, 1)
    AddItem(0x00, 0x085D, 1)
    AddItem(0x00, 0x085E, 1)
    AddItem(0x00, 0x085F, 1)
    AddItem(0x00, 0x0860, 1)
    AddItem(0x00, 0x0861, 1)
    AddItem(0x00, 0x0862, 1)
    AddItem(0x00, 0x0863, 1)
    AddItem(0x00, 0x0864, 1)
    AddItem(0x00, 0x0865, 1)
    AddItem(0x00, 0x0866, 1)
    AddItem(0x00, 0x0867, 1)

    Jump('loc_1AF03')

    def _loc_1ADF9(): pass

    label('loc_1ADF9')

    AddItem(0x01, 0x085C, 99)
    AddItem(0x01, 0x085D, 99)
    AddItem(0x01, 0x085E, 99)
    AddItem(0x01, 0x085F, 99)
    AddItem(0x01, 0x0860, 99)
    AddItem(0x01, 0x0861, 99)
    AddItem(0x01, 0x0862, 99)
    AddItem(0x01, 0x0863, 99)
    AddItem(0x01, 0x0864, 99)
    AddItem(0x01, 0x0865, 99)
    AddItem(0x01, 0x0866, 99)
    AddItem(0x01, 0x0867, 99)

    Jump('loc_1AF03')

    def _loc_1AE5E(): pass

    label('loc_1AE5E')

    AddItem(0x00, 0x085C, 1)

    Jump('loc_1AF03')

    def _loc_1AE6B(): pass

    label('loc_1AE6B')

    AddItem(0x00, 0x085D, 1)

    Jump('loc_1AF03')

    def _loc_1AE78(): pass

    label('loc_1AE78')

    AddItem(0x00, 0x085E, 1)

    Jump('loc_1AF03')

    def _loc_1AE85(): pass

    label('loc_1AE85')

    AddItem(0x00, 0x085F, 1)

    Jump('loc_1AF03')

    def _loc_1AE92(): pass

    label('loc_1AE92')

    AddItem(0x00, 0x0860, 1)

    Jump('loc_1AF03')

    def _loc_1AE9F(): pass

    label('loc_1AE9F')

    AddItem(0x00, 0x0861, 1)

    Jump('loc_1AF03')

    def _loc_1AEAC(): pass

    label('loc_1AEAC')

    AddItem(0x00, 0x0862, 1)

    Jump('loc_1AF03')

    def _loc_1AEB9(): pass

    label('loc_1AEB9')

    AddItem(0x00, 0x0863, 1)

    Jump('loc_1AF03')

    def _loc_1AEC6(): pass

    label('loc_1AEC6')

    AddItem(0x00, 0x0864, 1)

    Jump('loc_1AF03')

    def _loc_1AED3(): pass

    label('loc_1AED3')

    AddItem(0x00, 0x0865, 1)

    Jump('loc_1AF03')

    def _loc_1AEE0(): pass

    label('loc_1AEE0')

    AddItem(0x00, 0x0866, 1)

    Jump('loc_1AF03')

    def _loc_1AEED(): pass

    label('loc_1AEED')

    AddItem(0x00, 0x0867, 1)

    Jump('loc_1AF03')

    def _loc_1AEFA(): pass

    label('loc_1AEFA')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1AF03(): pass

    label('loc_1AF03')

    Jump('loc_1A8E9')

    def _loc_1AF08(): pass

    label('loc_1AF08')

    MenuCmd(0x03, 0)

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EndDebugScript')

    Return()

# id: 0x0026 offset: 0x1AF28
@scena.Code('Mg08_Tutorial_Flag')
def Mg08_Tutorial_Flag():
    Call(ScriptId.Current, 'BeginDebugScript')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1AF45(): pass

    label('loc_1AF45')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B115',
    )

    MenuCreate(0, 24, 24.0, 99)
    MenuAddItem(0, 'チュートリアルフラグリセット', 0x00000042)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 0, 0x450)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'チュートリアルデッキ構築完了', 0x00000043, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.TestScenaFlags, ScenaFlag(0x008A, 1, 0x451)),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MenuCmd(0x08, 0, 'チュートリアルをスキップする', 0x00000044, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))
    MenuSetPos(0, 0x01, 24, 24, 0x01)
    MenuShow(0, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000042, 'loc_1B04A'),
        (0x00000043, 'loc_1B0A6'),
        (0x00000044, 'loc_1B0AE'),
        (-1, 'loc_1B107'),
    )

    def _loc_1B04A(): pass

    label('loc_1B04A')

    ClearScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    ClearScenaFlags(ScenaFlag(0x008B, 2, 0x45A))
    ClearScenaFlags(ScenaFlag(0x008B, 3, 0x45B))
    ClearScenaFlags(ScenaFlag(0x008E, 0, 0x470))
    ClearScenaFlags(ScenaFlag(0x008E, 1, 0x471))
    ClearScenaFlags(ScenaFlag(0x008E, 2, 0x472))
    ClearScenaFlags(ScenaFlag(0x008E, 3, 0x473))
    ClearScenaFlags(ScenaFlag(0x008E, 4, 0x474))
    ClearScenaFlags(ScenaFlag(0x008E, 5, 0x475))
    ClearScenaFlags(ScenaFlag(0x008E, 6, 0x476))
    ClearScenaFlags(ScenaFlag(0x008E, 7, 0x477))
    ClearScenaFlags(ScenaFlag(0x008F, 0, 0x478))
    ClearScenaFlags(ScenaFlag(0x008F, 1, 0x479))
    ClearScenaFlags(ScenaFlag(0x008F, 2, 0x47A))
    ClearScenaFlags(ScenaFlag(0x008F, 3, 0x47B))
    ClearScenaFlags(ScenaFlag(0x008F, 4, 0x47C))
    ClearScenaFlags(ScenaFlag(0x008F, 5, 0x47D))
    ClearScenaFlags(ScenaFlag(0x008F, 6, 0x47E))
    ClearScenaFlags(ScenaFlag(0x008F, 7, 0x47F))
    ClearScenaFlags(ScenaFlag(0x0090, 0, 0x480))
    ClearScenaFlags(ScenaFlag(0x0090, 1, 0x481))
    ClearScenaFlags(ScenaFlag(0x0090, 2, 0x482))
    ClearScenaFlags(ScenaFlag(0x0090, 3, 0x483))
    ClearScenaFlags(ScenaFlag(0x0090, 4, 0x484))
    ClearScenaFlags(ScenaFlag(0x0090, 5, 0x485))
    ClearScenaFlags(ScenaFlag(0x0090, 6, 0x486))
    ClearScenaFlags(ScenaFlag(0x0090, 7, 0x487))
    ClearScenaFlags(ScenaFlag(0x0091, 0, 0x488))
    ClearScenaFlags(ScenaFlag(0x008A, 0, 0x450))

    Jump('loc_1B110')

    def _loc_1B0A6(): pass

    label('loc_1B0A6')

    SetScenaFlags(ScenaFlag(0x008A, 0, 0x450))

    Jump('loc_1B110')

    def _loc_1B0AE(): pass

    label('loc_1B0AE')

    SetScenaFlags(ScenaFlag(0x008A, 1, 0x451))
    SetScenaFlags(ScenaFlag(0x008B, 2, 0x45A))
    SetScenaFlags(ScenaFlag(0x008B, 3, 0x45B))
    SetScenaFlags(ScenaFlag(0x008E, 0, 0x470))
    SetScenaFlags(ScenaFlag(0x008E, 1, 0x471))
    SetScenaFlags(ScenaFlag(0x008E, 2, 0x472))
    SetScenaFlags(ScenaFlag(0x008E, 3, 0x473))
    SetScenaFlags(ScenaFlag(0x008E, 4, 0x474))
    SetScenaFlags(ScenaFlag(0x008E, 5, 0x475))
    SetScenaFlags(ScenaFlag(0x008E, 6, 0x476))
    SetScenaFlags(ScenaFlag(0x008E, 7, 0x477))
    SetScenaFlags(ScenaFlag(0x008F, 0, 0x478))
    SetScenaFlags(ScenaFlag(0x008F, 1, 0x479))
    SetScenaFlags(ScenaFlag(0x008F, 2, 0x47A))
    SetScenaFlags(ScenaFlag(0x008F, 3, 0x47B))
    SetScenaFlags(ScenaFlag(0x008F, 4, 0x47C))
    SetScenaFlags(ScenaFlag(0x008F, 5, 0x47D))
    SetScenaFlags(ScenaFlag(0x008F, 6, 0x47E))
    SetScenaFlags(ScenaFlag(0x008F, 7, 0x47F))
    SetScenaFlags(ScenaFlag(0x0090, 0, 0x480))
    SetScenaFlags(ScenaFlag(0x0090, 1, 0x481))
    SetScenaFlags(ScenaFlag(0x0090, 2, 0x482))
    SetScenaFlags(ScenaFlag(0x0090, 3, 0x483))
    SetScenaFlags(ScenaFlag(0x0090, 4, 0x484))
    SetScenaFlags(ScenaFlag(0x0090, 5, 0x485))
    SetScenaFlags(ScenaFlag(0x0090, 6, 0x486))
    SetScenaFlags(ScenaFlag(0x0090, 7, 0x487))
    SetScenaFlags(ScenaFlag(0x0091, 0, 0x488))

    Jump('loc_1B110')

    def _loc_1B107(): pass

    label('loc_1B107')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B110(): pass

    label('loc_1B110')

    Jump('loc_1AF45')

    def _loc_1B115(): pass

    label('loc_1B115')

    MenuCmd(0x03, 0)

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(ScriptId.Current, 'EndDebugScript')

    Return()

# id: 0x0027 offset: 0x1B134
@scena.Code('FC_mapjump_open')
def FC_mapjump_open():
    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B13D(): pass

    label('loc_1B13D')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B418',
    )

    MenuCreate(1, 24, 24.0, 99)
    MenuAddItem(1, '全部セット', 0x00000000)
    MenuAddItem(1, '全部クリア', 0x00000001)
    MenuAddItem(1, 'NEW全部セット', 0x00000002)
    MenuAddItem(1, 'NEW全部クリア', 0x00000003)
    MenuSetPos(1, 0x01, 400, 200, 0x01)
    MenuShow(1, 0xF7)
    MenuCmd(0x03, 1)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B1F3'),
        (0x00000001, 'loc_1B290'),
        (0x00000002, 'loc_1B32F'),
        (0x00000003, 'loc_1B39C'),
        (-1, 'loc_1B40A'),
    )

    def _loc_1B1F3(): pass

    label('loc_1B1F3')

    Call(ScriptId.Debug, 'FC_mapjump_open_all')
    OP_79(0x0D, 0x0001)
    OP_79(0x0D, 0x0002)
    OP_79(0x0E, 0x0054)
    OP_79(0x0D, 0x0004)
    OP_79(0x0D, 0x0003)
    OP_79(0x0D, 0x0006)
    OP_79(0x0D, 0x0007)
    OP_79(0x0D, 0x0009)
    OP_79(0x0D, 0x000A)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:マップの登録フラグをonにしました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1B413')

    def _loc_1B290(): pass

    label('loc_1B290')

    Call(ScriptId.Debug, 'FC_mapjump_close_all')
    OP_79(0x0F, 0x0001)
    OP_79(0x0F, 0x0002)
    OP_79(0x0E, 0x0054)
    OP_79(0x0F, 0x0004)
    OP_79(0x0F, 0x0003)
    OP_79(0x0F, 0x0006)
    OP_79(0x0F, 0x0007)
    OP_79(0x0F, 0x0009)
    OP_79(0x0F, 0x000A)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:マップの登録フラグをoffにしました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1B413')

    def _loc_1B32F(): pass

    label('loc_1B32F')

    OP_71(0x00, 0x25EE, 0x28DB)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:マップの NEW 登録フラグをonにしました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1B413')

    def _loc_1B39C(): pass

    label('loc_1B39C')

    OP_71(0x01, 0x25EE, 0x28DB)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:マップの NEW 登録フラグをoffにしました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1B413')

    def _loc_1B40A(): pass

    label('loc_1B40A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B413(): pass

    label('loc_1B413')

    Jump('loc_1B13D')

    def _loc_1B418(): pass

    label('loc_1B418')

    Return()

# id: 0x0028 offset: 0x1B41C
@scena.Code('FC_mapjump_open_all')
def FC_mapjump_open_all():
    OP_71(0x00, 0x2300, 0x25ED)

    Return()

# id: 0x0029 offset: 0x1B424
@scena.Code('FC_mapjump_close_all')
def FC_mapjump_close_all():
    OP_71(0x01, 0x2300, 0x25ED)

    Return()

# id: 0x002A offset: 0x1B42C
@scena.Code('FC_SetHealParty')
def FC_SetHealParty():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B435(): pass

    label('loc_1B435')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B604',
    )

    MenuCreate(1, 24, 24.0, 99)
    MenuAddItem(1, 'パーティ全回復', 0x00000000)
    MenuAddItem(1, 'パーティ瀕死', 0x00000001)
    MenuAddItem(1, 'パーティ全滅', 0x00000002)
    MenuAddItem(1, 'パーティCP 0', 0x00000003)
    MenuAddItem(1, 'パーティCP 150', 0x00000004)
    MenuAddItem(1, 'パーティEP 0', 0x00000005)
    MenuAddItem(1, 'パーティEP MAX', 0x00000006)
    MenuAddItem(1, 'パーティBP MAX', 0x00000007)
    MenuSetPos(1, 0x01, 224, 24, 0x01)
    MenuShow(1, 0xF8)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B575'),
        (0x00000001, 'loc_1B582'),
        (0x00000002, 'loc_1B59F'),
        (0x00000003, 'loc_1B5B4'),
        (0x00000004, 'loc_1B5C1'),
        (0x00000005, 'loc_1B5CE'),
        (0x00000006, 'loc_1B5DB'),
        (0x00000007, 'loc_1B5E8'),
        (-1, 'loc_1B5F1'),
    )

    def _loc_1B575(): pass

    label('loc_1B575')

    OP_48(0x00, 0xFFFF, 0x002F, 0x0000)

    Jump('loc_1B5FF')

    def _loc_1B582(): pass

    label('loc_1B582')

    OP_48(0x00, 0xFFFF, 0x000A, 0x0001)
    OP_48(0x00, 0xFFFF, 0x0014, 0x0000)
    OP_48(0x00, 0xFFFF, 0x001E, 0x0000)

    Jump('loc_1B5FF')

    def _loc_1B59F(): pass

    label('loc_1B59F')

    OP_48(0x00, 0xFFFF, 0x000A, 0x0000)
    OP_48(0x00, 0xFFFF, 0x001E, 0x0000)

    Jump('loc_1B5FF')

    def _loc_1B5B4(): pass

    label('loc_1B5B4')

    OP_48(0x00, 0xFFFF, 0x001E, 0x0000)

    Jump('loc_1B5FF')

    def _loc_1B5C1(): pass

    label('loc_1B5C1')

    OP_48(0x00, 0xFFFF, 0x001E, 0x0096)

    Jump('loc_1B5FF')

    def _loc_1B5CE(): pass

    label('loc_1B5CE')

    OP_48(0x00, 0xFFFF, 0x0014, 0x0000)

    Jump('loc_1B5FF')

    def _loc_1B5DB(): pass

    label('loc_1B5DB')

    OP_48(0x00, 0xFFFF, 0x0014, 0x1388)

    Jump('loc_1B5FF')

    def _loc_1B5E8(): pass

    label('loc_1B5E8')

    OP_69(0x15, 0x0007)

    Jump('loc_1B5FF')

    def _loc_1B5F1(): pass

    label('loc_1B5F1')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1B5FF')

    def _loc_1B5FF(): pass

    label('loc_1B5FF')

    Jump('loc_1B435')

    def _loc_1B604(): pass

    label('loc_1B604')

    Return()

# id: 0x002B offset: 0x1B608
@scena.Code('FC_SetEquip')
def FC_SetEquip():
    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1B611(): pass

    label('loc_1B611')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BB7C',
    )

    MenuCreate(0, 24, 24.0, 99)
    MenuAddItem(0, 'アイテム全消去（装備も外す）', 0x00000000)
    MenuAddItem(0, 'クラフト、オーダー全消去', 0x00000001)
    MenuAddItem(0, '装備ロック設定', 0x00000002)
    MenuAddItem(0, '装備ロック解除', 0x00000003)
    MenuAddItem(0, 'マスタークオーツのレベル設定', 0x00000004)
    MenuAddItem(0, '全員のCAMP_JOINフラグ設定', 0x00000005)
    MenuSetPos(0, 0x01, 65535, 65535, 0x01)
    MenuShow(0, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_1B765'),
        (0x00000001, 'loc_1B7DF'),
        (0x00000002, 'loc_1B84D'),
        (0x00000003, 'loc_1B8C4'),
        (0x00000004, 'loc_1B93D'),
        (0x00000005, 'loc_1B9BE'),
        (-1, 'loc_1BB69'),
    )

    def _loc_1B765(): pass

    label('loc_1B765')

    OP_70(0x01, 0xFFFF, 0xFF)
    OP_70(0x0C, 0xFFFF, 0xFF, 0x01)
    OP_70(0x0C, 0xFFFF, 0x00, 0x01)
    OP_70(0x0C, 0xFFFF, 0x01, 0x01)
    AddItem(0x03, 0x0000, 0)
    OP_67(0x03, 0xFFFF)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:全アイテムを消去しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1B7DF(): pass

    label('loc_1B7DF')

    CraftCtrl(0x03, 0xFFFF)
    CraftCtrl(0x07, 0xFFFF)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:全クラフト、オーダーを消去しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1B84D(): pass

    label('loc_1B84D')

    Call(ScriptId.System2, 'FC_Equip_Lock')
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:キャラごとの装備禁止を設定しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1B8C4(): pass

    label('loc_1B8C4')

    Call(ScriptId.System2, 'FC_Equip_UnLock')
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:キャラごとの装備禁止を解除しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1B93D(): pass

    label('loc_1B93D')

    Call(ScriptId.System2, 'FC_Set_Mquartz_Lv')
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:マスタークオーツのレベルを設定しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1B9BE(): pass

    label('loc_1B9BE')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['米莉亞姆'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['奧蕾莉亞將軍'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['奧利維特皇子'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['克洛提德'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['遊擊士托瓦爾'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['緋之羅賽莉亞'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['喬治'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['亞爾賽德子爵'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['剛毅艾奈絲'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['魔弓恩奈雅'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['陷阱師傑諾'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['破壞獸雷歐尼達斯'], 0x00000001)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x00000001)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:全員のCAMP_JOINフラグを設定しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1BB77')

    def _loc_1BB69(): pass

    label('loc_1BB69')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BB77')

    def _loc_1BB77(): pass

    label('loc_1BB77')

    Jump('loc_1B611')

    def _loc_1BB7C(): pass

    label('loc_1BB7C')

    Return()

# id: 0x002C offset: 0x1BB80
@scena.Code('FC_AVoiceFlagAllClear')
def FC_AVoiceFlagAllClear():
    OP_71(0x01, 0x1200, 0x12D5)

    Return()

# id: 0x002D offset: 0x1BB88
@scena.Code('FC_PartyMemberEdit')
def FC_PartyMemberEdit():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1BB91(): pass

    label('loc_1BB91')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BF10',
    )

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 65535, 200, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            'ここで人数を変更してもすぐには反映されません。\n',
            '人数設定後にパーティの入れ替え(clear_party)を\n',
            '行うと反映されます。',
            TxtCtl.Enter,
        ),
    )

    MenuCreate(2, 0, 40.0, 0)

    If(
        (
            (Expr.PushVar, 0x2B),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BCA4',
    )

    MenuAddItem(2, '★DEBUG:パーティ人数[４]', 0x00000000)

    Jump('loc_1BCCF')

    def _loc_1BCA4(): pass

    label('loc_1BCA4')

    MenuAddItem(2, '　　　　パーティ人数[４]', 0x00000000)

    def _loc_1BCCF(): pass

    label('loc_1BCCF')

    If(
        (
            (Expr.PushVar, 0x2B),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD0A',
    )

    MenuAddItem(2, '★DEBUG:パーティ人数[５]', 0x00000001)

    Jump('loc_1BD35')

    def _loc_1BD0A(): pass

    label('loc_1BD0A')

    MenuAddItem(2, '　　　　パーティ人数[５]', 0x00000001)

    def _loc_1BD35(): pass

    label('loc_1BD35')

    If(
        (
            (Expr.PushVar, 0x2B),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD70',
    )

    MenuAddItem(2, '★DEBUG:パーティ人数[６]', 0x00000002)

    Jump('loc_1BD9B')

    def _loc_1BD70(): pass

    label('loc_1BD70')

    MenuAddItem(2, '　　　　パーティ人数[６]', 0x00000002)

    def _loc_1BD9B(): pass

    label('loc_1BD9B')

    If(
        (
            (Expr.PushVar, 0x2B),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BDD6',
    )

    MenuAddItem(2, '★DEBUG:パーティ人数[７]', 0x00000003)

    Jump('loc_1BE01')

    def _loc_1BDD6(): pass

    label('loc_1BDD6')

    MenuAddItem(2, '　　　　パーティ人数[７]', 0x00000003)

    def _loc_1BE01(): pass

    label('loc_1BE01')

    If(
        (
            (Expr.PushVar, 0x2B),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BE3C',
    )

    MenuAddItem(2, '★DEBUG:パーティ人数[８]', 0x00000004)

    Jump('loc_1BE67')

    def _loc_1BE3C(): pass

    label('loc_1BE3C')

    MenuAddItem(2, '　　　　パーティ人数[８]', 0x00000004)

    def _loc_1BE67(): pass

    label('loc_1BE67')

    MenuSetPos(2, 0x01, 65535, 65535, 0x00)
    MenuShow(2, 0xF8)
    MenuCmd(0x03, 2)
    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x00000000, 'loc_1BEB7'),
        (0x00000001, 'loc_1BEC5'),
        (0x00000002, 'loc_1BED3'),
        (0x00000003, 'loc_1BEE1'),
        (0x00000004, 'loc_1BEEF'),
        (-1, 'loc_1BEFD'),
    )

    def _loc_1BEB7(): pass

    label('loc_1BEB7')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x4),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BEC5(): pass

    label('loc_1BEC5')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x5),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BED3(): pass

    label('loc_1BED3')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x6),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BEE1(): pass

    label('loc_1BEE1')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BEEF(): pass

    label('loc_1BEEF')

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0x8),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BEFD(): pass

    label('loc_1BEFD')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1BF0B')

    def _loc_1BF0B(): pass

    label('loc_1BF0B')

    Jump('loc_1BB91')

    def _loc_1BF10(): pass

    label('loc_1BF10')

    Return()

# id: 0x002E offset: 0x1BF14
@scena.Code('FC_SystemSaveFlagEdit')
def FC_SystemSaveFlagEdit():
    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1BF1D(): pass

    label('loc_1BF1D')

    If(
        (
            (Expr.PushVar, 0xF8),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CE92',
    )

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_23(0x05, 65535, 100, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            'システムセーブフラグを確認／編集できます。',
            TxtCtl.Enter,
        ),
    )

    MenuCreate(2, 0, 40.0, 0)
    MenuCreate(2, 32, 24.0, 99)

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0002)"),
            Expr.Return,
        ),
        'loc_1BFD5',
    )

    MenuAddItem(2, '■ノーマルエンド見た', 0x0000000A)

    Jump('loc_1BFFB')

    def _loc_1BFD5(): pass

    label('loc_1BFD5')

    MenuAddItem(2, '□ノーマルエンド見た', 0x0000000A)

    def _loc_1BFFB(): pass

    label('loc_1BFFB')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0003)"),
            Expr.Return,
        ),
        'loc_1C031',
    )

    MenuAddItem(2, '■トゥルーエンド見た', 0x0000000B)

    Jump('loc_1C057')

    def _loc_1C031(): pass

    label('loc_1C031')

    MenuAddItem(2, '□トゥルーエンド見た', 0x0000000B)

    def _loc_1C057(): pass

    label('loc_1C057')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0004)"),
            Expr.Return,
        ),
        'loc_1C09C',
    )

    MenuAddItem(2, '■最終絆イベントを見た・アリサ', 0x00000028)

    Jump('loc_1C0D1')

    def _loc_1C09C(): pass

    label('loc_1C09C')

    MenuAddItem(2, '□最終絆イベントを見た・アリサ', 0x00000028)

    def _loc_1C0D1(): pass

    label('loc_1C0D1')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0005)"),
            Expr.Return,
        ),
        'loc_1C116',
    )

    MenuAddItem(2, '■最終絆イベントを見た・ラウラ', 0x00000029)

    Jump('loc_1C14B')

    def _loc_1C116(): pass

    label('loc_1C116')

    MenuAddItem(2, '□最終絆イベントを見た・ラウラ', 0x00000029)

    def _loc_1C14B(): pass

    label('loc_1C14B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0006)"),
            Expr.Return,
        ),
        'loc_1C18D',
    )

    MenuAddItem(2, '■最終絆イベントを見た・エマ', 0x0000002A)

    Jump('loc_1C1BF')

    def _loc_1C18D(): pass

    label('loc_1C18D')

    MenuAddItem(2, '□最終絆イベントを見た・エマ', 0x0000002A)

    def _loc_1C1BF(): pass

    label('loc_1C1BF')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0007)"),
            Expr.Return,
        ),
        'loc_1C204',
    )

    MenuAddItem(2, '■最終絆イベントを見た・フィー', 0x0000002B)

    Jump('loc_1C239')

    def _loc_1C204(): pass

    label('loc_1C204')

    MenuAddItem(2, '□最終絆イベントを見た・フィー', 0x0000002B)

    def _loc_1C239(): pass

    label('loc_1C239')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0008)"),
            Expr.Return,
        ),
        'loc_1C27B',
    )

    MenuAddItem(2, '■最終絆イベントを見た・サラ', 0x0000002C)

    Jump('loc_1C2AD')

    def _loc_1C27B(): pass

    label('loc_1C27B')

    MenuAddItem(2, '□最終絆イベントを見た・サラ', 0x0000002C)

    def _loc_1C2AD(): pass

    label('loc_1C2AD')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0009)"),
            Expr.Return,
        ),
        'loc_1C2EF',
    )

    MenuAddItem(2, '■最終絆イベントを見た・トワ', 0x0000002D)

    Jump('loc_1C321')

    def _loc_1C2EF(): pass

    label('loc_1C2EF')

    MenuAddItem(2, '□最終絆イベントを見た・トワ', 0x0000002D)

    def _loc_1C321(): pass

    label('loc_1C321')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000A)"),
            Expr.Return,
        ),
        'loc_1C366',
    )

    MenuAddItem(2, '■最終絆イベントを見た・ユウナ', 0x0000002E)

    Jump('loc_1C39B')

    def _loc_1C366(): pass

    label('loc_1C366')

    MenuAddItem(2, '□最終絆イベントを見た・ユウナ', 0x0000002E)

    def _loc_1C39B(): pass

    label('loc_1C39B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000B)"),
            Expr.Return,
        ),
        'loc_1C3E6',
    )

    MenuAddItem(2, '■最終絆イベントを見た・アルティナ', 0x0000002F)

    Jump('loc_1C421')

    def _loc_1C3E6(): pass

    label('loc_1C3E6')

    MenuAddItem(2, '□最終絆イベントを見た・アルティナ', 0x0000002F)

    def _loc_1C421(): pass

    label('loc_1C421')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000C)"),
            Expr.Return,
        ),
        'loc_1C466',
    )

    MenuAddItem(2, '■最終絆イベントを見た・ミュゼ', 0x00000030)

    Jump('loc_1C49B')

    def _loc_1C466(): pass

    label('loc_1C466')

    MenuAddItem(2, '□最終絆イベントを見た・ミュゼ', 0x00000030)

    def _loc_1C49B(): pass

    label('loc_1C49B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000D)"),
            Expr.Return,
        ),
        'loc_1C4E6',
    )

    MenuAddItem(2, '■最終絆イベントを見た・アルフィン', 0x00000031)

    Jump('loc_1C521')

    def _loc_1C4E6(): pass

    label('loc_1C4E6')

    MenuAddItem(2, '□最終絆イベントを見た・アルフィン', 0x00000031)

    def _loc_1C521(): pass

    label('loc_1C521')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000E)"),
            Expr.Return,
        ),
        'loc_1C566',
    )

    MenuAddItem(2, '■最終絆イベントを見た・エリゼ', 0x00000032)

    Jump('loc_1C59B')

    def _loc_1C566(): pass

    label('loc_1C566')

    MenuAddItem(2, '□最終絆イベントを見た・エリゼ', 0x00000032)

    def _loc_1C59B(): pass

    label('loc_1C59B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0010)"),
            Expr.Return,
        ),
        'loc_1C5E0',
    )

    MenuAddItem(2, '■エンディングを迎えた・アリサ', 0x00000014)

    Jump('loc_1C615')

    def _loc_1C5E0(): pass

    label('loc_1C5E0')

    MenuAddItem(2, '□エンディングを迎えた・アリサ', 0x00000014)

    def _loc_1C615(): pass

    label('loc_1C615')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0011)"),
            Expr.Return,
        ),
        'loc_1C65A',
    )

    MenuAddItem(2, '■エンディングを迎えた・ラウラ', 0x00000015)

    Jump('loc_1C68F')

    def _loc_1C65A(): pass

    label('loc_1C65A')

    MenuAddItem(2, '□エンディングを迎えた・ラウラ', 0x00000015)

    def _loc_1C68F(): pass

    label('loc_1C68F')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0012)"),
            Expr.Return,
        ),
        'loc_1C6D1',
    )

    MenuAddItem(2, '■エンディングを迎えた・エマ', 0x00000016)

    Jump('loc_1C703')

    def _loc_1C6D1(): pass

    label('loc_1C6D1')

    MenuAddItem(2, '□エンディングを迎えた・エマ', 0x00000016)

    def _loc_1C703(): pass

    label('loc_1C703')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0013)"),
            Expr.Return,
        ),
        'loc_1C748',
    )

    MenuAddItem(2, '■エンディングを迎えた・フィー', 0x00000017)

    Jump('loc_1C77D')

    def _loc_1C748(): pass

    label('loc_1C748')

    MenuAddItem(2, '□エンディングを迎えた・フィー', 0x00000017)

    def _loc_1C77D(): pass

    label('loc_1C77D')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0014)"),
            Expr.Return,
        ),
        'loc_1C7BF',
    )

    MenuAddItem(2, '■エンディングを迎えた・サラ', 0x00000018)

    Jump('loc_1C7F1')

    def _loc_1C7BF(): pass

    label('loc_1C7BF')

    MenuAddItem(2, '□エンディングを迎えた・サラ', 0x00000018)

    def _loc_1C7F1(): pass

    label('loc_1C7F1')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0015)"),
            Expr.Return,
        ),
        'loc_1C833',
    )

    MenuAddItem(2, '■エンディングを迎えた・トワ', 0x00000019)

    Jump('loc_1C865')

    def _loc_1C833(): pass

    label('loc_1C833')

    MenuAddItem(2, '□エンディングを迎えた・トワ', 0x00000019)

    def _loc_1C865(): pass

    label('loc_1C865')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0016)"),
            Expr.Return,
        ),
        'loc_1C8AA',
    )

    MenuAddItem(2, '■エンディングを迎えた・ユウナ', 0x0000001A)

    Jump('loc_1C8DF')

    def _loc_1C8AA(): pass

    label('loc_1C8AA')

    MenuAddItem(2, '□エンディングを迎えた・ユウナ', 0x0000001A)

    def _loc_1C8DF(): pass

    label('loc_1C8DF')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0017)"),
            Expr.Return,
        ),
        'loc_1C92A',
    )

    MenuAddItem(2, '■エンディングを迎えた・アルティナ', 0x0000001B)

    Jump('loc_1C965')

    def _loc_1C92A(): pass

    label('loc_1C92A')

    MenuAddItem(2, '□エンディングを迎えた・アルティナ', 0x0000001B)

    def _loc_1C965(): pass

    label('loc_1C965')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0018)"),
            Expr.Return,
        ),
        'loc_1C9AA',
    )

    MenuAddItem(2, '■エンディングを迎えた・ミュゼ', 0x0000001C)

    Jump('loc_1C9DF')

    def _loc_1C9AA(): pass

    label('loc_1C9AA')

    MenuAddItem(2, '□エンディングを迎えた・ミュゼ', 0x0000001C)

    def _loc_1C9DF(): pass

    label('loc_1C9DF')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0019)"),
            Expr.Return,
        ),
        'loc_1CA2A',
    )

    MenuAddItem(2, '■エンディングを迎えた・アルフィン', 0x0000001D)

    Jump('loc_1CA65')

    def _loc_1CA2A(): pass

    label('loc_1CA2A')

    MenuAddItem(2, '□エンディングを迎えた・アルフィン', 0x0000001D)

    def _loc_1CA65(): pass

    label('loc_1CA65')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x001A)"),
            Expr.Return,
        ),
        'loc_1CAAA',
    )

    MenuAddItem(2, '■エンディングを迎えた・エリゼ', 0x0000001E)

    Jump('loc_1CADF')

    def _loc_1CAAA(): pass

    label('loc_1CAAA')

    MenuAddItem(2, '□エンディングを迎えた・エリゼ', 0x0000001E)

    def _loc_1CADF(): pass

    label('loc_1CADF')

    MenuSetPos(2, 0x01, 65535, 65535, 0x00)
    MenuShow(2, 0xF8)
    MenuCmd(0x03, 2)
    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Switch(
        (
            (Expr.PushVar, 0xF8),
            Expr.Return,
        ),
        (0x0000000A, 'loc_1CBC7'),
        (0x0000000B, 'loc_1CBE4'),
        (0x00000014, 'loc_1CC01'),
        (0x00000015, 'loc_1CC1E'),
        (0x00000016, 'loc_1CC3B'),
        (0x00000017, 'loc_1CC58'),
        (0x00000018, 'loc_1CC75'),
        (0x00000019, 'loc_1CC92'),
        (0x0000001A, 'loc_1CCAF'),
        (0x0000001B, 'loc_1CCCC'),
        (0x0000001C, 'loc_1CCE9'),
        (0x0000001D, 'loc_1CD06'),
        (0x0000001E, 'loc_1CD23'),
        (0x00000028, 'loc_1CD40'),
        (0x00000029, 'loc_1CD5D'),
        (0x0000002A, 'loc_1CD7A'),
        (0x0000002B, 'loc_1CD97'),
        (0x0000002C, 'loc_1CDB4'),
        (0x0000002D, 'loc_1CDD1'),
        (0x0000002E, 'loc_1CDEE'),
        (0x0000002F, 'loc_1CE0B'),
        (0x00000030, 'loc_1CE28'),
        (0x00000031, 'loc_1CE45'),
        (0x00000032, 'loc_1CE62'),
        (-1, 'loc_1CE7F'),
    )

    def _loc_1CBC7(): pass

    label('loc_1CBC7')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0002)"),
            Expr.Return,
        ),
        'loc_1CBDB',
    )

    OP_19(0x01, 0x0002)

    Jump('loc_1CBDF')

    def _loc_1CBDB(): pass

    label('loc_1CBDB')

    OP_19(0x00, 0x0002)

    def _loc_1CBDF(): pass

    label('loc_1CBDF')

    Jump('loc_1CE8D')

    def _loc_1CBE4(): pass

    label('loc_1CBE4')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0003)"),
            Expr.Return,
        ),
        'loc_1CBF8',
    )

    OP_19(0x01, 0x0003)

    Jump('loc_1CBFC')

    def _loc_1CBF8(): pass

    label('loc_1CBF8')

    OP_19(0x00, 0x0003)

    def _loc_1CBFC(): pass

    label('loc_1CBFC')

    Jump('loc_1CE8D')

    def _loc_1CC01(): pass

    label('loc_1CC01')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0010)"),
            Expr.Return,
        ),
        'loc_1CC15',
    )

    OP_19(0x01, 0x0010)

    Jump('loc_1CC19')

    def _loc_1CC15(): pass

    label('loc_1CC15')

    OP_19(0x00, 0x0010)

    def _loc_1CC19(): pass

    label('loc_1CC19')

    Jump('loc_1CE8D')

    def _loc_1CC1E(): pass

    label('loc_1CC1E')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0011)"),
            Expr.Return,
        ),
        'loc_1CC32',
    )

    OP_19(0x01, 0x0011)

    Jump('loc_1CC36')

    def _loc_1CC32(): pass

    label('loc_1CC32')

    OP_19(0x00, 0x0011)

    def _loc_1CC36(): pass

    label('loc_1CC36')

    Jump('loc_1CE8D')

    def _loc_1CC3B(): pass

    label('loc_1CC3B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0012)"),
            Expr.Return,
        ),
        'loc_1CC4F',
    )

    OP_19(0x01, 0x0012)

    Jump('loc_1CC53')

    def _loc_1CC4F(): pass

    label('loc_1CC4F')

    OP_19(0x00, 0x0012)

    def _loc_1CC53(): pass

    label('loc_1CC53')

    Jump('loc_1CE8D')

    def _loc_1CC58(): pass

    label('loc_1CC58')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0013)"),
            Expr.Return,
        ),
        'loc_1CC6C',
    )

    OP_19(0x01, 0x0013)

    Jump('loc_1CC70')

    def _loc_1CC6C(): pass

    label('loc_1CC6C')

    OP_19(0x00, 0x0013)

    def _loc_1CC70(): pass

    label('loc_1CC70')

    Jump('loc_1CE8D')

    def _loc_1CC75(): pass

    label('loc_1CC75')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0014)"),
            Expr.Return,
        ),
        'loc_1CC89',
    )

    OP_19(0x01, 0x0014)

    Jump('loc_1CC8D')

    def _loc_1CC89(): pass

    label('loc_1CC89')

    OP_19(0x00, 0x0014)

    def _loc_1CC8D(): pass

    label('loc_1CC8D')

    Jump('loc_1CE8D')

    def _loc_1CC92(): pass

    label('loc_1CC92')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0015)"),
            Expr.Return,
        ),
        'loc_1CCA6',
    )

    OP_19(0x01, 0x0015)

    Jump('loc_1CCAA')

    def _loc_1CCA6(): pass

    label('loc_1CCA6')

    OP_19(0x00, 0x0015)

    def _loc_1CCAA(): pass

    label('loc_1CCAA')

    Jump('loc_1CE8D')

    def _loc_1CCAF(): pass

    label('loc_1CCAF')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0016)"),
            Expr.Return,
        ),
        'loc_1CCC3',
    )

    OP_19(0x01, 0x0016)

    Jump('loc_1CCC7')

    def _loc_1CCC3(): pass

    label('loc_1CCC3')

    OP_19(0x00, 0x0016)

    def _loc_1CCC7(): pass

    label('loc_1CCC7')

    Jump('loc_1CE8D')

    def _loc_1CCCC(): pass

    label('loc_1CCCC')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0017)"),
            Expr.Return,
        ),
        'loc_1CCE0',
    )

    OP_19(0x01, 0x0017)

    Jump('loc_1CCE4')

    def _loc_1CCE0(): pass

    label('loc_1CCE0')

    OP_19(0x00, 0x0017)

    def _loc_1CCE4(): pass

    label('loc_1CCE4')

    Jump('loc_1CE8D')

    def _loc_1CCE9(): pass

    label('loc_1CCE9')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0018)"),
            Expr.Return,
        ),
        'loc_1CCFD',
    )

    OP_19(0x01, 0x0018)

    Jump('loc_1CD01')

    def _loc_1CCFD(): pass

    label('loc_1CCFD')

    OP_19(0x00, 0x0018)

    def _loc_1CD01(): pass

    label('loc_1CD01')

    Jump('loc_1CE8D')

    def _loc_1CD06(): pass

    label('loc_1CD06')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0019)"),
            Expr.Return,
        ),
        'loc_1CD1A',
    )

    OP_19(0x01, 0x0019)

    Jump('loc_1CD1E')

    def _loc_1CD1A(): pass

    label('loc_1CD1A')

    OP_19(0x00, 0x0019)

    def _loc_1CD1E(): pass

    label('loc_1CD1E')

    Jump('loc_1CE8D')

    def _loc_1CD23(): pass

    label('loc_1CD23')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x001A)"),
            Expr.Return,
        ),
        'loc_1CD37',
    )

    OP_19(0x01, 0x001A)

    Jump('loc_1CD3B')

    def _loc_1CD37(): pass

    label('loc_1CD37')

    OP_19(0x00, 0x001A)

    def _loc_1CD3B(): pass

    label('loc_1CD3B')

    Jump('loc_1CE8D')

    def _loc_1CD40(): pass

    label('loc_1CD40')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0004)"),
            Expr.Return,
        ),
        'loc_1CD54',
    )

    OP_19(0x01, 0x0004)

    Jump('loc_1CD58')

    def _loc_1CD54(): pass

    label('loc_1CD54')

    OP_19(0x00, 0x0004)

    def _loc_1CD58(): pass

    label('loc_1CD58')

    Jump('loc_1CE8D')

    def _loc_1CD5D(): pass

    label('loc_1CD5D')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0005)"),
            Expr.Return,
        ),
        'loc_1CD71',
    )

    OP_19(0x01, 0x0005)

    Jump('loc_1CD75')

    def _loc_1CD71(): pass

    label('loc_1CD71')

    OP_19(0x00, 0x0005)

    def _loc_1CD75(): pass

    label('loc_1CD75')

    Jump('loc_1CE8D')

    def _loc_1CD7A(): pass

    label('loc_1CD7A')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0006)"),
            Expr.Return,
        ),
        'loc_1CD8E',
    )

    OP_19(0x01, 0x0006)

    Jump('loc_1CD92')

    def _loc_1CD8E(): pass

    label('loc_1CD8E')

    OP_19(0x00, 0x0006)

    def _loc_1CD92(): pass

    label('loc_1CD92')

    Jump('loc_1CE8D')

    def _loc_1CD97(): pass

    label('loc_1CD97')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0007)"),
            Expr.Return,
        ),
        'loc_1CDAB',
    )

    OP_19(0x01, 0x0007)

    Jump('loc_1CDAF')

    def _loc_1CDAB(): pass

    label('loc_1CDAB')

    OP_19(0x00, 0x0007)

    def _loc_1CDAF(): pass

    label('loc_1CDAF')

    Jump('loc_1CE8D')

    def _loc_1CDB4(): pass

    label('loc_1CDB4')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0008)"),
            Expr.Return,
        ),
        'loc_1CDC8',
    )

    OP_19(0x01, 0x0008)

    Jump('loc_1CDCC')

    def _loc_1CDC8(): pass

    label('loc_1CDC8')

    OP_19(0x00, 0x0008)

    def _loc_1CDCC(): pass

    label('loc_1CDCC')

    Jump('loc_1CE8D')

    def _loc_1CDD1(): pass

    label('loc_1CDD1')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x0009)"),
            Expr.Return,
        ),
        'loc_1CDE5',
    )

    OP_19(0x01, 0x0009)

    Jump('loc_1CDE9')

    def _loc_1CDE5(): pass

    label('loc_1CDE5')

    OP_19(0x00, 0x0009)

    def _loc_1CDE9(): pass

    label('loc_1CDE9')

    Jump('loc_1CE8D')

    def _loc_1CDEE(): pass

    label('loc_1CDEE')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000A)"),
            Expr.Return,
        ),
        'loc_1CE02',
    )

    OP_19(0x01, 0x000A)

    Jump('loc_1CE06')

    def _loc_1CE02(): pass

    label('loc_1CE02')

    OP_19(0x00, 0x000A)

    def _loc_1CE06(): pass

    label('loc_1CE06')

    Jump('loc_1CE8D')

    def _loc_1CE0B(): pass

    label('loc_1CE0B')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000B)"),
            Expr.Return,
        ),
        'loc_1CE1F',
    )

    OP_19(0x01, 0x000B)

    Jump('loc_1CE23')

    def _loc_1CE1F(): pass

    label('loc_1CE1F')

    OP_19(0x00, 0x000B)

    def _loc_1CE23(): pass

    label('loc_1CE23')

    Jump('loc_1CE8D')

    def _loc_1CE28(): pass

    label('loc_1CE28')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000C)"),
            Expr.Return,
        ),
        'loc_1CE3C',
    )

    OP_19(0x01, 0x000C)

    Jump('loc_1CE40')

    def _loc_1CE3C(): pass

    label('loc_1CE3C')

    OP_19(0x00, 0x000C)

    def _loc_1CE40(): pass

    label('loc_1CE40')

    Jump('loc_1CE8D')

    def _loc_1CE45(): pass

    label('loc_1CE45')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000D)"),
            Expr.Return,
        ),
        'loc_1CE59',
    )

    OP_19(0x01, 0x000D)

    Jump('loc_1CE5D')

    def _loc_1CE59(): pass

    label('loc_1CE59')

    OP_19(0x00, 0x000D)

    def _loc_1CE5D(): pass

    label('loc_1CE5D')

    Jump('loc_1CE8D')

    def _loc_1CE62(): pass

    label('loc_1CE62')

    If(
        (
            (Expr.Eval, "OP_19(0x02, 0x000E)"),
            Expr.Return,
        ),
        'loc_1CE76',
    )

    OP_19(0x01, 0x000E)

    Jump('loc_1CE7A')

    def _loc_1CE76(): pass

    label('loc_1CE76')

    OP_19(0x00, 0x000E)

    def _loc_1CE7A(): pass

    label('loc_1CE7A')

    Jump('loc_1CE8D')

    def _loc_1CE7F(): pass

    label('loc_1CE7F')

    ExecExpressionWithVar(
        0xF8,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1CE8D')

    def _loc_1CE8D(): pass

    label('loc_1CE8D')

    Jump('loc_1BF1D')

    def _loc_1CE92(): pass

    label('loc_1CE92')

    Return()

# id: 0x002F offset: 0x1CE94
@scena.Code('FC_SetCostume')
def FC_SetCostume():
    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_1CE9D(): pass

    label('loc_1CE9D')

    If(
        (
            (Expr.PushVar, 0xF7),
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D61D',
    )

    MenuCreate(1, 24, 24.0, 99)
    MenuAddItem(1, 'コスチュームフラグ全員セット', 0x00000000)
    MenuAddItem(1, 'コスチュームフラグ全員クリア', 0x00000001)
    MenuAddItem(1, 'コスチューム系アイテム大量入手', 0x00000002)
    MenuSetPos(1, 0x01, 65535, 65535, 0x01)
    MenuShow(1, 0xF7)

    Switch(
        (
            (Expr.PushVar, 0xF7),
            Expr.Return,
        ),
        (0x00000000, 'loc_1CF7F'),
        (0x00000001, 'loc_1D0EC'),
        (0x00000002, 'loc_1D259'),
        (-1, 'loc_1D60A'),
    )

    def _loc_1CF7F(): pass

    label('loc_1CF7F')

    MenuChrFlagCmd(0x00, ChrTable['黎恩'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['亞莉莎'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['艾略特'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['勞拉'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['馬奇亞斯'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['艾瑪'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['尤西斯'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['菲'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['蓋烏斯'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['米莉亞姆'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['尤娜'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['庫爾特'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['亞爾緹娜'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['繆潔'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['亞修'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['莎拉'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['奧蕾莉亞將軍'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['阿加特'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['安潔莉卡'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['奧利維特皇子'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['提妲'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['緹歐'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['雪倫'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['克洛'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['克洛提德'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['遊擊士托瓦爾'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['艾絲蒂爾'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['約修亞'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['玲'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['羅伊德'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['艾莉'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['蘭迪'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['緋之羅賽莉亞'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['喬治'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['亞爾賽德子爵'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['杜巴莉'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['剛毅艾奈絲'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['魔弓恩奈雅'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['陷阱師傑諾'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['破壞獸雷歐尼達斯'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['瑟蕾奴'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['托娃'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['愛麗榭'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['艾爾芬皇女'], 0x02000000)
    MenuChrFlagCmd(0x00, ChrTable['琪雅'], 0x02000000)

    Jump('loc_1D618')

    def _loc_1D0EC(): pass

    label('loc_1D0EC')

    MenuChrFlagCmd(0x01, ChrTable['黎恩'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['亞莉莎'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['艾略特'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['勞拉'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['馬奇亞斯'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['艾瑪'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['尤西斯'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['菲'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['蓋烏斯'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['米莉亞姆'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['尤娜'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['庫爾特'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['亞爾緹娜'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['繆潔'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['亞修'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['莎拉'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['奧蕾莉亞將軍'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['阿加特'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['安潔莉卡'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['奧利維特皇子'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['提妲'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['緹歐'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['雪倫'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['克洛'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['克洛提德'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['遊擊士托瓦爾'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['艾絲蒂爾'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['約修亞'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['玲'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['羅伊德'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['艾莉'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['蘭迪'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['緋之羅賽莉亞'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['喬治'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['亞爾賽德子爵'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['杜巴莉'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['剛毅艾奈絲'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['魔弓恩奈雅'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['陷阱師傑諾'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['破壞獸雷歐尼達斯'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['瑟蕾奴'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['托娃'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['愛麗榭'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['艾爾芬皇女'], 0x02000000)
    MenuChrFlagCmd(0x01, ChrTable['琪雅'], 0x02000000)

    Jump('loc_1D618')

    def _loc_1D259(): pass

    label('loc_1D259')

    AddItem(0x0F, 0x00C1, 5)
    AddItem(0x00, 0x03B6, 1)
    AddItem(0x00, 0x03B7, 1)
    AddItem(0x00, 0x03B8, 1)
    AddItem(0x00, 0x03B9, 1)
    AddItem(0x00, 0x03BA, 1)
    AddItem(0x00, 0x03BB, 1)
    AddItem(0x00, 0x03BC, 1)
    AddItem(0x00, 0x03BD, 1)
    AddItem(0x00, 0x03BE, 1)
    AddItem(0x00, 0x03BF, 1)
    AddItem(0x00, 0x03C0, 1)
    AddItem(0x00, 0x03C1, 1)
    AddItem(0x00, 0x03C2, 1)
    AddItem(0x00, 0x03C3, 1)
    AddItem(0x00, 0x03C4, 1)
    AddItem(0x00, 0x03C5, 1)
    AddItem(0x00, 0x03C6, 1)
    AddItem(0x00, 0x03C7, 1)
    AddItem(0x00, 0x03C8, 1)
    AddItem(0x00, 0x03C9, 1)
    AddItem(0x00, 0x03CA, 1)
    AddItem(0x00, 0x03CB, 1)
    AddItem(0x00, 0x03CC, 1)
    AddItem(0x00, 0x0424, 1)
    AddItem(0x00, 0x0425, 1)
    AddItem(0x00, 0x0426, 1)
    AddItem(0x00, 0x0427, 1)
    AddItem(0x00, 0x0428, 1)
    AddItem(0x00, 0x0429, 1)
    AddItem(0x00, 0x042A, 1)
    AddItem(0x00, 0x042B, 1)
    AddItem(0x00, 0x042C, 1)
    AddItem(0x00, 0x042D, 1)
    AddItem(0x00, 0x042E, 1)
    AddItem(0x00, 0x042F, 1)
    AddItem(0x00, 0x0430, 1)
    AddItem(0x00, 0x0431, 1)
    AddItem(0x00, 0x0432, 1)
    AddItem(0x00, 0x0433, 1)
    AddItem(0x00, 0x0434, 1)
    AddItem(0x00, 0x0435, 1)
    AddItem(0x00, 0x0436, 1)
    AddItem(0x00, 0x0437, 1)
    AddItem(0x00, 0x0438, 1)
    AddItem(0x00, 0x0439, 1)
    AddItem(0x00, 0x043A, 1)
    AddItem(0x00, 0x043B, 1)
    AddItem(0x00, 0x043C, 1)
    AddItem(0x00, 0x043D, 1)
    AddItem(0x00, 0x043E, 1)
    AddItem(0x00, 0x043F, 1)
    AddItem(0x00, 0x0440, 1)
    AddItem(0x00, 0x0441, 1)
    AddItem(0x00, 0x0442, 1)
    AddItem(0x00, 0x0443, 1)
    AddItem(0x00, 0x0444, 1)
    AddItem(0x00, 0x0445, 1)
    AddItem(0x00, 0x0446, 1)
    AddItem(0x00, 0x0447, 1)
    AddItem(0x00, 0x0448, 1)
    AddItem(0x00, 0x0449, 1)
    AddItem(0x00, 0x044A, 1)
    AddItem(0x00, 0x044B, 1)
    AddItem(0x00, 0x044C, 1)
    AddItem(0x00, 0x044D, 1)
    AddItem(0x00, 0x044E, 1)
    AddItem(0x00, 0x044F, 1)
    AddItem(0x00, 0x0450, 1)
    AddItem(0x00, 0x0451, 1)
    AddItem(0x00, 0x0452, 1)
    AddItem(0x00, 0x0453, 1)
    AddItem(0x00, 0x0454, 1)
    AddItem(0x00, 0x0455, 1)
    AddItem(0x00, 0x0456, 1)
    AddItem(0x00, 0x0457, 1)
    AddItem(0x00, 0x0458, 1)
    AddItem(0x00, 0x0459, 1)
    AddItem(0x00, 0x045A, 1)
    AddItem(0x00, 0x045B, 1)
    AddItem(0x00, 0x045C, 1)
    AddItem(0x00, 0x045D, 1)
    AddItem(0x00, 0x045E, 1)
    AddItem(0x00, 0x045F, 1)
    AddItem(0x00, 0x0460, 1)
    AddItem(0x00, 0x0461, 1)
    AddItem(0x00, 0x0462, 1)
    AddItem(0x00, 0x0463, 1)
    AddItem(0x00, 0x0464, 1)
    AddItem(0x00, 0x0465, 1)
    AddItem(0x00, 0x0466, 1)
    AddItem(0x00, 0x0467, 1)
    AddItem(0x00, 0x0468, 1)
    AddItem(0x00, 0x0469, 1)
    AddItem(0x00, 0x046A, 1)
    AddItem(0x00, 0x046B, 1)
    AddItem(0x00, 0x046C, 1)
    AddItem(0x00, 0x046D, 1)
    AddItem(0x00, 0x046E, 1)
    AddItem(0x00, 0x046F, 1)
    AddItem(0x00, 0x0470, 1)
    AddItem(0x00, 0x0471, 1)
    AddItem(0x00, 0x0472, 1)
    AddItem(0x00, 0x0473, 1)
    AddItem(0x00, 0x0474, 1)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Talk(
        0xFFFF,
        (
            0xB,
            TxtCtl.ShowAll,
            '★DEBUG:コスチューム系アイテムを入手しました。',
            TxtCtl.Enter,
        ),
    )

    WaitForMsg()

    OP_25(0x00)
    OP_25(0x01)
    OP_23(0x05, 65535, 65535, 65535, 65535, 0x00)

    Jump('loc_1D618')

    def _loc_1D60A(): pass

    label('loc_1D60A')

    ExecExpressionWithVar(
        0xF7,
        (
            (Expr.PushLong, 0xFFFFFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_1D618')

    def _loc_1D618(): pass

    label('loc_1D618')

    Jump('loc_1CE9D')

    def _loc_1D61D(): pass

    label('loc_1D61D')

    Return()

# id: 0x0030 offset: 0x1D620
@scena.AnimeClips('_EV_Party_Set')
def _EV_Party_Set():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00002F49,
            name   = '',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
