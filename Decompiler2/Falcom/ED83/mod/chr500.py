import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED83.Parser.scena_writer_helper import *
import arianrhod

scena = createScenaWriter('chr500.dat')

# id: 0x0000 offset: 0x1028
@scena.AnimeClipTable('AnimeClipTable')
def AnimeClipTable():
    return ScenaAnimeClipTable(
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'RUN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'SIT_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000001,
            asset      = 'C_CHR033_DF1',
            symbol     = 'PRE_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_WAIT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_ATTACK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_DAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_WEAK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_WEAKDAMAGE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_POWERUP_F',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_POWERUP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_POWERUPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_DEAD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_DEADa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT01_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT02_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT02_00a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT03_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT03_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT03_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT03_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000100,
            asset      = 'C_CHR033_BT1',
            symbol     = 'BTL_CRAFT03_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_01a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_02a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_03a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_04a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_05a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_06c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_08a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000010,
            asset      = 'C_CHR033_SC1',
            symbol     = 'BTL_S_CRAFT00_09a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'PRE_WAIT_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'SIT_WAIT_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_DEAD1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_DF1',
            symbol     = 'SIT_WAIT+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WAIT1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIRE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIREa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKIREb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKUBI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_AKUBI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ASENUGUIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ATAMAKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ATAMAKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYEBYEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_BYE_WALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK+3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK-1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK-2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_AGO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_MOVE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_MOVEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_PEN_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_RYOTE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_DESK_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_FALL',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GAKKARI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_GOUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_GOUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_GOUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHUc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HAKUSHU_2c',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HANASIKAKEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HITEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HITEI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASSc',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASSc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_GLASS_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_CUP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_CUPc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKI_w',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOLD_JOKKIc_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOOKAKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_HOOKAKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_INORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KABEMOTARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAIWA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAMIHARAI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KANGEI2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KAZETUYO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEIREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KEYBOARD_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHOa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHOb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_2_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3b',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KINCHO_3_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_KUZUSISUWARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MEGANEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MOKUREIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_MUKKII',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_ODOROKI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_OJIGIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLDa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_HOLD_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_LOOK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_MISERU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_MISERUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_SOUSA_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALKa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_PHONE_TALK_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_REIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_GYUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_ATAMA_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_AWASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_KOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_MAE_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_RYOTE_SIRI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SEKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SEKI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIAN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIANFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_DOWN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_D',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SITN_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_JIMEN',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SIT_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEPa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_GAKE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_GAKEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SLEEP_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SQUAT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_SQUATa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_1',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_2',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_3',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TAORE_4',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'EV_TEBURI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEBURI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSIb_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEKOSI_t_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEMUNE_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TEUKASEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_TORIDASI_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMI_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIFa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIFb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UDEGUMIF_t',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_UKETORIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASUa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASUb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_s',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_sa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_WATASU_KAMI_sb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YAREYARE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YARUKIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUME',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUME_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUMEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YASUMEa_U',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YORIKAKARIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFT',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFTa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_LEFTb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITA',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITAa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_SITAb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MAEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UE',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UEa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_UEb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGI',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGIa',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHRX01_EV',
            symbol     = 'EV_YUBISASI_MIGIb',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev00025',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev00025a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev03020',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev03025',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev03025a',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev30150',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev32030',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev35000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev45005',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev86000',
        ),
        ScenaAnimeClipTableEntry(
            catalog    = 0x00000002,
            asset      = 'C_CHR033_EV',
            symbol     = 'ev86000a',
        ),
    )

# id: 0x0001 offset: 0x6CE4
@scena.Code('Init')
def Init():
    AnimeClipCmd(0x04, 0xFFFE, 'C_CHR033_BT1', '')
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0002 offset: 0x6D04
@scena.Code('DefaultFace')
def DefaultFace():
    SetChrFace(0x03, 0xFFFE, '0[autoE0]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0003 offset: 0x6D2C
@scena.Code('Ani_EV_Load')
def Ani_EV_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0004 offset: 0x6D38
@scena.Code('Ani_BT1_Load')
def Ani_BT1_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000100 | 2)

    Return()

# id: 0x0005 offset: 0x6D44
@scena.Code('Ani_SC1_Load')
def Ani_SC1_Load():
    AnimeClipLoadByCatalog(0xFFFE, 0x00000010)

    Return()

# id: 0x0006 offset: 0x6D50
@scena.Code('Ani_EV_Release')
def Ani_EV_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000002)

    Return()

# id: 0x0007 offset: 0x6D5C
@scena.Code('Ani_BT1_Release')
def Ani_BT1_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000100 | 2)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0008 offset: 0x6D70
@scena.Code('Ani_SC_Release')
def Ani_SC_Release():
    AnimeClipReleaseByCatalog(0xFFFE, 0x00000010)
    OP_04(0x0B, 'SpringOn')

    Return()

# id: 0x0009 offset: 0x6D84
@scena.Code('AniAttachMainWeapon')
def AniAttachMainWeapon():
    LoadAsset('C_EQU090')
    AttachEquip(0xFFFE, 'C_EQU090', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x000A offset: 0x6DE0
@scena.Code('AniDetachMainWeapon')
def AniDetachMainWeapon():
    ReleaseAsset('C_EQU090')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x000B offset: 0x6E24
@scena.Code('AniReset')
def AniReset():
    Call(ScriptId.Current, 'DefaultFace')
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x000C offset: 0x6E54
@scena.Code('AniSetWorkWait')
def AniSetWorkWait():
    Return()

# id: 0x000D offset: 0x6E58
@scena.Code('SpringOn')
def SpringOn():
    OP_8A(0xFE, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftFH02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'LeftMA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMB05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'RightMA05', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM01', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM02', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM03', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM04', 0.2)
    OP_8A(0xFE, 0xFFFE, 'BM05', 0.2)

    Return()

# id: 0x000E offset: 0x72B8
@scena.Code('SpringOff')
def SpringOff():
    OP_8A(0xFF, 0xFFFE, 'FH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftFH02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightHD05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'FS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BS05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftSB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'LeftMA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMB05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'RightMA05', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM01', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM02', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM03', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM04', 0.2)
    OP_8A(0xFF, 0xFFFE, 'BM05', 0.2)

    Return()

# id: 0x000F offset: 0x7718
@scena.Code('SpringEvOff')
def SpringEvOff():
    Return()

# id: 0x0010 offset: 0x771C
@scena.Code('AniBtl_AttackAttachEquip')
def AniBtl_AttackAttachEquip():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')

    Return()

# id: 0x0011 offset: 0x7748
@scena.Code('AniBtl_AttackTest')
def AniBtl_AttackTest():
    CreateThread(0xFFFE, 0x01, ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0012 offset: 0x7788
@scena.Code('AniWait_Test1')
def AniWait_Test1():
    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 1.0, 1.03333, -1.0, 0x00, 0x00)

    Return()

# id: 0x0013 offset: 0x77A8
@scena.Code('AniBtlWait_Test1')
def AniBtlWait_Test1():
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.0, 10.0, 10.0333, -1.0, 0x00, 0x00)

    Return()

# id: 0x0014 offset: 0x77CC
@scena.Code('AniTurn')
def AniTurn():
    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_7809',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_7828')

    def _loc_7809(): pass

    label('loc_7809')

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_7828(): pass

    label('loc_7828')

    Sleep(250)
    OP_38(0xFFFE, 0x00, 0x00, 'AniWait')

    Return()

# id: 0x0015 offset: 0x783C
@scena.Code('AniWait')
def AniWait():
    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x80000),
            Expr.And,
            Expr.Return,
        ),
        'loc_788C',
    )

    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_7905')

    def _loc_788C(): pass

    label('loc_788C')

    If(
        (
            (Expr.Eval, "ChrPhysicsCmd(0x02, 0xFFFE, 0x00000000)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_78DE',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Jump('loc_7905')

    def _loc_78DE(): pass

    label('loc_78DE')

    PlayChrAnimeClip(0xFFFE, 'WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    def _loc_7905(): pass

    label('loc_7905')

    Return()

# id: 0x0016 offset: 0x7908
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
        'loc_795F',
    )

    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_797E')

    def _loc_795F(): pass

    label('loc_795F')

    PlayChrAnimeClip(0xFFFE, 'WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_797E(): pass

    label('loc_797E')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0017 offset: 0x7988
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
        'loc_79D2',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_79F0')

    def _loc_79D2(): pass

    label('loc_79D2')

    PlayChrAnimeClip(0xFFFE, 'RUN', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_79F0(): pass

    label('loc_79F0')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0018 offset: 0x79FC
@scena.Code('AniSitWait')
def AniSitWait():
    Call(ScriptId.Current, 'SpringOff')
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'SIT_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0019 offset: 0x7A34
@scena.Code('AniWait1')
def AniWait1():
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'WAIT1', 0x01, 0x01, 0x00, 0x00, 0x01, -2.0, -0.0333333, -0.0333333, -0.0333333, 0x00, 0x00)

    Return()

# id: 0x001A offset: 0x7A64
@scena.Code('StopAnimeSlot1')
def StopAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)
    Call(ScriptId.CurrentCharacter, 'SpringOn')

    Return()

# id: 0x001B offset: 0x7A94
@scena.Code('StopSitAnimeSlot1')
def StopSitAnimeSlot1():
    PlayChrAnimeClip(0xFFFE, '_stop_', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x01, 0x00)

    Return()

# id: 0x001C offset: 0x7AB8
@scena.Code('AniAttachPhone')
def AniAttachPhone():
    LoadAsset('C_EQU320')
    AttachEquip(0xFFFE, 'C_EQU320', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x001D offset: 0x7B14
@scena.Code('AniDetachPhone')
def AniDetachPhone():
    ReleaseAsset('C_EQU320')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x001E offset: 0x7B5C
@scena.Code('ShowEquip')
def ShowEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_2A(0x00, 0xFFFE, '', 'L_arm_point', 0x01)

    Return()

# id: 0x001F offset: 0x7B84
@scena.Code('EraseEquip')
def EraseEquip():
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x00)
    OP_2A(0x00, 0xFFFE, '', 'L_arm_point', 0x00)

    Return()

# id: 0x0020 offset: 0x7BAC
@scena.Code('AniAttachEquip')
def AniAttachEquip():
    Call(ScriptId.Current, 'AniEquipEQU092_R')
    Call(ScriptId.Current, 'AniEquipEQU092_L')

    Return()

# id: 0x0021 offset: 0x7BD8
@scena.Code('BtlDefaultFace')
def BtlDefaultFace():
    SetChrFace(0x03, 0xFFFE, '2[autoE2]', '0[autoM0]', '0[autoB0]', '#b', '0')

    Return()

# id: 0x0022 offset: 0x7C00
@scena.Code('AniBtlInit')
def AniBtlInit():
    Call(ScriptId.Current, 'Ani_BT1_Load')
    Call(ScriptId.BtlCom, 'AniBtlInit')
    ReleaseEffect(0xFFFE, 0x82)
    ReleaseEffect(0xFFFE, 0x83)
    ReleaseEffect(0xFFFE, 0x80)
    LoadEffect(0xFFFE, 0x82, 'battle/atk033_0.eff')
    LoadEffect(0xFFFE, 0x83, 'battle/atk033_1.eff')
    LoadEffect(0xFFFE, 0x80, 'battle/moncharge.eff')
    LoadAsset('C_EQU090')
    AttachEquip(0xFFFE, 'C_EQU090', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    AnimeClipCmd(0x04, 0xFFFE, 'C_CHR033_BT1', '')
    Call(ScriptId.Current, 'SpringOff')
    OP_04(0x0B, 'AniWait')

    Return()

# id: 0x0023 offset: 0x7CDC
@scena.Code('AniBtlStart')
def AniBtlStart():
    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x195),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D32',
    )

    OP_3B(0x32, (0xFF, 0x1B58, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_7DCB')

    def _loc_7D32(): pass

    label('loc_7D32')

    If(
        (
            (Expr.PushValueByIndex, 0x3),
            (Expr.PushLong, 0x19B),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_7D88',
    )

    OP_3B(0x32, (0xFF, 0x1B5A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_7DCB')

    def _loc_7D88(): pass

    label('loc_7D88')

    OP_3B(0x32, (0xFF, 0x1B5C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFE, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_7DCB(): pass

    label('loc_7DCB')

    OP_3B(0x39, 0xFFFE)

    Return()

# id: 0x0024 offset: 0x7DD0
@scena.Code('AniBtlReady')
def AniBtlReady():
    Return()

# id: 0x0025 offset: 0x7DD4
@scena.Code('AniBtlWait')
def AniBtlWait():
    # ChrSetAbnormalStatus(0xFFFE, AbnormalStatus.Death | AbnormalStatus.Deathblow, 0xff, 0xff)
    # ChrSetBattleFlags(0xFFFE, 0x1)
    Call(ScriptId.Current, 'BtlDefaultFace')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0026 offset: 0x7E0C
@scena.Code('AniBtlMove')
def AniBtlMove():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, 0.5)
    Call(ScriptId.BtlCom, 'AniBtlMove')

    Return()

# id: 0x0027 offset: 0x7E40
@scena.Code('AniBtlTurn')
def AniBtlTurn():
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x0028 offset: 0x7E64
@scena.Code('AniBtlAttack')
def AniBtlAttack():
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x48, 0xFFFB)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCreateChrAfterImage(0xFFFE)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, 66.6667, 67.2, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x01, 0x01, 0x00, 0x01, 0x00, 0.2, 67.2333, 67.4333, -0.0333333, 0x00, 0x00)

    If(
        (
            (Expr.Eval, "BattleCmd(0x62, 0xFFFE, 0x0A)"),
            (Expr.PushLong, 0x2),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F57',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_7F3B',
    )

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1B8A, 0x0), (0xFF, 0x1B8B, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    Jump('loc_7F57')

    def _loc_7F3B(): pass

    label('loc_7F3B')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1B5E, 0x0), (0xFF, 0x1B5F, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_7F57(): pass

    label('loc_7F57')

    OP_6C(0xFFFE, 1.0)
    BattleSetChrAfterImageOn(0xFFFE, 0.1, 0.1, 0.22, 0.45, 1.0)
    SetChrFace(0x03, 0xFFFE, '2', '2', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x82, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 0.75, 0x0), (0xEE, 0.75, 0x0), (0xEE, 0.75, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAE, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -2.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlAttackDamageAnime00')
    CameraCmd(0x0A, 0.3, 0.25, 0.1, 0x001E, 0x03E8, 0x0190, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.15, 0x001E, 0x03E8, 0x02BC, 0.3, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Sleep(166)
    Sleep(166)
    WaitForThreadExit(0xFFFE, 0x02)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlAttackDamageAnime00')
    Sleep(166)
    Sleep(166)
    WaitForThreadExit(0xFFFE, 0x02)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlAttackDamageAnime00')
    Sleep(333)
    BattleSetChrAfterImageOff()
    Sleep(166)
    BattleSetChrAfterImageOn(0xFFFE, 0.1, 0.1, 0.22, 0.45, 1.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.4, 68.3, 68.5, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.4, 68.5333, 68.6, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.4)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x01, 0x00, 0x00, 0x00, 0.05, 68.6333, -1.0, -1.0, 0x00, 0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFB)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    PlayEffect(0xFFFE, (0xFF, 0x83, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCmd(0x0A, 0.64, 0.3, 0.2, 0x001E, 0x0258, 0x0258, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.25, 0x001E, 0x02BC, 0x02BC, 0.45, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x05DC, 0x012C, 0x0000, 0x05DC, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F66, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x05DC, 0x012C, 0x0000, 0x05DC, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlAttackDamage01')
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    Sleep(133)
    OP_6C(0xFFFE, 0.2)
    BattleSetChrAfterImageOff()
    Sleep(266)
    OP_6C(0xFFFE, 1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    WaitForThreadExit(0xFFFE, 0x02)

    Return()

# id: 0x0029 offset: 0x82C4
@scena.Code('AniBtlCounter')
def AniBtlCounter():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_8324',
    )

    OP_3B(0x32, (0xFF, 0x1B9B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_8367')

    def _loc_8324(): pass

    label('loc_8324')

    OP_3B(0x32, (0xFF, 0x1B74, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_8367(): pass

    label('loc_8367')

    Call(ScriptId.BtlCom, 'AniBtlCounter')

    Return()

# id: 0x002A offset: 0x837C
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
        'loc_83C9',
    )

    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_83EE')

    def _loc_83C9(): pass

    label('loc_83C9')

    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x01, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_83EE(): pass

    label('loc_83EE')

    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x002B offset: 0x83F8
@scena.Code('AniBtlDamageVoice')
def AniBtlDamageVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_8498',
    )

    If(
        (
            (Expr.Eval, "ChrGetAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_8477',
    )

    OP_3B(0x32, (0xFF, 0x1B9A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_8493')

    def _loc_8477(): pass

    label('loc_8477')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1B98, 0x0), (0xFF, 0x1B99, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_8493(): pass

    label('loc_8493')

    Jump('loc_851B')

    def _loc_8498(): pass

    label('loc_8498')

    If(
        (
            (Expr.Eval, "ChrGetAbnormalStatus2(0xFFFE)"),
            (Expr.PushLong, 0x10),
            Expr.And,
            Expr.Return,
        ),
        'loc_84FF',
    )

    OP_3B(0x32, (0xFF, 0x1B73, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_851B')

    def _loc_84FF(): pass

    label('loc_84FF')

    OP_3B(0x3A, 0xFFFE, (0xFF, 0x1B71, 0x0), (0xFF, 0x1B72, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0))

    def _loc_851B(): pass

    label('loc_851B')

    Return()

# id: 0x002C offset: 0x851C
@scena.Code('AniBtlGuardBreakVoice')
def AniBtlGuardBreakVoice():
    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_857C',
    )

    OP_3B(0x32, (0xFF, 0x1B96, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_85BF')

    def _loc_857C(): pass

    label('loc_857C')

    OP_3B(0x32, (0xFF, 0x1B6F, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_85BF(): pass

    label('loc_85BF')

    Return()

# id: 0x002D offset: 0x85C0
@scena.Code('AniBtlSwoon')
def AniBtlSwoon():
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')

    If(
        (
            (Expr.Eval, "OP_B4()"),
            (Expr.PushLong, 0x1),
            Expr.And,
            Expr.Return,
        ),
        'loc_860A',
    )

    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)

    Jump('loc_865E')

    def _loc_860A(): pass

    label('loc_860A')

    OP_80(0.2)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    def _loc_865E(): pass

    label('loc_865E')

    Return()

# id: 0x002E offset: 0x8660
@scena.Code('AniBtlWeak')
def AniBtlWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)

    Return()

# id: 0x002F offset: 0x86A0
@scena.Code('AniBtlTensionMax')
def AniBtlTensionMax():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle_sys/tensionmax.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr033_03_0.eff')
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.08, 1.3, -0.01, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 11.0, -13.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.7, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.08, 1.3, -0.01, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, -5.0, 0.0, 700, 0x01)
    CameraSetDistance(0x03, 1.6, 700)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_87EC',
    )

    OP_3B(0x32, (0xFF, 0x1B92, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_882F')

    def _loc_87EC(): pass

    label('loc_87EC')

    OP_3B(0x32, (0xFF, 0x1B66, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_882F(): pass

    label('loc_882F')

    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F79, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2,11111133', '0000JH0', '0', '#b', '0')
    Sleep(666)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8FA6, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(100)
    SetChrFace(0x03, 0xFFFE, '3773', '2662', '0', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, -0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_8AAF',
    )

    OP_3B(0x32, (0xFF, 0x1B93, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_8AF2')

    def _loc_8AAF(): pass

    label('loc_8AAF')

    OP_3B(0x32, (0xFF, 0x1B67, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_8AF2(): pass

    label('loc_8AF2')

    OP_3B(0xFF, 0.5, 0.7, 0.4)
    OP_6C(0xFFFE, 1.2)
    SetChrFace(0x03, 0xFFFE, '6662', '733131313333', '0', '#b', '0')
    CameraCmd(0x0A, 0.008, 0.008, 0.0, 0x03E8, 0x03E8, 0x01F4, 0x0000, 0x0000, 0x00)
    OP_5E(0x00, 0x0002, 0.1, 0x00C8, 0x05DC, 0x0190, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 0.75, 0.0, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 1.0, 1.0, 700, 0x01)
    CameraSetDistance(0x03, 5.5, 700)
    Sleep(333)
    CameraCmd(0x11, 0x03, 0.0, 20.0, 0.0, 0x1388, 0x01)
    CameraCmd(0x16, 0x03, 2.4, 5000)
    CameraCmd(0x0C, 0x03, 0.0, -0.1, 0.0, 5000)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_02a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(666)
    Call(ScriptId.Current, 'SpringOn')
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'ReleaseEffect')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0030 offset: 0x8C40
@scena.Code('AniBtlDying')
def AniBtlDying():
    Call(ScriptId.Current, 'AniBtlDamage')
    Sleep(1000)

    Return()

# id: 0x0031 offset: 0x8C54
@scena.Code('AniBtlDead')
def AniBtlDead():
    If(
        (
            (Expr.Eval, "BattleCmd(0x0D, 0xFFFE)"),
            Expr.Not,
            (Expr.PushLong, 0x10000),
            Expr.And,
            Expr.Return,
        ),
        'loc_8D09',
    )

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_8CC6',
    )

    OP_3B(0x32, (0xFF, 0x1B97, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_8D09')

    def _loc_8CC6(): pass

    label('loc_8CC6')

    OP_3B(0x32, (0xFF, 0x1B70, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_8D09(): pass

    label('loc_8D09')

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0xF04B),
            (Expr.PushLong, 0xF043),
            Expr.Sub,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_8D21(): pass

    label('loc_8D21')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8DE8',
    )

    ExecExpressionWithReg(
        0x04,
        (
            (Expr.PushLong, 0xF043),
            (Expr.PushReg, 0x2),
            Expr.Add,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, (0x11, 0x4, 0x0), 'chr033')"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8DDA',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, (0x11, 0x4, 0x0), 'chr035')"),
            Expr.Return,
        ),
        'loc_8D80',
    )

    BattleCmd(0xBB, (0x11, 0x2, 0x0), (0xFF, 0x0, 0x0))

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x1),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_8D80(): pass

    label('loc_8D80')

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, (0x11, 0x4, 0x0), 'chr039')"),
            Expr.Return,
        ),
        'loc_8DAD',
    )

    BattleCmd(0xBB, (0x11, 0x2, 0x0), (0xFF, 0x1, 0x0))

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x2),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_8DAD(): pass

    label('loc_8DAD')

    If(
        (
            (Expr.Eval, "BattleCmd(0xBA, (0x11, 0x4, 0x0), 'chr037')"),
            Expr.Return,
        ),
        'loc_8DDA',
    )

    BattleCmd(0xBB, (0x11, 0x2, 0x0), (0xFF, 0x2, 0x0))

    ExecExpressionWithReg(
        0x03,
        (
            (Expr.PushLong, 0x4),
            Expr.Or2,
            Expr.Return,
        ),
    )

    def _loc_8DDA(): pass

    label('loc_8DDA')

    ExecExpressionWithReg(
        0x02,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_8D21')

    def _loc_8DE8(): pass

    label('loc_8DE8')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_8E2E',
    )

    If(
        (
            (Expr.Eval, "BattleCmd(0x0F, 0xF080, 0x0000)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8E2E',
    )

    DebugLog(0x00, (0xFF, 0xA, 0x0))
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlRelease')
    WaitForThreadExit(0xFFFE, 0x02)

    def _loc_8E2E(): pass

    label('loc_8E2E')

    SetChrFace(0x03, 0xFFFE, 'B', '1', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Sleep(500)

    Return()

# id: 0x0032 offset: 0x8E74
@scena.Code('AniBtlAria')
def AniBtlAria():
    Call(ScriptId.BtlCom, 'AniBtlAria', (0xFF, 0x1B68, 0x0), (0xFF, 0x0, 0x0), (0xEE, -1.0, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x0033 offset: 0x8E9C
@scena.Code('AniBtlArts')
def AniBtlArts():
    Call(ScriptId.BtlCom, 'AniBtlArts', (0xFF, 0x1B69, 0x0), (0xFF, 0x0, 0x0), (0xDD, 'NODE_CENTER'))

    Return()

# id: 0x0034 offset: 0x8EC4
@scena.Code('AniBtlCharge')
def AniBtlCharge():
    If(
        (
            (Expr.Eval, "BattleCmd(0x62, 0xFFFE, 0x0E)"),
            Expr.Return,
        ),
        'loc_8F5B',
    )

    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)

    Jump('loc_903D')

    def _loc_8F5B(): pass

    label('loc_8F5B')

    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.5)
    PlayEffect(0xFFFE, (0xFF, 0x80, 0x0), 0xFFFE, 0x00000103, (0xDD, 'NODE_CENTER'), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), (0xFF, 0x0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x00)
    OP_3B(0x00, (0xFF, 0xFD5, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.5)
    Sleep(1000)

    def _loc_903D(): pass

    label('loc_903D')

    Return()

# id: 0x0035 offset: 0x9040
@scena.Code('AniBtlRelease')
def AniBtlRelease():
    BattleCmd(0x47)
    CameraCmd(0x00)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_905C',
    )

    BattleCmd(0x48, 0xF080)

    def _loc_905C(): pass

    label('loc_905C')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9074',
    )

    BattleCmd(0x48, 0xF081)

    def _loc_9074(): pass

    label('loc_9074')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_908C',
    )

    BattleCmd(0x48, 0xF082)

    def _loc_908C(): pass

    label('loc_908C')

    BattleCmd(0x46, 0.5, 6.0, 15.0)
    Sleep(666)

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x1),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_90DD',
    )

    BattleClearChrAbnormalStatus(0xF080, 0x00008000)
    BattleClearChrAbnormalStatus(0xF080, 0x00400000)
    DebugLog(0x00, (0xFF, 0xA, 0x0))

    def _loc_90DD(): pass

    label('loc_90DD')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x2),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_9115',
    )

    BattleClearChrAbnormalStatus(0xF081, 0x00008000)
    BattleClearChrAbnormalStatus(0xF081, 0x00400000)

    def _loc_9115(): pass

    label('loc_9115')

    If(
        (
            (Expr.PushReg, 0x3),
            (Expr.PushLong, 0x4),
            Expr.And,
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_914D',
    )

    BattleClearChrAbnormalStatus(0xF082, 0x00008000)
    BattleClearChrAbnormalStatus(0xF082, 0x00400000)

    def _loc_914D(): pass

    label('loc_914D')

    Sleep(666)

    Return()

# id: 0x0036 offset: 0x9154
@scena.Code('AniBtlCraft00')
def AniBtlCraft00():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr033_00_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr033_00_1.eff')
    LoadEffect(0xFFFE, 0x9F, 'battle/damage02.eff')
    BattleTargetsIterInit(0x00)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    SetChrFace(0x03, 0xFFFE, '3', '2[autoM2]', '5', '3', '0')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 0.95, -0.22, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -14.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.1, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.75, -0.1, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -15.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 3.5, 1000)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_9316',
    )

    OP_3B(0x32, (0xFF, 0x1B8C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_9359')

    def _loc_9316(): pass

    label('loc_9316')

    OP_3B(0x32, (0xFF, 0x1B60, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_9359(): pass

    label('loc_9359')

    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAD, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), 0.6, (0xFF, 0x64, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    SetChrFace(0x03, 0xFFFE, '2', '2[autoM2]', '0', '2', '0')
    Sleep(500)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2', '2', '0', '#b', '0')
    Sleep(233)
    OP_5E(0x00, 0x0000, 0.35, 0x00C8, 0x03E8, 0x0190, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(100)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x48, 0xFFF9)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    SetChrFace(0x03, 0xFFFE, '2', '17', '', '#b', '0')
    OP_3B(0x00, (0xFF, 0x8FA6, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FC1, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x00C8, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(133)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_9601',
    )

    OP_3B(0x32, (0xFF, 0x1B8D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_9644')

    def _loc_9601(): pass

    label('loc_9601')

    OP_3B(0x32, (0xFF, 0x1B61, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_9644(): pass

    label('loc_9644')

    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -1.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCmd(0x0A, 0.02, 0.008, 0.0, 0x0064, 0x00FA, 0x0064, 0x0000, 0x0000, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFF5, 0.0, 0.0, 1.5, 6.0, 0x00, 0x00)
    BattleCmd(0x47)
    CameraCmd(0x16, 0x02, 5.5, 1000)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlCraftDamage')
    BattleCmd(0x3A, 0xFFFE)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 1.0, 4.0, 0x00, 0x00)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '2', '12', '', '#b', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitForThreadExit(0xFFFE, 0x02)
    ReleaseEffect(0xFFFE, 0x90)
    ReleaseEffect(0xFFFE, 0x91)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0037 offset: 0x97A0
@scena.Code('AniBtlCraft01')
def AniBtlCraft01():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr033_01_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr033_01_1.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr033_01_2.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/cr033_01_3.eff')
    LoadEffect(0xFFFE, 0x94, 'battle/cr033_01_4.eff')
    LoadEffect(0xFFFE, 0x95, 'battle/cr033_01_5.eff')
    LoadEffect(0xFFFE, 0x9F, 'battle/damage02.eff')
    BattleTargetsIterInit(0x00)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    SetChrFace(0x03, 0xFFFE, '3', '2[autoM2]', '5', '3', '0')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.01, 1.2, 0.06, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -4.0, -1.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.2, 0)
    CameraCmd(0x0B, 0x03, 36.0, 0x0000)
    CameraCmd(0x16, 0x03, 0.5, 3000)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(333)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_99D1',
    )

    OP_3B(0x32, (0xFF, 0x1B8E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_9A14')

    def _loc_99D1(): pass

    label('loc_99D1')

    OP_3B(0x32, (0xFF, 0x1B62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_9A14(): pass

    label('loc_9A14')

    Sleep(666)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '8', '6', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F72, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FB4, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    CameraCmd(0x14, 0x02, 0xFFFE, '', 0.03, 2.03, 0.05, 500)
    CameraRotateByTarget(0xFFFE, '', 0x02, -9.0, -3.0, 0.0, 500, 0x01)
    CameraCmd(0x05, 0x02, 6.3, 500)
    CameraCmd(0x0B, 0x02, 42.0, 0x01F4)
    OP_5E(0x00, 0x0002, 0.15, 0x000A, 0x0190, 0x012C, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x94, 0x0), 0xFFFE, 0x00000003, (0xDD, 'R_arm_point:NODE_EFFECT01'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -2.299999952316284, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAC, 0x0), 0.6, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(266)
    CameraCmd(0x16, 0x03, 4.0, 5000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -25.0, -3.0, 0.0, 5000, 0x01)
    CameraCmd(0x0C, 0x03, 0.0, 2.24208e-44, 0.0, 5000)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '6', '2[autoM2]', '1', '6', '0')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Fade(0x65, 250, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.0, 3.9, -5.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -25.0, 0.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.5, 0)
    CameraCmd(0x0C, 0x03, 0.0, 0.5, 0.0, 4000)
    ChrSetPhysicsFlags(0xFFFE, 0x00000080)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x8F93, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_9DAD',
    )

    OP_3B(0x32, (0xFF, 0x1B8F, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_9DF0')

    def _loc_9DAD(): pass

    label('loc_9DAD')

    OP_3B(0x32, (0xFF, 0x1B63, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_9DF0(): pass

    label('loc_9DF0')

    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.5, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 15.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.5, 0)
    Sleep(0)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x48, 0xFFF9)
    BattleCmd(0x8A)
    BattleCmd(0x46, 0.5, 6.0, 15.0)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraCmd(0x07, 0x00BF)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFE, 0x00000004, (0xDD, 'R_arm_point:NODE_EFFECT01'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, -0.5, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, -0.5, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    StopEffect(0xFFFE, 0x02, 0x01)
    CameraCmd(0x0A, 0.0, 0.2, 0.0, 0x0000, 0x01F4, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0x00, (0xFF, 0x8FA6, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FC1, 0x0), 0.5, (0xFF, 0x0, 0x0), 0.0, -1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0384, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.7, 0.9, 0.15)
    Sleep(433)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlCraftDamage01')
    CameraCmd(0x0A, 0.0, 1.25, 0.0, 0x0000, 0x012C, 0x0064, 0x0000, 0x0000, 0x00)
    Sleep(1500)
    Call(ScriptId.Current, 'BtlDefaultFace')
    WaitForThreadExit(0xFFFE, 0x02)
    ReleaseEffect(0xFFFE, 0x90)
    ReleaseEffect(0xFFFE, 0x91)
    ReleaseEffect(0xFFFE, 0x92)
    ReleaseEffect(0xFFFE, 0x93)
    ReleaseEffect(0xFFFE, 0x94)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x0038 offset: 0xA078
@scena.Code('AniBtlCraftDamage')
def AniBtlCraftDamage():
    Call(ScriptId.BtlCom, 'AniBtlDamageTargets', (0xFF, 0x3F8, 0x0), (0xDD, 'NODE_CENTER'), (0xEE, 1.0, 0x0), (0xFF, 0x3, 0x0), (0xFF, 0xFFFF, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0))

    Return()

# id: 0x0039 offset: 0xA0C4
@scena.Code('AniBtlCraftDamage01')
def AniBtlCraftDamage01():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_A0CC(): pass

    label('loc_A0CC')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_A192',
    )

    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFB, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x3F8, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(50)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_A0CC')

    def _loc_A192(): pass

    label('loc_A192')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x003A offset: 0xA198
@scena.Code('AniBtlAttackDamage00')
def AniBtlAttackDamage00():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_A1A0(): pass

    label('loc_A1A0')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_A1D5',
    )

    Sleep(30)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_A1A0')

    def _loc_A1D5(): pass

    label('loc_A1D5')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x003B offset: 0xA1DC
@scena.Code('AniBtlAttackDamage01')
def AniBtlAttackDamage01():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_A1E4(): pass

    label('loc_A1E4')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_A219',
    )

    Sleep(30)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_A1E4')

    def _loc_A219(): pass

    label('loc_A219')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x003C offset: 0xA220
@scena.Code('AniBtlAttackDamageAnime00')
def AniBtlAttackDamageAnime00():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_A228(): pass

    label('loc_A228')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_A256',
    )

    Sleep(30)
    BattleDamageAnime(0xFFFB, (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0x01)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_A228')

    def _loc_A256(): pass

    label('loc_A256')

    BattleTargetsIterReset(0x01, 0xFFFE)

    Return()

# id: 0x003D offset: 0xA25C
@scena.Code('AniBtlCraft02')
def AniBtlCraft02():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x90, 'battle/cr033_00_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/cr033_02_1.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/cr033_02_2.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/cr033_02_3.eff')
    BattleTargetsIterInit(0x00)
    Call(ScriptId.Current, 'SpringOff')
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0001)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    OP_46(0x00, 0xFFFE, 0xFFFF, 0x0000)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCmd(0x47)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.17, 0.83, -0.03, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 9.0, 17.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x14, 0x02, 0xFFFE, '', -0.16, 0.76, -0.36, 800)
    CameraRotateByTarget(0xFFFE, '', 0x02, 17.0, 35.0, 0.0, 800, 0x01)
    CameraCmd(0x05, 0x02, 3.3, 800)
    CameraCmd(0x0B, 0x02, 40.0, 0x0320)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_01', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '2', '2[autoM2]', '0', '2', '0')
    Sleep(166)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_A47E',
    )

    OP_3B(0x32, (0xFF, 0x1B90, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_A4C1')

    def _loc_A47E(): pass

    label('loc_A47E')

    OP_3B(0x32, (0xFF, 0x1B64, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_A4C1(): pass

    label('loc_A4C1')

    Sleep(333)
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFE, 0x0000000C, (0xDD, ''), (0xEE, -0.30000001192092896, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.30000001192092896, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8FAD, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F78, 0x0), 0.7, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000003, (0xDD, 'R_arm_point:NODE_EFFECT01'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -2.4000000953674316, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F69, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '3', '2[autoM2]', '5', '3', '0')
    Sleep(500)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFE, 0x00000003, (0xDD, 'R_arm_point:NODE_EFFECT01'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(166)
    SetChrFace(0x03, 0xFFFE, '2', '6[autoM6]', '7', '2', '0')
    Sleep(166)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.15, 0.84, 0.2, 600)
    CameraRotateByTarget(0xFFFE, '', 0x03, 26.2, 11.0, 0.0, 600, 0x01)
    CameraSetDistance(0x03, 4.4, 600)
    Sleep(166)
    OP_3B(0x00, (0xFF, 0x8F02, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    If(
        (
            (Expr.Eval, "IsBattleModelEqualTo(0xFFFE, 'C_CHR033_C00')"),
            Expr.Return,
        ),
        'loc_A7CF',
    )

    OP_3B(0x32, (0xFF, 0x1B91, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    Jump('loc_A812')

    def _loc_A7CF(): pass

    label('loc_A7CF')

    OP_3B(0x32, (0xFF, 0x1B65, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)

    def _loc_A812(): pass

    label('loc_A812')

    Sleep(133)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    CameraCmd(0x16, 0x03, 4.0, 500)
    Sleep(100)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F02, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0384, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    Sleep(333)
    OP_3B(0x00, (0xFF, 0x8F07, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0384, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(100)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlCraftDamage02')
    OP_5E(0x00, 0x0002, 0.4, 0x00C8, 0x01F4, 0x0190, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    CameraCmd(0x0A, 0.2, 0.35, 0.0, 0x0000, 0x012C, 0x0064, 0x0000, 0x0014, 0x00)
    OP_3B(0x00, (0xFF, 0x8F0C, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0384, 0x012C, 0x0000, 0x0384, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    BattleCmd(0x47)
    CameraCmd(0x05, 0x02, 12.5, 500)
    CameraCmd(0x14, 0x02, 0xFFFE, '', -0.15, 0.5, 0.8, 500)
    CameraRotateByTarget(0xFFFE, '', 0x02, 26.0, 10.0, 0.0, 500, 0x01)
    CameraCmd(0x0B, 0x03, 50.0, 0x1388)
    OP_4E(1.0, 0.0, 0x03)
    Sleep(1266)
    OP_3B(0x01, (0xFF, 0x8F0C, 0x0), (0xFF, 0x7D0, 0x0))
    WaitForThreadExit(0xFFFE, 0x02)
    ReleaseEffect(0xFFFE, 0x90)
    ReleaseEffect(0xFFFE, 0x91)
    ReleaseEffect(0xFFFE, 0x92)
    ReleaseEffect(0xFFFE, 0x93)
    Call(ScriptId.Current, 'BtlDefaultFace')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')

    Return()

# id: 0x003E offset: 0xAA3C
@scena.Code('AniBtlCraftDamage02')
def AniBtlCraftDamage02():
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_AA41(): pass

    label('loc_AA41')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_AB07',
    )

    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 2.5, 0x0), (0xEE, 0.5, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3F8, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8BF0, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(100)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_AA41')

    def _loc_AB07(): pass

    label('loc_AB07')

    Return()

# id: 0x003F offset: 0xAB08
@scena.Code('AniBtlCraft03')
def AniBtlCraft03():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x98, 'battle/crdh03_0.eff')
    LoadEffect(0xFFFE, 0x99, 'battle/crdh03_1.eff')
    LoadEffect(0xFFFE, 0x9A, 'battle/damage02.eff')
    LoadEffect(0xFFFE, 0x9B, 'battle/crdh04_6.eff')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    BattleSaveChrPosition(0xFFFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFF5, 0.0, -1.0)
    BattleCreateChrDummy(0xFFFE, 5)
    ChrSetPhysicsFlags(0xFFFE, 0x00000800)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B61, 0x00000020)
    ChrSetPhysicsFlags(0x0B5E, 0x00000080)
    ChrSetPhysicsFlags(0x0B5F, 0x00000080)
    ChrSetPhysicsFlags(0x0B60, 0x00000080)
    ChrSetPhysicsFlags(0x0B61, 0x00000080)
    BattleSetChrPos(0x0B5E, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B5F, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B60, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B61, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B5E, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B5F, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B60, 0xFFF5, 0.0, -1.0)
    BattleTurnChrDirection(0x0B61, 0xFFF5, 0.0, -1.0)
    BattleSetChrPos(0x0B62, 0xFFFE, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5E, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5F, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B60, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B61, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B5E, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B5F, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B60, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B61, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B5E, 0x00000040)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000040)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000040)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B61, 0x00000040)
    ChrSetPhysicsFlags(0x0B61, 0x00000020)
    ChrSetPhysicsFlags(0x0B62, 0x00000040)
    ChrSetPhysicsFlags(0x0B62, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.1, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.2, 2200)
    CameraRotateByTarget(0xFFFE, '', 0x03, 8.0, -48.0, 0.0, 2200, 0x01)
    CameraSetDistance(0x03, 1.85, 2200)
    CreateThread(0xFFFE, 0x01, ScriptId.Current, 'AniBtlCraft03_Mouth01')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5E, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5F, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B60, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B61, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.15, 90.1, 90.1, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.75)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayChrAnimeClip(0x0B5E, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B5E, 0.675)
    ChrClearPhysicsFlags(0x0B5E, 0x00000040)
    ChrClearPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B5E, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B5F, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B5F, 0.6)
    ChrClearPhysicsFlags(0x0B5F, 0x00000040)
    ChrClearPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetRGBA(0x0B5F, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B5F, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B60, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B60, 0.525)
    ChrClearPhysicsFlags(0x0B60, 0x00000040)
    ChrClearPhysicsFlags(0x0B60, 0x00000020)
    ChrSetRGBA(0x0B60, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B60, '2', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B61, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.25, 90.1, 90.8333, -1.0, 0x00, 0x00)
    OP_6C(0x0B61, 0.45)
    ChrClearPhysicsFlags(0x0B61, 0x00000040)
    ChrClearPhysicsFlags(0x0B61, 0x00000020)
    ChrSetRGBA(0x0B61, 1.0, 1.0, 1.0, 0.2, 1000, 0x03)
    SetChrFace(0x03, 0x0B61, '2', '0', '', '#b', '0')
    Sleep(333)
    Sleep(400)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.3)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.0, 1.5, 300)
    CameraRotateByTarget(0xFFFE, '', 0x00, 3.0, -30.0, 0.0, 300, 0x01)
    CameraSetDistance(0x03, 6.5, 300)
    WaitForThreadExit(0xFFFE, 0x01)
    SetChrFace(0x03, 0xFFFE, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B5E, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B5F, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B60, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B61, '2', '2', '', '#b', '0')
    Sleep(33)
    Sleep(133)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCmd(0x09, 0.15, 0.15, 0.35)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlCraft03_Dash')
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Sleep(1)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x48, 0xFFF9)
    BattleCmd(0x46, 0.15, 8.5, 9.5)
    Sleep(2)
    CreateThread(0x0B5E, 0x02, ScriptId.Current, 'AniBtlCraft03_Dash')
    PlayChrAnimeClip(0x0B5E, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B5E, 1.3)
    Sleep(2)
    CreateThread(0x0B5F, 0x02, ScriptId.Current, 'AniBtlCraft03_Dash')
    PlayChrAnimeClip(0x0B5F, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B5F, 1.3)
    Sleep(2)
    CreateThread(0x0B60, 0x02, ScriptId.Current, 'AniBtlCraft03_Dash')
    PlayChrAnimeClip(0x0B60, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B60, 1.3)
    Sleep(2)
    CreateThread(0x0B61, 0x02, ScriptId.Current, 'AniBtlCraft03_Dash')
    PlayChrAnimeClip(0x0B61, 'BTL_S_CRAFT01_08', 0x00, 0x01, 0x00, 0x00, 0x00, 0.1, 30.4, 31.2333, -1.0, 0x00, 0x00)
    OP_6C(0x0B61, 1.3)
    Sleep(200)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0x0B62, '', 0.0, 1.25, 0.0, 4000)
    Sleep(66)
    CreateThread(0xFFFE, 0x01, ScriptId.Current, 'AniBtlCraft03_Damage')
    Sleep(133)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)
    ChrSetRGBA(0x0B5F, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)
    ChrSetRGBA(0x0B60, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)
    ChrSetRGBA(0x0B61, 1.0, 1.0, 1.0, 0.0, 400, 0x03)
    Sleep(33)
    Sleep(166)
    SetChrFace(0x03, 0xFFFE, '3', '0', '', '#b', '0')
    WaitForThreadExit(0xFFFE, 0x02)
    WaitForThreadExit(0x0B5E, 0x02)
    WaitForThreadExit(0x0B5F, 0x02)
    WaitForThreadExit(0x0B60, 0x02)
    WaitForThreadExit(0x0B61, 0x02)
    ChrSetPhysicsFlags(0xFFFE, 0x00000040)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0x0B5E, 0x00000040)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000040)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000040)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B61, 0x00000040)
    ChrSetPhysicsFlags(0x0B61, 0x00000020)
    BattleCmd(0x18)
    Sleep(500)
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x9B, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.8500000238418579, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    Sleep(166)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 1.0, 300, 0x03)
    Sleep(1000)
    WaitForThreadExit(0xFFFE, 0x01)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrClearPhysicsFlags(0xFFFE, 0x00000800)

    Return()

# id: 0x0040 offset: 0xB5E4
@scena.Code('AniBtlCraft03_Dash')
def AniBtlCraft03_Dash():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 8.0, 6.5, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 12.0, 6.5, 0x00, 0x00)
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 24.0, 8.5, 0x00, 0x00)

    Return()

# id: 0x0041 offset: 0xB630
@scena.Code('AniBtlCraft03_Mouth01')
def AniBtlCraft03_Mouth01():
    SetChrFace(0x03, 0xFFFE, 'A', '8', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, 'A', '3', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, 'A', '8', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, '2', '3', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, '2', '1', '', '#b', '0')
    Sleep(150)
    SetChrFace(0x03, 0xFFFE, '2', '8', '', '#b', '0')

    Return()

# id: 0x0042 offset: 0xB694
@scena.Code('AniBtlCraft03_Damage')
def AniBtlCraft03_Damage():
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_B69C(): pass

    label('loc_B69C')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_B71F',
    )

    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(30)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_B69C')

    def _loc_B71F(): pass

    label('loc_B71F')

    Return()

# id: 0x0043 offset: 0xB720
@scena.Code('AniBtlCraft04')
def AniBtlCraft04():
    Call(ScriptId.BtlCom, 'AniBtlCraftBegin')
    LoadEffect(0xFFFE, 0x98, 'battle/crdh04_0.eff')
    LoadEffect(0xFFFE, 0x99, 'battle/crdh04_1.eff')
    LoadEffect(0xFFFE, 0x9A, 'battle/crdh04_2.eff')
    LoadEffect(0xFFFE, 0x9B, 'battle/crdh04_3.eff')
    LoadEffect(0xFFFE, 0x9C, 'battle/crdh04_4.eff')
    LoadEffect(0xFFFE, 0x9D, 'battle/crdh04_5.eff')
    LoadEffect(0xFFFE, 0x9E, 'battle/crdh04_6.eff')
    CameraCmd(0x00)
    BattleCmd(0x47)
    BattleCmd(0x48, 0xFFFE)
    BattleCmd(0x46, 0.25, 6.0, 15.0)
    Call(ScriptId.BtlCom, 'AniBtlMove')
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, -1.0)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    BattleSaveChrPosition(0xFFFE, 0)
    BattleCreateChrDummy(0xFFFE, 3)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0x0B5E, 0x00000080)
    ChrSetPhysicsFlags(0x0B5F, 0x00000080)
    ChrSetPhysicsFlags(0x0B60, 0x00000080)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    ChrSetPhysicsFlags(0xFFFB, 0x00000080)
    BattleSetChrPos(0x0B5E, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B5F, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B60, 0xFFFB, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B5E, 0xFFFE, 120.0, -1.0)
    BattleTurnChrDirection(0x0B5F, 0xFFFE, 240.0, -1.0)
    BattleTurnChrDirection(0x0B60, 0xFFFE, 180.0, -1.0)
    BattleSetChrPos(0x0B5E, 0x0B5E, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B5F, 0x0B5F, 0.0, 0.0, 10.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B5E, 0xFFFB, 0.0, -1.0)
    BattleTurnChrDirection(0x0B5F, 0xFFFB, 0.0, -1.0)
    BattleSaveChrPosition(0xFFFE, 0)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B5E, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    BattleSetChrPos(0x0B5F, 0xFFFB, 0.0, 0.0, -3.0, -1.0, 0x00, 0x01)
    PlayChrAnimeClip(0x0B5E, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5F, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ChrSetRGBA(0x0B5E, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B5F, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetRGBA(0x0B60, 0.0, 0.0, 0.0, 0.0, 0, 0x03)
    ChrSetPhysicsFlags(0x0B5E, 0x00000040)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000040)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetPhysicsFlags(0x0B60, 0x00000040)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    CameraCmd(0x00)
    BattleCmd(0x47)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 15.0, -50.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 4.1, 0)
    Fade(0xFF, 0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.0, 1.25, 0.2, 700)
    CameraRotateByTarget(0xFFFE, '', 0x03, 10.0, 26.0, 0.0, 700, 0x01)
    CameraSetDistance(0x03, 2.65, 700)
    SetChrFace(0x03, 0xFFFE, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFE, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x9C, 0x0), 0xFFFB, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(300)
    Sleep(400)
    SetChrFace(0x03, 0xFFFE, '2', '3', '', '#b', '0')
    CameraCmd(0x14, 0x00, 0xFFFE, '', 0.0, 1.35, 0.2, 700)
    CameraCmd(0x05, 0x00, 3.8, 700)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x01, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(133)
    CameraSetDistance(0x03, 4.5, 700)
    Sleep(233)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 0.9, 0.0, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -2.0, -160.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 7.1, 0)
    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    Fade(0xFF, 0, 0x0000)
    ChrClearPhysicsFlags(0x0B5E, 0x00000040)
    ChrClearPhysicsFlags(0x0B5E, 0x00000020)
    ChrClearPhysicsFlags(0x0B5F, 0x00000040)
    ChrClearPhysicsFlags(0x0B5F, 0x00000020)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    ChrSetRGBA(0x0B5F, 1.0, 1.0, 1.0, 1.0, 1000, 0x03)
    CameraSetPosByTarget(0x03, 0xFFFB, '', 0.0, 1.2, 0.0, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, -240.0, 0.0, 4000, 0x01)
    CameraSetDistance(0x03, 8.1, 4000)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x9B, 0x0), 0x0B5E, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    PlayEffect(0xFFFE, (0xFF, 0x9B, 0x0), 0x0B5F, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Sleep(166)
    SetChrFace(0x03, 0x0B5E, '3', '0', '', '#b', '0')
    SetChrFace(0x03, 0x0B5F, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(0x0B5E, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B5E, 1.4)
    Sleep(33)
    PlayChrAnimeClip(0x0B5F, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B5F, 1.4)
    Sleep(300)
    Sleep(300)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT01_13', 0x00, 0x00, 0x00, 0x00, 0x00, 0.5, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.2)
    WaitAnimeClip(0x0B5F, 0.0, 0x00)
    WaitAnimeClip(0x0B5E, 0.0, 0x00)
    PlayChrAnimeClip(0x0B5E, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0x0B5F, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0x0B5E, 1.4)
    OP_6C(0x0B5F, 1.4)
    SetChrFace(0x03, 0x0B5E, '2', '2', '', '#b', '0')
    SetChrFace(0x03, 0x0B5F, '2', '2', '', '#b', '0')
    Sleep(100)
    CreateThread(0x0B5E, 0x02, ScriptId.Current, 'AniBtlCraft04_Dash')
    CreateThread(0x0B5F, 0x02, ScriptId.Current, 'AniBtlCraft04_Dash')
    Sleep(100)
    ChrClearPhysicsFlags(0x0B60, 0x00000040)
    ChrClearPhysicsFlags(0x0B60, 0x00000020)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0x0B60, 0x0000000C, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.8999999761581421, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    CameraCmd(0x09, 0.15, 0.15, 0.5)
    Sleep(1)
    ChrSetPhysicsFlags(0x0B60, 0x00000040)
    ChrSetPhysicsFlags(0x0B60, 0x00000020)
    OP_5E(0x00, 0x0002, 0.45, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Sleep(66)
    OP_5E(0x01, 0x0190)
    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    Sleep(33)
    CameraCmd(0x05, 0x00, 9.1, 1500)
    SetChrFace(0x03, 0xFFFE, '3', '0', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT01_10', 0x00, 0x00, 0x00, 0x00, 0x00, 0.4, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 1.4)
    Sleep(66)
    CreateThread(0xFFFE, 0x02, ScriptId.Current, 'AniBtlCraft04_Dash2')
    SetChrFace(0x03, 0xFFFE, '6', 'B', '', '#b', '0')
    Sleep(200)
    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    Fade(0x65, 100, 1.0, 0x0000)
    Fade(0xFE, 0)
    WaitForThreadExit(0x0B5E, 0x02)
    WaitForThreadExit(0x0B5F, 0x02)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0x0B5F, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleSetChrPos(0x0B5E, 0x0B5E, 2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleSetChrPos(0x0B5F, 0x0B5F, -2.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    BattleTurnChrDirection(0x0B5E, 0xFFFB, 180.0, -1.0)
    BattleTurnChrDirection(0x0B5F, 0xFFFB, 180.0, -1.0)
    PlayChrAnimeClip(0x0B5E, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B5E, 0.5)
    PlayChrAnimeClip(0x0B5F, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0x0B5F, 0.5)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_03', 0x00, 0x01, 0x00, 0x00, 0x00, 0.0, 90.1667, 90.5, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    SetChrFace(0x03, 0xFFFE, '6', 'A', '', '#b', '0')
    CameraCmd(0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 1.2, 1.0, 0.35, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 20.0, 9.0, 0, 0x01)
    CameraSetDistance(0x03, 2.9, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 2.5, 1.0, 0.35, 4000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 10.0, 11.0, 4000, 0x01)
    CameraSetDistance(0x03, 3.0, 4000)
    CameraCmd(0x09, 0.2, 0.2, 2.0)
    Sleep(66)
    OP_5E(0x00, 0x0002, 0.4, 0x0000, 0x0000, 0x0000, 0.0, 0xFFFF, -9000.0, -9000.0, -9000.0)
    Sleep(100)
    ChrSetRGBA(0x0B5E, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    ChrSetRGBA(0x0B5F, 1.0, 1.0, 1.0, 0.0, 2000, 0x03)
    BattleDamage(0xFFFB, 0xFFFE, 100)
    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    OP_5E(0x01, 0x0320)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    Sleep(1000)
    Sleep(333)
    Call(ScriptId.BtlCom, 'AniBtlCraftFinish')
    BattleSetChrPos(0xFFFE, 0xFFF4, 0.0, 0.0, 0.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitForThreadExit(0x0B5E, 0x02)
    WaitForThreadExit(0x0B5F, 0x02)
    ChrSetPhysicsFlags(0x0B5E, 0x00000040)
    ChrSetPhysicsFlags(0x0B5E, 0x00000020)
    ChrSetPhysicsFlags(0x0B5F, 0x00000040)
    ChrSetPhysicsFlags(0x0B5F, 0x00000020)
    BattleCmd(0x18)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    ChrClearPhysicsFlags(0xFFFB, 0x00000080)

    Return()

# id: 0x0044 offset: 0xC330
@scena.Code('AniBtlCraft04_Dash')
def AniBtlCraft04_Dash():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 6.2, 0x00, 0x00)

    Return()

# id: 0x0045 offset: 0xC34C
@scena.Code('AniBtlCraft04_Dash2')
def AniBtlCraft04_Dash2():
    BattleSetChrPos(0xFFFE, 0xFFFE, 0.0, 0.0, 8.5, 7.2, 0x00, 0x00)

    Return()

# id: 0x0046 offset: 0xC368
@scena.Code('AniBtlSCraft00')
def AniBtlSCraft00():
    Call(ScriptId.BtlCom, 'AniBtlSCraftBegin')
    AnimeClipCmd(0x04, 0xFFFE, 'C_CHR033_SC1', '')
    LoadEffect(0xFFFE, 0x90, 'battle/sc033_00_0.eff')
    LoadEffect(0xFFFE, 0x91, 'battle/sc033_00_1.eff')
    LoadEffect(0xFFFE, 0x92, 'battle/sc033_00_2.eff')
    LoadEffect(0xFFFE, 0x93, 'battle/sc033_00_3.eff')
    LoadEffect(0xFFFE, 0x94, 'battle/sc033_00_4.eff')
    LoadEffect(0xFFFE, 0x95, 'battle/sc033_00_5.eff')
    LoadEffect(0xFFFE, 0x96, 'battle/sc033_00_6.eff')
    LoadEffect(0xFFFE, 0x97, 'battle/sc033_00_7.eff')
    LoadEffect(0xFFFE, 0x98, 'battle/sc033_00_8.eff')
    LoadEffect(0xFFFE, 0x99, 'battle/sc033_00_9.eff')
    LoadEffect(0xFFFE, 0x9A, 'battle/sc033_00_10.eff')
    LoadEffect(0xFFFE, 0x9B, 'battle/sc033_00_11.eff')
    LoadEffect(0xFFFE, 0x9C, 'battle/sc033_00_12.eff')
    LoadEffect(0xFFFE, 0x9D, 'battle/sc033_00_13.eff')
    LoadEffect(0xFFFE, 0x9F, 'battle/cic033_0.eff')
    PlayEffect(0xFFFE, (0xFF, 0x90, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x02)
    OP_3B(0x00, (0xFF, 0x1012, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_C0(0x0002, 1.65)
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    ChrSetPhysicsFlags(0xFFFE, 0x00000080)
    ChrSetPhysicsFlags(0xFFFE, 0x00000200)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    ChrSetPhysicsFlags(0xFFF9, 0x00000080)
    ChrSetPhysicsFlags(0xFFF9, 0x00000200)
    SetChrPos(0xFFFE, 0.0, 0.0, -50.0, 0.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, -1.0, 0.5)
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    def _loc_C630(): pass

    label('loc_C630')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_C67B',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFEA, -1.0, 0.5)
    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlFloat', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    BattleTargetsIterNext(0xFFFE)
    Sleep(1)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_C630')

    def _loc_C67B(): pass

    label('loc_C67B')

    Call(ScriptId.Current, 'SpringOff')
    Call(ScriptId.Current, 'EraseEquip')
    LoadAsset('C_EQU090')
    AttachEquip(0xFFFE, 'C_EQU090', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    Sleep(0)
    Fade(0x65, 1500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCmd(0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, 'F', '2[autoM2]', '4', 'F', '0')
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.41, 0.8, -0.54, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, -162.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 1.6, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.17, 1.61, 0.28, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x03, 16.0, -25.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x03, 0.6, 3000)
    CameraCmd(0x0B, 0x03, 25.0, 0x0BB8)
    OP_3B(0x00, (0xFF, 0x8F27, 0x0), 0.8, (0xFF, 0x1F4, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1000)
    OP_3B(0x32, (0xFF, 0x1B6A, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1500)
    SetChrFace(0x03, 0xFFFE, '3', '2[autoM2]', '4', '3', '0')
    CameraCmd(0x07, 0x00BF)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.1, 1.31, 0.69, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x03, 3.0, 0.0, 0.0, 1500, 0x01)
    CameraCmd(0x05, 0x02, 0.7, 1500)
    CameraCmd(0x0B, 0x02, 40.0, 0x05DC)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_45(0xFFFE, 15.0, -15.0, 0.0, 0x01F4, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetDistance(0x03, 1.1, 10000)
    Sleep(700)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x04)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x05)
    OP_3B(0x00, (0xFF, 0x8FA8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.49, 1.06, 1.58, 200)
    CameraRotateByTarget(0xFFFE, '', 0x03, -8.0, 23.0, 0.0, 200, 0x01)
    CameraSetDistance(0x03, 3.6, 200)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0064, 0x0000)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00FA, 0x00C8, 1.0, 0xF011, 0.0, 1.0, 0.0)
    OP_3B(0xFF, 0.5, 0.7, 0.2)
    Sleep(150)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.49, 2.61, 1.58, 3000)
    CameraRotateByTarget(0xFFFE, '', 0x03, -7.0, 23.0, 0.0, 3000, 0x01)
    CameraSetDistance(0x03, 10.0, 3000)
    Sleep(500)
    StopEffect(0xFFFE, 0x04, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x9F, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8B7D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(1666)
    LoadAsset('C_CHRX10')
    BattleCreateTempChar(0x0000, 0xFFFF, 'C_CHRX10', '')
    ChrClearPhysicsFlags(0x0B68, 0x00000040)
    ChrClearPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(0x0B68, 0x00000020)
    ChrSetPhysicsFlags(0x0B68, 0x00000200)
    ChrSetPhysicsFlags(0x0B68, 0x00000080)
    SetChrPos(0x0B68, 0.0, 0.0, -50.0, 0.0)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -2.28, -0.42, -5.36, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 7.0, 22.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 10.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    OP_3B(0x32, (0xFF, 0x1B6B, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.5, 0.7, 0.6)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x8F62, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_45(0xFFFE, 45.0, 45.0, 90.0, 0x01F4, 0x0000)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0x0B68, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), 0x07)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -2.75, 8.39, -6.77, 1200)
    CameraRotateByTarget(0xFFFE, '', 0x03, -39.0, 22.0, 0.0, 1200, 0x01)
    CameraSetDistance(0x03, 15.0, 1200)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '2', '7', '7', '2', '0')
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x94, 0x0), 0x0B68, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), 0x06)
    OP_3B(0x00, (0xFF, 0x8F2D, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0708, 0x0258, 0x0000, 0x0708, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 2.0)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.42, 1.59, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 2.0, 2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.0, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', 0.2, 1.74, 1.59, 1500)
    CameraRotateByTarget(0xFFFE, '', 0x03, -13.0, -14.0, 0.0, 1500, 0x01)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 3.0)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0000, 0x0000)
    SetChrFace(0x03, 0xFFFE, '3', '3', '0', '3', '0')
    Sleep(1000)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.47, 0.54, -5.94, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, 6.0, 4.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 10.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetDistance(0x03, 8.5, 1500)
    Sleep(1500)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(233)
    OP_3B(0x00, (0xFF, 0x8FA6, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_45(0xFFFE, 0.0, 0.0, 0.0, 0x0064, 0x0000)
    SetChrFace(0x03, 0xFFFE, '2', '0', '', '#b', '0')
    CameraSetPosByTarget(0x03, 0xFFFE, '', -0.23, 0.95, -5.88, 150)
    CameraRotateByTarget(0xFFFE, '', 0x03, 0.0, 0.0, 0.0, 150, 0x01)
    CameraSetDistance(0x03, 8.0, 150)
    Sleep(150)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleCmd(0x13, 0xFFFE, 0x0001, 0xFFFF, 0x00000000, 0x00000578, 0x00000000)
    Sleep(1)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_D04A(): pass

    label('loc_D04A')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_D072',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFF, 180.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_D04A')

    def _loc_D072(): pass

    label('loc_D072')

    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0x0B68, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    OP_3B(0x00, (0xFF, 0x8F96, 0x0), 0.8, (0xFF, 0x3E8, 0x0), 0.0, -3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FAA, 0x0), 0.5, (0xFF, 0x3E8, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraSetPos(0x03, 2.38, 1.57, -49.52, 0)
    CameraRotate(0x03, 354.0, 2.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 11.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPos(0x03, 11.72, 4.01, -7.9, 1000)
    CameraRotate(0x03, 356.0, -149.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 30.1, 1000)
    OP_3B(0xFF, 0.5, 0.7, 0.6)
    BattleSetChrPos(0x0B68, 0xFFFE, 0.0, 0.0, 25.0, 3.75, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 3.0)
    CameraCmd(0x07, 0x00BF)
    ChrSetPhysicsFlags(0xFFFE, 0x00000040)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    StopEffect(0xFFFE, 0x05, 0x01)
    OP_3B(0xFF, 0.3, 0.5, 2.0)
    CameraSetPos(0x03, 6.86, 4.79, 20.05, 1000)
    CameraRotate(0x03, 352.0, -161.0, 0.0, 1000, 0x01)
    CameraSetDistance(0x03, 36.0, 1000)
    BattleSetChrPos(0x0B68, 0xFFFF, 0.0, 0.0, 0.0, 3.75, 0x02, 0x00)
    CameraCmd(0x07, 0x00BF)
    CameraSetPos(0x03, 5.62, 12.73, 20.6, 1500)
    CameraRotate(0x03, 341.0, 195.0, 0.0, 1500, 0x01)
    CameraSetDistance(0x03, 30.0, 1500)
    StopEffect(0xFFFE, 0x03, 0x01)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_D2AA(): pass

    label('loc_D2AA')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_D2D2',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_D2AA')

    def _loc_D2D2(): pass

    label('loc_D2D2')

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 0.0, 6.5, 1.0, 0.5, 0x02, 0x00)
    OP_3B(0x00, (0xFF, 0x8F41, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x00, 'AniBtlFloat')
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D3A6',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 1.5, 5.0, 0.0, 0.5, 0x02, 0x00)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x00, 'AniFall')

    def _loc_D3A6(): pass

    label('loc_D3A6')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D3FA',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, -1.5, 5.0, 0.0, 0.5, 0x02, 0x00)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x00, 'AniBtlFloat')

    def _loc_D3FA(): pass

    label('loc_D3FA')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_D44A',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 0.0, 3.5, -1.0, 0.5, 0x02, 0x00)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x00, 'AniFall')

    def _loc_D44A(): pass

    label('loc_D44A')

    CameraCmd(0x07, 0x00BF)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrClearPhysicsFlags(0xFFFE, 0x00000040)
    ChrClearPhysicsFlags(0xFFFE, 0x00000020)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 5.0, -20.0, 0.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x93, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x05)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraSetPos(0x03, -1.38, 7.18, -15.89, 0)
    CameraRotate(0x03, 346.0, 151.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.7, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    StopEffect(0xFFFE, 0x05, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x95, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x07)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FA6, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 3.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x32, (0xFF, 0x1B6C, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0xFF, 0.5, 0.7, 0.15)
    Sleep(166)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, -0.25, 0x0), (0xEE, 0.5, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x08)
    Sleep(233)
    OP_6C(0xFFFE, 4.0)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00FA, 0x00C8, 0.5, 0xF011, 0.0, 1.0, 0.0)
    BattleSetChrPos(0xFFFE, 0xFFF9, 0.0, 6.5, 10.0, 10.0, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x91, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x03)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 4.0)
    Sleep(100)
    OP_4E(1.0, 0.0, 0x03)
    StopEffect(0xFFFE, 0x05, 0x01)
    StopEffect(0xFFFE, 0x06, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x97, 0x0), 0x0B68, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), (0xEE, 1.2000000476837158, 0x0), 0x09)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    CameraSetPos(0x03, 0.0, 0.0, 0.0, 0)
    CameraRotate(0x03, 13.0, 170.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 10.0, 0)
    CameraCmd(0x05, 0x00, 7.0, 500)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_D8D8(): pass

    label('loc_D8D8')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_D900',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_D8D8')

    def _loc_D900(): pass

    label('loc_D900')

    ReleaseEffect(0xFFFE, 0x96)
    LoadEffect(0xFFFE, 0x96, 'battle/sc033_00_14.eff')
    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    BattleSetChrPos(0xFFFB, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    OP_5C(0xFFFB, 0x00, 'Root')
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, -30.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 4.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 0.0, -15.0, 0.0, 0x00, 0x00)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, 1.53, -0.0, 8.99, 0)
    CameraRotate(0x03, 11.0, 339.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.8, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x02, 0x02, 1.64, 0.0, -4.17, 500)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, 15.0, 12.5, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x08)
    BattleCmd(0x3A, 0xFFFE)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 5.0, 0x02, 0x00)
    Sleep(166)
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.10000000149011612, 0x0), (0xEE, -0.20000000298023224, 0x0), 25.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0A)
    OP_3B(0x00, (0xFF, 0x8F1C, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 9.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00C8, 0x0096, 0.5, 0xFFFB, 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x0320, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.5, 0.7, 0.1)
    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_4C(0xFFFB, 0.1, 0.3, 0.6, 0x0000, 0x03)
    OP_4C(0xFFFB, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    SetChrFace(0x03, 0xFFFB, 'B', '7', '', '#b', '0')
    Sleep(10)
    PlayChrAnimeClip(0xFFFB, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, 0.25, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(40)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    BattleCmd(0x3A, 0xFFFE)
    Fade(0x01, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    OP_5C(0xFFFB, 0x01, 'Root')
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E0FD',
    )

    BattleSetChrPos(0xFFFB, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    OP_5C(0xFFFB, 0x00, 'Root')
    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 4.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 0.0, 15.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.0)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -2.69, -0.53, 4.26, 0)
    CameraRotate(0x03, 17.0, 144.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.5, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x02, 0x02, -2.77, 0.32, -0.17, 500)
    CameraCmd(0x04, 0x02, 8.0, 150.0, 0.0, 500, 0x01)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, 15.0, 12.5, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x08)
    BattleCmd(0x3A, 0xFFFE)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 5.0, 0x02, 0x00)
    Sleep(166)
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -0.20000000298023224, 0x0), 25.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0A)
    OP_3B(0x00, (0xFF, 0x8F1C, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 9.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00C8, 0x0096, 0.5, 0xFFFB, 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x0320, 0x0000, 0x0000, 0x00)
    SetChrFace(0x03, 0xFFFB, 'B', '7', '', '#b', '0')
    OP_3B(0xFF, 0.5, 0.7, 0.1)
    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_4C(0xFFFB, 0.1, 0.3, 0.6, 0x0000, 0x03)
    OP_4C(0xFFFB, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    Sleep(10)
    PlayChrAnimeClip(0xFFFB, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, 1.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(40)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    BattleCmd(0x3A, 0xFFFE)
    Fade(0x01, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    OP_5C(0xFFFB, 0x01, 'Root')

    def _loc_E0FD(): pass

    label('loc_E0FD')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E530',
    )

    BattleSetChrPos(0xFFFB, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    OP_5C(0xFFFB, 0x00, 'Root')
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, 0.0, -40.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 4.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 0.0, -15.0, 0.0, 0x00, 0x00)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, -1.99, 1.59, -9.21, 0)
    CameraRotate(0x03, 349.0, 143.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 8.8, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x02, 0x02, -2.42, 1.5, 4.84, 500)
    CameraCmd(0x04, 0x02, 352.0, 145.0, 0.0, 500, 0x01)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, 15.0, 12.5, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x08)
    BattleCmd(0x3A, 0xFFFE)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 5.0, 0x02, 0x00)
    Sleep(166)
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -0.20000000298023224, 0x0), 25.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0A)
    OP_3B(0x00, (0xFF, 0x8F1C, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 9.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00C8, 0x0096, 0.5, 0xFFFB, 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x0320, 0x0000, 0x0000, 0x00)
    SetChrFace(0x03, 0xFFFB, 'B', '7', '', '#b', '0')
    OP_3B(0xFF, 0.5, 0.7, 0.1)
    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_4C(0xFFFB, 0.1, 0.3, 0.6, 0x0000, 0x03)
    OP_4C(0xFFFB, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    Sleep(10)
    PlayChrAnimeClip(0xFFFB, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, 1.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(40)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    BattleCmd(0x3A, 0xFFFE)
    Fade(0x01, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    OP_5C(0xFFFB, 0x01, 'Root')

    def _loc_E530(): pass

    label('loc_E530')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_E971',
    )

    BattleSetChrPos(0xFFFB, 0xFFEA, 0.0, 0.0, 0.0, 0.0, 0x00, 0x00)
    OP_5C(0xFFFB, 0x00, 'Root')
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, -30.0, 40.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    ChrClearPhysicsFlags(0xFFFB, 0x00000040)
    ChrClearPhysicsFlags(0xFFFB, 0x00000020)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_3B(0x00, (0xFF, 0x10F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_6C(0xFFFE, 4.0)
    BattleTurnChrDirection(0xFFFE, 0xFFEA, 0.0, 0.0)
    BattleSetChrPos(0xFFFE, 0xFFEA, 0.0, 0.0, 15.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 0.0, 0.0)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, 0.9, 0.62, -2.66, 0)
    CameraRotate(0x03, 4.0, 334.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 6.0, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraCmd(0x02, 0x02, 1.16, 0.62, 1.81, 500)
    CameraCmd(0x04, 0x02, 1.0, 335.0, 0.0, 500, 0x01)
    BattleSetChrPos(0xFFFE, 0xFFFB, 0.0, 0.0, 15.0, 12.5, 0x00, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x96, 0x0), 0xFFFE, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x08)
    BattleCmd(0x3A, 0xFFFE)
    BattleSetChrPosAsync(0xFFFE, 0xFFFE, 0.0, 0.0, 10.0, 5.0, 0x02, 0x00)
    Sleep(166)
    OP_5D(0xFFFB, 'Root', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0x0000, 0x03, 0x00)
    PlayEffect(0xFFFE, (0xFF, 0x98, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, -0.20000000298023224, 0x0), 25.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0A)
    OP_3B(0x00, (0xFF, 0x8F1C, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8FBC, 0x0), 0.4, (0xFF, 0x0, 0x0), 0.0, 9.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00C8, 0x0096, 0.5, 0xFFFB, 0.0, 1.0, 0.0)
    CameraCmd(0x0A, 0.0, 0.4, 0.0, 0x0000, 0x0032, 0x0320, 0x0000, 0x0000, 0x00)
    SetChrFace(0x03, 0xFFFB, 'B', '7', '', '#b', '0')
    OP_3B(0xFF, 0.5, 0.7, 0.1)
    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_4C(0xFFFB, 0.1, 0.3, 0.6, 0x0000, 0x03)
    OP_4C(0xFFFB, 0.0, 0.0, 0.0, 0x01F4, 0x03)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    Sleep(10)
    PlayChrAnimeClip(0xFFFB, 'BTL_CRUCIFIXION', 0x01, 0x00, 0x00, 0x00, 0x00, 1.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(40)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06b', 0x00, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(500)
    BattleCmd(0x3A, 0xFFFE)
    Fade(0x01, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    OP_5C(0xFFFB, 0x01, 'Root')

    def _loc_E971(): pass

    label('loc_E971')

    ChrSetPhysicsFlags(0xFFFB, 0x00000040)
    ChrSetPhysicsFlags(0xFFFB, 0x00000020)
    StopEffect(0xFFFE, 0x02, 0x01)
    StopEffect(0xFFFE, 0x03, 0x01)
    StopEffect(0xFFFE, 0x08, 0x01)
    StopEffect(0xFFFE, 0x09, 0x01)
    StopEffect(0xFFFE, 0x0A, 0x01)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    BattleSetChrPos(0xFFFE, 0xFFFF, 0.0, 0.0, 10.0, 0.0, 0x00, 0x00)
    BattleTurnChrDirection(0xFFFE, 0xFFFB, 180.0, 0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_07', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '2', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x9D, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)
    OP_3B(0x00, (0xFF, 0x8F27, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraSetPos(0x03, 0.51, 2.81, 6.81, 0)
    CameraRotate(0x03, 359.0, 11.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 11.3, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPos(0x03, -0.58, 6.99, -2.61, 2500)
    CameraRotate(0x03, 336.0, 15.0, 5.0, 1250, 0x01)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_EAF1(): pass

    label('loc_EAF1')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_EB19',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFF, 180.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_EAF1')

    def _loc_EB19(): pass

    label('loc_EB19')

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 0.0, 6.5, 1.0, 0.0, 0x02, 0x00)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EB6C',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 1.5, 5.0, 0.0, 0.0, 0x02, 0x00)

    def _loc_EB6C(): pass

    label('loc_EB6C')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EB9F',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, -1.5, 5.0, 0.0, 0.0, 0x02, 0x00)

    def _loc_EB9F(): pass

    label('loc_EB9F')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EBD2',
    )

    BattleSetChrPosAsync(0xFFFB, 0xFFFF, 0.0, 3.5, -1.0, 0.0, 0x02, 0x00)

    def _loc_EBD2(): pass

    label('loc_EBD2')

    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_EBD7(): pass

    label('loc_EBD7')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_EBFF',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_EBD7')

    def _loc_EBFF(): pass

    label('loc_EBFF')

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x01, 'AniBtlCrucifixion')
    SetChrFace(0x03, 0xFFFB, 'B', 'F', '', '#b', '0')
    Sleep(1)
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0B)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_ED4D',
    )

    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x01, 'AniBtlCrucifixion')
    SetChrFace(0x03, 0xFFFB, 'B', 'F', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0B)

    def _loc_ED4D(): pass

    label('loc_ED4D')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EE0F',
    )

    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x01, 'AniBtlCrucifixion')
    SetChrFace(0x03, 0xFFFB, 'B', 'F', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0B)

    def _loc_EE0F(): pass

    label('loc_EE0F')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_EED1',
    )

    AnimeClipLoadMultiple(0xFFFB, 0x00, 'AniBtlCrucifixion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '')
    OP_38(0xFFFB, 0x00, 0x00, 'EraseEquip')
    OP_38(0xFFFB, 0x00, 0x01, 'AniBtlCrucifixion')
    SetChrFace(0x03, 0xFFFB, 'B', 'F', '', '#b', '0')
    PlayEffect(0xFFFE, (0xFF, 0x99, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0B)

    def _loc_EED1(): pass

    label('loc_EED1')

    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraCmd(0x07, 0x00BF)
    OP_3B(0x32, (0xFF, 0x1B6D, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    ChrSetPhysicsFlags(0xFFF9, 0x00000040)
    ChrSetPhysicsFlags(0xFFF9, 0x00000020)
    Fade(0x65, 200, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPosByTarget(0x03, 0xFFFE, '', -4.43, 2.72, -9.37, 0)
    CameraRotateByTarget(0xFFFE, '', 0x03, -7.0, 24.0, -3.0, 0, 0x01)
    CameraSetDistance(0x03, 13.3, 0)
    CameraCmd(0x14, 0x02, 0xFFFE, '', -4.43, 3.03, -9.37, 1000)
    CameraRotateByTarget(0xFFFE, '', 0x02, -8.0, 25.0, -3.0, 1000, 0x01)
    CameraCmd(0x05, 0x02, 11.3, 1000)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_08a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    SetChrFace(0x03, 0xFFFE, '1', '2', '', '#b', '0')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_09', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x02, 0x02, -3.23, 4.39, 1.91, 1000)
    CameraCmd(0x04, 0x02, -18.0, 24.0, -3.0, 1000, 0x01)
    Sleep(333)
    SetChrFace(0x03, 0xFFFE, '2', '6J737JJ6', '2', '2', '0')
    PlayEffect(0xFFFE, (0xFF, 0x92, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x04)
    OP_3B(0x00, (0xFF, 0x8F2E, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x13F8, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 4.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x03E8, 0x012C, 0x0000, 0x03E8, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_5E(0x00, 0x0000, 0.8, 0x0096, 0x00FA, 0x00C8, 1.0, 0xF011, 0.0, 1.0, 0.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_09a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    CameraCmd(0x07, 0x00BF)
    ChrSetPhysicsFlags(0xFFFE, 0x00000040)
    ChrSetPhysicsFlags(0xFFFE, 0x00000020)
    ChrClearPhysicsFlags(0xFFF9, 0x00000040)
    ChrClearPhysicsFlags(0xFFF9, 0x00000020)
    Fade(0x65, 500, 1.0, 0x0000)
    Fade(0xFE, 0)
    CameraSetPos(0x03, 0.38, 5.3, 4.03, 0)
    CameraRotate(0x03, 358.0, 10.0, 0.0, 0, 0x01)
    CameraSetDistance(0x03, 11.3, 0)
    CameraCmd(0x0B, 0x03, 40.0, 0x0000)
    CameraSetPos(0x03, 1.0, 5.07, 4.51, 4000)
    CameraRotate(0x03, 343.0, 15.0, -5.0, 4000, 0x01)
    BattleTargetsIterReset(0x01, 0xFFFE)
    OP_3B(0x00, (0xFF, 0x13EC, 0x0), 0.8, (0xFF, 0x3E8, 0x0), 0.0, 1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0BB8, 0x0258, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x8F31, 0x0), 0.6, (0xFF, 0x3E8, 0x0), 0.0, 1.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    def _loc_F2AD(): pass

    label('loc_F2AD')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_F2D5',
    )

    BattleTurnChrDirection(0xFFFB, 0xFFFE, 0.0, -1.0)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_F2AD')

    def _loc_F2D5(): pass

    label('loc_F2D5')

    BattleTargetsIterInit(0x00)
    BattleTargetsIterReset(0x01, 0xFFFE)
    EffectCmd(0x0F, 0xFFFE, 0x0099, 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0C)
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_F397',
    )

    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0C)

    def _loc_F397(): pass

    label('loc_F397')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_F3FE',
    )

    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0C)

    def _loc_F3FE(): pass

    label('loc_F3FE')

    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Gtr,
            Expr.Return,
        ),
        'loc_F465',
    )

    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, 'NODE_HEAD'), (0xEE, 0.0, 0x0), (0xEE, -0.18000000715255737, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0C)

    def _loc_F465(): pass

    label('loc_F465')

    PlayEffect(0xFFFE, (0xFF, 0x9B, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 6.5, 0x0), (0xEE, 0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x0D)
    Sleep(1500)
    OP_3B(0x32, (0xFF, 0x1B6E, 0x0), 1.0, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    Sleep(2000)
    PlayEffect(0xFFFE, (0xFF, 0x9C, 0x0), 0xFFFF, 0x00000000, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 6.5, 0x0), (0xEE, 0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), (0xEE, 1.5, 0x0), 0x0E)
    OP_3B(0x01, (0xFF, 0x13EC, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x01, (0xFF, 0x8F31, 0x0), (0xFF, 0x3E8, 0x0))
    OP_3B(0x00, (0xFF, 0x8F2D, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    OP_3B(0x00, (0xFF, 0x114A, 0x0), 0.8, (0xFF, 0x0, 0x0), 0.0, 0.0, 0x0000, 0xFFFF, 0.0, 0.0, 0.0, 0.0, '', 0x04B0, 0x012C, 0x0000, 0x04B0, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000, 0x0000)
    CameraCmd(0x0A, 0.25, 0.25, 0.0, 0x0064, 0x07D0, 0x0064, 0x0000, 0x0000, 0x00)
    OP_3B(0xFF, 0.7, 0.9, 1.5)
    Sleep(500)
    Fade(0x03, 2000, 1.0, 0x0000)
    Fade(0xFF, 0, 0x0000)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    ReleaseEffect(0xFFFE, 0x90)
    ReleaseEffect(0xFFFE, 0x91)
    ReleaseEffect(0xFFFE, 0x92)
    ReleaseEffect(0xFFFE, 0x93)
    ReleaseEffect(0xFFFE, 0x94)
    ReleaseEffect(0xFFFE, 0x95)
    ReleaseEffect(0xFFFE, 0x96)
    ReleaseEffect(0xFFFE, 0x97)
    ReleaseEffect(0xFFFE, 0x98)
    ReleaseEffect(0xFFFE, 0x99)
    ReleaseEffect(0xFFFE, 0x9A)
    ReleaseEffect(0xFFFE, 0x9B)
    ReleaseEffect(0xFFFE, 0x9C)
    ReleaseEffect(0xFFFE, 0x9D)
    WaitForThreadExit(0xFFFE, 0x02)
    WaitForThreadExit(0xFFFE, 0x03)
    Call(ScriptId.Current, 'BtlDefaultFace')
    AnimeClipCmd(0x05, 0xFFFE, 'C_CHR033_SC1', '')
    ChrClearPhysicsFlags(0xFFFE, 0x000002A0)
    ChrClearPhysicsFlags(0xFFF9, 0x000002A0)
    OP_38(0xFFF9, 0x00, 0x01, 'ShowEquip')
    BattleDeleteTempChar(0xFFFF)
    ChrSetRGBA(0xFFFE, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    ChrSetRGBA(0xFFF9, 1.0, 1.0, 1.0, 1.0, 0, 0x03)
    BattleTargetsIterReset(0x01, 0xFFFE)
    def _loc_F6F9(): pass

    label('loc_F6F9')

    If(
        (
            (Expr.PushReg, 0x1),
            Expr.Return,
        ),
        'loc_F722',
    )

    OP_38(0xFFFB, 0x00, 0x00, 'ShowEquip')
    BattleTargetsIterNext(0xFFFE)

    ExecExpressionWithReg(
        0x01,
        (
            (Expr.PushLong, 0x1),
            Expr.Sub2,
            Expr.Return,
        ),
    )

    Jump('loc_F6F9')

    def _loc_F722(): pass

    label('loc_F722')

    BattleCmd(0x6C, 0x0001)
    Sleep(1)
    Call(ScriptId.BtlCom, 'AniBtlSCraftFinish')

    Return()

# id: 0x0047 offset: 0xF740
@scena.Code('AniBtlSCraftDamage')
def AniBtlSCraftDamage():
    BattleDamageAnime(0xFFFB, (0xEE, 0.5, 0x0), (0xEE, 0.800000011920929, 0x0), 0x01)
    PlayEffect(0xFFFE, (0xFF, 0x3F8, 0x0), 0xFFFB, 0x0000000C, (0xDD, 'NODE_CENTER'), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), (0xEE, 0.0, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0xFF)

    Return()

# id: 0x0048 offset: 0xF7A0
@scena.Code('EraseCross')
def EraseCross():
    PlayEffect(0xFFFE, (0xFF, 0x9A, 0x0), 0xFFFB, 0x00000003, (0xDD, ''), (0xEE, 0.0, 0x0), (0xEE, 0.5, 0x0), (0xEE, -0.20000000298023224, 0x0), 0.0, 0.0, 0.0, (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), (0xEE, 1.0, 0x0), 0x0C)

    Return()

# id: 0x0049 offset: 0xF7E4
@scena.Code('AniEvAttachEquip')
def AniEvAttachEquip():
    LoadAsset('C_EQU090')
    AttachEquip(0xFFFE, 'C_EQU090', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)

    Return()

# id: 0x004A offset: 0xF840
@scena.Code('AniEvDetachEquip')
def AniEvDetachEquip():
    ReleaseAsset('C_EQU090')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)

    Return()

# id: 0x004B offset: 0xF884
@scena.Code('AniEvBtlWait')
def AniEvBtlWait():
    Call(ScriptId.Current, 'ShowEquip')
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004C offset: 0xF8C0
@scena.Code('AniEvBtlMove')
def AniEvBtlMove():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_MOVE', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004D offset: 0xF908
@scena.Code('AniEvAttack')
def AniEvAttack():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_ATTACK', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004E offset: 0xF97C
@scena.Code('AniEvDamage')
def AniEvDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x004F offset: 0xF9F0
@scena.Code('AniEvWeakDamage')
def AniEvWeakDamage():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAKDAMAGE', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0050 offset: 0xFA68
@scena.Code('AniEvAria')
def AniEvAria():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARIA', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0051 offset: 0xFA94
@scena.Code('AniEvArts')
def AniEvArts():
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTS', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_ARTSa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0052 offset: 0xFAEC
@scena.Code('AniEvBtlWalk')
def AniEvBtlWalk():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WALK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0053 offset: 0xFB34
@scena.Code('AniEvWeak')
def AniEvWeak():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_WEAK', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0054 offset: 0xFB7C
@scena.Code('AniEvPowerup')
def AniEvPowerup():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP_F', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUP', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_POWERUPa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0055 offset: 0xFC24
@scena.Code('AniEvDead')
def AniEvDead():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEAD', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0056 offset: 0xFC98
@scena.Code('AniEvDeada')
def AniEvDeada():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_DEADa', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0057 offset: 0xFCE0
@scena.Code('AniEvDead1')
def AniEvDead1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'EV_DEAD1', 0x01, 0x01, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0058 offset: 0xFD28
@scena.Code('AniEvSCraft00')
def AniEvSCraft00():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0059 offset: 0xFD78
@scena.Code('AniEvSCraft00_1')
def AniEvSCraft00_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005A offset: 0xFDFC
@scena.Code('AniEvSCraft00_2')
def AniEvSCraft00_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005B offset: 0xFE64
@scena.Code('AniEvSCraft00_3')
def AniEvSCraft00_3():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_03a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005C offset: 0xFECC
@scena.Code('AniEvSCraft00_4')
def AniEvSCraft00_4():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005D offset: 0xFF1C
@scena.Code('AniEvSCraft00_5')
def AniEvSCraft00_5():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_04', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_04a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005E offset: 0xFF84
@scena.Code('AniEvSCraft00_6')
def AniEvSCraft00_6():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_05a', 0x00, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x005F offset: 0xFFEC
@scena.Code('AniEvSCraft00_7')
def AniEvSCraft00_7():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0060 offset: 0x10054
@scena.Code('AniEvSCraft00_8')
def AniEvSCraft00_8():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06b', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_06c', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0061 offset: 0x100E8
@scena.Code('AniEvSCraft00_9')
def AniEvSCraft00_9():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_07', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0062 offset: 0x1011C
@scena.Code('AniEvSCraft00_10')
def AniEvSCraft00_10():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_08', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_08a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0063 offset: 0x10184
@scena.Code('AniEvSCraft00_11')
def AniEvSCraft00_11():
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_09', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_S_CRAFT00_09a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0064 offset: 0x101EC
@scena.Code('AniEvCraft00')
def AniEvCraft00():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0065 offset: 0x10220
@scena.Code('AniEvCraft00_1')
def AniEvCraft00_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0066 offset: 0x10284
@scena.Code('AniEvCraft00_2')
def AniEvCraft00_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Call(ScriptId.Current, 'SpringOff')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    Call(ScriptId.Current, 'SpringOn')
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_03', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0067 offset: 0x10300
@scena.Code('AniEvCraft01')
def AniEvCraft01():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0068 offset: 0x1034C
@scena.Code('AniEvCraft01_1')
def AniEvCraft01_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT01_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0069 offset: 0x103CC
@scena.Code('AniEvCraft02')
def AniEvCraft02():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT00_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006A offset: 0x10400
@scena.Code('AniEvCraft02_1')
def AniEvCraft02_1():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT02_00a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006B offset: 0x10480
@scena.Code('AniEvCraft03')
def AniEvCraft03():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_00', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006C offset: 0x104B4
@scena.Code('AniEvCraft03_1')
def AniEvCraft03_1():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_01', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_01a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006D offset: 0x10518
@scena.Code('AniEvCraft03_2')
def AniEvCraft03_2():
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_02', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_CRAFT03_02a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006E offset: 0x10584
@scena.Code('AniEv00025')
def AniEv00025():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev00025', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev00025a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x006F offset: 0x105F4
@scena.Code('AniEv03020')
def AniEv03020():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev03020', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0070 offset: 0x10638
@scena.Code('AniEv03025')
def AniEv03025():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev03025', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev03025a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0071 offset: 0x106A8
@scena.Code('AniEv30150')
def AniEv30150():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev30150', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(1500)
    OP_6C(0xFFFE, 0.3)
    Sleep(400)
    OP_6C(0xFFFE, 1.0)
    Sleep(166)
    OP_6C(0xFFFE, 0.5)
    Sleep(1000)
    OP_6C(0xFFFE, 1.0)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0072 offset: 0x10738
@scena.Code('AniEv32030')
def AniEv32030():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev32030', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0073 offset: 0x107A0
@scena.Code('AniEv35000')
def AniEv35000():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('ShowEquip', 0x000B)
    Call(ScriptId.Current, 'EraseEquip')
    PlayChrAnimeClip(0xFFFE, 'ev35000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    Sleep(833)
    Call(ScriptId.Current, 'AniAttachMainWeapon')
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'BTL_WAIT', 0x01, 0x01, 0x00, 0x00, 0x00, 0.2, -0.0333333, -0.0333333, 0.0, 0x00, 0x00)

    Return()

# id: 0x0074 offset: 0x10830
@scena.Code('AniEv45005')
def AniEv45005():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    PlayChrAnimeClip(0xFFFE, 'ev45005', 0x01, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x0075 offset: 0x10874
@scena.Code('AniAttachEQU442')
def AniAttachEQU442():
    LoadAsset('C_EQU442')
    AttachEquip(0xFFFE, 'C_EQU442', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_76(0xFFFE, 'R_arm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0076 offset: 0x108F8
@scena.Code('AniDetachEQU442')
def AniDetachEQU442():
    ReleaseAsset('C_EQU442')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x0077 offset: 0x10940
@scena.Code('AniAttachEQU417')
def AniAttachEQU417():
    LoadAsset('C_EQU417')
    AttachEquip(0xFFFE, 'C_EQU417', 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_2A(0x00, 0xFFFE, '', 'R_arm_point', 0x01)
    OP_76(0xFFFE, 'R_arm_point', 'equip', 0x00, 0x01, 0.0, -1.0, -1.0, -1.0)

    Return()

# id: 0x0078 offset: 0x109C4
@scena.Code('AniDetachEQU417')
def AniDetachEQU417():
    ReleaseAsset('C_EQU417')
    DeatchEquip(0xFFFE, 'R_arm_point', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0)
    OP_54(0x0B, 0xFFFE)

    Return()

# id: 0x0079 offset: 0x10A0C
@scena.Code('AniEv86000')
def AniEv86000():
    Call(ScriptId.Current, 'SpringOff')
    PlayChrAnimeClip(0xFFFE, 'ev86000', 0x00, 0x00, 0x00, 0x00, 0x00, -2.0, -1.0, -1.0, -1.0, 0x00, 0x00)
    OP_6C(0xFFFE, 0.5)
    Sleep(1066)
    OP_6C(0xFFFE, 0.1)
    Sleep(333)
    OP_6C(0xFFFE, 0.0)

    Return()

# id: 0x007A offset: 0x10A58
@scena.Code('AniEv86000b')
def AniEv86000b():
    Call(ScriptId.Current, 'SpringOff')
    SetEndhookFunction('SpringOn', 0x000B)
    OP_80(0.0)
    PlayChrAnimeClip(0xFFFE, 'ev86000', 0x00, 0x01, 0x00, 0x00, 0x00, -2.0, -0.0333333, -0.0333333, 0.566667, 0x00, 0x00)
    OP_6C(0xFFFE, 0.3)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)
    PlayChrAnimeClip(0xFFFE, 'ev86000a', 0x01, 0x00, 0x00, 0x00, 0x00, 0.2, -1.0, -1.0, -1.0, 0x00, 0x00)
    WaitAnimeClip(0xFFFE, 0.0, 0x00)

    Return()

# id: 0x007B offset: 0x10AE0
@scena.AnimeClips('_AniAttachMainWeapon')
def _AniAttachMainWeapon():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU090',
        ),
    )

# id: 0x007C offset: 0x10B40
@scena.AnimeClips('_AniBtl_AttackTest')
def _AniBtl_AttackTest():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
    )

# id: 0x007D offset: 0x10BA0
@scena.AnimeClips('_AniWait_Test1')
def _AniWait_Test1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'WAIT',
        ),
    )

# id: 0x007E offset: 0x10C00
@scena.AnimeClips('_AniBtlWait_Test1')
def _AniBtlWait_Test1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x007F offset: 0x10C60
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
            name   = 'WALK',
        ),
    )

# id: 0x0080 offset: 0x10CE0
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
            name   = 'WAIT',
        ),
    )

# id: 0x0081 offset: 0x10D90
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

# id: 0x0082 offset: 0x10E10
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

# id: 0x0083 offset: 0x10E90
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

# id: 0x0084 offset: 0x10EF0
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

# id: 0x0085 offset: 0x10F50
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

# id: 0x0086 offset: 0x10FB0
@scena.AnimeClips('_AniBtlInit')
def _AniBtlInit():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk033_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/atk033_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/moncharge.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU090',
        ),
    )

# id: 0x0087 offset: 0x11080
@scena.AnimeClips('_AniBtlStart')
def _AniBtlStart():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B58,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5C,
            name   = '',
        ),
    )

# id: 0x0088 offset: 0x11130
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

# id: 0x0089 offset: 0x11190
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

# id: 0x008A offset: 0x111F0
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
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B5F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAE,
            name   = '',
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
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_ATTACK',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F66,
            name   = '',
        ),
    )

# id: 0x008B offset: 0x11400
@scena.AnimeClips('_AniBtlCounter')
def _AniBtlCounter():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B9B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B74,
            name   = '',
        ),
    )

# id: 0x008C offset: 0x11480
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

# id: 0x008D offset: 0x11500
@scena.AnimeClips('_AniBtlDamageVoice')
def _AniBtlDamageVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B9A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B98,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B99,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B73,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B71,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x1B74,
            name   = '',
        ),
    )

# id: 0x008E offset: 0x11620
@scena.AnimeClips('_AniBtlGuardBreakVoice')
def _AniBtlGuardBreakVoice():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B96,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6F,
            name   = '',
        ),
    )

# id: 0x008F offset: 0x116A0
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

# id: 0x0090 offset: 0x11750
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

# id: 0x0091 offset: 0x117B0
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
            name   = 'battle/cr033_03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B92,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B66,
            name   = '',
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
            dword4 = 0x00008F79,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B93,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B67,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_02a',
        ),
    )

# id: 0x0092 offset: 0x11A10
@scena.AnimeClips('_AniBtlDead')
def _AniBtlDead():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B97,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B70,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_DEAD',
        ),
    )

# id: 0x0093 offset: 0x11AC0
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

# id: 0x0094 offset: 0x11B70
@scena.AnimeClips('_AniBtlCraft00')
def _AniBtlCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B60,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
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
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FC1,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B61,
            name   = '',
        ),
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
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0095 offset: 0x11E00
@scena.AnimeClips('_AniBtlCraft01')
def _AniBtlCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_01_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B62,
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
            dword4 = 0x00008F72,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FB4,
            name   = '',
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
            name   = 'BTL_CRAFT01_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F93,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B8F,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B63,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FC1,
            name   = '',
        ),
    )

# id: 0x0096 offset: 0x12150
@scena.AnimeClips('_AniBtlCraft02')
def _AniBtlCraft02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_02_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_02_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cr033_02_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT02_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B90,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B64,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAD,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F78,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F69,
            name   = '',
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
            dword4 = 0x00008F02,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B91,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B65,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F02,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F07,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F0C,
            name   = '',
        ),
    )

# id: 0x0097 offset: 0x12430
@scena.AnimeClips('_AniBtlCraftDamage02')
def _AniBtlCraftDamage02():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008BF0,
            name   = '',
        ),
    )

# id: 0x0098 offset: 0x12490
@scena.AnimeClips('_AniBtlCraft03')
def _AniBtlCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh03_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh03_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/damage02.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '2',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '3',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x0099 offset: 0x12880
@scena.AnimeClips('_AniBtlCraft04')
def _AniBtlCraft04():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/crdh04_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
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
            name   = 'BTL_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_13',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT01_10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '0',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0x0B5E,
            dword4 = 0x00000000,
            name   = '1',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x009A offset: 0x12C00
@scena.AnimeClips('_AniBtlSCraft00')
def _AniBtlSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_1.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_2.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_3.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_4.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_5.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_6.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_7.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_8.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_9.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_10.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_11.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_12.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_13.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/cic033_0.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00001012,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU090',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F27,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008B7D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_CHRX10',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6B,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F62,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F96,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FAA,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F41,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FA6,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0003,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'battle/sc033_00_14.eff',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFB,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFB,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFB,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000010F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F1C,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008FBC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFB,
            dword4 = 0x00000000,
            name   = 'BTL_CRUCIFIXION',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F27,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000013F8,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09a',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x000013EC,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F31,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0005,
            type2  = 0xFFFF,
            dword4 = 0x00001B6E,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x00008F2D,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0004,
            type2  = 0xFFFF,
            dword4 = 0x0000114A,
            name   = '',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x009B offset: 0x139D0
@scena.AnimeClips('_AniEvAttachEquip')
def _AniEvAttachEquip():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU090',
        ),
    )

# id: 0x009C offset: 0x13A30
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

# id: 0x009D offset: 0x13A90
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

# id: 0x009E offset: 0x13AF0
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

# id: 0x009F offset: 0x13B70
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

# id: 0x00A0 offset: 0x13BF0
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

# id: 0x00A1 offset: 0x13C70
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

# id: 0x00A2 offset: 0x13CD0
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

# id: 0x00A3 offset: 0x13D50
@scena.AnimeClips('_AniEvBtlWalk')
def _AniEvBtlWalk():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WALK',
        ),
    )

# id: 0x00A4 offset: 0x13DB0
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

# id: 0x00A5 offset: 0x13E10
@scena.AnimeClips('_AniEvPowerup')
def _AniEvPowerup():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_POWERUP_F',
        ),
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

# id: 0x00A6 offset: 0x13EC0
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

# id: 0x00A7 offset: 0x13F40
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

# id: 0x00A8 offset: 0x13FA0
@scena.AnimeClips('_AniEvDead1')
def _AniEvDead1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'EV_DEAD1',
        ),
    )

# id: 0x00A9 offset: 0x14000
@scena.AnimeClips('_AniEvSCraft00')
def _AniEvSCraft00():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_00',
        ),
    )

# id: 0x00AA offset: 0x14060
@scena.AnimeClips('_AniEvSCraft00_1')
def _AniEvSCraft00_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
    )

# id: 0x00AB offset: 0x140E0
@scena.AnimeClips('_AniEvSCraft00_2')
def _AniEvSCraft00_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_02a',
        ),
    )

# id: 0x00AC offset: 0x14160
@scena.AnimeClips('_AniEvSCraft00_3')
def _AniEvSCraft00_3():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_03a',
        ),
    )

# id: 0x00AD offset: 0x141E0
@scena.AnimeClips('_AniEvSCraft00_4')
def _AniEvSCraft00_4():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_01a',
        ),
    )

# id: 0x00AE offset: 0x14240
@scena.AnimeClips('_AniEvSCraft00_5')
def _AniEvSCraft00_5():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_04a',
        ),
    )

# id: 0x00AF offset: 0x142C0
@scena.AnimeClips('_AniEvSCraft00_6')
def _AniEvSCraft00_6():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_05a',
        ),
    )

# id: 0x00B0 offset: 0x14340
@scena.AnimeClips('_AniEvSCraft00_7')
def _AniEvSCraft00_7():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06a',
        ),
    )

# id: 0x00B1 offset: 0x143C0
@scena.AnimeClips('_AniEvSCraft00_8')
def _AniEvSCraft00_8():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06b',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_06c',
        ),
    )

# id: 0x00B2 offset: 0x14440
@scena.AnimeClips('_AniEvSCraft00_9')
def _AniEvSCraft00_9():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_07',
        ),
    )

# id: 0x00B3 offset: 0x144A0
@scena.AnimeClips('_AniEvSCraft00_10')
def _AniEvSCraft00_10():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_08a',
        ),
    )

# id: 0x00B4 offset: 0x14520
@scena.AnimeClips('_AniEvSCraft00_11')
def _AniEvSCraft00_11():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_S_CRAFT00_09a',
        ),
    )

# id: 0x00B5 offset: 0x145A0
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

# id: 0x00B6 offset: 0x14600
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

# id: 0x00B7 offset: 0x14680
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
            name   = 'BTL_CRAFT00_03',
        ),
    )

# id: 0x00B8 offset: 0x14700
@scena.AnimeClips('_AniEvCraft01')
def _AniEvCraft01():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT01_00',
        ),
    )

# id: 0x00B9 offset: 0x14760
@scena.AnimeClips('_AniEvCraft01_1')
def _AniEvCraft01_1():
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

# id: 0x00BA offset: 0x147E0
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

# id: 0x00BB offset: 0x14840
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

# id: 0x00BC offset: 0x148C0
@scena.AnimeClips('_AniEvCraft03')
def _AniEvCraft03():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_00',
        ),
    )

# id: 0x00BD offset: 0x14920
@scena.AnimeClips('_AniEvCraft03_1')
def _AniEvCraft03_1():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_01',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_01a',
        ),
    )

# id: 0x00BE offset: 0x149A0
@scena.AnimeClips('_AniEvCraft03_2')
def _AniEvCraft03_2():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_02',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_CRAFT03_02a',
        ),
    )

# id: 0x00BF offset: 0x14A20
@scena.AnimeClips('_AniEv00025')
def _AniEv00025():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00025',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev00025a',
        ),
    )

# id: 0x00C0 offset: 0x14AA0
@scena.AnimeClips('_AniEv03020')
def _AniEv03020():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03020',
        ),
    )

# id: 0x00C1 offset: 0x14B00
@scena.AnimeClips('_AniEv03025')
def _AniEv03025():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03025',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev03025a',
        ),
    )

# id: 0x00C2 offset: 0x14B80
@scena.AnimeClips('_AniEv30150')
def _AniEv30150():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev30150',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x00C3 offset: 0x14C00
@scena.AnimeClips('_AniEv32030')
def _AniEv32030():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev32030',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x00C4 offset: 0x14C80
@scena.AnimeClips('_AniEv35000')
def _AniEv35000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev35000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'BTL_WAIT',
        ),
    )

# id: 0x00C5 offset: 0x14D00
@scena.AnimeClips('_AniEv45005')
def _AniEv45005():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev45005',
        ),
    )

# id: 0x00C6 offset: 0x14D60
@scena.AnimeClips('_AniAttachEQU442')
def _AniAttachEQU442():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0002,
            type2  = 0xFFFF,
            dword4 = 0x00000000,
            name   = 'C_EQU442',
        ),
    )

# id: 0x00C7 offset: 0x14DC0
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

# id: 0x00C8 offset: 0x14E20
@scena.AnimeClips('_AniEv86000')
def _AniEv86000():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev86000',
        ),
    )

# id: 0x00C9 offset: 0x14E80
@scena.AnimeClips('_AniEv86000b')
def _AniEv86000b():
    return ScenaAnimeClips(
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev86000',
        ),
        ScenaAnimeClipItem(
            type   = 0x0009,
            type2  = 0xFFFE,
            dword4 = 0x00000000,
            name   = 'ev86000a',
        ),
    )

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
