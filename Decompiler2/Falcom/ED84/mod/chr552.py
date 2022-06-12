import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED84.Parser.scena_writer_helper import *
try:
    import chr552_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('chr552.dat')

# id: 0x0000 offset: 0xDA8
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'TURN_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR032_DF1',
            symbol     = 'TURN_RIGHT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR032_BT1',
            symbol     = 'BTL_CRAFT02_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'WAIT1_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'BTL_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_DF1',
            symbol     = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKIRE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_KATATE_R',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_KATATE_L',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ENZETU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FALLa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_FUAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GOUREI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_2_sc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HAKUSHU_3_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HIRUMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HISOHISOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_INORI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_JUMP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_JUMPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KATATE_DAKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_LAND',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MAEKAGAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MEGANE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NAISHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_NORIDASIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_GYU_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_AWASE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UDEGUMI_st',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WARAI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YAREYARE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YARUKI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX00_EV',
            symbol     = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev00070',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev00070a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev03035',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev03035a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev50525',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'ev50525a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'DROPCLOTHES_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'DROPCLOTHES_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR032_EV',
            symbol     = 'DROPCLOTHES_03',
        ),
    )

# id: 0x0001 offset: 0x7BA8
@scena.Code('Init')
def Init():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000100)
    Call(ScriptId.Current, 'OnChangeAttach')
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0002 offset: 0x7BD0
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0003 offset: 0x7BF8
@scena.Code('OnChangeAttach')
def OnChangeAttach():
    If(
        (
            (Expr.Eval, "ModelCmd(0x0A, 0x00)"),
            Expr.Return,
        ),
        'loc_7C19',
    )

    Call(ScriptId.Current, 'AniAttachMainWeapon')

    def _loc_7C19(): pass

    label('loc_7C19')

    Return()

# id: 0x0004 offset: 0x7C1C
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0005 offset: 0x7C28
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000100)

    Return()

# id: 0x0006 offset: 0x7C34
@scena.Code('Ani_SC_Load')
def Ani_SC_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000010)

    Return()

# id: 0x0007 offset: 0x7C40
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0008 offset: 0x7C4C
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000100)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0009 offset: 0x7C60
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x000A offset: 0x7C74
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000B offset: 0x7C80
@scena.Code('AniResetWorkRun')
def AniResetWorkRun():
    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000C offset: 0x7C8C
@scena.Code('AniReset')
def AniReset():
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x000D offset: 0x7CC4
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB01', 0.2)

    Return()

# id: 0x000E offset: 0x7D0C
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB01', 0.2)

    Return()

# id: 0x000F offset: 0x7D54
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0010 offset: 0x7D58
@scena.Code('AniTurn')
def AniTurn():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7DC9',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_7E62')

    def _loc_7DC9(): pass

    label('loc_7DC9')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_7E04',
    )

    PlayChrAnimeClip(0xFFFE, 'TURN_LEFT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_7E3B')

    def _loc_7E04(): pass

    label('loc_7E04')

    If(
        (
            (Expr.Eval, "ModelCmd(0x47, 0x00, 0xFFFE)"),
            (Expr.PushLong, 0x0),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_7E3B',
    )

    PlayChrAnimeClip(0xFFFE, 'TURN_RIGHT', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_7E3B(): pass

    label('loc_7E3B')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    def _loc_7E62(): pass

    label('loc_7E62')

    Return()

# id: 0x0011 offset: 0x7E64
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_7EAC',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_7F7B')

    def _loc_7EAC(): pass

    label('loc_7EAC')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7EF6',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Jump('loc_7F7B')

    def _loc_7EF6(): pass

    label('loc_7EF6')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7F5C',
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(0xFFFE, 'PRE_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.3, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Jump('loc_7F7B')

    def _loc_7F5C(): pass

    label('loc_7F5C')

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    def _loc_7F7B(): pass

    label('loc_7F7B')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0012 offset: 0x7F90
@scena.Code('AniWalk')
def AniWalk():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7FE7',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_800F')

    def _loc_7FE7(): pass

    label('loc_7FE7')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_800F(): pass

    label('loc_800F')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0013 offset: 0x8018
@scena.Code('AniBack')
def AniBack():
    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x01, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0014 offset: 0x804C
@scena.Code('AniRun')
def AniRun():
    Call(ScriptId.Current, 'SpringOff')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_8096',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_80BD')

    def _loc_8096(): pass

    label('loc_8096')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlayChrAnimeClip(0xFFFE, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_80BD(): pass

    label('loc_80BD')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0015 offset: 0x80C8
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0016 offset: 0x8100
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x03)

    Return()

# id: 0x0017 offset: 0x8130
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x0018 offset: 0x8160
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x0019 offset: 0x8184
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    Return()

# id: 0x001A offset: 0x8188
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    Return()

# id: 0x001B offset: 0x818C
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)

    Return()

# id: 0x001C offset: 0x81EC
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x001D offset: 0x8234
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x001E offset: 0x825C
@scena.Code('AniBtlInit')
def AniBtlInit():
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x2D)
    ReleaseEffect(0xFFFE, 0x2E)
    LoadEffect(0xFFFE, 0x2D, 'battle/cr032_02_1.eff')
    LoadEffect(0xFFFE, 0x2E, 'battle/cr032_02_2.eff')
    ReleaseEffect(0xFFFE, 0x22)
    ReleaseEffect(0xFFFE, 0x23)
    ReleaseEffect(0xFFFE, 0x24)
    LoadEffect(0xFFFE, 0x22, 'battle/atk032_0.eff')
    LoadEffect(0xFFFE, 0x23, 'battle/atk032_1.eff')
    LoadEffect(0xFFFE, 0x24, 'battle/atk032_2.eff')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)
    PlayEffect(0xFFFE, (0xFF, 0x24, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    ReleaseEffect(0xFFFE, 0x20)
    LoadEffect(0xFFFE, 0x20, 'battle/moncharge.eff')

    Return()

# id: 0x001F offset: 0x83B8
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0020 offset: 0x83E0
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_hand_point', 0x01)

    Return()

# id: 0x0021 offset: 0x8408
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x197),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_846C',
    )

    OP_3B(0x32, (0xFF, 0x4F50, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_8521')

    def _loc_846C(): pass

    label('loc_846C')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x13B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_84D0',
    )

    OP_3B(0x32, (0xFF, 0x4F4E, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_8521')

    def _loc_84D0(): pass

    label('loc_84D0')

    OP_3B(0x32, (0xFF, 0x4F4C, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0x006B, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_8521(): pass

    label('loc_8521')

    Sleep(1200)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0022 offset: 0x852C
@scena.Code('AniBtlReady')
def AniBtlReady():
    Return()

# id: 0x0023 offset: 0x8530
@scena.Code('AniBtlWait')
def AniBtlWait():
    OP_80(0.2)
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_860E',
    )

    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)
    PlayEffect(0xFFFE, (0xFF, 0x24, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)

    Jump('loc_8695')

    def _loc_860E(): pass

    label('loc_860E')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_866F',
    )

    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)

    Jump('loc_8695')

    def _loc_866F(): pass

    label('loc_866F')

    If(
        (
            (Expr.PushReg, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8695',
    )

    EffectCmd(0x14, 0xFFFE, 0x10, 1.0, 1.0, 1.0, 1.0, 0x00C8, 0x03)

    def _loc_8695(): pass

    label('loc_8695')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0024 offset: 0x86A0
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x0025 offset: 0x86D8
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0026 offset: 0x86FC
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', 'A', '', '#b', '0')
    Sleep(200)

    If(
        (
            (Expr.Eval, "BattleCmd(0x62, 0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_879A',
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x4F52, 0x0), (0xFF, 0x4F53, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_879A(): pass

    label('loc_879A')

    Sleep(550)

    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    Sleep(130)

    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x23, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.019999999552965164, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x8FB3, 0x0), (0xEE, 0.5, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(100)

    Sleep(400)

    CameraCmd(0x0A, 0.07, 0.05, 0.01, 30, 330, 150, 0, 0, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3FA, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x1, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3FA, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, (0xFF, 0x8FB3, 0x0), (0xFF, 0x7D0, 0x0))
    Sleep(100)

    SetChrFace(0x03, 0xFFFE, '6', '8', '', '#b', '0')
    Sleep(150)

    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0027 offset: 0x8AA8
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    OP_3B(0x32, (0xFF, 0x4F68, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x0028 offset: 0x8B0C
@scena.Code('AniBtlDamage')
def AniBtlDamage():
    SetChrFace(0x03, 0xFFFE, 'B', '3', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleCmd(0xAF, 0xFFFE)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8B59',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_8B7E')

    def _loc_8B59(): pass

    label('loc_8B59')

    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_8B7E(): pass

    label('loc_8B7E')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0029 offset: 0x8B88
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "BattleGetChrAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_8BFD',
    )

    OP_3B(0x32, (0xFF, 0x4F67, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_8C19')

    def _loc_8BFD(): pass

    label('loc_8BFD')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x4F65, 0x0), (0xFF, 0x4F66, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_8C19(): pass

    label('loc_8C19')

    Return()

# id: 0x002A offset: 0x8C1C
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    OP_3B(0x32, (0xFF, 0x4F5F, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x002B offset: 0x8C70
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    EffectCmd(0x0F, 0xFFFE, 0x0024, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_8CD1',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_8D25')

    def _loc_8CD1(): pass

    label('loc_8CD1')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_8D25(): pass

    label('loc_8D25')

    Return()

# id: 0x002C offset: 0x8D28
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    OP_80(0.2)
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x002D offset: 0x8D60
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    LoadEffect(0xFFFE, 0x30, 'battle_sys/tensionmax.eff')
    LoadEffect(0xFFFE, 0x31, 'battle_sys/tensionup.eff')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.7)
    SetChrFace(0x03, 0xFFFE, 'F2', '0[autoM0]', '0', '#b', '0')
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.35, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, 8.0, 6.0, 0, 0x01)
    CameraSetDistance(0x03, 3.25, 0)
    CameraCmd(0x0C, 0x03, 0.0, -0.15, 0.0, 8000)
    CameraCmd(0x11, 0x03, -5.0, 22.0, 0.0, 0x1F40, 0x01)
    CameraSetHeight(0x03, -1.2, 3000)
    BattleCmd(0x4B, 0x1F40, 0x03)
    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    OP_6C(0xFFFE, 0.4)
    CameraCmd(0x0A, 0.02, 0.02, 0.0, 500, 2000, 500, 0, 0, 0x00)
    Sleep(500)

    OP_3B(0x32, (0xFF, 0x4F5A, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(333)

    SetChrFace(0x03, 0xFFFE, '1', '4[autoM4]', '0', '#b', '0')
    Sleep(666)

    OP_6C(0xFFFE, 0.2)
    Sleep(666)

    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, -0.0333333, -0.0333333, 1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '3773', '2662', '0', '#b', '0')
    EffectCmd(0x10, 0xFFFE, 0x0031, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x30, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F00, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    SetChrFace(0x03, 0xFFFE, '6', '73', '0', '#b', '0')
    CameraCmd(0x0A, 0.1, 0.1, 0.0, 30, 600, 500, 0, 0, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 0x001E, 0x0258, 0x0190, 0x00000000, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.7, 0.9, 0.6)
    CameraSetHeight(0x03, 1.3, 450)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 450)
    Sleep(333)

    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '4[autoM4]', '0', '#b', '0')
    CameraSetHeight(0x03, 1.0, 5000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    Sleep(766)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x002E offset: 0x91D0
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x002F offset: 0x91E4
@scena.Code('AniBtlDead')
def AniBtlDead():
    BattleSetChrStatus(PseudoChrId.Self, BattleStatus.HPPercent, 100)
    BattleClearChrAbnormalStatus(PseudoChrId.Self, AbnormalStatus.Death)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x00, 0x00)
    OP_0C(0x00, 0x01)
    OP_0E(0x00, 0x01, 0x01)
    OP_0C(0x01, 0x01)
    OP_0E(0x01, 0x00, 0x02)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x07, 0x00, '')
    BattleCmd(0x08, 0x00)
    Call(ScriptId.Current, 'AniBtlWait')

    return
    If(
        (
            (Expr.Eval, "BattleGetChrFlags(0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_9247',
    )

    OP_3B(0x32, (0xFF, 0x4F64, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_9247(): pass

    label('loc_9247')

    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Sleep(500)

    Return()

# id: 0x0030 offset: 0x928C
@scena.Code('AniBtlAria')
def AniBtlAria():
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_9336',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x7D9, 0x0), 0xFFFE, 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '7', '0', '', '#b', '0')

    Jump('loc_9455')

    def _loc_9336(): pass

    label('loc_9336')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x7D9, 0x0), 0xFFFE, 0x00000021, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0x8B7E, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x4F5D, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    SetChrFace(0x03, 0xFFFE, '7', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)

    SetChrFace(0x03, 0xFFFE, '7', '0', '', '#b', '0')

    def _loc_9455(): pass

    label('loc_9455')

    Return()

# id: 0x0031 offset: 0x9458
@scena.Code('AniBtlArts')
def AniBtlArts():
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleCmd(0x4B, 0x00FA, 0x03)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(400)

    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x4F5E, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x7DB, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8B7F, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(500)

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x05, 0x00, '')
    BattleCmd(0x06, 0x00)
    SetChrFace(0x03, 0xFFFE, '0', '0', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x07DB)

    Return()

# id: 0x0032 offset: 0x9600
@scena.Code('AniBtlEscape')
def AniBtlEscape():
    Call(ScriptId.BtlCom, 'AniBtlEscape', (0xFF, 0x0, 0x0), (0xFF, 0x1, 0x0))
    LoadEffect(0xFFFE, 0x30, 'event/evc32_00.eff')
    OP_43(0x65, 200, 1.0, 0)
    OP_43(0xFE, 0)
    Call(ScriptId.CurrentCharacter, 'BtlDefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', -0.09, -0.3, -0.05, 0)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x64),
            Expr.Mod,
            (Expr.PushLong, 0x32),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_96C5',
    )

    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, -18.0, 0.0, 0, 0x01)

    Jump('loc_96DA')

    def _loc_96C5(): pass

    label('loc_96C5')

    CameraRotateByTarget(0xFFFE, '', 0x03, 4.0, 18.0, 0.0, 0, 0x01)

    def _loc_96DA(): pass

    label('loc_96DA')

    CameraSetDistance(0x03, 4.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, 'NODE_HEAD', -0.09, -0.2, -0.05, 3000)
    CameraSetDistance(0x03, 2.34, 3000)
    CameraCmd(0x0B, 0x03, 40.0, 0x0BB8)
    BattleCmd(0x4B, 0x0000, 0x03)
    Sleep(500)

    OP_3B(0x00, (0xFF, 0x773A, 0x0), (0xEE, 0.30000001192092896, 0x0), (0xFF, 0x1F4, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayEffect(0xFFFE, (0xFF, 0x30, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.019999999552965164, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x13B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_981B',
    )

    OP_3B(0x32, (0xFF, 0x4F4F, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_986C')

    def _loc_981B(): pass

    label('loc_981B')

    OP_3B(0x32, (0xFF, 0x4F4D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_986C(): pass

    label('loc_986C')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x13B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_9887',
    )

    OP_3B(0x34, (0xFF, 0x4F4F, 0x0))

    Jump('loc_988F')

    def _loc_9887(): pass

    label('loc_9887')

    OP_3B(0x34, (0xFF, 0x4F4D, 0x0))

    def _loc_988F(): pass

    label('loc_988F')

    OP_3B(0x01, (0xFF, 0x773A, 0x0), (0xFF, 0x1F4, 0x0))
    OP_3B(0x00, (0xFF, 0x764C, 0x0), (0xEE, 0.5, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 500, 0x03)
    EffectCmd(0x14, 0xFFFE, 0x10, 0.0, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    Sleep(500)

    EffectCmd(0x14, 0xFFFE, 0x02, 0.0, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    Sleep(500)

    ChrClearPhysicsFlags(0xFFFE, 0x00000200)
    ChrClearPhysicsFlags(0xFFFE, 0x00000200)
    BattleSetChrPos(0xFFFE, 0xFFF4, 10000.0, 0.0, 0.0, -1.0, 0x00, 0x10)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleDamage(0xFFFE, 0xFFFE, 0x64, 0x00)
    ReleaseEffect(0xFFFE, 0x30)

    Return()

# id: 0x0033 offset: 0x9988
@scena.Code('AniBtlBluff')
def AniBtlBluff():
    Call(ScriptId.BtlCom, 'AniBtlBluff')

    Return()

# id: 0x0034 offset: 0x9998
@scena.Code('AniBtlBluffVoice')
def AniBtlBluffVoice():
    OP_3B(0x32, (0xFF, 0x4F51, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(2000)

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0035 offset: 0x99F4
@scena.Code('AniBtlLinkAttackVoice')
def AniBtlLinkAttackVoice():
    OP_3B(0x3A, 0xFFFE, (0xFF, 0x4F68, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    Return()

# id: 0x0036 offset: 0x9A14
@scena.Code('AniBtlLinkChase')
def AniBtlLinkChase():
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseBegin')
    BattleTargetsIterReset(0xFF, 0xFFFE)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    Sleep(200)

    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -0.1, 2.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.3, 10.0, 10.0, -1.0, 0x00, 0x00)
    Sleep(166)

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', 'A', '', '#b', '0')
    Sleep(200)

    OP_3B(0x32, (0xFF, 0x4F53, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(550)

    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    Sleep(130)

    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x23, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.019999999552965164, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x8FB3, 0x0), (0xEE, 0.5, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    Sleep(100)

    Sleep(400)

    CameraCmd(0x0A, 0.07, 0.05, 0.01, 30, 330, 150, 0, 0, 0x00)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3FA, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3FA, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, (0xFF, 0x8FB3, 0x0), (0xFF, 0x7D0, 0x0))
    CameraCmd(0x09, 0.01, 0.01, 0.5)
    OP_3B(0x00, (0xFF, 0x8BF0, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurStart', (0xFF, 0x0, 0x0))
    Sleep(60)

    Call(ScriptId.BtlCom, 'AniBtlLinkAttackSlow')
    Sleep(40)

    SetChrFace(0x03, 0xFFFE, '6', '8', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 2.0, 0x00, 0x01)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    EffectCmd(0x14, 0xFFFE, 0x10, 1.0, 1.0, 1.0, 0.0, 0x00C8, 0x03)
    Call(ScriptId.BtlCom, 'AniBtlLinkAttackBlurEnd')
    Sleep(200)

    BattleCmd(0x3F, 0xFFFE)
    EffectCmd(0x12, 0xFFFE, 0x03FA)
    Call(ScriptId.BtlCom, 'AniBtlLinkChaseFinish')

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0037 offset: 0x9FF0
@scena.Code('AniBtlLinkRushStart')
def AniBtlLinkRushStart():
    SetChrFace(0x03, 0xFFFE, '6', 'A[autoMA]', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0038 offset: 0xA02C
@scena.Code('AniBtlLinkRushMove')
def AniBtlLinkRushMove():
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0039 offset: 0xA050
@scena.Code('AniBtlLinkRush')
def AniBtlLinkRush():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0xFF, 0xFFFE)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '', '#b', '0')
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    Call(ScriptId.BtlCom, 'AniBtlBurstWait')
    LoadEffect(0xFFFE, 0x31, 'battle/atk032_3.eff')
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPosAsync(0xFFFE, 0xFFF4, 0.0, 0.0, -2.0, 4.0, 0x00, 0x01)
    BattleCmd(0x3F, 0xFFFE)
    BattleCmd(0x48, 0xFFFB, 0x0001)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '6', 'A', '', '#b', '0')
    Sleep(200)

    Sleep(550)

    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    Sleep(130)

    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.019999999552965164, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x8FB3, 0x0), (0xEE, 0.5, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    Sleep(100)

    Sleep(400)

    CameraCmd(0x0A, 0.07, 0.05, 0.01, 30, 330, 150, 0, 0, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3FA, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x1, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(200)

    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3FA, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))
    OP_3B(0x00, (0xFF, 0x10F3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x01, (0xFF, 0x8FB3, 0x0), (0xFF, 0x7D0, 0x0))
    Sleep(100)

    SetChrFace(0x03, 0xFFFE, '6', '8', '', '#b', '0')
    Sleep(130)

    SetChrFace(0x03, 0xFFFE, '6', '0', '', '#b', '0')
    Sleep(100)

    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)
    WaitForThreadExit(0xFFFE, 0x02)
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.35)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 200, 0x03)
    EffectCmd(0x14, 0xFFFE, 0x10, 1.0, 1.0, 1.0, 0.0, 0x00C8, 0x03)
    Call(ScriptId.Sound, 'SE_LINK_STEP')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, -4.0, 0.2, 0x00, 0x11)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x31)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x3),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x003A offset: 0xA4E4
@scena.Code('AniBtlLinkBurst')
def AniBtlLinkBurst():
    Call(ScriptId.Current, 'AniBtlLinkRush')

    Return()

# id: 0x003B offset: 0xA4F8
@scena.Code('AniBtlLinkLastAttack')
def AniBtlLinkLastAttack():
    Call(ScriptId.Current, 'AniBtlLinkChase')

    Return()

# id: 0x003C offset: 0xA50C
@scena.Code('AniBtlBraveOrderCancel')
def AniBtlBraveOrderCancel():
    Call(ScriptId.BtlCom, 'AniBtlBraveOrderCancel')

    Return()

# id: 0x003D offset: 0xA528
@scena.Code('AniBtlBraveOrder00')
def AniBtlBraveOrder00():
    Call(ScriptId.Current, 'SetAntiOrder')
    Call(ScriptId.BtlCom, 'AniBtlBraveOrder00')

    Return()

# id: 0x003E offset: 0xA550
@scena.Code('AniBtlBraveOrderAnime')
def AniBtlBraveOrderAnime():
    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A5BF',
    )

    SetChrFace(0x03, 0xFFFE, '777776', '', '', '#b', '0')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Call(ScriptId.Current, 'SpringOn')

    Jump('loc_A5BF')

    def _loc_A5BF(): pass

    label('loc_A5BF')

    Return()

# id: 0x003F offset: 0xA5C0
@scena.Code('AniBtlBraveOrderVoice')
def AniBtlBraveOrderVoice():
    If(
        (
            (Expr.PushReg, 0x5),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A689',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xA9, 0x00, 0x00000000)"),
            (Expr.PushLong, 0x10D0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A638',
    )

    OP_3B(0x32, (0xFF, 0x4F5B, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Jump('loc_A689')

    def _loc_A638(): pass

    label('loc_A638')

    OP_3B(0x32, (0xFF, 0x4F5C, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    def _loc_A689(): pass

    label('loc_A689')

    Return()

# id: 0x0040 offset: 0xA68C
@scena.Code('AniBtlAntiOrder00')
def AniBtlAntiOrder00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    BattleTurnChrDirection(0xFFFE, 0xFFF3, 0.0, -1.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.3, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -6.0, -7.0, 0, 0x01)
    CameraSetDistance(0x03, 2.7, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    BattleCmd(0x4B, 0x0000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.29, 0.0, 2000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -6.0, 4.0, 2000, 0x01)
    CameraSetDistance(0x03, 2.0, 2000)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')

    If(
        (
            (Expr.Eval, "BattleCmd(0xA9, 0x00, 0x00000000)"),
            (Expr.PushLong, 0xFFFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A7C2',
    )

    Sleep(666)

    Sleep(333)

    BattleCmd(0xA7, 0x01)

    Jump('loc_A7C5')

    def _loc_A7C2(): pass

    label('loc_A7C2')

    Sleep(666)

    def _loc_A7C5(): pass

    label('loc_A7C5')

    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')
    Call(ScriptId.Current, 'SetAntiOrder')
    Call(ScriptId.BtlCom, 'AniBtlAntiOrder')

    Return()

# id: 0x0041 offset: 0xA800
@scena.Code('SetAntiOrder')
def SetAntiOrder():
    ExecExpressionWithReg(
        0x05,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0042 offset: 0xA80C
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    If(
        (
            (Expr.Eval, "BattleCmd(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_A8A3',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(0xFFFE, (0xFF, 0x20, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)

    Jump('loc_A995')

    def _loc_A8A3(): pass

    label('loc_A8A3')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x20, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0xFD5, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    Sleep(1000)

    def _loc_A995(): pass

    label('loc_A995')

    Return()

# id: 0x0043 offset: 0xA998
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x30, 'battle/cr032_00_0.eff')
    LoadEffect(0xFFFE, 0x38, 'battle/cr032_00_1.eff')
    LoadEffect(0xFFFE, 0x31, 'battle/cr032_00_10.eff')
    LoadEffect(0xFFFE, 0x32, 'battle/cr032_00_20.eff')
    LoadEffect(0xFFFE, 0x33, 'battle/cr032_00_30.eff')
    LoadEffect(0xFFFE, 0x34, 'battle/cr032_00_40.eff')
    LoadEffect(0xFFFE, 0x35, 'battle/cr032_00_50.eff')
    LoadEffect(0xFFFE, 0x36, 'battle/cr032_00_60.eff')
    LoadEffect(0xFFFE, 0x37, 'battle/cr032_00_70.eff')
    BattleTargetsIterInit(0x00)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleCmd(0x47)
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 1.4, 1.25, -1.95, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.0, -35.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.5, 0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4545454', '', '#b', '0')
    OP_6C(0xFFFE, 1.0)
    Sleep(200)

    OP_3B(0x32, (0xFF, 0x4F54, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    PlayEffect(0xFFFE, (0xFF, 0x30, 0x0), 0xFFFE, 0x0000000C, (0xDD, 'NODE_L_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.5, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.800000011920929, 0x0), (0xEE, 0.800000011920929, 0x0), (0xEE, 0.800000011920929, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x9078, 0x0), (0xEE, 0.800000011920929, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 3.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraSetHeight(0x03, -1.0, 400)
    CameraCmd(0x0C, 0x03, 0.0, 0.0, 0.1, 400)
    CameraCmd(0x11, 0x03, 0.0, 2.0, -2.0, 0x0190, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(233)

    SetChrFace(0x03, 0xFFFE, '2', '545454', '2', '#b', '0')
    Sleep(233)

    OP_3B(0x00, (0xFF, 0x10DF, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x9079, 0x0), (0xEE, 0.800000011920929, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 2.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(166)

    OP_5E(0x00, 0x0003, 0.5, 0x0032, 0x0096, 0x0064, 0x3E4CCCCD, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.0, 6.0, 15.0)
    BattleCmd(0x47)
    CameraCmd(0x0C, 0x03, 0.0, 0.25, 0.0, 250)
    CameraCmd(0x11, 0x03, 5.0, 20.0, 0.0, 0x1F40, 0x01)
    CameraSetHeight(0x03, 3.0, 250)
    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x32, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x33, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x34, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x35, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x36, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x37, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 3.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10E3, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2', '14', '2', '#b', '0')
    OP_4E(1.5, 0.0, 0x03)
    Sleep(1500)

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.7, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1000)

    OP_3B(0x00, (0xFF, 0x10EE, 0x0), (0xEE, 0.699999988079071, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x9064, 0x0), (0xEE, 0.800000011920929, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 3.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x8F6B, 0x0), (0xEE, 0.5, 0x0), (0xFF, 0xC8, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x708, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x0708, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    OP_3B(0x01, (0xFF, 0x10E3, 0x0), (0xFF, 0x3E8, 0x0))
    Sleep(100)

    CameraCmd(0x00)
    CameraCmd(0x0C, 0x02, 0.0, 4.0, 0.0, 750)
    CameraCmd(0x11, 0x02, -15.0, 0.0, 0.0, 0x02EE, 0x01)
    CameraCmd(0x07, 0x00BF)
    ReleaseEffect(0xFFFE, 0x31)
    ReleaseEffect(0xFFFE, 0x32)
    ReleaseEffect(0xFFFE, 0x33)
    ReleaseEffect(0xFFFE, 0x34)
    ReleaseEffect(0xFFFE, 0x35)
    ReleaseEffect(0xFFFE, 0x36)
    ReleaseEffect(0xFFFE, 0x37)
    ReleaseEffect(0xFFFE, 0x38)
    LoadEffect(0xFFFE, 0x31, 'battle/cr032_00_11.eff')
    LoadEffect(0xFFFE, 0x32, 'battle/cr032_00_21.eff')
    LoadEffect(0xFFFE, 0x33, 'battle/cr032_00_31.eff')
    LoadEffect(0xFFFE, 0x34, 'battle/cr032_00_41.eff')
    LoadEffect(0xFFFE, 0x35, 'battle/cr032_00_51.eff')
    LoadEffect(0xFFFE, 0x36, 'battle/cr032_00_61.eff')
    LoadEffect(0xFFFE, 0x37, 'battle/cr032_00_71.eff')
    LoadEffect(0xFFFE, 0x38, 'battle/cr032_00_9.eff')
    Sleep(66)

    CameraCmd(0x00)
    CameraCmd(0x0C, 0x01, 0.0, -4.0, 0.0, 700)
    CameraCmd(0x11, 0x01, 15.0, 0.0, 0.0, 0x02BC, 0x01)
    CameraSetHeight(0x01, -3.0, 700)
    Sleep(333)

    OP_4E(1.0, 0.0, 0x03)
    OP_3B(0x32, (0xFF, 0x4F55, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleCmd(0x82, 0x00, 0xFFFE, 0x00000002)

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_B439(): pass

    label('loc_B439')

    If(
        (
            (Expr.PushReg, 0x3),
            Expr.Return,
        ),
        'loc_BC90',
    )

    Call(ScriptId.Current, 'AniBtlCraft00_getTarget')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B57E',
    )

    PlayEffect(0xFFFE, (0xFF, 0x37, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.95, 0.85, 1.0, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_B57E(): pass

    label('loc_B57E')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B6A0',
    )

    PlayEffect(0xFFFE, (0xFF, 0x36, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.6, 0.68, 0.35, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_B6A0(): pass

    label('loc_B6A0')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B7C2',
    )

    PlayEffect(0xFFFE, (0xFF, 0x35, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.65, 0.4, 0.8, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_B7C2(): pass

    label('loc_B7C2')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B8E4',
    )

    PlayEffect(0xFFFE, (0xFF, 0x34, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.45, 0.8, 0.39, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_B8E4(): pass

    label('loc_B8E4')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BA06',
    )

    PlayEffect(0xFFFE, (0xFF, 0x33, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.8, 0.3, 0.3, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_BA06(): pass

    label('loc_BA06')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB28',
    )

    PlayEffect(0xFFFE, (0xFF, 0x32, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.25, 0.525, 0.75, 1.0, 0x0000, 0x03)

    Jump('loc_BC45')

    def _loc_BB28(): pass

    label('loc_BB28')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BC45',
    )

    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    EffectCmd(0x13, 0xFFFE, 0x02, 0x00FA)
    OP_3B(0x00, (0xFF, 0x8F1D, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(250)

    PlayEffect(0xFFFE, (0xFF, 0x38, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    EffectCmd(0x14, 0xFFFE, 0x03, 0.85, 0.65, 0.2, 1.0, 0x0000, 0x03)

    def _loc_BC45(): pass

    label('loc_BC45')

    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    OP_5E(0x00, 0x0000, 0.5, 0x0032, 0x0096, 0x0064, 0x3E4CCCCD, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    Sleep(30)

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_B439')

    def _loc_BC90(): pass

    label('loc_BC90')

    CameraCmd(0x07, 0x00BF)
    CameraCmd(0x00)
    CameraSetHeight(0x03, -0.2, 3000)
    CameraCmd(0x0C, 0x03, 0.0, 0.0, 0.1, 3000)
    CameraCmd(0x11, 0x03, 0.0, 5.0, -2.0, 0x0BB8, 0x01)
    Sleep(1500)

    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0044 offset: 0xBCFC
@scena.Code('AniBtlCraft00_getTarget')
def AniBtlCraft00_getTarget():
    BattleTargetsIterReset(0x00, 0xFFFE)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_BD31',
    )

    ExecExpressionWithReg(
        0x00,
        (
            Expr.Rand,
            (Expr.PushReg, 0x0),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_BD17(): pass

    label('loc_BD17')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_BD31',
    )

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_BD17')

    def _loc_BD31(): pass

    label('loc_BD31')

    Return()

# id: 0x0045 offset: 0xBD34
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    Call(ScriptId.Current, 'SpringOff')
    LoadEffect(0xFFFE, 0x30, 'battle/cr032_01_0.eff')
    LoadEffect(0xFFFE, 0x31, 'battle/cr032_01_1.eff')
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.4, 1.5, -3.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, -6.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 5.5, 0)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 5000)
    CameraCmd(0x11, 0x03, 2.0, -0.0, 0.0, 0x1388, 0x01)
    CameraSetHeight(0x03, 0.5, 5000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4[autoM4]', '', '#b', '0')
    OP_3B(0x32, (0xFF, 0x4F56, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(1500)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F1A, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    Sleep(300)

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x30, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x10EB, 0x0), (0xEE, 0.800000011920929, 0x0), (0xFF, 0x190, 0x0), 0.0, (0xEE, 3.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x9067, 0x0), (0xEE, 0.6000000238418579, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    Sleep(750)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, 0xFFFE, '2', '5[autoM4]', '', '#b', '0')
    OP_5E(0x00, 0x0000, 0.7, 0x0064, 0x00FA, 0x0064, 0x3E4CCCCD, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, (0xFF, 0x10E0, 0x0), (0xEE, 0.699999988079071, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x9059, 0x0), (0xEE, 0.800000011920929, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 3.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x3E8, 0x0), (0xFF, 0x12C, 0x0), 0x0000, 0x03E8, 0x0000, 0x0001, 0xFFFE, 0x0000, 0.0)
    OP_3B(0x01, (0xFF, 0x10EB, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x01, (0xFF, 0x9067, 0x0), (0xFF, 0x3E8, 0x0))
    Sleep(333)

    OP_43(0x65, 100, 1.0, 0)
    OP_43(0xFE, 0)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraCmd(0x0C, 0x03, 0.0, -1.2, 0.0, 0)
    CameraCmd(0x11, 0x03, 20.0, 0.0, 0.0, 0x0000, 0x01)
    Sleep(1)

    BattleCmd(0x48, 0xFFFE, 0x0001)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x32, (0xFF, 0x4F57, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x00, 0xFFFE)
    def _loc_C25B(): pass

    label('loc_C25B')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_C32D',
    )

    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1106, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(30)

    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_C25B')

    def _loc_C32D(): pass

    label('loc_C32D')

    Sleep(1000)

    BattleCmd(0x47)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000003, 0x00000000, 0x00000000)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFF9, 0x0001)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTargetsIterReset(0x00, 0xFFFE)
    def _loc_C361(): pass

    label('loc_C361')

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_C449',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFDD, 0.0, -1.0)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    BattleDamage(0xFFFB, 0xFFFE, 0x64, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x31, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x1107, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(30)

    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x00,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_C361')

    def _loc_C449(): pass

    label('loc_C449')

    Sleep(1000)

    BattleTargetsIterReset(0x00, 0xFFFE)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0046 offset: 0xC4F8
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    Call(ScriptId.Current, 'SpringOff')
    LoadEffect(0xFFFE, 0x30, 'battle/cr032_02_0.eff')
    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EffectCmd(0x0F, 0xFFFE, 0x0022, 0x01)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -10.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.7, 0)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 4000)
    CameraCmd(0x11, 0x03, 10.0, -10.0, 0.0, 0x0FA0, 0x01)
    CameraSetHeight(0x03, 0.5, 4000)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '4', '', '#b', '0')
    Sleep(500)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(233)

    OP_3B(0x00, (0xFF, 0xFFFF, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x905B, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x64, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    Sleep(266)

    PlayEffect(0xFFFE, (0xFF, 0x30, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    SetChrFace(0x03, 0xFFFE, '12', '15', '5', '#b', '0')
    Sleep(100)

    CameraCmd(0x00)
    CameraSetHeight(0x03, 1.0, 350)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 350)
    CameraCmd(0x11, 0x03, 20.0, 0.0, 0.0, 0x015E, 0x01)
    OP_5E(0x00, 0x0000, 0.7, 0x0064, 0x00FA, 0x0064, 0x3E4CCCCD, 0xFFFF, '', -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), (0xEE, 0.699999988079071, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    CameraCmd(0x07, 0x00BF)
    CameraCmd(0x00)
    CameraSetHeight(0x03, 0.5, 4000)
    CameraCmd(0x0C, 0x03, 0.0, 0.1, 0.0, 4000)
    CameraCmd(0x11, 0x03, 5.0, 0.0, 0.0, 0x0FA0, 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)

    BattleDamage(0xFFFE, 0xFFFE, 0x64, 0x00)
    EffectCmd(0x12, 0xFFFE, 0x0030)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayEffect(0xFFFE, (0xFF, 0x22, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_R_HAND'), (0xEE, 0.0, 0x0), (0xEE, -0.07000000029802322, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x10)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0047 offset: 0xC8E4
@scena.Code('AniBtlConditionExchange')
def AniBtlConditionExchange():
    OP_3B(0x32, (0xFF, 0x4F58, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)
    OP_3B(0x00, (0xFF, 0x1106, 0x0), (0xEE, 0.699999988079071, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFF, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0048 offset: 0xC988
@scena.Code('AniBtlConditionExchangeEnd')
def AniBtlConditionExchangeEnd():
    OP_3B(0x32, (0xFF, 0x4F59, 0x0), (0xEE, 1.0, 0x0), (0xFF, 0x0, 0x0), 0.0, (0xEE, 0.0, 0x0), 0x0000, 0xFFFE, 0.0, 0.0, 0.0, (0xEE, 0.0, 0x0), '', (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0.0)

    Return()

# id: 0x0049 offset: 0xC9DC
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004A offset: 0xCA18
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004B offset: 0xCA44
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0xCAB8
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0xCB2C
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0xCBA4
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0xCBD0
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xCC28
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0051 offset: 0xCC54
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0052 offset: 0xCC9C
@scena.Code('AniEvPowerUp')
def AniEvPowerUp():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0053 offset: 0xCD14
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0054 offset: 0xCD88
@scena.Code('AniEvDeada')
def AniEvDeada():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0xCDD0
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0xCE18
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0057 offset: 0xCE4C
@scena.Code('AniEvCraft00_1')
def AniEvCraft00_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0058 offset: 0xCEB0
@scena.Code('AniEvCraft00_2')
def AniEvCraft00_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0059 offset: 0xCF14
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0xCF48
@scena.Code('AniEvCraft01_1')
def AniEvCraft01_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005B offset: 0xCFAC
@scena.Code('AniEvCraft01_2')
def AniEvCraft01_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005C offset: 0xD010
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0xD044
@scena.Code('AniEvCraft02_1')
def AniEvCraft02_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005E offset: 0xD0A8
@scena.Code('AniEvCraft02_01')
def AniEvCraft02_01():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0xD10C
@scena.Code('AniEvDropclothes_01')
def AniEvDropclothes_01():
    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_01', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0xD140
@scena.Code('AniEvDropclothes_02')
def AniEvDropclothes_02():
    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'DROPCLOTHES_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0061 offset: 0xD1A4
@scena.Code('AniEv00070')
def AniEv00070():
    PlayChrAnimeClip(0xFFFE, 'ev00070', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'ev00070a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0062 offset: 0xD1FC
@scena.Code('AniEv03035')
def AniEv03035():
    PlayChrAnimeClip(0xFFFE, 'ev03035', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'ev03035a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0063 offset: 0xD24C
@scena.Code('AniAttachEQU417')
def AniAttachEQU417():
    LoadAsset('C_EQU417')
    AttachEquip(0xFFFE, 'C_EQU417', 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    OP_76(0xFFFE, 'R_hand_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0064 offset: 0xD2D4
@scena.Code('AniDetachEQU417')
def AniDetachEQU417():
    ReleaseAsset('C_EQU417')
    DeatchEquip(0xFFFE, 'R_hand_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    ModelCmd(0x0B, 0xFFFE)

    Return()

# id: 0x0065 offset: 0xD31C
@scena.Code('AniEv50525')
def AniEv50525():
    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev50525', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)

    OP_2A(0x00, 0xFFFE, '', 'R_hand_point', 0x01)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    PlayChrAnimeClip(0xFFFE, 'ev50525a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0066 offset: 0xD3A0
@scena.AnimeClips('_AniTurn')
def _AniTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_LEFT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'TURN_RIGHT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0067 offset: 0xD4A0
@scena.AnimeClips('_AniWait')
def _AniWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'PRE_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x0068 offset: 0xD5A0
@scena.AnimeClips('_AniWalk')
def _AniWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x0069 offset: 0xD620
@scena.AnimeClips('_AniBack')
def _AniBack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WALK',
        ),
    )

# id: 0x006A offset: 0xD680
@scena.AnimeClips('_AniRun')
def _AniRun():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'RUN',
        ),
    )

# id: 0x006B offset: 0xD700
@scena.AnimeClips('_AniSitWait')
def _AniSitWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'SIT_WAIT',
        ),
    )

# id: 0x006C offset: 0xD760
@scena.AnimeClips('_AniWait1')
def _AniWait1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT1',
        ),
    )

# id: 0x006D offset: 0xD7C0
@scena.AnimeClips('_AniAttachPhone')
def _AniAttachPhone():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU320',
        ),
    )

# id: 0x006E offset: 0xD820
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
    )

# id: 0x006F offset: 0xD940
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F50,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F4E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F4C,
            name   = '',
        ),
    )

# id: 0x0070 offset: 0xD9F0
@scena.AnimeClips('_AniBtlWait')
def _AniBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0071 offset: 0xDA50
@scena.AnimeClips('_AniBtlTurn')
def _AniBtlTurn():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x0072 offset: 0xDAB0
@scena.AnimeClips('_AniBtlAttack')
def _AniBtlAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F52,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F53,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
    )

# id: 0x0073 offset: 0xDC00
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F68,
            name   = '',
        ),
    )

# id: 0x0074 offset: 0xDC60
@scena.AnimeClips('_AniBtlDamage')
def _AniBtlDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0075 offset: 0xDCE0
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F67,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F65,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F66,
            name   = '',
        ),
    )

# id: 0x0076 offset: 0xDD90
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5F,
            name   = '',
        ),
    )

# id: 0x0077 offset: 0xDDF0
@scena.AnimeClips('_AniBtlSwoon')
def _AniBtlSwoon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0078 offset: 0xDEA0
@scena.AnimeClips('_AniBtlWeak')
def _AniBtlWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0079 offset: 0xDF00
@scena.AnimeClips('_AniBtlTensionMax')
def _AniBtlTensionMax():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionmax.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle_sys/tensionup.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F00,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
    )

# id: 0x007A offset: 0xE070
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F64,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
    )

# id: 0x007B offset: 0xE0F0
@scena.AnimeClips('_AniBtlAria')
def _AniBtlAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x007C offset: 0xE1C0
@scena.AnimeClips('_AniBtlArts')
def _AniBtlArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x007D offset: 0xE2C0
@scena.AnimeClips('_AniBtlEscape')
def _AniBtlEscape():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'event/evc32_00.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000773A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F4F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F4D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000764C,
            name   = '',
        ),
    )

# id: 0x007E offset: 0xE3E0
@scena.AnimeClips('_AniBtlBluffVoice')
def _AniBtlBluffVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F51,
            name   = '',
        ),
    )

# id: 0x007F offset: 0xE440
@scena.AnimeClips('_AniBtlLinkAttackVoice')
def _AniBtlLinkAttackVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F68,
            name   = '',
        ),
    )

# id: 0x0080 offset: 0xE4A0
@scena.AnimeClips('_AniBtlLinkChase')
def _AniBtlLinkChase():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F53,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
    )

# id: 0x0081 offset: 0xE660
@scena.AnimeClips('_AniBtlLinkRushStart')
def _AniBtlLinkRushStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0082 offset: 0xE6C0
@scena.AnimeClips('_AniBtlLinkRushMove')
def _AniBtlLinkRushMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x0083 offset: 0xE720
@scena.AnimeClips('_AniBtlLinkRush')
def _AniBtlLinkRush():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk032_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0084 offset: 0xE8C0
@scena.AnimeClips('_AniBtlBraveOrderAnime')
def _AniBtlBraveOrderAnime():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
    )

# id: 0x0085 offset: 0xE920
@scena.AnimeClips('_AniBtlBraveOrderVoice')
def _AniBtlBraveOrderVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F5C,
            name   = '',
        ),
    )

# id: 0x0086 offset: 0xE9A0
@scena.AnimeClips('_AniBtlAntiOrder00')
def _AniBtlAntiOrder00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x0087 offset: 0xEA00
@scena.AnimeClips('_AniBtlCharge')
def _AniBtlCharge():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00000FD5,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0088 offset: 0xEAB0
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_20.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_30.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_40.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_50.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_60.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_70.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F54,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009078,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010DF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009079,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E3,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010EE,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009064,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_21.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_31.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_41.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_51.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_61.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_71.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F55,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1D,
            name   = '',
        ),
    )

# id: 0x0089 offset: 0xF100
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F56,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010EB,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009067,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010E0,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00009059,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F57,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001106,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001107,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x008A offset: 0xF3E0
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr032_02_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000FFFF,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000905B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x008B offset: 0xF550
@scena.AnimeClips('_AniBtlConditionExchange')
def _AniBtlConditionExchange():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001106,
            name   = '',
        ),
    )

# id: 0x008C offset: 0xF5D0
@scena.AnimeClips('_AniBtlConditionExchangeEnd')
def _AniBtlConditionExchangeEnd():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00004F59,
            name   = '',
        ),
    )

# id: 0x008D offset: 0xF630
@scena.AnimeClips('_AniEvBtlWait')
def _AniEvBtlWait():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x008E offset: 0xF690
@scena.AnimeClips('_AniEvBtlMove')
def _AniEvBtlMove():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_MOVE',
        ),
    )

# id: 0x008F offset: 0xF6F0
@scena.AnimeClips('_AniEvAttack')
def _AniEvAttack():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0090 offset: 0xF770
@scena.AnimeClips('_AniEvDamage')
def _AniEvDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0091 offset: 0xF7F0
@scena.AnimeClips('_AniEvWeakDamage')
def _AniEvWeakDamage():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0092 offset: 0xF870
@scena.AnimeClips('_AniEvAria')
def _AniEvAria():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARIA',
        ),
    )

# id: 0x0093 offset: 0xF8D0
@scena.AnimeClips('_AniEvArts')
def _AniEvArts():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTS',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ARTSa',
        ),
    )

# id: 0x0094 offset: 0xF950
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0095 offset: 0xF9B0
@scena.AnimeClips('_AniEvWeak')
def _AniEvWeak():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WEAK',
        ),
    )

# id: 0x0096 offset: 0xFA10
@scena.AnimeClips('_AniEvPowerUp')
def _AniEvPowerUp():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUPa',
        ),
    )

# id: 0x0097 offset: 0xFA90
@scena.AnimeClips('_AniEvDead')
def _AniEvDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0098 offset: 0xFB10
@scena.AnimeClips('_AniEvDeada')
def _AniEvDeada():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEADa',
        ),
    )

# id: 0x0099 offset: 0xFB70
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD1',
        ),
    )

# id: 0x009A offset: 0xFBD0
@scena.AnimeClips('_AniEvCraft00')
def _AniEvCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x009B offset: 0xFC30
@scena.AnimeClips('_AniEvCraft00_1')
def _AniEvCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_01a',
        ),
    )

# id: 0x009C offset: 0xFCB0
@scena.AnimeClips('_AniEvCraft00_2')
def _AniEvCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_02a',
        ),
    )

# id: 0x009D offset: 0xFD30
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x009E offset: 0xFD90
@scena.AnimeClips('_AniEvCraft01_1')
def _AniEvCraft01_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00a',
        ),
    )

# id: 0x009F offset: 0xFE10
@scena.AnimeClips('_AniEvCraft01_2')
def _AniEvCraft01_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_01a',
        ),
    )

# id: 0x00A0 offset: 0xFE90
@scena.AnimeClips('_AniEvCraft02')
def _AniEvCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
    )

# id: 0x00A1 offset: 0xFEF0
@scena.AnimeClips('_AniEvCraft02_1')
def _AniEvCraft02_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_00a',
        ),
    )

# id: 0x00A2 offset: 0xFF70
@scena.AnimeClips('_AniEvCraft02_01')
def _AniEvCraft02_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01a',
        ),
    )

# id: 0x00A3 offset: 0xFFF0
@scena.AnimeClips('_AniEvDropclothes_01')
def _AniEvDropclothes_01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_01',
        ),
    )

# id: 0x00A4 offset: 0x10050
@scena.AnimeClips('_AniEvDropclothes_02')
def _AniEvDropclothes_02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'DROPCLOTHES_03',
        ),
    )

# id: 0x00A5 offset: 0x100D0
@scena.AnimeClips('_AniEv00070')
def _AniEv00070():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00070',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00070a',
        ),
    )

# id: 0x00A6 offset: 0x10150
@scena.AnimeClips('_AniEv03035')
def _AniEv03035():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03035',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03035a',
        ),
    )

# id: 0x00A7 offset: 0x101D0
@scena.AnimeClips('_AniAttachEQU417')
def _AniAttachEQU417():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU417',
        ),
    )

# id: 0x00A8 offset: 0x10230
@scena.AnimeClips('_AniEv50525')
def _AniEv50525():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev50525',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev50525a',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
